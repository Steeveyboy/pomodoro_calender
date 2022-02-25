
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
        /* min-height: 20rem; */
        max-width: 40rem;
        padding: 2rem;
        border-radius: 5px;
        margin: auto;
        vertical-align: middle;
        background-color: rgba(255, 30, 0, 0.781);
    }
    .timer-container h1 {
        color: rgb(243, 243, 222);
        font-size: 8rem;
        margin: 1rem;
        /* font-family:'Courier New'; */
    }
    .timer-container button {
        /* color: black; */
    }
</style>


