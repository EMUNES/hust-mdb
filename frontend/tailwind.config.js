module.exports = {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      backgroundImage: theme => ({
        'head-background': "url('./src/assets/hust-background.jpg')"
      })
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
