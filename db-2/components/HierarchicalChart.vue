<script setup lang="ts">
import { AgChartsEnterpriseModule } from "ag-charts-enterprise";
import {
  ChartRef,
  ChartToolPanelsDef,
  ClientSideRowModelModule,
  ColDef,
  FirstDataRenderedEvent,
  GridApi,
  GridReadyEvent,
  ModuleRegistry,
} from "ag-grid-community";
import { IntegratedChartsModule } from "ag-grid-enterprise";
import { AgGridVue } from "ag-grid-vue3";
import { ref, shallowRef } from "vue";
import { getData } from "./data";

ModuleRegistry.registerModules([
  ClientSideRowModelModule,
  IntegratedChartsModule.with(AgChartsEnterpriseModule),
]);

let chartRef: ChartRef;

const heatmapColIds: string[] = [
  "year",
  "jan",
  "feb",
  "mar",
  "apr",
  "may",
  "jun",
  "jul",
  "aug",
  "sep",
  "oct",
  "nov",
  "dec",
];

const heatmapColDefs: ColDef[] = [
  { field: "year", width: 150, chartDataType: "category" },
  { field: "jan" },
  { field: "feb" },
  { field: "mar" },
  { field: "apr" },
  { field: "may" },
  { field: "jun" },
  { field: "jul" },
  { field: "aug" },
  { field: "sep" },
  { field: "oct" },
  { field: "nov" },
  { field: "dec" },
];

const waterfallColIds: string[] = ["financials", "amount"];

const waterfallColDefs: ColDef[] = [
  { field: "financials", width: 150, chartDataType: "category" },
  { field: "amount", chartDataType: "series" },
];

const gridApi = shallowRef<GridApi | null>(null);
const columnDefs = ref<ColDef[]>(heatmapColDefs);
const defaultColDef = ref<ColDef>({
  flex: 1,
  minWidth: 100,
});
const popupParent = ref<HTMLElement | null>(document.body);
const chartToolPanelsDef = ref<ChartToolPanelsDef>({
  defaultToolPanel: "settings",
});
const rowData = ref<any[]>([]);

function onFirstDataRendered(params: FirstDataRenderedEvent) {
  chartRef = params.api.createRangeChart({
    chartContainer: document.querySelector("#myChart8") as any,
    chartType: "heatmap",
    cellRange: {
      columns: heatmapColIds,
    },
  })!;
}
function updateChart(chartType: "heatmap" | "waterfall") {
  getData(chartType).then((rowData) => {
    gridApi.value?.updateGridOptions({
      columnDefs: chartType === "heatmap" ? heatmapColDefs : waterfallColDefs,
      rowData,
    });
    gridApi.value?.updateChart({
      type: "rangeChartUpdate",
      chartId: chartRef.chartId,
      chartType,
      cellRange: {
        columns: chartType === "heatmap" ? heatmapColIds : waterfallColIds,
      },
    });
  });
}

const onGridReady = (params: GridReadyEvent) => {
  gridApi.value = params.api;
};
</script>

<template>
  <div style="height: 100%">
    <div class="wrapper">
      <div class="gap-6 button-container">
        <button v-on:click="updateChart('heatmap')">Heatmap</button>
        <button v-on:click="updateChart('waterfall')">Waterfall</button>
      </div>
      <ag-grid-vue
        style="width: 1200px; height: 300px; zoom: 0.6"
        :columnDefs="columnDefs"
        :defaultColDef="defaultColDef"
        :popupParent="popupParent"
        :cellSelection="true"
        :enableCharts="true"
        :chartToolPanelsDef="chartToolPanelsDef"
        :rowData="rowData"
        @grid-ready="onGridReady"
        @first-data-rendered="onFirstDataRendered"
      ></ag-grid-vue>
      <div id="myChart8"></div>
    </div>
  </div>
</template>

<style>
.wrapper {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.button-container {
  display: flex;
  flex-wrap: wrap;
}

#myGrid {
  flex: 1;
}

#myChart8 {
  flex: 1;
  width: 1200px;
  height: 600px;
  zoom: 0.6;
}
</style>
