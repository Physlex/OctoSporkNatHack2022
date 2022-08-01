base_fetch_url = "http://127.0.0.1:5000"

const record_button = document.getElementById("start-test")
record_button.onclick = async() => {
    fetch_url = base_fetch_url + "/muse/recording?duration=120";
    options = {
        method: 'GET',
        mode: 'same-origin',
        cache: 'default',
        headers: {'Content-Type': 'application/json'}
    };
    const response = await fetch(fetch_url, options);
    let json_response = response.json();
    console.log(json_response);
    return json_response;
}

const display_button = document.getElementById("display-button")
display_button.onclick = async() => {
    fetch_url = base_fetch_url + '/muse/display';
    options = {
        method: 'GET',
        mode: 'same-origin',
        cache: 'default',
        headers: {'Content-Type': 'applica'}
    }
}
