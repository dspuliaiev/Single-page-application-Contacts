<template>
  <div class="captcha-container">
    <img :src="captchaImage" alt="CAPTCHA" />
  </div>
</template>

<script>
import axiosClient from '../api/axiosClient';

export default {
  data() {
    return {
      captchaImage: '',
      captchaKey: '',
    };
  },
  methods: {
    getCaptcha() {
      axiosClient.get('captcha/')
        .then(response => {
          this.captchaImage = response.data.captcha_image_url;
          this.captchaKey = response.data.captcha_key;
          this.$emit('set-captcha-key', this.captchaKey);
        })
        .catch(error => {
          console.error('Ошибка при загрузке CAPTCHA:', error);
        });
    }
  },
  mounted() {
    this.getCaptcha();
  }
};
</script>

<style scoped>
.captcha-container img {
  width: 200px;
  height: 100px;
}
</style>
