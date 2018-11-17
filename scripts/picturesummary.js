'use strict'

function loadPictureSummary() {

  createProgressBar();
  
  var row = createTag('div', 'row');
  row.innerHTML = 'Your Car';
  renderImages();

  row = createTag('div', 'row');
  row.innerHTML = 'Disputant Car';
  renderImages();

  row = createTag('div', 'row');
  row.innerHTML = 'ID card Picture';


  row = createTag('div', 'row');
  row.innerHTML = 'Driver card Picture';

  row = createTag('div', 'row');
  var buttonProceed = createTag('a', 'btn btn-outline-primary btn-sm');
  buttonProceed.innerHTML = 'Proceed';
  buttonProceed.id = 'button-proceed'

  buttonProceed.onclick = function() {
    window.location.href = 'QR.html';
  }
}

function renderImages() {
  var img;
  for (let i = 0; i < 4; i++) {
    img = createTag('img', 'm-1');
    if (images[i]) {
      img.src = images[i];
    } else {
      img.src = 'http://weknowyourdreams.com/images/unicorn/unicorn-04.jpg';
    }
    img.style.height = '120px';
    img.style.width = '120px';
  }
}
