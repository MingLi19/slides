<script setup lang="ts">
import { AgChartsEnterpriseModule } from "ag-charts-enterprise";
import { ModuleRegistry } from "ag-grid-community";
import { AllEnterpriseModule, SparklinesModule } from "ag-grid-enterprise";
import { AgGridVue } from "ag-grid-vue3";
import { ref } from "vue";
import { getData } from "./stocks";

ModuleRegistry.registerModules([
  AllEnterpriseModule,
  SparklinesModule.with(AgChartsEnterpriseModule),
]);

const rowData = ref(getData());

const columnDefs = ref([
  { field: "symbol" },
  { field: "name" },
  {
    field: "change",
    cellRenderer: "agSparklineCellRenderer",
  },
  {
    field: "volume",
  },
]);

const defaultColDef = ref({ flex: 1 });
</script>

<template>
  <div>
    <ag-grid-vue
      style="width: 900px; height: 450px"
      class="ag-theme-alpine"
      :rowData="rowData"
      :columnDefs="columnDefs"
      :defaultColDef="defaultColDef"
    ></ag-grid-vue>
  </div>
</template>
