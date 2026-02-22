<script>
  import { onMount } from "svelte";
  import { getUpper } from "$lib/upper.js";

  let data = [];
  let chartCanvas;

  onMount(async () => {
    const { Chart } = await import("chart.js/auto");
    const zoomPlugin = await import("chartjs-plugin-zoom");

    Chart.register(zoomPlugin.default);

    data = await getUpper();

    new Chart(chartCanvas, {
      type: "line",
      data: {
        labels: data.map((w) => w.date),
        datasets: [
          {
            label: "Bench press",
            data: data.map((w) => w.value),
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

<div class="upper-box hover:brightness-110 transition">
  <div class="relative h-full p-4">
    <div class="h-[400px]">
      <canvas bind:this={chartCanvas}></canvas>
    </div>
    <p class="absolute right-0 bottom-0 pr-2 text-gray-600">Upper</p>
  </div>
</div>

<style>
  .upper-box {
    flex: 1 1 340px;
    min-width: 280px;
    min-height: 60vh;
    border: 1px solid var(--card-border);
    border-radius: 8px;
    background-color: var(--card-bg);
    box-shadow: var(--card-shadow);
  }
</style>
