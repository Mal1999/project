document.addEventListener('DOMContentLoaded', function () {
    const loginBtn = document.getElementById('loginBtn');
    const loginPageBtn = document.getElementById('loginPageBtn');
    const registerLink = document.getElementById('registerLink');
    const loginPage = document.getElementById('loginPage');
    const loginForm = document.getElementById('loginForm');

    loginBtn.addEventListener('click', () => showLogin());
    loginPageBtn.addEventListener('click', () => showLogin());
    registerLink.addEventListener('click', () => showRegister());

    function showLogin() {
        loginPage.style.display = 'block';
    }

    function showRegister() {
        window.location.href = 'register.html';
    }

    function login() {
        // Add logic for handling login (can be done on the server side)
        alert('Login logic goes here');
        // Redirect to the dashboard or another page
        window.location.href = 'dashboard.html';
    }
});
