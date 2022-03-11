
<script>
    export let text;
    console.log("being Created ");
</script>

<div class="task">
    <div class="headings">
        <div class="taskText">
            <h3 class="taskText">{text.name}</h3>
        </div>
        <div class="tomatos">
            <p>{text.periodsComplete}/{text.periods}</p>
        </div>
    </div>
    <div class="hiddenDetails">
        <a>Description</a>
        <a>Deadline</a>
    </div>
</div>

<style>

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
        /* justify-content: center; */
        /* display: flex; */
        max-width: 44rem;
        width: 100%;
        background-color: rgb(243, 243, 222);
        border-radius: 7px;
        margin: auto;
        margin-top: 0.5rem;
        cursor: pointer;
        height: 4rem;
        transition: height 0.3s;
    }

    .task:hover {
        border: 2px solid;
        height: 6rem;
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


    .task:hover .hiddenDetails{
        /* transform: scaleY(0); */
        
        height: 2rem;
        opacity: 100%;
        visibility: visible;
        position: relative;
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
