const form = document.querySelector('form');
const inputs = form.querySelectorAll('input');

form.addEventListener('submit', (event) => {
  event.preventDefault();
  let isValid = true;

  inputs.forEach((input) => {
    if (input.type === 'email') {
      // Validate email field
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(input.value)) {
        isValid = false;
        input.classList.add('error');
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
    form.submit();
  }
});