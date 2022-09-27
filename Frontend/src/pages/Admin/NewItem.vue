<template>
  <div class="content">
    <div class="container">
      <div class="row">
        <el-button type="primary" @click="goback"> Back </el-button>
        <b> New item </b>
      </div>
      <div style="margin: 20px 0"></div>

      <div class="row">
        <div class="col">
          <Card>
            Name
            <el-input
              v-model="name"
              placeholder="Please type the name of item"
            ></el-input>
            <div style="margin: 20px 0"></div>
            Description
            <el-input
              type="textarea"
              :rows="3"
              placeholder="Please type description of the item here"
              v-model="inputdescription"
            >
            </el-input>
            <div style="margin: 20px 0"></div>
            Item Image (Currently not link to backend yet)
            <el-upload
              class="upload-demo"
              drag
              action="https://jsonplaceholder.typicode.com/posts/"
              multiple
            >
              <i class="el-icon-upload"></i>
              <div class="el-upload__text">
                Drag File overhere, or<em>Click to upload</em>
              </div>
              <div class="el-upload__tip" slot="tip">
                jpg/png file only and no more than 500kb
              </div>
            </el-upload>
          </Card>
        </div>

        <div class="col">
          <Card>
            <el-input
              v-model="name"
              placeholder="Please type the name of item"
            ></el-input>
          </Card>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Card from "src/components/Cards/Card.vue";

export default {
  components: {
    Card,
  },
  data() {
    return {
      name: "",
      inputdescription: "",
    };
  },
  methods: {
    goback() {
      this.$router.push("/admin/product");
    },
  },
};
</script>