
<script>
    export let text;
    console.log("being Created ");
</script>

<div class="task">
    <h3 class="taskText">{text.name}</h3>
    <div class="tomatos">
       <p>{text.periodsComplete}/{text.periods}</p>
    </div>
</div>

<style>
    .task {
        justify-content: center;
        display: flex;
        max-width: 44rem;
        width: 100%;
        background-color: rgb(243, 243, 222);
        border-radius: 7px;
        margin: auto;
        margin-top: 0.5rem;
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
