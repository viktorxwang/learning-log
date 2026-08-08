# Learning Log — Django API + React frontend

The project is now split in two:

- `learning_log/` — Django project, now serving a JSON REST API (via Django
  REST Framework) instead of rendering HTML templates for the main app.
- `frontend/` — a React app (Vite) that consumes that API.

The old server-rendered templates/views (`learning_logs/views.py` +
`templates/`) are still there and still work if you want them, but the React
app does not use them — it talks to `/api/...` directly.

## 1. Run the Django API

```bash
cd learning_log
python -m venv ll_env          # if you don't already have one set up
source ll_env/bin/activate     # Windows: ll_env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate       # only needed if db.sqlite3 isn't already migrated
python manage.py runserver
```

This serves the API at `http://127.0.0.1:8000/api/`:

| Method | URL                          | Purpose                          |
|--------|-------------------------------|-----------------------------------|
| GET    | `/api/topics/`                | list all topics                  |
| POST   | `/api/topics/`                | create a topic (`{"text": "..."}`)|
| GET    | `/api/topics/<id>/`           | one topic + its entries nested   |
| GET    | `/api/entries/?topic=<id>`    | entries for one topic            |
| POST   | `/api/entries/`               | create entry (`{"topic": id, "text": "..."}`) |
| DELETE | `/api/topics/<id>/` / `/api/entries/<id>/` | delete             |

The Django admin (`/admin/`) still works as before.

## 2. Run the React frontend

In a second terminal:

```bash
cd frontend
npm install
npm run dev
```

This starts Vite's dev server, normally at `http://localhost:5173`. Open that
in your browser — it fetches topics/entries from the Django API you started
in step 1.

CORS is already configured in `learning_log/settings.py`
(`CORS_ALLOWED_ORIGINS`) to allow `localhost:5173` to call the API. If you
change the Vite port, add it there too.

## What was added to the Django side

- `rest_framework` and `corsheaders` added to `INSTALLED_APPS`
- `learning_logs/serializers.py` — turns `Topic`/`Entry` model instances into JSON
- `learning_logs/api_views.py` — `TopicViewSet` / `EntryViewSet` (list/create/update/delete)
- `learning_logs/api_urls.py` — router wiring those viewsets to `/api/topics/`, `/api/entries/`
- `learning_log/urls.py` — includes the API urls at `/api/`
- Fixed a pre-existing bug in `views.py::new_entry` (it referenced `topic.id`
  before `topic` was defined, and called `redirect` instead of `render` for
  the GET case)

## What's in the React app

- `src/api/client.js` — thin axios wrapper around the Django API
- `src/pages/TopicsPage.jsx` — list topics, add a new topic
- `src/pages/TopicPage.jsx` — view one topic's entries, add a new entry
- `react-router-dom` handles the two routes (`/` and `/topics/:topicId`)

## Where to go from here

- **Auth**: the original book's later chapters add per-user topics/entries
  and login. To bring that over, you'd add Django's session auth or
  `djangorestframework-simplejwt` for token auth, add an `owner` field to
  `Topic`, and filter querysets by `request.user` in the viewsets.
- **Editing/deleting from the UI**: the API already supports `PUT`/`DELETE`
  on both endpoints — the React app just doesn't have buttons for it yet.
- **Styling**: current components are unstyled beyond `App.css`; worth
  polishing once the data flow feels right.
- **Deployment**: Django (API) and the built React app (`npm run build` →
  `frontend/dist/`) can be deployed separately, or you can have Django serve
  the built `dist/` as static files from a single origin instead of running
  two servers.
