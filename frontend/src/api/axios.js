import axios from 'axios';

// Получение CSRF токена из cookie
function getCSRFToken() {
  const cookies = document.cookie.split(';');
  for (let cookie of cookies) {
    const [name, value] = cookie.trim().split('=');
    if (name === 'csrftoken') {
      return decodeURIComponent(value);
    }
  }
  return '';
}

// Настройка Axios
const instance = axios.create({
  baseURL: 'http://localhost:8000/api', // Измените на ваш URL
  headers: {
    'X-CSRFToken': getCSRFToken(),
    'Content-Type': 'application/json',
  },
  withCredentials: true,
});

// Переопределение заголовка Content-Type для запросов с FormData
instance.interceptors.request.use((config) => {
  if (config.data instanceof FormData) {
    config.headers['Content-Type'] = 'multipart/form-data';
  }
  return config;
});

export default instance;
