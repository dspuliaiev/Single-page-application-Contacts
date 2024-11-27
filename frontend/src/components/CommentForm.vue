<template>
  <form @submit.prevent="handleSubmit">
    <label for="username">Имя пользователя:</label>
    <input id="username" v-model="username" type="text" required />

    <label for="email">Email:</label>
    <input id="email" v-model="email" type="email" required />

    <label for="text">Текст комментария:</label>
    <textarea id="text" v-model="text" required></textarea>

    <captcha @set-captcha-key="setCaptchaKey" />

    <label for="captcha">Введите CAPTCHA:</label>
    <input id="captcha" v-model="captchaValue" type="text" required />

    <button type="submit">Отправить комментарий</button>
  </form>
</template>

<script>
import axiosClient from '../api/axiosClient';
import Captcha from './Captcha';

export default {
  components: {
    Captcha
  },
  data() {
    return {
      username: '',
      email: '',
      text: '',
      captchaKey: '',
      captchaValue: ''
    };
  },
  methods: {
    handleSubmit() {
      axiosClient.post('comments/', {
        username: this.username,
        email: this.email,
        text: this.text,
        captcha_key: this.captchaKey,
        captcha_value: this.captchaValue
      })
        .then(() => {
          alert('Комментарий успешно отправлен!');
          this.username = '';
          this.email = '';
          this.text = '';
          this.captchaValue = '';
        })
        .catch((error) => {
          console.error('Ошибка при отправке комментария:', error);
        });
    },
    setCaptchaKey(key) {
      this.captchaKey = key;
    }
  }
};
</script>
