
<script>

    let tomatos = 0;
    let descBox;
    let descBoxHeight = "0rem";

    import { createEventDispatcher } from "svelte";
    const dispatch = createEventDispatcher();

    let props;
    // let mouseOver = false;
    // const mouseCover = event => {
    //     mouseOver = !mouseOver;
    // };

    

    const viewDescription = event => {
        console.log(descBox);
        if(descBoxHeight == "0rem"){descBoxHeight = ("6rem");}
        else{descBoxHeight = "0rem";}
    };

    const viewDate = event => {
        // console.log(descBox);
        // if(descBoxHeight == "0rem"){descBoxHeight = ("6rem");}
        // else{descBoxHeight = "0rem";}
    };

    const mouseLeave = event => {
        descBoxHeight = "0rem";
    };

    const showDetails = event => {
        let dets = document.getElementsByClassName("taskMaker")[0].getElementsByClassName("hiddenDetails")[0];
        if(dets.style.display == "flex" && !mouseOver){
            dets.style.display = "none";
        }
        else{
            dets.style.display = "flex";
        }
    };

    const submitTask = event => {
        console.log(event.key);
        if(event.key == 'Enter'){
            let inputText = document.getElementById("inputText");
            let description = document.getElementsByTagName("textArea")[0];
            let duedate = new Date(2022,3,14,23,56);
            let sendOff = {id: text.id, text: inputText.value, periods: tomatos, description:description.value, dueDate: duedate};
            dispatch("change", sendOff);
            inputText.value = "";
            tomatos = 0;
            description.value="";
        }
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

<div class="task taskMaker" on:mouseleave={mouseLeave}>
    <div class="headings">
        <div class="taskText">
            <input type="text" id="inputText" class="inputText" placeholder="Make Task" on:keypress={submitTask} on:focus={showDetails} on:blur={showDetails}>
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
    <div class="hiddenDetails" >
        <a on:click={viewDescription}>Description</a>
        <a on:click={viewDate}>Deadline</a>
    </div>
    <div class="description" bind:this={descBox} style="--box-height: {descBoxHeight};">
        <textarea placeholder="Write Here.."></textarea>
    </div>
</div>

<style>

    textarea {
        /* visibility: collapse; */
        width: 90%;
        height: 90%;
        /* overflow-x: scroll; */
        resize: none;
        
        /* height: var(--box-height); */
    }

    .description {
        width: 90%;
        align-self: center;
        margin: auto;
        height: var(--box-height);
        transition: height 0.15s linear; 
    }

    .durationButtons button{
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
        height: 0rem;
        visibility: hidden;
        width: 100%;
        padding-bottom: 2px;
        justify-content: space-evenly;
        opacity: 0;
        transition: opacity 0.2s 0.1s linear, height 0.25s linear;
    }

    .inputText::placeholder {
        color: #333;
        font-size: 1.17rem;
        font-weight: bold;
    }

    .taskMaker {
        max-width: 44rem;
        width: 100%;
        background-color: rgba(143, 126, 125, 0.562);
        border-radius: 7px;
        margin: auto;
        overflow: hidden;
        cursor: pointer;
        height: fit-content;
        margin-top: 0.5rem;
    }

    .taskMaker .taskText{
        text-align: center;
        align-items: center;
        width: 80%;
    }

    .taskMaker:hover {     
        background-color: rgb(243, 243, 222);
    }

    .taskMaker:hover .hiddenDetails{   
        visibility: visible;
        opacity: 100%;
        height: 2rem;
        display: flex;
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
