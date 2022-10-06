<template>
  <div class="content">
    <div class="container">
      <div class="row">
        <el-button type="primary" @click="goback"> Back </el-button>
        <el-button plain>New Item</el-button>

        <!-- <b> New item </b> -->
      </div>
      <div style="margin: 20px 0"></div>

      <div class="row">
        <div class="col">
          <!-- <el-form ref="form" :model="form" label-width="95px"> -->
          <Card>
            <el-form ref="form" :model="form" label-width="95px">
              <el-form-item
                label="Name"
                :rules="[
                  {
                    required: true,
                    message: 'Item name cannot be empty',
                  },
                ]"
              >
                <el-input v-model="form.name" autocomplete="off"></el-input>
              </el-form-item>

              <el-form-item label="Description">
                <el-input
                  type="textarea"
                  :rows="3"
                  placeholder="Please type description of the item here"
                  v-model="form.inputdescription"
                ></el-input>
              </el-form-item>

              <el-form-item label="Item Image (currently not linked yet)">
                <el-upload
                  class="upload-demo"
                  drag
                  action="https://jsonplaceholder.typicode.com/posts/"
                  multiple
                >
                  <i class="el-icon-upload"></i>
                  <div class="el-upload__text">
                    Drag File overhere, or
                    <em>Click to upload</em> <br />jpg/png file only and no more
                    than 500kb
                  </div>
                  <!-- <div class="el-upload__tip" slot="tip">
                  jpg/png file only and no more than 500kb
                </div> -->
                </el-upload>
              </el-form-item>

              <el-form-item
                label="cost"
                prop="cost"
                :rules="[
                  {
                    required: true,
                    message: 'cost cannot be empty',
                  },
                  {
                    type: 'number',
                    message: 'cost must be number',
                  },
                ]"
              >
                <el-input
                  v-model.number="form.cost"
                  autocomplete="off"
                ></el-input>
              </el-form-item>

              <el-form-item
                label="price"
                prop="price"
                :rules="[
                  {
                    required: true,
                    message: 'price cannot be empty',
                  },
                  {
                    type: 'number',
                    message: 'price must be number',
                  },
                ]"
              >
                <el-input
                  v-model.number="form.price"
                  autocomplete="off"
                ></el-input>
              </el-form-item>

              <el-form-item label="Expire date">
                <el-date-picker
                  type="date"
                  placeholder="Choose a date"
                  v-model="form.expDate"
                  style="width: 100%"
                ></el-date-picker>
              </el-form-item>
            </el-form>
          </Card>
          <!-- </el-form> -->
        </div>

        <div class="col">
          <!-- <el-form ref="form" :model="form"> -->
          <Card>
            <el-form ref="form" :model="form">
              <el-form-item
                label="quantity"
                prop="quantity"
                :rules="[
                  {
                    required: true,
                    message: 'quantity cannot be empty',
                  },
                  {
                    type: 'number',
                    message: 'quantity must be number',
                  },
                ]"
              >
                <el-input
                  v-model.number="form.quantity"
                  autocomplete="off"
                ></el-input>
              </el-form-item>

              <el-form-item label="Category">
                <el-select
                  v-model="form.category"
                  placeholder="Choose a Category"
                >
                  <el-option label="Computer" value="Computer"></el-option>
                  <el-option label="Food" value="Food"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item label="Vendor">
                <el-input v-model="form.nameBrand"></el-input>
              </el-form-item>
              <el-form-item
                label="weight"
                prop="weight"
                :rules="[
                  {
                    required: true,
                    message: 'weight cannot be empty',
                  },
                  {
                    type: 'number',
                    message: 'weight must be number',
                  },
                ]"
              >
                <el-input
                  v-model.number="form.weight"
                  autocomplete="off"
                ></el-input>
              </el-form-item>
              <el-form-item label="Storage Location">
                <el-select
                  v-model="form.region"
                  placeholder="Please choose location"
                >
                  <el-option label="A" value="A"></el-option>
                  <el-option label="B" value="B"></el-option>
                  <el-option label="C" value="C"></el-option>
                  <el-option label="D" value="D"></el-option>
                </el-select>
              </el-form-item>
            </el-form>
          </Card>
          <!-- </el-form> -->
          <el-button type="danger" @click="saveItem"> Save Changes </el-button>
          <el-button type="primary" @click="postItem">
            Publish Item to WareHouse
          </el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Card from "src/components/Cards/Card.vue";
import Axios from "axios";
const WareHouseUrl = "https://java-jivers.herokuapp.com/item";

export default {
  components: {
    Card,
  },
  data() {
    return {
      form: {
        name: "",
        // inputdescription: "",
        // cost: "",
        // price: "",
        // expDate: "",
        quantity: "",
        category: "",
        nameBrand: "",
        weight: "",
      },
    };
  },
  methods: {
    goback() {
      this.$router.push("/admin/product");
    },
    saveItem() {
      localStorage.form = this.form;
      console.log(this.form);
    },
    postItem() {
      if (this.name == "") {
        this.$message({
          message: "No item name",
          type: "warning",
        });
      } else {
        Axios.post(WareHouseUrl, this.form).then(
          (res) => console.log(res),
          this.$router.push("/admin/product")
        );
        this.$message({
          message: "Added Sucessful",
          type: "success",
        });
      }
    },
  },
};
</script>
