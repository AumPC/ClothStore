'use strict'

function loadLogin () {
  document.getElementsByTagName('body')[0].className = 'gradient-bg';

  var div = createTag('div', 'text-center icon-login');
  var img = createTag('img', 'img-fluid', div);
  img.src = 'pic/icon_fullsize.png';

  var div = createTag('div', 'login text-center mb-3');
  var form = createTag('form', '', div);

  var formGroup = createTag('div', 'form-group', form);
  var input = createTag('input', 'login-form text-center', formGroup);
  input.setAttribute('type', 'text');
  input.setAttribute('placeholder', 'Username');
  input.id = 'username';

  var formGroup = createTag('div', 'form-group', form);
  var input = createTag('input', 'login-form text-center', formGroup);
  input.setAttribute('type', 'password');
  input.setAttribute('placeholder', 'Password');
  input.id = 'password';

  var buttonLogin = createTag('button', 'btn btn-raised btn-secondary', div);
  buttonLogin.setAttribute('type', 'button');
  buttonLogin.innerHTML = 'SIGN IN';
  buttonLogin.onclick = function(){
    document.getElementsByTagName('body')[0].className = '';
    window.location.href = 'snap.html';
  };
}
