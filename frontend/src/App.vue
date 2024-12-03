<!-- App.vue -->
<template>
  <div id="app">
    <header>
      <h1>Комментарии</h1>
    </header>
    <main>
      <router-view />
    </main>
    <footer>
      <p>&copy; 2024 Все права защищены</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

header {
  background-color: #34495e;
  color: white;
  padding: 10px 0;
}

footer {
  background-color: #ecf0f1;
  padding: 10px 0;
  font-size: 14px;
}
</style>
