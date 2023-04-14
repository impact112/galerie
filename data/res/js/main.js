function handleFormSubmit(formId, successFunction) {
  const form = document.getElementById(formId);
  if (!form) return;
  const dataFields = document.querySelectorAll("input, select, textarea");
  dataFields.forEach((field) => {
    field.addEventListener("input", () => {
      const errorElement = document.querySelector(`#${field.id}-errors`);
      if (errorElement) {
        errorElement.innerHTML = "";
      }
    });
  });
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const formData = new FormData(form);
    fetch(form.action, {
      method: "POST",
      body: formData,
    })
      .then((response) => {
        if (response.status === 400) {
          response.json().then((data) => {
            const errorMessages = Object.entries(data.errors);
            errorMessages.forEach(([field, message]) => {
              const errorElement = document.querySelector(`#${field}-errors`);
              errorElement.innerHTML = `<div class="alert alert-danger">${message}</div>`;
            });
          });
        } else if (response.status === 200) {
          response.json().then((data) => successFunction(data));
        }
      })
      .catch((error) => console.error(error));
  });
}

handleFormSubmit("login_form", function (data) {
  const params = new URLSearchParams(window.location.search);
  const redirect = params.get("redirect");
  if (redirect) window.location = redirect;
  else window.location = "/";
});

handleFormSubmit("register_form", function (data) {
  window.location = "/";
});

handleFormSubmit("upload_form", function (data) {
  window.location = `/post/${data.post}`;
});

handleFormSubmit("addtag_form", function (data) {
  window.location.reload();
});
