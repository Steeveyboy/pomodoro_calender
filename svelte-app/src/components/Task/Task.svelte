
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
            descBoxHeight = (descBox.children[0].offsetHeight*0.06 + 1 + "rem");
            // descBox.children[0].style.border = "1px dotted";
        }
        else{
            descBoxHeight = "0rem";
            // descBox.children[0].style.border = "0px none";    
        }
    };

    const selectTask = event => {
        // let sendOff = {text: inputText.value, periods: tomatos, description:description.value, dueDate: duedate};
        console.log("egg");
        // periodsComplete += 1;
        // text.periodsComplete +=1;
        dispatch("select", {props: text, component: task});
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
        <a>Deadline</a>
    </div>
    <div class="description" bind:this={descBox} style="--box-height: {descBoxHeight};">
        <article>
            {text.description}
        </article>
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
        align-self: center;
        margin: auto;
        height: var(--box-height);
        transition: height 0.15s linear; 
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
        transition: opacity 0.2s 0.1s linear, height 0.25s linear;
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
