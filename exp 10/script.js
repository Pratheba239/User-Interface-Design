document.getElementById('registrationForm').addEventListener('submit', function (e) {
    e.preventDefault();
  
    
    const name = document.getElementById('name');
    const email = document.getElementById('email');
    const password = document.getElementById('password');
    const confirmPassword = document.getElementById('confirmPassword');
  
    
    clearErrors();
  
  
    let isValid = true;
  
    if (validator.isEmpty(name.value)) {
      showError(name, 'Name is required');
      isValid = false;
    }
  
    if (!validator.isEmail(email.value)) {
      showError(email, 'Invalid email address');
      isValid = false;
    }
  
    if (!validator.isLength(password.value, { min: 6 })) {
      showError(password, 'Password must be at least 6 characters');
      isValid = false;
    }
  
    if (!validator.equals(password.value, confirmPassword.value)) {
      showError(confirmPassword, 'Passwords do not match');
      isValid = false;
    }
  
    if (isValid) {
      alert('Form submitted successfully!');
      
    }
  });
  
  function showError(input, message) {
    const formControl = input.parentElement;
    const small = formControl.querySelector('.error-message');
    small.innerText = message;
    small.style.display = 'block';
    input.style.borderColor = 'red';
  }
  
  function clearErrors() {
    const errorMessages = document.querySelectorAll('.error-message');
    const inputs = document.querySelectorAll('input');
    errorMessages.forEach((msg) => {
      msg.innerText = '';
      msg.style.display = 'none';
    });
    inputs.forEach((input) => {
      input.style.borderColor = '#ddd';
    });
  }
  