<template>
  <form @submit.prevent="handleSubmit">
    <label for="file">Выберите файл:</label>
    <input type="file" @change="handleFileChange" required />

    <button type="submit">Загрузить</button>
  </form>
</template>

<script>
import axiosClient from '../api/axiosClient';

export default {
  data() {
    return {
      file: null
    };
  },
  methods: {
    handleFileChange(event) {
      this.file = event.target.files[0];
    },
    handleSubmit() {
      const formData = new FormData();
      formData.append('file', this.file);

      axiosClient.post('files/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
        .then(() => {
          alert('Файл успешно загружен!');
          this.file = null;
        })
        .catch((error) => {
          console.error('Ошибка при загрузке файла:', error);
        });
    }
  }
};
</script>
