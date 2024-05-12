const openFormBtn = document.getElementById('openFormBtn');
const formPopup = document.getElementById('formPopup');

openFormBtn.addEventListener('click', () => {
  formPopup.style.display = 'block';
});

formPopup.addEventListener('submit', (event) => {
  event.preventDefault();
  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const phone = document.getElementById('phone').value;
  
  console.log(`Name: ${name}, Email: ${email}, Phone: ${phone}`);
  
  formPopup.style.display = 'none';
});