<!-- components/CommentsPage.vue -->
<template>
  <div>
    <h2> </h2>
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

export default {
  components: {
    CommentForm,
    CommentList,
    Pagination
  },
  data() {
    return {
      postId: 1, // Примерное значение, замените на реальное значение
    };
  },
  computed: {
    ...mapState(['currentPage', 'totalPages']),
  },
  methods: {
    ...mapActions(['fetchComments', 'setCurrentPage']),
    handlePageChange(page) {
      this.setCurrentPage(page);
      this.fetchComments();
    },
  },
  mounted() {
    this.fetchComments();
  },
};
</script>