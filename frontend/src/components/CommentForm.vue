<!-- components/CommentForm.vue -->
<template>
  <form @submit.prevent="submitComment">
    <div>
      <label for="userName">User Name:</label>
      <input id="userName" v-model="userName" placeholder="User Name" required pattern="[A-Za-z0-9]+" />
    </div>
    <div>
      <label for="email">E-mail:</label>
      <input id="email" v-model="email" placeholder="E-mail" required type="email" />
    </div>
    <div>
      <label for="homePage">Home Page:</label>
      <input id="homePage" v-model="homePage" placeholder="Home Page" type="url" />
    </div>
    <div class="captcha-container">
      <img :src="captchaImage" alt="Captcha" />
      <button @click.prevent="reloadCaptcha">Обновить капчу</button>
    </div>
    <div>
      <label for="captchaText">Введите текст с капчи:</label>
      <input id="captchaText" v-model="captchaText" placeholder="Введите текст с капчи" required pattern="[A-Za-z0-9]+" />
    </div>
    <div>
      <label for="text">Text:</label>
      <textarea id="text" v-model="text" placeholder="Введите комментарий" required></textarea>
    </div>
    <div>
      <input type="file" @change="handleFileUpload" accept="image/*,text/plain" />
      <img v-if="previewImage" :src="previewImage" alt="Preview" class="preview-image" />
    </div>
    <button type="submit">Отправить</button>
  </form>
</template>

<script>
import axios from '../api/axios';

export default {
  props: ['postId'],
  data() {
    return {
      userName: '',
      email: '',
      homePage: '',
      captchaKey: '',
      captchaText: '',
      captchaImage: '',
      text: '',
      file: null,
      previewImage: '',
    };
  },
  methods: {
    async loadCaptcha() {
      try {
        const response = await axios.get('/captcha/');
        this.captchaKey = response.data.key;
        this.captchaImage = response.data.image_url;
      } catch (error) {
        console.error('Ошибка при загрузке капчи:', error);
      }
    },
    async reloadCaptcha() {
      await this.loadCaptcha();
    },
    handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        if (file.type.startsWith('image/')) {
          const reader = new FileReader();
          reader.onload = (e) => {
            const img = new Image();
            img.src = e.target.result;
            img.onload = () => {
              const canvas = document.createElement('canvas');
              const maxWidth = 320;
              const maxHeight = 240;
              let width = img.width;
              let height = img.height;

              if (width > height) {
                if (width > maxWidth) {
                  height *= maxWidth / width;
                  width = maxWidth;
                }
              } else {
                if (height > maxHeight) {
                  width *= maxHeight / height;
                  height = maxHeight;
                }
              }

              canvas.width = width;
              canvas.height = height;
              const ctx = canvas.getContext('2d');
              ctx.drawImage(img, 0, 0, width, height);
              this.previewImage = canvas.toDataURL(file.type);
            };
          };
          reader.readAsDataURL(file);
        } else if (file.type === 'text/plain' && file.size <= 100 * 1024) {
          this.file = file;
        }
      }
    },
    async submitComment() {
      try {
        const formData = new FormData();
        formData.append('user_name', this.userName);
        formData.append('email', this.email);
        formData.append('home_page', this.homePage);
        formData.append('captcha_0', this.captchaKey);
        formData.append('captcha_1', this.captchaText);
        formData.append('text', this.text);
        if (this.file) {
          formData.append('file', this.file);
        }

        await axios.post(`/comments/${this.postId}/`, formData);
        alert('Комментарий добавлен!');
        this.userName = '';
        this.email = '';
        this.homePage = '';
        this.captchaText = '';
        this.text = '';
        this.file = null;
        this.previewImage = '';
        await this.loadCaptcha();
        this.$emit('commentAdded');
      } catch (error) {
        alert('Ошибка при добавлении комментария: ' + error.response.data.message);
      }
    },
  },
  mounted() {
    this.loadCaptcha();
  },
};
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
  max-width: 400px;
  margin: 0 auto;
}

div {
  margin-bottom: 10px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input, textarea {
  width: 100%;
  padding: 10px;
  font-size: 16px;
}

.captcha-container {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.captcha-container img {
  margin-right: 10px;
}

button {
  padding: 10px;
  font-size: 16px;
  cursor: pointer;
}

.preview-image {
  max-width: 320px;
  max-height: 240px;
  margin-top: 10px;
}
</style>
