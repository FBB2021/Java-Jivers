<!-- This is the homepage for the user -->
<!-- Three sections. First is a searh bar, for searching items. No current functionality. Second is a display of three items that are nearly out of stock. No functionality yet. Third is a table below that shows recent items. Was displaying placeholder data, but no longer works for unknown reason-->
<template>
  <div class="content">
    <div class="container-fluid">
      <div class="row">
          <div class="col-md-4 col-xl-4">
            <div class="search-bar">
            <base-input type="text" label="Search" :disabled="false" placeholder="Try typing 'new'" v-model="model">
            </base-input>
            </div>
          </div>
          <div class="col-md-8 col-xl-8">
            Items close to out of stock
            <div class="row">
              
              <div class="col-md-4 col-xl-4">
                <div class="image-items">
                  <img src="img/adrian-sulyok-sczNLg6rrhQ-unsplash.jpg" class="img-thumbnail" alt="placeholder">
                  Quantity:2
                </div>
                
              </div>
              <div class="col-md-4 col-xl-4">
                <div class="image-items">
                  <img src="img/adrian-sulyok-sczNLg6rrhQ-unsplash.jpg" class="img-thumbnail" alt="placeholder">
                  Quantity:2
                </div>
                
              </div>
              <div class="col-md-4 col-xl-4">
                <div class="image-items">
                  <img src="img/adrian-sulyok-sczNLg6rrhQ-unsplash.jpg" class="img-thumbnail" alt="placeholder">
                  Quantity:2
                </div>
                
              </div>
              
              
              
            </div>
            
        </div>
      </div>
    </div>


    <div class="container-fluid">
      <div class="row">

        <div class="col-12">
          <card class="card-plain">
            <template slot="header">
              <h4 class="card-title">Recent Searches</h4>
            </template>
            <div class="table-responsive">
              <l-table class="table-hover" :columns="table2.columns" :data="table2.data">
              </l-table>
            </div>
          </card>
        </div>

      </div>
    </div>
  </div>
</template>
<script>
import LTable from 'src/components/Table.vue'
import Card from 'src/components/Cards/Card.vue'
const tableColumns = ['ID', 'Name', 'Brand', 'Category', 'Quantity', 'Price', 'Location']
const tableData = [{
  id: 1,
  name: 'Chicken Magnet',
  brand: 'KfC',
  category: 'Tool',
  quantity: '1',
  price: '$5.00',
  location: 'K'
},
{
  id: 2,
  name: 'Chicken Magnet',
  brand: 'KfC',
  category: 'Tool',
  quantity: '1',
  price: '$5.00',
  location: 'K'
}]
export default {
  components: {
    LTable,
    Card
  },
  data() {
    return {
      table1: {
        columns: [...tableColumns],
        data: [...tableData]
      },
      table2: {
        columns: [...tableColumns],
        data: [...tableData]
      }
    }
  }
}
</script>
<style>
.search-bar {
  color: rgb(54, 53, 56);
}

.search-bar label {
  margin: 10px;
}
.image-items {
  text-align: center;
}

</style>
