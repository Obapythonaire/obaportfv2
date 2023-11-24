// 1 This worked but not with bs-theme=auto/light/dark and not storing user preference
// const modeToggle = document.getElementById("modeToggle");
// const body = document.body

// modeToggle.addEventListener("click", function () {
//     document.body.classList.toggle("dark-mode");
// });


// 5 This worked with bs-theme=auto/light/dark and not storing user preference

// function myFunction() {
//     var element = document.body;
//     element.dataset.bsTheme =
//         element.dataset.bsTheme == "light" ? "dark" : "light";
// }

// 6 to accomodate user preference
function myFunction() {
    var element = document.body;
    var currentTheme = element.dataset.bsTheme === "light" ? "dark" : "light";

    // Toggle between light and dark themes
    element.dataset.bsTheme = currentTheme;

    // Save the user's preference to localStorage
    localStorage.setItem('themePreference', currentTheme);
}

// Check user's saved preference and apply it when the page loads
document.addEventListener("DOMContentLoaded", function() {
    var savedTheme = localStorage.getItem('themePreference');

    if (savedTheme) {
        document.body.dataset.bsTheme = savedTheme;
    }
});
