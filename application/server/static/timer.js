const timer = document.getElementById("timer")
const timerbutton = document.getElementById("button-2")
let timerOn = false

    function startTimer(duration, display) {
        var timer = duration, minutes, seconds;
        setInterval(function () {
            minutes = parseInt(timer / 60, 10);
            seconds = parseInt(timer % 60, 10);

            minutes = minutes < 10 ? "0" + minutes : minutes;
            seconds = seconds < 10 ? "0" + seconds : seconds;

            display.textContent = minutes + ":" + seconds;

            if (--timer < 0) {
                timer = duration;
            }
        }, 1000);
    }

    timerbutton.onclick = function () {
        if (timerOn == false) {
            let display = document.getElementById('time');
            startTimer(60 * 4, display);
            timerOn = true
        }
    };