<script>
  import { onMount } from "svelte";

  let weights = [];

  onMount(async () => {
    const res = await fetch("http://localhost:5001/weights");
    weights = await res.json();
  });
  $: latestWeight = weights[weights.length - 1];
</script>

<div class="stats-box hover:brightness-110 transition">
  <div class="relative h-full">
    <p class="text-2xl text-white">{latestWeight?.weight || "--"} lbs</p>
    <div bind:this={chartDiv}></div>

    <p class="absolute right-0 bottom-0 pr-2 text-gray-600">stats</p>
  </div>
</div>

<style>
  .stats-box {
    border: 0.1px solid rgb(65, 68, 69); 
    background-color: rgb(34, 38, 44);
    width: 21vw;
    height: 50vh;
    border-radius: 8px;
    background: linear-gradient(
      to bottom,
      rgb(34, 38, 44) 10%,
      rgb(34, 38, 44) 10%
    );
    box-shadow:
      0 4px 6px rgba(0, 0, 0, 0.3),
      0 1px 3px rgba(0, 0, 0, 0.2);
  }
</style>
