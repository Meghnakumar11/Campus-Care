const signUpBtn = document.getElementById("signUp");
const signInBtn = document.getElementById("signIn");
const container = document.getElementById("container");

// Panel switching
signUpBtn.addEventListener("click", () => {
    container.classList.add("right-panel-active");
});

signInBtn.addEventListener("click", () => {
    container.classList.remove("right-panel-active");
});


// -------------------------
// SIGNUP SUBMIT HANDLER
// -------------------------
document.getElementById("signupForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const username = document.getElementById("signup-username").value;
    const rollno = document.getElementById("signup-rollno").value;
    const email = document.getElementById("signup-email").value;
    const password = document.getElementById("signup-password").value;

    const res = await fetch("http://127.0.0.1:5000/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify({
            username,
            rollno,
            email,
            password
        })
    });

    const data = await res.json();
    alert(data.message || data.error);

    if (data.message) {
        // After successful signup → switch to login panel
        container.classList.remove("right-panel-active");
    }
});

// LOGIN SUBMIT HANDLER
document.getElementById("loginForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const userInput = document.getElementById("login-username").value;
    const password = document.getElementById("login-password").value;

    const res = await fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify({
            usern
