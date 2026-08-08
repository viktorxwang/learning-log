import { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'
import { getTopic, createEntry } from '../api/client'

export default function TopicPage() {
  const { topicId } = useParams()
  const [topic, setTopic] = useState(null)
  const [newEntryText, setNewEntryText] = useState('')
  const [error, setError] = useState(null)

  function loadTopic() {
    getTopic(topicId)
      .then(setTopic)
      .catch(() => setError('Could not load this topic.'))
  }

  useEffect(loadTopic, [topicId])

  async function handleSubmit(e) {
    e.preventDefault()
    if (!newEntryText.trim()) return
    await createEntry(topicId, newEntryText.trim())
    setNewEntryText('')
    loadTopic() // refresh entries
  }

  if (error) return <p style={{ color: 'crimson' }}>{error}</p>
  if (!topic) return <p>Loading…</p>

  return (
    <div>
      <p><Link to="/">&larr; All topics</Link></p>
      <h1>{topic.text}</h1>

      <h2>Add a new entry</h2>
      <form onSubmit={handleSubmit}>
        <textarea
          cols={80}
          rows={4}
          value={newEntryText}
          onChange={e => setNewEntryText(e.target.value)}
        />
        <br />
        <button type="submit">Add entry</button>
      </form>

      <h2>Entries</h2>
      {topic.entries.length === 0 && <p>No entries yet.</p>}
      {topic.entries.map(entry => (
        <article key={entry.id} style={{ marginBottom: '1.5rem' }}>
          <p style={{ color: '#666', fontSize: '0.85rem' }}>
            {new Date(entry.date_added).toLocaleString()}
          </p>
          <p>{entry.text}</p>
        </article>
      ))}
    </div>
  )
}
