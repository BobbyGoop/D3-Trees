async function submitForm(e, form) {
    // 1. Prevent reloading page
    e.preventDefault();
    // 2. Submit the form
    // 2.1 User Interaction
    const btnSubmit = document.getElementById('btnSubmit');
    btnSubmit.disabled = true;
    setTimeout(() => btnSubmit.disabled = false, 2000);
    // 2.2 Build JSON body
    const jsonFormData = buildJsonFormData(form);
    console.log(jsonFormData)
    // 2.3 Build Headers
    const headers = { "Content-Type": "application/json" }
       
    // 2.4 Request & Response
    const response = await performPostHttpRequest(`/api/clients/`, headers, jsonFormData); // Uses JSON Placeholder
    console.log(response);
    //2.5 Inform user of result
    if(response)
        window.location.reload(true)
        //window.location = `/success.html?FirstName=${response.FirstName}&LastName=${response.LastName}&Email=${response.Email}&id=${response.id}`;
    else
        alert(`An error occured.`);
}


function buildJsonFormData(form) {
    const jsonFormData = { };
    for(const pair of new FormData(form)) {
        jsonFormData[pair[0]] = pair[1];
    }
    return jsonFormData;
}

async function performPostHttpRequest(fetchLink, headers, body) {
    if(!fetchLink || !headers || !body) {
        throw new Error("One or more POST request parameters was not passed.");
    }
    try {
        const rawResponse = await fetch(fetchLink, {
            method: "POST",
            headers: headers,
            body: JSON.stringify(body)
        });
        const content = await rawResponse.json();
        return content;
    }
    catch(err) {
        console.error(`Error at fetch POST: ${err}`);
        throw err;
    }
}
/*--/Functions--*/

/*--Event Listeners--*/
const sampleForm = document.querySelector("#sampleForm");
if(sampleForm) {
    sampleForm.addEventListener("submit", function(e) {
        submitForm(e, this);
    });
}

