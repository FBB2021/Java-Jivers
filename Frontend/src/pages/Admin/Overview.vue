<!-- Overview page copied from Product page code, then edited -->
<template>
    <div class="content">
        <div class="container">
            <div class="row">
                <div class="col-md-4 col-xl-4">
                    <div class="search-bar">
                        <base-input
                            type="text"
                            label="Search"
                            :disabled="false"
                            placeholder="Try typing 'new'"
                            v-model="searchInput"
                        >
                        </base-input>
                    </div>
                </div>
                <div class="col-md-8 col-xl-8">
                    <h3>Items with total largest weight</h3>
                    <div class="row">
                        <div class="col-md-4 col-xl-4">
                            <div class="image-items">
                                <img
                                    src="img/apple1.jpg"
                                    class="img-thumbnail"
                                    alt="placeholder"
                                />
                                Apple : 2 left
                            </div>
                        </div>
                        <div class="col-md-4 col-xl-4">
                            <div class="image-items">
                                <img
                                    src="img/iphone.jpg"
                                    class="img-thumbnail"
                                    alt="placeholder"
                                />
                                iphone 13 plus: 247 left
                            </div>
                        </div>
                        <div class="col-md-4 col-xl-4">
                            <div class="image-items">
                                <img
                                    src="img/chair.jpg"
                                    class="img-thumbnail"
                                    alt="placeholder"
                                />
                                Chair: 260 left
                            </div>
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
                                    :data="tableData.slice(0, pageSize)"
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
                this.totalPage = (this.tableData.length / this.pageSize) * 10;
                console.log(response.data);
                console.log(response);
                console.log(this.totalPage);
                this.loading = false;
            });
        },
        searchItem() {
            console.log("The input is: ");
            console.log(this.searchInput);
            cosole.log(typeof tableData);
            // for(item in this.tableData){
            //     console.log(item);
            // //     if(item.name == this.searchInput){
            // //         console.log("The item is " + item.name)
            // //         console.log("Equal!!")
            // //     }
            // }
        },
        openNewItem() {
            this.$router.push("/admin/newitem");
        },

        // edit item

        edit(row) {
            console.log(row);
            console.log(row.idItem);
            this.$root.ITEMID = row.idItem;
            console.log(this.$root.ITEMID);
            // this.$currentID = (row.idItem);
            // console.log(this.$currentID);

            this.$router.push("/admin/edititem");
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
