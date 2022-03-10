<script>
    import {Timer} from '../components/Timer';
    import {Task, TaskMaker } from '../components/Task';
    import {TaskContainer} from '../components/TaskContainer';
</script>

<div class="home-page">
    <h1>Welcome To Pomodoro Timer</h1>
    <Timer />
    <TaskContainer />
    <!-- <Task /> -->
    <!-- <TaskMaker/> -->

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
