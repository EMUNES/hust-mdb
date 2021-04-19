module.exports = {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      backgroundImage: theme => ({
        'head-background': "url('./src/assets/hust-background.jpg')",
        'hust-bg-full': "url('./src/assets/hust-bg-full.png')"
      }),
      transitionDuration: {
        '1500': '1500ms',
        '2000': '2000ms',
        '3000': '3000ms'
      },
      transitionDelay: {
        '1500': '1500ms',
        '2000': '2000ms',
        '2500': '2500ms',
        '3000': '3000ms',
        '3500': '3500ms'
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
