
<script>

    let tomatos = 0;
    import { createEventDispatcher } from "svelte";
    const dispatch = createEventDispatcher();

    let props;

    const onClick = event => {
        let inputText = document.getElementById("inputText")
        let sendOff = {text: inputText.value, periods: tomatos}
        dispatch("change", sendOff);
        inputText.value = "";
    };

</script>

<div class="task taskMaker">
    <div class="taskText">
        <input type="text" id="inputText" class="inputText" placeholder="Make Task" on:change={onClick}>
    </div>
    <div class="tomatos">
       <p>{tomatos}</p>
       <img src="timer.png" alt="" style="width:1.5rem; display:inline-block; margin-top:10px;"> 
    </div>
</div>

<style>
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

    .inputText::placeholder {
        color: #333;
        font-size: 1.17rem;
        /*margin-block-start: 1em;
        margin-block-end: 1em;
        margin-inline-start: 0px;
        margin-inline-end: 0px;*/
        font-weight: bold;
    }


    .taskMaker {
        justify-content: center;
        cursor: pointer;
        display: flex;
        max-width: 44rem;
        width: 100%;
        background-color: rgba(143, 126, 125, 0.562);
        border-radius: 7px;
        margin: auto;
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
