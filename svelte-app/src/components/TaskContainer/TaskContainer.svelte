<script>
    import { TaskMaker, Task } from "../Task";
    import { createEventDispatcher } from "svelte";

    let ex = {id:0, name:"First Task", periods:4, periodsComplete:0, description:"This is task 1 description. Its not too long", dueDate: new Date(2022,3,13,23,56)};
    let ex2 = {id:1, name:"Second Task", periods:2, periodsComplete:0, description:"Task 2 is fairly long, probably a few lines \n, might have a list: \n\t eggs \n\t bacon \n\t toast \n\t jus egg salad bacon cheese berger salad days peanute butter chocolate chocolate lorem epsum is too difficult to look up", dueDate: new Date(2022,3,21,23,59)};
    
    const dispatch = createEventDispatcher();

    export let selectedTask = "";
    let tasks = [ex, ex2];

    export function testIt(){
        console.log("here");
        if(selectedTask == ""){
            return;
        }
        tasks[tasks.findIndex(t => t.id == selectedTask.props.id)].periodsComplete += 1;
    }

    function change(event) {
        // console.log(event);
        let text = {name: event.detail.text, periods: event.detail.periods, description: event.detail.description, periodsComplete:0, dueDate:event.detail.dueDate};
        tasks[tasks.length] = text;
    };

    function selectTask(event) {
        if(selectedTask != "") {selectedTask.component.style.border = "";}
        selectedTask = event.detail;            
        selectedTask.component.style.border = "2px solid black";
        dispatch("select", selectedTask);
    };


</script>


<div class="task-container">
    <div class="tasks">
        {#each tasks as taskDetails}
            <Task bind:text={taskDetails} on:select={selectTask}/>
        {/each}
    </div>
    <TaskMaker on:change={change}/>
</div>
