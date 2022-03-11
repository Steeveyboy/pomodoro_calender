<script>
    import { TaskMaker, Task } from "../Task";

    let ex = {name:"First Task", periods:4, periodsComplete:0};
    let ex2 = {name:"Second Task", periods:2, periodsComplete:0};

    
    let tasks = [ex, ex2];

    function test(event) {
        console.log(event.detail);
        let text = {name: event.detail.text, periods: event.detail.periods, periodsComplete:0};
        // tasks.slice(1);
        tasks[tasks.length] = text;
        // console.log(document.createElement("task/"));
    };


</script>


<div class="task-container">
    <div class="tasks">
        {#each tasks as taskDetails}
            <Task text={taskDetails}/>
        {/each}
    </div>
    <TaskMaker on:change={test}/>
</div>