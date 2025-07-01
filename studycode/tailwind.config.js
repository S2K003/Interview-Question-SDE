/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      animation: {
        'pulse': 'pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      },
      backdropBlur: {
        xs: '2px',
      },
      fontFamily: {
        mono: ['Fira Code', 'Monaco', 'Cascadia Code', 'Roboto Mono', 'monospace'],
      }
    },
  },
  plugins: [],
}