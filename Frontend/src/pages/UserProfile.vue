<template>  
  <div class="content">
    <div class="container">
    <div class="row">
      <p class="h1">Products</p>
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

      <div class="col">
        <button type="button" class="btn btn-secondary btn-fill float-center btn-block">
                       Filter    
              </button>    
      </div>
      <div class="col-sm">
          <button type="button" class="btn btn-info btn-fill float-center btn-block ">
              + New Item
              </button>
      </div>
      <div class="col-sm">
          <button type="button" class="btn btn-warning btn-fill float-center btn-block">
                - Delete Item
              </button>    
      </div>
    </div>

</div>
</template>


<script>

  export default {
    components: {

    }
  }

</script>
<style>

</style>