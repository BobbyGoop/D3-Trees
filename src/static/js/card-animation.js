async function submitForm(e, form) {
  e.preventDefault();
  const btnSubmit = document.getElementById('btnSubmit');

  btnSubmit.disabled = true;
  setTimeout(() => btnSubmit.disabled = false, 2000);

  const jsonFormData = buildJsonFormData(form);
  console.log(jsonFormData)

  const headers = { "Content-Type": "application/json" }

  const response = await performPostHttpRequest(`/api/clients/`, headers, jsonFormData);
  console.log(response);

  if (response) window.location.reload(true);
  else alert(`Произошла ошибка сервера. Пожалуйста, повторите попытку позже.`);
}

function buildJsonFormData(form) {
  const jsonFormData = {};
  for (const pair of new FormData(form)) {
    console.log(pair)
    jsonFormData[pair[0]] = pair[1];
  }
  return jsonFormData;
}

async function performPostHttpRequest(fetchLink, headers, body) {
  if (!fetchLink || !headers || !body) {
    throw new Error("One or more POST request parameters was not passed.");
  }
  try {
    const rawResponse = await fetch(fetchLink, {
      method: "POST",
      headers: headers,
      body: JSON.stringify(body)
    });
    return rawResponse.status;
  }
  catch (err) {
    console.error(`Error at fetch POST: ${err}`);
    throw err;
  }
}

Date.prototype.toDateInputValue = (function () {
  let local = new Date(this);
  local.setMinutes(this.getMinutes() - this.getTimezoneOffset());
  return local.toJSON().slice(0, 10);
});

// Set data on date picker
document.getElementById('call-date').value = new Date().toDateInputValue();
//Movement Animation to happen
const card = document.querySelector(".card");
const container = document.querySelector(".container");
const sampleForm = document.querySelector("#sampleForm");

// send JSON data
sampleForm.addEventListener("submit", function (e) {
  submitForm(e, this);
});

//Moving Animation Event
container.addEventListener("mousemove", (e) => {
  let xAxis = (window.innerWidth / 2 - e.pageX) / 100;
  let yAxis = (window.innerHeight / 2 - e.pageY) / 100;
  card.style.transform = `rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;
});
//Animate In
container.addEventListener("mouseenter", (e) => {
  card.style.transition = "none";
});
//Animate Out
container.addEventListener("mouseleave", (e) => {
  card.style.transition = "all 0.5s ease";
  card.style.transform = `rotateY(0deg) rotateX(0deg)`;
});