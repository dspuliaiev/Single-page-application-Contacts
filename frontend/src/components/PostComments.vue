<!-- components/PostComments.vue -->
<template>
  <div>
    <h1>Комментарии к посту "{{ postTitle }}"</h1>
    <CommentForm :postId="postId" @commentAdded="fetchComments" />
    <CommentList />
    <Pagination @pageChanged="handlePageChange" :currentPage="currentPage" :totalPages="totalPages" />
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import CommentForm from './CommentForm.vue';
import CommentList from './CommentList.vue';
import Pagination from './Pagination.vue';
import axios from '../api/axios';

export default {
  components: {
    CommentForm,
    CommentList,
    Pagination
  },
  data() {
    return {
      postId: this.$route.params.id,
      postTitle: '',
    };
  },
  computed: {
    ...mapState(['currentPage', 'totalPages']),
  },
  methods: {
    ...mapActions(['fetchComments', 'setCurrentPage']),
    async fetchPostTitle() {
      try {
        const response = await axios.get(`/posts/${this.postId}/`);
        this.postTitle = response.data.title;
      } catch (error) {
        console.error('Ошибка при загрузке заголовка поста:', error);
      }
    },
    handlePageChange(page) {
      this.setCurrentPage(page);
      this.fetchComments();
    },
  },
  mounted() {
    this.fetchPostTitle();
    this.fetchComments();
  },
};
</script>