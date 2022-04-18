<script>
    import { TaskMaker, Task } from "../Task";
    import { createEventDispatcher, onMount } from "svelte";

    // let ex = {id:0, name:"First Task", periods:4, periodsComplete:0, description:"This is task 1 description. Its not too long", dueDate: new Date(2022,3,13,23,56)};
    // let ex2 = {id:1, name:"Second Task", periods:2, periodsComplete:0, description:"Task 2 is fairly long, probably a few lines \n, might have a list: \n\t eggs \n\t bacon \n\t toast \n\t jus egg salad bacon cheese berger salad days peanute butter chocolate chocolate lorem epsum is too difficult to look up", dueDate: new Date(2022,3,21,23,59)};
    
    const dispatch = createEventDispatcher();

    

    export let selectedTask = "";
    let tasks = [];

    export function testIt(){
        if(selectedTask == ""){
            return;
        }
        tasks[tasks.findIndex(t => t.id == selectedTask.props.id)].periodsComplete += 1;
        updateTasks;
    }

    export function updateTasks(){
        for(var i=0; i<tasks.length; i++){console.log(tasks[i].description)}
        localStorage.setItem('tasks', JSON.stringify(tasks));
        fetch("http://localhost:4000/updatetasks", {method:'POST', body:JSON.stringify({"tasks":tasks})});
    }

    function change(event) {
        let text = {name: event.detail.text, periods: event.detail.periods, description: event.detail.description, periodsComplete:0, dueDate:event.detail.dueDate};
        fetch("http://localhost:4000/addtask", {method:'POST', body:JSON.stringify(text)});
        tasks[tasks.length] = text;
    };

    function selectTask(event) {
        if(selectedTask != "") {selectedTask.component.style.border = "";}
        selectedTask = event.detail;            
        selectedTask.component.style.border = "2px solid black";
        dispatch("select", selectedTask);
    };

    onMount(() => {
        tasks = localStorage.getItem('tasks') != null ? JSON.parse(localStorage.getItem('tasks')) : [];
        console.log(tasks);
        let promise = fetch("http://localhost:4000/init", {method:'GET'})
        .then(response => response.json())
        .then(data => 
        {
            tasks=data.tasks;
            localStorage.setItem('tasks', JSON.stringify(tasks));
        });
    });

</script>


<div class="task-container">
    <div class="tasks">
        {#each tasks as taskDetails}
            <Task bind:text={taskDetails} on:select={selectTask} on:update={updateTasks}/>
        {/each}
    </div>
    <TaskMaker on:change={change}/>
</div>
