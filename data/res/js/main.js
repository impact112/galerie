function handleFormSubmit(formId, successFunction) {
  const form = document.getElementById(formId);
  if (!form) return;
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(form);
    fetch(form.action, {
      method: 'POST',
      body: formData,
    })
      .then((response) => {
        if (response.status === 400) {
          response.json().then((data) => {
            const errorMessages = Object.entries(data.errors);
            errorMessages.forEach(([field, message]) => {
              const errorElement = document.querySelector(`#${field}-errors`);
              errorElement.innerHTML += `<div class="alert alert-danger">${message}</div>`;
            });
          });
        } else if (response.status == 200) {
          response.json().then((data) => successFunction(data));
        }
      })
      .catch((error) => console.error(error));
  });
}

handleFormSubmit('login_form', function (data) {
  window.location = '/';
});

handleFormSubmit('register_form', function (data) {
  window.location = '/';
});

handleFormSubmit('upload_form', function (data) {
  window.location = `/post/${data.post}`;
});