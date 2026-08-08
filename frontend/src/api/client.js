import axios from 'axios'

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',
})

export const getTopics = () => api.get('topics/').then(r => r.data.results ?? r.data)
export const getTopic = (id) => api.get(`topics/${id}/`).then(r => r.data)
export const createTopic = (text) => api.post('topics/', { text }).then(r => r.data)
export const createEntry = (topicId, text) =>
  api.post('entries/', { topic: topicId, text }).then(r => r.data)

export default api
