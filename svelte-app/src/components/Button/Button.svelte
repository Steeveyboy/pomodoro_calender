
<script>
    import { createEventDispatcher } from "svelte";
    
    const dispatch = createEventDispatcher();
    
    export let props;

    const onClick = event => {
        dispatch("click", event);
    };

</script>

<button on:click={onClick}>
    <div class="buttonText">{props.text}</div>
</button>

<style type="text/css">
    button {
        border-radius: 1px;
        /* border-radius: ; */
    }
</style>
