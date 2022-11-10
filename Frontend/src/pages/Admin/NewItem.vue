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
                  v-model="form.desciption"
                ></el-input>
              </el-form-item>
               
              <el-form-item
                label="cost"
                prop="cost"
                :rules="[
                  {
                    required: true,
                    message: 'cost cannot be empty',
                  },
                ]"
              >
                <el-input v-model="form.cost" autocomplete="off"></el-input>
              </el-form-item>

              <el-form-item
                label="price"
                prop="price"
                :rules="[
                  {
                    required: true,
                    message: 'price cannot be empty',
                  },
                ]"
              >
                <el-input v-model="form.price" autocomplete="off"></el-input>
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
            <el-form ref="form" :model="form" label-width="95px">
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

  
              <el-form-item label="Vendor"
              :rules="[
                  {
                    required: true,
                    message: 'Vender cannot be empty',
                  },
                ]">
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
                ]"
              >
                <el-input
                  v-model="form.weight"
                  autocomplete="off"
                ></el-input>
              </el-form-item>
              <el-form-item
                label="Storage Location"
                :rules="[
                  {
                    required: true,
                    message: 'Location cannot be empty',
                  },
                ]"
              >
                <el-input v-model="form.nameLocation" autocomplete="off"></el-input>
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
const WareHouseUrl = "https://java-jivers-ims.herokuapp.com/item";

export default {
  components: {
    Card,
  },
  data() {
    return {
      form: {
        name: "",
         desciption: "",
         cost: "",
         price: "",
        // expDate: "",
        quantity: "",
        nameBrand: "",
        weight: "",
        nameLocation: "",
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
      if (this.form.name == "") {
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
