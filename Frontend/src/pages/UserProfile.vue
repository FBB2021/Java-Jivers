
<!-- This is the Product page -->

<template>
  <div class="content">
    <div class="container-fluid">
      <div class="row">
        <div class="col-12">
          
          <div class="input-group mb-3">
          <div class="input-group-prepend">
            <span class="input-group-text" id="basic-addon1">@</span>
          </div>
          <input type="text" class="form-control" placeholder="Search item" aria-label="SearchItem" 
            aria-describedby="basic-addon1">
          </div>
          <button type="submit" class="btn btn-danger position-relative">
                AddProduct <svg width="1em" height="1em" viewBox="0 0 16 16" class="position-absolute top-100 start-50 translate-middle mt-1 bi bi-caret-down-fill" fill="#212529" xmlns="http://www.w3.org/2000/svg"><path d="M7.247 11.14L2.451 5.658C1.885 5.013 2.345 4 3.204 4h9.592a1 1 0 0 1 .753 1.659l-4.796 5.48a1 1 0 0 1-1.506 0z"/></svg>
              </button>

          <button type="button" class="btn btn-info">Delete</button>

          <card class="strpied-tabled-with-hover"
                body-classes="table-full-width table-responsive"
          >
            <template slot="main">
              <h4 class="card-title">Product list</h4>
              <p class="card-category">This is a list that contains all of the products</p>
            </template>
            <l-table class="table-hover table-striped"
                     :columns="table1.columns"
                     :data="table1.data">
            </l-table>
          </card>

        </div>

      </div>
    </div>
  </div>
</template>
<script>
  import LTable from 'src/components/Table.vue'
  import Card from 'src/components/Cards/Card.vue'
  const tableColumns = ['Id', 'ItemName', 'Categorie', 'Quantity', 'Location','Weight']
  const tableData = [{
    id: 1,
    itemname: 'White Rice',
    categorie: 'Food',
    quantity: '234',
    location: 'A',
    weight: '54.4kg'
  },
  {
    id: 2,
    itemname: 'Black Rice',
    categorie: 'Food',
    quantity: '24',
    location: 'A',
    weight: '4.6kg'
  },
  {
    id: 3,
    itemname: 'Apple',
    categorie: 'Food',
    quantity: '34',
    location: 'A',
    weight: '56kg'
  },
  {
    id: 4,
    itemname: 'Car Toy',
    categorie: 'Toy',
    quantity: '56',
    location: 'B',
    weight: '123.4kg'
  },
  {
    id: 5,
    itemname: 'Puppy Doll',
    categorie: 'Toy',
    quantity: '94',
    location: 'B',
    weight: '9.8kg'
  }]
  export default {
    components: {
      LTable,
      Card
    },
    data () {
      return {
        table1: {
          columns: [...tableColumns],
          data: [...tableData]
        },
      }
    }
  }
</script>
<style>
  .strpied-tabled-with-hover{
    position: absolute;
    width: 1000px;
    top: 100px;  /* 距离上面50像素 */
    left: 50px;
    /* bottom: 50px; */
    /* overflow-y: auto; 当内容过多时y轴出现滚动条 */
    /* background-color: #545c64; */
  }
  .btn btn-info btn-fill float-center{
    position: absolute;
    width: 1000px;
    top: 10px;  /* 距离上面50像素 */
    left: 100px;
  }
</style>
