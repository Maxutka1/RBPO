module.exports = {
  extends: ['plugin:security/recommended'],
  plugins: ['security', 'no-secrets'],
  rules: {
    'no-secrets/no-secrets': 'error',
    'security/detect-eval-with-expression': 'error'
  }
};
