<!-- components/Pagination.vue -->
<template>
  <nav class="pagination-container">
    <ul class="pagination">
      <li @click="changePage(currentPage - 1)" :class="{ disabled: currentPage === 1 }">
        <span>Предыдущая страница</span>
      </li>
      <li v-for="page in pageArray" :key="page" @click="changePage(page)" :class="{ active: page === currentPage }">
        <span>{{ page }}</span>
      </li>
      <li @click="changePage(currentPage + 1)" :class="{ disabled: currentPage === totalPages }">
        <span>Следующая страница</span>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  props: {
    totalPages: {
      type: Number,
      required: true
    },
    currentPage: {
      type: Number,
      required: true
    }
  },
  computed: {
    // Генерация массива страниц на основе totalPages
    pageArray() {
      return Array.from({ length: this.totalPages }, (_, index) => index + 1);
    },
  },
  methods: {
    changePage(page) {
      if (page >= 1 && page <= this.totalPages) {
        this.$emit('pageChanged', page);
      }
    },
  },
};
</script>

<style scoped>
.pagination-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.pagination {
  display: flex;
  list-style: none;
  padding: 0;
}

.pagination li {
  margin: 0 5px;
  cursor: pointer;
}

.pagination li.active {
  font-weight: bold;
  color: #42b983;
}

.pagination li span {
  display: block;
  padding: 5px 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.pagination li.active span {
  background-color: #42b983;
  color: white;
  border-color: #42b983;
}

.pagination li.disabled {
  color: #ccc;
  cursor: not-allowed;
}

.pagination li.disabled span {
  border-color: #ccc;
}
</style>