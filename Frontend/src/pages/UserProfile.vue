<template>
  <div class="content">
    <div class="container">
      <div class="row">
        <h3>Products</h3>
      </div>

      <!-- The black row at the top of product page, showing the total statics -->
      <div class="p-3 mb-2 bg-dark text-white">
        Total items in Inventory: 153 Inventory value by price: $51.4k
      </div>
    <div class="row justify-content-center">
      <!-- Search bar -->
      <div class="col-7">
        <div class="input-group mb-3">
          <input
            type="text"
            class="form-control"
            placeholder="'type product name here"
            aria-label="type product name here"
            aria-describedby="basic-addon2"
          />
          <div class="input-group-append">
            <button class="btn btn-outline-secondary" type="button">
              Search
            </button>
          </div>
        </div>
      </div>
      <!-- Filter Button -->
      <div class="col">
        <button
          type="button"
          class="btn btn-secondary btn-fill float-center btn-block"
        >
          Filter
        </button>
      </div>
      <!-- Add item button -->
      <div class="col-sm">
        <button
          type="button"
          class="btn btn-info btn-fill float-center btn-block"
        >
          + New Item
        </button>
      </div>
      <!-- Delete item button -->
      <div class="col-sm">
        <button
          type="button"
          class="btn btn-warning btn-fill float-center btn-block"
        >
          - Delete Item
        </button>
      </div>
    </div>
    <!-- Display of table -->
    <el-row :gutter="20">
    
      <el-table :data="tableData" style="width: 100%">
        <el-table-column prop="name" label="Name" align = "center" sortable> </el-table-column>
        <el-table-column prop="nameBrand" label="Brand" align = "center" sortable> </el-table-column>
        <el-table-column prop="category" label="Category" :formatter="formatter"> </el-table-column>
        <el-table-column prop="nameLocation" label="Location" align = "center" sortable> </el-table-column>
        <el-table-column prop="quantity" label="Quantity" align = "center" sortable></el-table-column>
        <el-table-column prop="weight" label="Weight(Kg)" align = "center" sortable></el-table-column>
        <el-table-column label="">
          <template>
            <el-button type="primary" size="mini" icon="el-icon-edit">
            </el-button>
            <el-button type="danger" size="mini" icon="el-icon-delete">
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-row>
    </div>
    </div>
   </template>


<script>
// put the Url here
import Axios from "axios";
const todoUrl = "http://localhost:8000/item";

export default {
  data() {
    return {
      tableData: [],
      todoItem: {},
      editMode: false,
    };
  },
  // Most of the method doesn't work yet, wokring on to fix it
  methods: {
    // handleEdit(Name){
    //   // this.editMode = true;
    //   this.todoItem = this.tableData.find(((item) => item.Name = Name));
    //   console.log(this.todoItem);
    // },
    // async handleDelete(Name){
    //     await Axios.delete(`${todoUrl}/${Name}`);
    //     Axios.get(todoUrl).then((response) => (this.tableData = response.data));
    // }
  },
  // The get request at the begining to get all data
  created() {
    Axios.get(todoUrl).then((response) => (this.tableData = response.data));
  },
};
</script>

<style>
</style>