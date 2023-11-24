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

// For Subscriber Form
// function subscribe() {
//     // Get the email input value
//     var emailInput = document.getElementById("{{ subs_form.email.id_for_label }}");
//     var email = emailInput.value;

//     // Send data to the server using Fetch API
//     fetch("{% url 'subscribe' %}", {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json",
//             "X-CSRFToken": "{{ csrf_token }}", // Include CSRF token if needed
//         },
//         body: JSON.stringify({email: email}),
//     })
//     .then(response => response.json())
//     .then(data => {
//         // Handle the response data
//         if (data.status === 'success') {
//             // Display a success popup
//             Swal.fire({
//                 title: data.message,
//                 icon: 'success',
//                 confirmButtonText: 'OK'
//             });
//         } else {
//             // Display an error popup
//             Swal.fire({
//                 title: 'Error',
//                 text: data.message,
//                 icon: 'error',
//                 confirmButtonText: 'OK'
//             });
//         }
//     })
//     .catch(error => {
//         console.error('Error:', error);
//         // Handle errors as needed (e.g., display an error message)
//     });

//     // Optionally, you can clear the form input
//     emailInput.value = '';

//     // Prevent the form from submitting in the traditional way
//     return false;
// }


// Another

// function subscribe() {
//     // Get the email input value
//     var emailInput = document.getElementById("{{ subs_form.email.id_for_label }}");
//     var email = emailInput.value;

//     // Send data to the server using Fetch API with CSRF token
//     fetch("{% url 'subscribe' %}", {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json",
//             "X-CSRFToken": "{{ csrf_token }}",
//         },
//         body: JSON.stringify({ email: email }),
//     })
//     .then(response => response.json())
//     .then(data => {
//         // Handle the response data
//         if (data.status === 'success') {
//             // Display a success popup on the same page
//             showPopup('success', data.message);
//         } else {
//             // Display an error popup on the same page
//             showPopup('error', data.message);
//         }
//     })
//     .catch(error => {
//         console.error('Error:', error);
//         // Handle errors as needed (e.g., display an error message)
//     });

//     // Optionally, you can clear the form input
//     emailInput.value = '';

//     // Prevent the form from submitting in the traditional way
//     return false;
// }

// function showPopup(type, message) {
//     // Create a new element for the popup
//     var popup = document.createElement('div');
//     popup.className = 'popup ' + type; // You can style 'popup' and 'success'/'error' in your CSS

//     // Create a text node with the message
//     var textNode = document.createTextNode(message);

//     // Append the text node to the popup
//     popup.appendChild(textNode);

//     // Append the popup to the body or another container element
//     document.body.appendChild(popup);

//     // Remove the popup after a certain duration (e.g., 3 seconds)
//     setTimeout(function() {
//         document.body.removeChild(popup);
//     }, 3000); // Adjust the duration as needed
// }


// And Another

// function subscribe(event) {
//     event.preventDefault(); // Prevent the default form submission behavior

//     var form = document.getElementById('subs_form');
//     var formData = new FormData(form);

//     // Use fetch to send a POST request to the server
//     fetch(form.action, {
//         method: 'POST',
//         body: formData,
//     })
//     .then(response => response.json())
//     .then(data => {
//         // Display the success or error message in a popup
//         if (data.message === 'success') {
//             alert('Email added successfully.');
//         } else if (data.message === 'error') {
//             console.log(data.message)
//             alert('Email already exists in the newsletter.');
//         }
//     });
// }

// Yet Another
// .then(function(data) {
//     console.log('Received the following response:', data);

//     // Check for success or error messages in the response
//     if (data.toLowerCase().includes('success')) {
//         alert('Email added successfully.');
//     } else if (data.toLowerCase().includes('error')) {
//         console.log('Error message:', data);
//         alert('Email already exists in the newsletter.');
//     } else {
//         console.log('Unexpected response:', data);
//         alert('Unexpected response from the server.');
//     }
// })


