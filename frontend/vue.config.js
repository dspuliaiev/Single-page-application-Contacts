const path = require('path');

module.exports = {
  // Настройка базового пути для приложения
  publicPath: process.env.NODE_ENV === 'production' ? '/static/' : '/',
  
  // Настройка путей вывода
  outputDir: path.resolve(__dirname, '../static/'), // Папка, куда компилируются статические файлы для Django
  assetsDir: 'assets', // Каталог для хранения ассетов (CSS, JS, изображений)

  // Настройка прокси-сервера для разработки (перенаправление API-запросов на Django-сервер)
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000', // URL сервера Django
        changeOrigin: true,
        secure: false,
      },
      '/captcha': {
        target: 'http://localhost:8000', // Для CAPTCHA
        changeOrigin: true,
        secure: false,
      },
    },
  },

  // Настройка CSS (если используется SCSS или PostCSS)
  css: {
    loaderOptions: {
      scss: {
        additionalData: `@import "@/styles/global.scss";`, // Автоматическое подключение глобальных стилей
      },
    },
  },

  // Настройка Webpack для добавления alias и поддержки дополнительных плагинов
  configureWebpack: {
    resolve: {
      alias: {
        '@': path.resolve(__dirname, 'src'), // Короткий путь для импорта компонентов
      },
    },
  },

  // Включение анализа бандлов (для оптимизации)
  pluginOptions: {
    webpackBundleAnalyzer: {
      openAnalyzer: false, // Выключить автоматическое открытие
    },
  },

  // Настройка Source Maps (для отладки)
  productionSourceMap: false, // Отключение source maps в продакшене для меньшего размера файлов
};
