
<script>

    let tomatos = 0;
    import { createEventDispatcher } from "svelte";
    const dispatch = createEventDispatcher();

    let props;
    let mouseOver = false;
    const mouseCover = event => {
        mouseOver = !mouseOver;
    };

    const showDetails = event => {
        console.log(event);
        let dets = document.getElementsByClassName("taskMaker")[0].getElementsByClassName("hiddenDetails")[0];
        if(dets.style.display == "flex" && !mouseOver){
            dets.style.display = "none";
        }
        else{
            dets.style.display = "flex";
        }
    };

    const onClick = event => {
        let inputText = document.getElementById("inputText")
        let sendOff = {text: inputText.value, periods: tomatos}
        dispatch("change", sendOff);
        inputText.value = "";
    };

    const increment = event => {
        tomatos += 1;
    };
    const decrement = event => {
        if(tomatos > 0){
            tomatos -= 1;
        }
    };

</script>

<div class="task taskMaker" on:pointerover={mouseCover} on:pointerout={mouseCover}>
    <div class="headings">
        <div class="taskText">
            <input type="text" id="inputText" class="inputText" placeholder="Make Task" on:change={onClick} on:focus={showDetails} on:blur={showDetails}>
        </div>
        <div class="tomatos">
            <p>{tomatos}</p>
            <img src="timer.png" alt="" style="width:1.5rem; display:inline-block; margin-top:10px;"> 
        </div>
        <div class="durationButtons">
            <button on:click={increment}>Up</button>
            <button on:click={decrement}>Dn</button>
        </div>
    </div>
    <div class="hiddenDetails">
        <a>Description</a>
        <a>Deadline</a>
    </div>
</div>

<style>
    .durationButtons button{
        /* display: flex; */
        font-size: 0.6rem;
    }

    .durationButtons {
        display: inline-grid;
        align-self: center;
        padding-left: 1rem;
    }

    .inputText {
        background-color: rgba(143, 126, 125, 0.0);
        outline: none;
        border: none;
        margin-top: 6px;
        width: 100%;
        height: 80%;
        color: #333;
        font-size: 1.17em;
        font-weight: bold;
    }

    .headings {
        display: flex;
        /* justify-content: center; */
        padding-left: 6%;
    }

    .hiddenDetails {
        /* display: none; */
        
        visibility: hidden;
        width: 100%;
        padding-bottom: 2px;
        justify-content: space-evenly;
        display: flex;
        opacity: 0;
        transition: opacity 0.2s 0.1s linear;
    }

    .inputText::placeholder {
        color: #333;
        font-size: 1.17rem;
        font-weight: bold;
    }

    .taskMaker {
        justify-content: center;
        cursor: pointer;
        /* display: flex; */
        max-width: 44rem;
        width: 100%;
        background-color: rgba(143, 126, 125, 0.562);
        border-radius: 7px;
        margin: auto;
        height: 4rem;
        margin-top: 0.5rem;
        transition: height 0.3s;
    }

    .taskMaker .taskText{
        text-align: center;
        align-items: center;
        width: 80%;
    }

    .taskMaker:hover {     
        background-color: rgb(243, 243, 222);
        height: 6rem;
    }

    .taskMaker:hover .hiddenDetails{     
        opacity: 100%;
        visibility: visible;
        position: relative;
    }

    .tomatos {
        display: inline-block;
        text-align: right;
    }
    
    .taskText {
        text-align: left;
        width: 80%;
    }

    .tomatos p{
        font-size: larger;
        font-weight: bold; 
        display: inline-block;
    }

</style>
