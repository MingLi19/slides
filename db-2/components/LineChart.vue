<script setup lang="ts">
import { AgChartsEnterpriseModule } from "ag-charts-enterprise";
import {
  ChartRef,
  ChartToolPanelsDef,
  ChartType,
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
import { getData } from "./earning";

ModuleRegistry.registerModules([
  ClientSideRowModelModule,
  IntegratedChartsModule.with(AgChartsEnterpriseModule),
]);

let chartRef: ChartRef;

const gridApi = shallowRef<GridApi | null>(null);
const columnDefs = ref<ColDef[]>([
  {
    field: "period",
    chartDataType: "category",
    headerName: "Financial Period",
    width: 150,
  },
  {
    field: "recurring",
    chartDataType: "series",
    headerName: "Recurring revenue",
  },
  {
    field: "individual",
    chartDataType: "series",
    headerName: "Individual sales",
  },
]);
const defaultColDef = ref<ColDef>({
  flex: 1,
  minWidth: 100,
});
const popupParent = ref<HTMLElement | null>(document.body);
const chartToolPanelsDef = ref<ChartToolPanelsDef>({
  defaultToolPanel: "settings",
});
const rowData = ref<any[]>(getData());

function onFirstDataRendered(params: FirstDataRenderedEvent) {
  chartRef = params.api.createRangeChart({
    chartContainer: document.querySelector("#myChart3") as any,
    cellRange: {
      columns: ["period", "recurring", "individual"],
    },
    chartType: "line",
  })!;
}
function updateChart(chartType: ChartType) {
  gridApi.value?.updateChart({
    type: "rangeChartUpdate",
    chartId: `${chartRef.chartId}`,
    chartType: chartType,
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
        <button v-on:click="updateChart('line')">Line</button>
        <button v-on:click="updateChart('stackedLine')">Stacked Line</button>
        <button v-on:click="updateChart('normalizedLine')">
          Normalized Line
        </button>
        <button v-on:click="updateChart('area')">Grouped Area</button>
        <button v-on:click="updateChart('stackedArea')">Stacked Area</button>
        <button v-on:click="updateChart('normalizedArea')">
          Normalized Area
        </button>
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
      <div id="myChart3"></div>
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

#myChart3 {
  flex: 1;
  width: 1200px;
  height: 600px;
  zoom: 0.6;
}
</style>
