module.exports = {
  presets: [
    [
      '@vue/cli-plugin-babel/preset',
      {
        useBuiltIns: 'entry', // Добавление полифилов для старых браузеров
        corejs: 3, // Версия core-js (для современных функций)
      },
    ],
  ],
};
