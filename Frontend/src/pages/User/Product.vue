<template>
    <div class="content">
        <div class="container">
            <!-- <h3>Products</h3> -->
            <!-- The black row at the top of product page, showing the total statics -->
            <div class="p-3 mb-2 bg-dark text-white">
                Total items in Inventory: {{ this.tableData.length }}
            </div>
            <el-form :inline="true" :model="formInline" class="form-inline">
                <!-- Search bar -->
                <el-form-item>
                    <el-input
                        placeholder="Type item name to search"
                        prefix-icon="el-icon-search"
                        v-model="searchInput"
                    >
                    </el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="searchItem"
                        >Search</el-button
                    >
                    <el-button type="info" @click="reset">Reset</el-button>
                </el-form-item>

                <!-- Filter Button -->
                <el-form-item>
                    <!-- <button
                        type="button"
                        class="
                            btn btn-secondary btn-fill
                            float-center
                            btn-block
                        "
                    >
                        Filter
                    </button> -->
                </el-form-item>
            </el-form>

            <!-- Display of table -->
            <el-row :gutter="20">
                <el-table
                    :data="
                        tableData.slice(
                            (this.currentPage - 1) * this.pageSize,
                            this.currentPage * this.pageSize
                        )
                    "
                    style="width: 100%"
                    v-loading="loading"
                >
                    <el-table-column
                        prop="name"
                        label="Name"
                        align="center"
                        sortable
                    >
                    </el-table-column>
                    <el-table-column
                        prop="nameBrand"
                        label="Brand"
                        align="center"
                        sortable
                    >
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
                </el-table>
                <!-- Pagination -->
                <el-pagination
                    :current-page="this.currentPage"
                    background
                    @current-change="handleCurrentChange"
                    layout="prev, pager, next"
                    :total="this.totalPage"
                >
                </el-pagination>
            </el-row>
        </div>
    </div>
</template>
<script>
// put the Url here
import Axios from "axios";
const backendUrl = "https://java-jivers-ims.herokuapp.com/item";

export default {
    data() {
        return {
            loading: true,
            searchInput: "",
            tableData: [],
            todoItem: {},
            editMode: false,
            currentPage: 1,
            pageSize: 7,
            totalPage: 0,
        };
    },
    // Most of the method doesn't work yet, wokring on to fix it
    methods: {
        // Send a get request to backend and request data
        getTableData() {
            Axios.get(backendUrl).then((response) => {
                this.tableData = response.data;
                this.totalPage = (this.tableData.length / this.pageSize) * 10;
                this.loading = false;
            });
        },
        reset() {
            Axios.get(backendUrl).then((response) => {
                this.tableData = response.data;
                this.totalPage = (this.tableData.length / this.pageSize) * 10;
                this.loading = false;
            });
        },
        searchItem() {
            try {
                Axios.get("items/itemviewset/", {
                    params: { name: this.searchInput },
                }).then((response) => {
                    console.log(response.data);
                    this.tableData = response.data;
                    this.totalPage =
                        (this.tableData.length / this.pageSize) * 10;
                    this.loading = false;
                });
            } catch (error) {
                this.$message({
                    message: "Product not found",
                    type: "error",
                });
            }
        },
        // handle page change for pagination
        handleCurrentChange(val) {
            this.currentPage = val;
        },
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

<style></style>
