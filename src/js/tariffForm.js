// Уязвимость: потенциальный XSS через innerHTML
function displayTariff(userInput) {
    document.getElementById('output').innerHTML = userInput;
}

// Уязвимость: опасный eval
function processExpression(expr) {
    eval(expr);
}
