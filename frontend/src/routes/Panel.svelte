<script>
  import Current from "./Current.svelte";
  import Stats from "./Stats.svelte";
  import Future from "./Future.svelte";

    import { onMount } from 'svelte';
  
  let currentTime = '';
  
  onMount(() => {
    // Update time immediately
    updateTime();
    
    // Update every second
    const interval = setInterval(updateTime, 1000);
    
    // Cleanup when component is destroyed
    return () => clearInterval(interval);
  });
  
  function updateTime() {
    const now = new Date();
    currentTime = now.toLocaleTimeString();
  }

</script>

<div class="bar hover:brightness-110 transition pl-2">{currentTime}</div>

<div class="cards">
  <Stats />
  <Current />
  <Future />
</div>

<style>
  .bar {
    border: 0.01px, rgb(98, 101, 103), solid;
    border-radius: 3px;
    width: 80vw;

    margin: auto;
    margin-top: 1vh;
    margin-bottom: 15vh;
    background-color: rgb(34, 38, 44);
    color: rgb(107, 111, 121);
     box-shadow:
      0 4px 6px rgba(0, 0, 0, 0.2),
      0 1px 3px rgba(0, 0, 0, 0.1);
  }
  .cards {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 80vw;
    margin-left: 5vw;
    margin-right: 5vw;
    margin: auto;
  }
</style>
