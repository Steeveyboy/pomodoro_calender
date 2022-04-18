<script>
    import { createEventDispatcher } from "svelte";
    
</script>


<div class="navbar">
    <ul class="horizontal ws-black">
        <li style="float: left;"><a class="logo">PomoCalender</a></li>
        <li><a><i style='font-size:16px' class='far'>&#xf185</i> Settings</a></li>
    </ul>
</div>

<style type="text/css">
    .logo {
        font-family: 'Lobster', cursive;
        font-weight:500;
    }
    .ws-black {
        background-color: #cd615e!important;
        color: white!important;
    }
    li {
        float: right;
    }
    ul {
        border-radius: 4px;
        list-style-type: none;
        margin: 0;
        padding: 0;
        overflow: hidden;
    }
    li a {
        cursor: pointer;
        display: block;
        color: white;
        text-align: center;
        padding: 14px 16px;
        text-decoration: none;
    }
    li a:hover:not(.logo) {
        background-color: rgba(151, 82, 82, 0.603);
    }

</style>
