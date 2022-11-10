<!-- Overview page copied from Product page code, then edited -->
<template>
    <div class="content">
        <div class="container">
            <div class="row">
                <div class="col-md-4 col-xl-4"></div>
                <div class="col-md-8 col-xl-8">
                    <h3>Items with total largest weight</h3>
                    <div class="row">
                        <div class="col-md-4 col-xl-4">
                            {{ "Product: " + largestTotalWeightData[0].name
                            }}<br />
                            {{
                                " Total weight: " +
                                largestTotalWeightData[0].quantity *
                                    largestTotalWeightData[0].weight +
                                "kg"
                            }}
                        </div>
                        <div class="col-md-4 col-xl-4">
                            {{ "Product: " + largestTotalWeightData[1].name
                            }}<br />
                            {{
                                " Total weight: " +
                                largestTotalWeightData[1].quantity *
                                    largestTotalWeightData[1].weight +
                                "kg"
                            }}
                        </div>
                        <div class="col-md-4 col-xl-4">
                            {{ "Product: " + largestTotalWeightData[2].name
                            }}<br />
                            {{
                                " Total weight: " +
                                largestTotalWeightData[2].quantity *
                                    largestTotalWeightData[2].weight +
                                "kg"
                            }}
                        </div>
                    </div>
                </div>
            </div>

            <!-- Display of table -->

            <div class="container-fluid">
                <div class="row">
                    <div class="col-12">
                        <card class="card-plain">
                            <template slot="header">
                                <h4 class="card-title">
                                    Items nearly out of stock
                                </h4>
                            </template>
                            <el-row :gutter="20">
                                <el-table
                                    :data="stockData.slice(0, pageSize)"
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
                            </el-row>
                        </card>
                    </div>
                </div>
            </div>
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
            stockData: [],
            largestTotalWeightData: [],
            todoItem: {},
            editMode: false,
            currentPage: 1,
            pageSize: 4,
            totalPage: 0,
        };
    },
    // Most of the method doesn't work yet, wokring on to fix it
    methods: {
        // Send a get request to backend and request data
        getTableData() {
            Axios.get(backendUrl).then((response) => {
                this.tableData = response.data;
                this.loading = false;
                this.getLowestStock();
                this.getLargestTotalWeight();
            });
        },
        getLowestStock() {
            this.stockData = this.tableData
                .sort(function (a, b) {
                    return a.quantity - b.quantity;
                })
                .slice(0, this.pageSize);
        },
        getLargestTotalWeight() {
            this.largestTotalWeightData = this.tableData
                .sort(function (a, b) {
                    return b.quantity * b.weight - a.quantity * a.weight;
                })
                .slice(0, 3);
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
