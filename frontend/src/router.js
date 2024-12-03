// router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './components/HomePage.vue';
import PostComments from './components/PostComments.vue';

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage,
  },
  {
    path: '/posts/:id',
    name: 'PostComments',
    component: PostComments,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

