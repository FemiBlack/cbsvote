module.exports = {
  root: true, // set to true
  env: {
    node: true,
  },
  extends: [
    'plugin:vue/recommended',
    // '@vue/airbnb',
  ],
  parserOptions: {
    parser: 'babel-eslint', // uncomment
    sourceType: 'module',
    // allowImportExportEverywhere: true
  },
  rules: {
    'import/no-named-as-default': 0,
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
  },
};
