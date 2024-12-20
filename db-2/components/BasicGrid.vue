<script setup lang="ts">
import { ColDef, ModuleRegistry } from "ag-grid-community";
import { AllEnterpriseModule } from "ag-grid-enterprise";
import { AgGridVue } from "ag-grid-vue3";
import { ref } from "vue";
import { getData } from "./olympics";

ModuleRegistry.registerModules([AllEnterpriseModule]);

const columnDefs = ref<ColDef[]>([
  { field: "country" },
  { field: "year" },
  { field: "athlete" },
  { field: "sport" },
  { field: "gold", aggFunc: "sum", enableValue: true },
  { field: "silver", aggFunc: "sum", enableValue: true },
  { field: "bronze", aggFunc: "sum", enableValue: true },
]);
const defaultColDef = ref<ColDef>({
  flex: 1,
  minWidth: 100,
  filter: true,
  enableRowGroup: true,
  enablePivot: true,
});
const autoGroupColumnDef = ref<ColDef>({
  minWidth: 200,
});
const rowGroupPanelShow = ref<"always" | "onlyWhenGrouping" | "never">(
  "always"
);
const sideBar = ref<boolean>(true);
const rowData = ref(getData());
</script>

<template>
  <div style="height: 100%">
    <ag-grid-vue
      style="width: 1300px; height: 650px; zoom: 0.7"
      :columnDefs="columnDefs"
      :defaultColDef="defaultColDef"
      :rowData="rowData"
      :sideBar="sideBar"
      :autoGroupColumnDef="autoGroupColumnDef"
      :rowGroupPanelShow="rowGroupPanelShow"
    ></ag-grid-vue>
  </div>
</template>

<style></style>
