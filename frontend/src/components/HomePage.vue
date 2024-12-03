<!-- components/HomePage.vue -->
<template>
  <div>
    <h1>Главная страница</h1>
    <ul class="post-list">
      <li v-for="post in posts" :key="post.id" class="post-item">
        <div>
          <strong>{{ post.title }}</strong>
          <p>{{ post.content }}</p>
          <router-link :to="`/posts/${post.id}`">Комментарии</router-link>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from '../api/axios';

export default {
  data() {
    return {
      posts: [],
    };
  },
  methods: {
    async fetchPosts() {
      try {
        const response = await axios.get('/posts/');
        this.posts = response.data;
      } catch (error) {
        console.error('Ошибка при загрузке постов:', error);
      }
    },
  },
  mounted() {
    this.fetchPosts();
  },
};
</script>

<style scoped>
.post-list {
  list-style: none;
  padding: 0;
}

.post-item {
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 10px;
  margin-bottom: 10px;
}

.post-item strong {
  font-size: 18px;
}

.post-item p {
  margin: 10px 0;
}
</style>