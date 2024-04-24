fetch("http://localhost:8080/webhooks/rest/webhook", {
    method: "POST", // Assuming you are sending a POST request
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        message: "tell me the price of wheat"
    })
}).then(response => {
    if (response.ok) {
        return response.json();
    } else {
        throw new Error('Network response was not ok.');
    }
}).then(data => {
    console.log(data);
}).catch(error => {
    console.error('There was a problem with the fetch operation:', error);
});
