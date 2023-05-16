const form = document.querySelector('form');
const inputs = form.querySelectorAll('input');
const errorMessage = document.getElementById('error-message');

form.addEventListener('submit', (event) => {
  event.preventDefault();
  let isValid = true;

  inputs.forEach((input) => {
    if (input.id === 'celular') {
      // Validate celular field
      const celularRegex = /^\d{11}$/; // Update regex to match 11 digits
      if (!celularRegex.test(input.value)) {
        isValid = false;
        input.classList.add('error');
        errorMessage.textContent = 'O celular deve ter 11 dígitos';
        errorMessage.style.display = 'block'; // Display error message
      } else {
        input.classList.remove('error');
      }
    } else if (input.value.trim() === '') {
      // Validate other fields
      isValid = false;
      input.classList.add('error');
    } else {
      input.classList.remove('error');
    }
  });

  if (isValid) {
    // Submit form and redirect to success page
    form.submit();
    window.location.href = 'success.html';
  }
});

const celularField = document.getElementById('celular');
celularField.addEventListener('keypress', (event) => {
  const key = event.key;
  if (isNaN(key)) {
    event.preventDefault();
  }
});