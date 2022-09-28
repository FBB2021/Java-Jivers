<template>
  <div class="content">
    <div class="container">
      <!-- <h3>Products</h3> -->
      <!-- The black row at the top of product page, showing the total statics -->
      <div class="p-3 mb-2 bg-dark text-white">
        Total items in Inventory: {{  this.tableData.length  }} Inventory value by price: $51.4k
      </div>
      <div class="row justify-content-center">
        <!-- Search bar -->
        <div class="col-7">
          <div class="input-group mb-3">
            <input type="text" class="form-control" placeholder="'type product name here"
              aria-label="type product name here" aria-describedby="basic-addon2" />
            <div class="input-group-append">
              <button class="btn btn-outline-secondary" type="button">
                Search
              </button>
            </div>
          </div>
        </div>
        <!-- Filter Button -->
        <div class="col">
          <button type="button" class="btn btn-secondary btn-fill float-center btn-block">
            Filter
          </button>
        </div>
        <!-- Add item button -->
        <div class="col-sm">
          <button type="button" class="btn btn-info btn-fill float-center btn-block" @click="openNewItem">
            + New Item
          </button>
        </div>
        <!-- Delete item button -->
        <div class="col-sm">
          <button type="button" class="btn btn-warning btn-fill float-center btn-block">
            - Delete Item
          </button>
        </div>
      </div>
      <!-- Display of table -->
      <el-row :gutter="20">
        <el-table :data="tableData.slice((this.currentPage-1)*this.pageSize, this.currentPage * this.pageSize)"
         style="width: 100%" v-loading="loading">
          <el-table-column prop="name" label="Name" align="center" sortable>
          </el-table-column>
          <el-table-column prop="nameBrand" label="Brand" align="center" sortable>
          </el-table-column>
          <el-table-column
            prop="category"
            label="Category"
            :formatter="formatter"
          >
          </el-table-column>
          <el-table-column
            prop="nameLocation"
            label="Location"
            align="center"
            sortable
          >
          </el-table-column>
          <el-table-column
            prop="quantity"
            label="Quantity"
            align="center"
            sortable
          ></el-table-column>
          <el-table-column
            prop="weight"
            label="Weight(kg)"
            align="center"
            sortable
          ></el-table-column>
          <el-table-column label="">
            <template slot-scope="scope">
              <el-button type="primary" size="mini" icon="el-icon-edit">
              </el-button>
              <el-button type="danger" size="mini" icon="el-icon-delete" @click="del(scope.row)">
              </el-button>
            </template>
          </el-table-column>
        </el-table>
        <!-- Pagination -->
        <el-pagination :current-page="this.currentPage" background @current-change="handleCurrentChange"
          layout="prev, pager, next" :total="this.totalPage">
        </el-pagination>
      </el-row>
    </div>
  </div>
</template>


<script>
// put the Url here
import Axios from "axios";
const todoUrl = "https://java-jivers.herokuapp.com/item";

export default {
  data() {
    return {
      loading: true,
      tableData: [],
      todoItem: {},
      editMode: false,
      currentPage:1,
      pageSize: 15,
      totalPage: 0,
    };
  },
  // Most of the method doesn't work yet, wokring on to fix it
  methods: {
    // Send a get request to backend and request data
    getTableData() {
      Axios.get(todoUrl).then((response) => {
        this.tableData = response.data;
        this.totalPage = (this.tableData.length / this.pageSize) * 10;
        console.log(response.data);
        console.log(response);
        console.log(this.totalPage);
        this.loading = false;
      });
    },
    // handle page change for pagination 
    handleCurrentChange(val) {
      this.currentPage = val;
    },
    openNewItem(){
      this.$router.push('/admin/newitem');
    },


    // delete function
    async del(row) {
      console.log(row);
      console.log(row.idItem);
      //127.0.0.1:8000/item/1637
      await Axios.delete(`${todoUrl}/${(row.idItem)}`);
      this.getTableData();
    }
  },
  // The get request at the begining to get all data
  // created() {
  //   Axios.get(todoUrl).then((response) => (this.todoList = response.data));
  // },

  // The get request at the begining to get all data
  created() {
    this.getTableData();
  },
};
</script>

<style>

</style>