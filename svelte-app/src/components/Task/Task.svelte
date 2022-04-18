
<script>
    export let text;
    let task;
    let descBox;
    let descBoxHeight = "0rem";
    // export let periodsComplete = text.periodsComplete;

    import { createEventDispatcher } from "svelte";
    const dispatch = createEventDispatcher();

    const viewDescription = event => {
        if(descBoxHeight == "0rem"){
            descBox.children[0].hidden=false;
            descBox.children[1].hidden=true;
            descBoxHeight = (descBox.children[0].offsetHeight*0.06 + 1 + "rem");
        }
        else{
            descBoxHeight = "0rem";
            // descBox.children[0].style.border = "0px none";    
        }
    };

    const selectTask = event => {
        // let sendOff = {text: inputText.value, periods: tomatos, description:description.value, dueDate: duedate};
        // console.log("egg");
        // periodsComplete += 1;
        // text.periodsComplete +=1;
        dispatch("select", {props: text, component: task});
    };

    const editDescription = event => {
        let txt = descBox.innerText;
        descBox.children[0].hidden = true;
        descBox.children[1].hidden = false;
        descBox.children[1].innerText = txt;
        console.log(descBox.children[1]);
    };

    const submitEdits = event => {
        descBox.children[0].innerText = descBox.children[1].value;
        descBox.children[1].hidden = true;
        descBox.children[0].hidden = false;
        dispatch("update");
    };

    const mouseLeave = event => {
        descBoxHeight = "0rem";
    };

</script>

<div class="task" on:mouseleave={mouseLeave} bind:this={task} on:click={selectTask}>
    <div class="headings">
        <div class="taskText">
            <h3 class="taskText">{text.name}</h3>
        </div>
        <div class="tomatos">
            <p>{text.periodsComplete}/{text.periods}</p>
        </div>
    </div>
    <div class="hiddenDetails">
        <a id="taskDesc" on:click={viewDescription}>Description</a>
        <a id="taskDead">Deadline</a>
    </div>
    <div class="description" bind:this={descBox} style="--box-height: {descBoxHeight};">
        <article on:dblclick={editDescription} id="descriptionBox">
            {text.description}
        </article>
        <textarea hidden=true on:blur={submitEdits}></textarea>
    </div>
</div>

<style>
    
    article {
        border-radius: 7px;
        background-color: rgb(223 195 194 / 50%);
        padding: 3px;
    }
    .description {
        width: 90%;
        height: 90%;
        align-self: center;
        margin: auto;
        height: var(--box-height);
        transition: height 0.15s linear; 
    }

    textarea {
        width: 100%;
        height: 90%;
        resize: none;
        overflow: hidden;
        border-radius: 7px;
    }

    .headings {
        display: flex;
        padding-left: 6%;
        width: 100%;
    }
    .taskText {
        text-align: left;
        width: 80%;
    }

    .task {
        max-width: 44rem;
        width: 100%;
        background-color: rgb(243, 243, 222);
        border-radius: 7px;
        margin: auto;
        overflow: hidden;
        cursor: pointer;
        height: fit-content;
        margin-top: 0.5rem;
    }

    .hiddenDetails {
        height: 0rem;
        visibility: hidden;
        width: 100%;
        padding-bottom: 2px;
        justify-content: space-evenly;
        opacity: 0;
        transition: opacity 0.1s 0.1s linear, height 0.15s linear;
    }


    .task:hover .hiddenDetails{
        visibility: visible;
        opacity: 100%;
        height: 2rem;
        display: flex;
    }

    .tomatos{
        display: inline-block;
    }
    
    .taskText{
        text-align: left;
        width: 80%;
    }

    .tomatos p{
        font-size: larger;
        font-weight: bold;  
        
    }



</style>
