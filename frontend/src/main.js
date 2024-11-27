import { createApp } from 'vue';
import App from './App.vue';
import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './views/HomePage.vue';
import RegistrationPage from './views/RegistrationPage.vue';
import CommentPage from './views/CommentPage.vue';

const routes = [
  { path: '/', component: HomePage },
  { path: '/register', component: RegistrationPage },
  { path: '/comments', component: CommentPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

createApp(App).use(router).mount('#app');
