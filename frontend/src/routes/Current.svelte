<script>
  import { onMount } from "svelte";

  let weights = [];
  let chartCanvas;

  onMount(async () => {
    // Import Chart.js only in browser
    const { Chart } = await import("chart.js/auto");
    const zoomPlugin = await import("chartjs-plugin-zoom");

    Chart.register(zoomPlugin.default);

    const res = await fetch("http://localhost:5001/weights");
    //const res = await fetch("http://100.89.197.38:5001/weights");
    weights = await res.json();

    new Chart(chartCanvas, {
      type: "line",
      data: {
        labels: weights.map((w) => w.date),
        datasets: [
          {
            label: "Weight",
            data: weights.map((w) => w.weight),
            borderColor: "rgb(234, 179, 8)",
            backgroundColor: "rgba(234, 179, 8, 0.1)",
            tension: 0.4,
            pointRadius: 4,
            pointHoverRadius: 6,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          zoom: {
            pan: {
              enabled: true,
              mode: "x",
            },
            zoom: {
              wheel: {
                enabled: true,
              },
              pinch: {
                enabled: true,
              },
              mode: "x",
            },
          },
        },
        scales: {
          y: {
            grid: { color: "rgba(255, 255, 255, 0.1)" },
            ticks: { color: "rgb(156, 163, 175)" },
          },
          x: {
            grid: { color: "rgba(255, 255, 255, 0.1)" },
            ticks: { color: "rgb(156, 163, 175)" },
          },
        },
      },
    });
  });
</script>

<div class="current-box hover:brightness-110 transition">
  <div class="relative h-full p-4">
    <div class="h-[400px]">
      <canvas bind:this={chartCanvas}></canvas>
    </div>
    <p class="absolute right-0 bottom-0 pr-2 text-gray-600">Current</p>
  </div>
</div>

<style>
  .current-box {
    border: 0.1px solid rgb(65, 68, 69);
    background-color: rgb(34, 38, 44);
    width: 30vw;
    height: 60vh;
    border-radius: 8px;
    box-shadow:
      0 4px 6px rgba(0, 0, 0, 0.3),
      0 1px 3px rgba(0, 0, 0, 0.2);
  }
</style>
