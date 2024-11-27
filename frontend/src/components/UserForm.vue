<template>
  <form @submit.prevent="handleSubmit">
    <label for="username">Имя пользователя:</label>
    <input id="username" v-model="username" type="text" required />

    <label for="email">Email:</label>
    <input id="email" v-model="email" type="email" required />

    <button type="submit">Зарегистрироваться</button>
  </form>
</template>

<script>
import axiosClient from '../api/axiosClient';

export default {
  data() {
    return {
      username: '',
      email: ''
    };
  },
  methods: {
    handleSubmit() {
      axiosClient.post('users/', {
        username: this.username,
        email: this.email
      })
        .then(() => {
          alert('Пользователь успешно зарегистрирован!');
          this.username = '';
          this.email = '';
        })
        .catch((error) => {
          console.error('Ошибка при создании пользователя:', error);
        });
    }
  }
};
</script>
