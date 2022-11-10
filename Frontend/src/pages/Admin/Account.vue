<template>
    <div class="content">
        <div class="container">
            <!-- <h3>Products</h3> -->
            <!-- The black row at the top of product page, showing the total statics -->
            <div class="p-3 mb-2 bg-dark text-white">
                Total numbers of users: {{ this.tableData.length }}
            </div>

            <div class="row">
                <div class="col-md-10 col-xl-10"></div>
                <el-form :inline="true" :model="formInline" class="form-inline">
                    <!-- Add item button -->
                    <el-form-item>
                        <button
                            type="button"
                            class="btn btn-info btn-fill float-right btn-block"
                            @click="openNewItem"
                        >
                            + Add User
                        </button>
                    </el-form-item>

                    <!-- Delete item button -->
                    <!-- <el-form-item>
                    <button
                        type="button"
                        class="btn btn-warning btn-fill float-center btn-block"
                    >
                        - Delete User
                    </button>
                </el-form-item> -->
                </el-form>
            </div>

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
                        prop="UserId"
                        label="User Id"
                        align="center"
                        sortable
                    >
                    </el-table-column>
                    <el-table-column
                        prop="username"
                        label="UserName"
                        align="center"
                        sortable
                    >
                    </el-table-column>
                    <el-table-column
                        prop="role"
                        label="Role"
                        align="center"
                        sortable
                    >
                    </el-table-column>
                    <el-table-column
                        prop="email"
                        label="Email"
                        align="center"
                        sortable
                    ></el-table-column>
                    <el-table-column
                        prop="contactNumber"
                        label="Contact Number"
                        align="center"
                        sortable
                    >
                    </el-table-column>

                    <el-table-column label="">
                        <template slot-scope="scope">
                            <!-- <el-button
                                type="primary"
                                size="mini"
                                icon="el-icon-edit"
                            >
                            </el-button> -->
                            <el-button
                                type="danger"
                                size="mini"
                                icon="el-icon-delete"
                                @click="del(scope.row)"
                            >
                            </el-button>
                        </template>
                    </el-table-column>
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

        <el-dialog
            title="Add New User"
            :visible.sync="dialogFormVisible"
            center
            width="500px"
        >
            <el-form :model="form" :rules="rules" ref="form">
                <el-form-item label="Username" :label-width="formLabelWidth">
                    <el-input
                        v-model="form.username"
                        placeholder="Mandatory"
                        autocomplete="off"
                    ></el-input>
                </el-form-item>
                <el-form-item label="Password" :label-width="formLabelWidth">
                    <el-input
                        v-model="form.password"
                        placeholder="Mandatory"
                        autocomplete="off"
                    ></el-input>
                </el-form-item>
                <el-form-item label="Email" :label-width="formLabelWidth">
                    <el-input
                        v-model="form.email"
                        placeholder="Mandatory"
                        autocomplete="off"
                    ></el-input>
                </el-form-item>
                <el-form-item label="Phone" :label-width="formLabelWidth">
                    <el-input
                        v-model="form.contactNumber"
                        autocomplete="off"
                    ></el-input>
                </el-form-item>
                <el-form-item label="Role" :label-width="formLabelWidth">
                    <el-select
                        v-model="form.role"
                        placeholder="Choose a role of the user, mandatory"
                    >
                        <el-option label="General" value="General"></el-option>
                        <el-option label="Admin" value="Admin"></el-option>
                    </el-select>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="dialogFormVisible = false">Cancel</el-button>
                <el-button type="primary" @click="ConfirmaddUser(form)"
                    >Confirm</el-button
                >
            </div>
        </el-dialog>
    </div>
</template>

<script>
// put the Url here
import Axios from "axios";
// const backendUrl = "https://java-jivers.herokuapp.com/item";
const backendUrl = "https://java-jivers-ims.herokuapp.com/user";
const postUrl = "https://java-jivers-ims.herokuapp.com/users/userviewset/";

export default {
    data() {
        return {
            loading: true,
            searchInput: "",
            tableData: [],
            todoItem: {},
            // editMode: false,
            currentPage: 1,
            pageSize: 15,
            totalPage: 0,
            dialogFormVisible: false,
            form: {
                username: "",
                password: "",
                role: "",
                email: "",
                contactNumber: "",
            },
            formLabelWidth: "80px",
            rules: {},
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
        searchItem() {
            // for (var i = 0; i < this.tableData.length; i++) {
            //     if(this.searchInput == this.tableData[i].username){
            //         this.tableData = this.tableData[i]
            //     }
            // }
        },
        // handle page change for pagination
        handleCurrentChange(val) {
            this.currentPage = val;
        },
        openNewItem() {
            this.dialogFormVisible = true;
        },

        // delete function
        async del(row) {
            console.log(row);
            console.log(row.UserId);

            await Axios.delete(`${backendUrl}/${row.UserId}`);
            this.$message({
                message: "Delete Sucessful",
                type: "success",
            });
            this.$router.go(0);
            // this.getTableData();
        },
        ConfirmaddUser(form) {
            console.log(form);
            this.dialogFormVisible = false;

            Axios.post(postUrl, form).then((res) => console.log(res));
            this.$message({
                message: "Added Sucessful",
                type: "success",
            });
            this.$router.go(0);
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
