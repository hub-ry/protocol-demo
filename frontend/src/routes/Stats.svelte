<script>
  import { onMount } from "svelte";
  import { getWeights } from "$lib/weights.js";

  let weights = [];
  let firstDate = "Loading...";
  let currDate = "Loading...";
  let daysDifference = "Loading...";

  onMount(async () => {
    weights = await getWeights();
    // Set firstDate after data loads
    if (weights.length > 0) {
      firstDate = weights[0].date;
      currDate = new Date();
      currDate = new Date().toLocaleDateString();
      currDate = new Date().toISOString().split("T")[0];
      const start = new Date(firstDate);
      const end = new Date(currDate);
      daysDifference = Math.floor((end - start) / (1000 * 60 * 60 * 24));
    }
  });
  $: latestWeight = weights[weights.length - 1];

  function getDaysPassed() {}
</script>

<div class="stats-box hover:brightness-110 transition">
  <div class="relative h-full">
    <div class="grid grid-cols-2 gap-2 p-2">
      <p class="stat-button text-yellow-400">Start-Date:</p>
      <p class="stat-button text-yellow-400">{firstDate}</p>
      <p class="stat-button text-yellow-400">Curr-Date:</p>
      <p class="stat-button text-yellow-400">{currDate}</p>
      <p class="stat-button text-yellow-400">Days Elapsed:</p>
      <p class="stat-button text-yellow-400">{daysDifference}</p>
      <p class="stat-button text-yellow-400">Status:</p>
      <p class="stat-button text-yellow-400">Weight-Loss</p>
      <p class="stat-button text-yellow-400">current-weight:</p>
      <p class="stat-button text-yellow-400">
        {latestWeight?.weight || "--"} lbs
      </p>
      <p class="stat-button text-yellow-400">goal-weight</p>
      <p class="stat-button text-yellow-400">demo lbs</p>
    </div>

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

  .stat-button {
    position: relative;
    margin-top: 10px;
    margin-left: 20px;
    margin-right: 5px;
    padding: 2px;
  }
</style>
