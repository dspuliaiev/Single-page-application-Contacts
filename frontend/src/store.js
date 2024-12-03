// store.js
import { createStore } from 'vuex';
import axios from './api/axios';

export default createStore({
  state: {
    comments: [],
    totalPages: 1,
    currentPage: 1,
    sortBy: 'created_at',
    sortOrder: 'desc',
  },
  mutations: {
    SET_COMMENTS(state, comments) {
      state.comments = comments;
    },
    SET_TOTAL_PAGES(state, totalPages) {
      state.totalPages = totalPages;
    },
    SET_CURRENT_PAGE(state, currentPage) {
      state.currentPage = currentPage;
    },
    SET_SORT_BY(state, sortBy) {
      state.sortBy = sortBy;
    },
    SET_SORT_ORDER(state, sortOrder) {
      state.sortOrder = sortOrder;
    },
  },
  actions: {
    async fetchComments({ commit, state }, postId) {
      try {
        const response = await axios.get(`/posts/${postId}/comments/?page=${state.currentPage}&sort_by=${state.sortBy}&order=${state.sortOrder}`);
        commit('SET_COMMENTS', response.data.results);
        commit('SET_TOTAL_PAGES', response.data.total_pages);
      } catch (error) {
        console.error('Ошибка при загрузке комментариев:', error);
      }
    },
    setCurrentPage({ commit }, page) {
      commit('SET_CURRENT_PAGE', page);
    },
    setSortBy({ commit }, sortBy) {
      commit('SET_SORT_BY', sortBy);
    },
    setSortOrder({ commit }, sortOrder) {
      commit('SET_SORT_ORDER', sortOrder);
    },
  },
  getters: {
    sortedComments: (state) => {
      return state.comments.slice().sort((a, b) => {
        const order = state.sortOrder === 'asc' ? 1 : -1;
        if (a[state.sortBy] < b[state.sortBy]) return -order;
        if (a[state.sortBy] > b[state.sortBy]) return order;
        return 0;
      });
    },
  },
});