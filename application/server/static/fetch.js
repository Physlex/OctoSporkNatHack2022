base_fetch_url = "http://127.0.0.1:5000"

const connect_button = document.getElementById("muse-connect-button")
connect_button.onclick = async() => {
    fetch_url = base_fetch_url + "/muse/connecting?muse_id=0";
    options = {
        method:'GET',
        mode: 'same-origin'
    };
    const response = await fetch(fetch_url, options);
    converted_response = response.json();
    console.log(converted_response);
    return converted_response;
}

const record_button = document.getElementById("muse-record-button")
record_button.onclick = async() => {
    fetch_url = base_fetch_url + "/muse/recording?duration=120";
    options = {
        method: 'GET',
        mode: 'same-origin',
        cache: 'default',
        headers: {'Content-Type': 'application/json'}
    };
    const response = await fetch(fetch_url, options);
    converted_response = response.json();
    console.log(converted_response);
    return converted_response;
}
