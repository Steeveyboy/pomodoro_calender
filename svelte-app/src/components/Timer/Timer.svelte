
<script>
    import { run } from "svelte/internal";
    import { createEventDispatcher } from "svelte";
    const dispatch = createEventDispatcher();

    let running = false;
    let duration = 1200;
    let timer = duration;
    let stringTime;

    function setRunning() {
        running = !running;
        if(running){
            document.querySelector(".timerButtons > button:nth-child(1)").innerHTML = "pause timer";
            document.querySelector(".timerButtons > button:nth-child(2)").hidden = false;
        }
        else{
            document.querySelector(".timerButtons > button:nth-child(1)").innerHTML = "start timer";
            document.querySelector(".timerButtons > button:nth-child(2)").hidden = true;
        }
    }

    function skipTimer() {
        setRunning();
        dispatch("timerDone");
        timer = duration;
        timeToString();
    }

    function timeToString() {
        var seconds = timer%60;
        var minutes = Math.floor(timer/60);
        stringTime = (("0" + minutes).slice(-2) + ":" + ("0" + seconds).slice(-2));
    }

    timeToString()

    setInterval(function (){
        if(running){
            timer -= 1;
            if(timer == 0){
                running = false;
                dispatch("timerDone");
                timer = duration;
            }
            timeToString();
        }
    }, 1000);
    
      
</script>

<div class="timer-container">
    <h1 id="countdown">{stringTime}</h1>
    <div class="timerButtons">
        <button on:click={setRunning}>start timer</button>
        <button on:click={skipTimer} hidden=true>skip</button>
    </div>
    
</div>

<style type="text/css">
    .timer-container {
        max-width: 40rem;
        padding: 2rem;
        margin: auto;
        vertical-align: middle;
        background-color: #f34b48e0;
        border-radius: 7px;
        border-style: solid;
        border-width: 1px;
    }
    .timer-container h1 {
        color: rgb(243, 243, 222);
        font-size: 8rem;
        margin: 1rem;
        /* font-family:'Courier New'; */
    }

    .timer-container button {
        border-radius: 5px;
        font-size: x-large;
        font-weight: bold;
        color: rgba(255, 30, 0, 0.705);
        background-color:rgb(243, 243, 222);
        cursor: pointer;
    }

</style>


