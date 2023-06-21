window.onload = () => {
    /* Pomodoro */
    let workTime;
    let breakTime;
    let restTime;
    let timesCompleted; /* Tiempos completados */
    let cyclesGoal;
    let cyclesCompleted = 0;

    /* Timer */
    let currentTime = 1; /* Minutos seteados */
    let seconds = 0;

    function timer(){
        if(currentTime > 0 || seconds > 0){
            if(seconds == 0){
                seconds = 59;
                currentTime--;
            } else{
                seconds--;
            }
            updateClock();
            console.log(currentTime, seconds);
            setTimeout(timer, 1000);
        } else{
            pomodoroController();
        }
    }

    
    function pomodoroController(){
        if(isRestTime()){
            cyclesCompleted++;
            if(!goalReached()){
                currentTime = restTime;
                timer();
                timesCompleted = 0;
            } else{
                console.log("Pomodoro Finished!");
            }

            return;
        }
        if(timesCompleted % 2 == 0){
            currentTime = workTime;
            timesCompleted++;
            timer();
            console.log("Time to Work! TC:" + timesCompleted);
        } else{
            currentTime = breakTime;
            timesCompleted++;
            timer();
            console.log("Time to break! TC:" + timesCompleted);
        }
    }

    function isRestTime(){
        return timesCompleted == 7;
    }

    function goalReached(){
        return cyclesGoal == cyclesGoal;
    }



    /* Frontend Connection */
    let clock = document.getElementById("clock");
    let cyclesInput = document.getElementById("cycles-input");
    let startButton = document.getElementById("start-button");
    let workTimeInput = document.getElementById("work-time");
    let breakTimeInput = document.getElementById("break-time");
    let restTimeInput = document.getElementById("rest-time");


    
    /* Button funtionality */
    startButton.onclick = () => {
        populateVariables();
        startPomodoro();
    }

    function startPomodoro() {
        console.log("started pomodoro");
        pomodoroController();
    }

    function populateVariables(){
        console.log("populate variables");
        workTime = workTimeInput.value;   /* Minutos */
        breakTime = breakTimeInput.value;   /* Minutos */
        restTime = restTimeInput.value;    /* Minutos */
        cyclesGoal = cyclesInput.value;    
        timesCompleted = 0;
    }



    /* Clock */
    let clockMinutes;
    let clockSeconds;

    function updateClock() {
        clockMinutes = formatNumbers(currentTime);
        clockSeconds = formatNumbers(seconds);
        clock.innerHTML = clockMinutes + ":" + clockSeconds;
    }

    function formatNumbers(time){
        let formattedDigits;
        if(time < 10){
            formattedDigits = "0" + time;
        } else{
            formattedDigits = time;
        }

        return formattedDigits;
    }

};