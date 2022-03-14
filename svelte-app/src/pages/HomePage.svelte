<script>
    import {Timer} from '../components/Timer';
    import {Task, TaskMaker } from '../components/Task';
    import {TaskContainer} from '../components/TaskContainer';

	let taskContainer;

    let headerMessage = "Welcome To Pomodoro Timer";

    function selectedTask(event) {
      headerMessage = event.detail.props.name;
    };

	function timerDone(event){
		taskContainer.testIt()
	}


</script>

<div class="home-page">
    <h1>{headerMessage}</h1>
    <!-- <iframe title="calendar" src="https://calendar.google.com/calendar/embed?height=300&wkst=1&bgcolor=%23ffffff&ctz=America%2FToronto&showTz=0&showCalendars=0&showTabs=1&showPrint=0&showDate=1&showNav=1&showTitle=0&src=am9uYXRoYW4ucXN0ZWV2ZXNAZ21haWwuY29t&color=%23039BE5" style="border-width:0" width="500" height="300" frameborder="0" scrolling="no"></iframe> -->

    <Timer on:timerDone={timerDone}/>
    <TaskContainer bind:this={taskContainer} on:select={selectedTask}/>
    <h1>DONE</h1>

</div>

<style type="text/css">
    .home-page {
      flex-direction: column;
      max-width: 45rem;
      margin: auto;
      text-align: center;
      align-items: center;
    }
  </style>
