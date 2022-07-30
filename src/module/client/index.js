// How to access html components from jscript
const button = document.getElementById("the-button");
const data = document.getElementById("data");

const first_key = "make";
const second_key = "model";

// Map of maps, one to one to one relationship
const cars = [
    {first_key: "Porsche", second_key: "9115"},
    {first_key: "Mercedes-Benz", second_key: "220SE"},
    {first_key: "Jaguar", second_key: "Mark VII"},
];

button.onclick = function() {  // This is how you 'set' a func
    /**
     * Apparently, this works on everything except
     * firefox. A little annoying, but not the worst.
     * 
     * As well, it's only a local host error, so for
     * a prototype, it doesn't make the project look bad.
     * 
     * The main thing is it takes very little effort
     * to \'jsonify'/ something and send it locally
     * to the frontend. As well, this may be multithreaded
     * by nature of it being an 'on click' event.
     * 
     */
    const url = "https://localhost:8080";
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        },
        body:JSON.stringify(cars)}).then(response => {
            if(response.ok) {
                return response.json();
            } else {
                alert("something is wrong");
            }
        })
        .then(jsonResponse => {    
            console.log(jsonResponse);
        })
    // Log the Error
    .catch((err) => console.error(err));
}
