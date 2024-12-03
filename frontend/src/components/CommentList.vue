<!-- components/CommentList.vue -->
<template>
  <div>
    <h2>Комментарии</h2>
    <div class="sorting">
      <label>Сортировать по:</label>
      <select v-model="sortBy" @change="setSortBy">
        <option value="user_name">User Name</option>
        <option value="email">E-mail</option>
        <option value="created_at">Дата добавления</option>
      </select>
      <select v-model="sortOrder" @change="setSortOrder">
        <option value="asc">По возрастанию</option>
        <option value="desc">По убыванию</option>
      </select>
    </div>
    <ul class="comment-list">
      <li v-for="comment in sortedComments" :key="comment.id" class="comment-item">
        <div>
          <strong>{{ comment.user_name }}</strong>
          <p v-html="comment.text"></p>
          <small>{{ comment.created_at }}</small>
        </div>
        <ul v-if="comment.replies">
          <li v-for="reply in comment.replies" :key="reply.id" class="reply-item">
            <div>
              <strong>{{ reply.user_name }}</strong>
              <p v-html="reply.text"></p>
              <small>{{ reply.created_at }}</small>
            </div>
          </li>
        </ul>
      </li>
    </ul>
    <Pagination :totalPages="totalPages" :currentPage="currentPage" @pageChanged="handlePageChange" />
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex';
import Pagination from './Pagination.vue';

export default {
  components: { Pagination },
  computed: {
    ...mapState(['totalPages', 'currentPage', 'sortBy', 'sortOrder']),
    ...mapGetters(['sortedComments']),
  },
  methods: {
    ...mapActions(['fetchComments', 'setCurrentPage', 'setSortBy', 'setSortOrder']),
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

<style scoped>
.comment-list {
  list-style: none;
  padding: 0;
}

.comment-item, .reply-item {
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 10px;
  margin-bottom: 10px;
}

.comment-item strong, .reply-item strong {
  font-size: 18px;
}

.comment-item p, .reply-item p {
  margin: 10px 0;
}

.comment-item small, .reply-item small {
  color: #777;
}

.sorting {
  margin-bottom: 20px;
}

.sorting label {
  margin-right: 10px;
}

.sorting select {
  padding: 5px;
  font-size: 16px;
}
</style>
