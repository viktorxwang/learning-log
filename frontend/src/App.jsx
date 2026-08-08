import { Routes, Route } from 'react-router-dom'
import TopicsPage from './pages/TopicsPage'
import TopicPage from './pages/TopicPage'
import './App.css'

function App() {
  return (
    <div className="app-shell">
      <header>
        <h1 className="brand">Learning Log</h1>
      </header>
      <main>
        <Routes>
          <Route path="/" element={<TopicsPage />} />
          <Route path="/topics/:topicId" element={<TopicPage />} />
        </Routes>
      </main>
    </div>
  )
}

export default App
