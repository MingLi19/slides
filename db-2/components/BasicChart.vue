<script setup lang="ts">
import { AgChartsEnterpriseModule } from "ag-charts-enterprise";
import {
  ClientSideRowModelModule,
  ColDef,
  ModuleRegistry,
} from "ag-grid-community";
import { IntegratedChartsModule } from "ag-grid-enterprise";
import { AgGridVue } from "ag-grid-vue3";
import { ref } from "vue";
import { getData } from "./olympics";

ModuleRegistry.registerModules([
  ClientSideRowModelModule,
  IntegratedChartsModule.with(AgChartsEnterpriseModule),
]);

const columnDefs = ref<ColDef[]>([
  // different ways to define 'categories'
  { field: "country", chartDataType: "category" },
  { field: "athlete", chartDataType: "category" },
  { field: "age", chartDataType: "category" },
  { field: "sport" },
  // excludes year from charts
  { field: "year", chartDataType: "excluded" },
  // different ways to define 'series'
  { field: "gold", chartDataType: "series" },
  { field: "silver", chartDataType: "series" },
  { field: "bronze" }, // inferred as series by grid
]);
const defaultColDef = ref<ColDef>({
  flex: 1,
  minWidth: 100,
  filter: true,
});
const popupParent = ref<HTMLElement | null>(document.body);
const rowData = ref(getData());
</script>

<template>
  <div style="height: 100%">
    <div class="wrapper">
      <ag-grid-vue
        style="width: 900px; height: 450px"
        :columnDefs="columnDefs"
        :defaultColDef="defaultColDef"
        :cellSelection="true"
        :popupParent="popupParent"
        :enableCharts="true"
        :rowData="rowData"
      ></ag-grid-vue>
    </div>
  </div>
</template>

<style></style>
