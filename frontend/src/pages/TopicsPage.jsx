import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { getTopics, createTopic } from '../api/client'

export default function TopicsPage() {
  const [topics, setTopics] = useState([])
  const [newTopicText, setNewTopicText] = useState('')
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  function loadTopics() {
    setLoading(true)
    getTopics()
      .then(setTopics)
      .catch(() => setError('Could not load topics. Is the Django server running?'))
      .finally(() => setLoading(false))
  }

  useEffect(loadTopics, [])

  async function handleSubmit(e) {
    e.preventDefault()
    if (!newTopicText.trim()) return
    const topic = await createTopic(newTopicText.trim())
    setTopics(prev => [...prev, topic])
    setNewTopicText('')
  }

  if (loading) return <p>Loading topics…</p>
  if (error) return <p style={{ color: 'crimson' }}>{error}</p>

  return (
    <div>
      <h1>Topics</h1>
      <ul>
        {topics.map(topic => (
          <li key={topic.id}>
            <Link to={`/topics/${topic.id}`}>{topic.text}</Link>
          </li>
        ))}
      </ul>

      <h2>Add a new topic</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={newTopicText}
          onChange={e => setNewTopicText(e.target.value)}
          placeholder="e.g. Chess"
        />
        <button type="submit">Add topic</button>
      </form>
    </div>
  )
}
