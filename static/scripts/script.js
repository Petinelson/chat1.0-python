document.querySelector('#show-register').addEventListener('click', () => {    
    document.querySelector('#login-form').style.display = 'none'
    document.querySelector('#register-form').style.display = 'block'
  })
  
  document.querySelector('#show-login').addEventListener('click', () => {
    document.querySelector('#login-form').style.display = 'block'
    document.querySelector('#register-form').style.display = 'none'
  })
  