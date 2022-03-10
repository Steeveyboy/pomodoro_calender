
<script>
    import { run } from "svelte/internal";

    let running = false;

    function setRunning() {
        running = !running;
    }
    
    setInterval(function (){
        if(running){
            var time = document.getElementById("countdown").innerHTML;
            var minutes = parseInt(time.slice(0,time.indexOf(":")));
            var seconds = parseInt(time.slice(time.indexOf(":")+1));
            var remainder = minutes*60 + seconds - 1;
            document.getElementById("countdown").innerHTML = ("0"+Math.floor(remainder/60)).slice(-2) + ":" + ("0" + remainder%60).slice(-2);
        }
    }, 1000);
    
      
</script>

<div class="timer-container">
    <h1 id="countdown">25:00</h1>
    <button on:click={setRunning}>start timer</button>
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


