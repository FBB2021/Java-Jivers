<template>  
  <div class="content">
    <div class="container">
    <div class="row">
     <h3> Products</h3>

    </div>

<!-- The black row at the top of product page, showing the total statics -->
    <div class="p-3 mb-2 bg-dark text-white">
      Total items in Inventory: 153 Inventory value by price: $51.4k</div>
    </div>
    <div class="row justify-content-center">

      <!-- Search bar -->
      <div class = "col-7"> 
        <div class="input-group mb-3">
          <input type="text" class="form-control" placeholder="'type product name here" 
                aria-label="type product name here" aria-describedby="basic-addon2">
            <div class="input-group-append">
              <button class="btn btn-outline-secondary" type="button">Search</button>
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
          <button type="button" class="btn btn-info btn-fill float-center btn-block">
              + New Item </button>
      </div>
      <!-- Delete item button -->
      <div class="col-sm">
          <button type="button" class="btn btn-warning btn-fill float-center btn-block">
                - Delete Item
              </button>    
      </div>
    </div>
    <!-- Display of table -->
    <div class = "row">
      <div class = "col-12">
          <table class="table table-bordered mt5 table-hover">
            <thead class="thead-dark">
              <tr>
                  <th> Item Name </th>
                  <th> Brand</th>
                  <th> Category </th>
                  <th> Location </th>
                  <th> Quantity </th>
                  <th> </th>
              </tr>
            </thead>
            <tbody>
                <tr v-for = "(item,i) in todoList" :key = "i">
                    <td class = "align-middle w-75"> 
                        {{  item.Name  }}
                    </td>
                    <td class = "align-middle text-center w-70" > 
                        {{  item.Brand  }}
                    </td>
                    <td class = "align-middle text-center w-70" > 
                        {{  item.Category  }}
                    </td>
                    <td class = "align-middle text-center w-60" > 
                        {{  item.Location  }}
                    </td>
                    <td class = "align-middle text-center w-60" > 
                        {{  item.Quantity  }}
                    </td>
                    <!-- Last column that contains two button -->
                    <td class = "align-middle text-center w-60" > 
                      >
                      <button
                        class = "btn btn-info btn-sm mx-1"
                        @click = "handleEdit(item.Name)"
                      >
                        Edit
                      </button>
                      <button
                        class = "btn btn-danger btn-sm mx-1"
                        @click = "handleDelete(item.Name)"
                      >
                        Delete
                      </button>
                    </td>
                </tr>
            </tbody>
          </table>

      </div>

    </div>
    

</div>
</template>


<script>
// put the Url here
import Axios from "axios";
const todoUrl = "http://localhost:3500/todo";

  export default {
    data(){
      return{
        todoList: [],
        todoItem: {},
        editMode: false
      }
    },
    // Most of the method doesn't work yet, wokring on to fix it 
    methods:{
      handleEdit(Name){
        // this.editMode = true;
        this.todoItem = this.todoList.find(((item) => item.Name = Name));
        console.log(this.todoItem);
      },
      async handleDelete(Name){
          await Axios.delete(`${todoUrl}/${Name}`);
          Axios.get(todoUrl).then((response) => (this.todoList = response.data));
      }

    },
    // The get request at the begining to get all data
    created(){
      Axios.get(todoUrl).then((response) => (this.todoList = response.data));
      
    },

  };

</script>

<style>

</style>