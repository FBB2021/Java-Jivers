<template>
  <div class="login"
       data-image="background-image">
    <card>
      <h4 slot="header" class="card-title">Sign In</h4>
      <form>
        <div class="row">
          <div class="col-md-20">
            <base-input type="text"
                        label="Email"
                        :disabled="false"
                        placeholder="type email address here"
                        v-model="input.email">
            </base-input>
          </div>
        </div>

        <div class="row">
          <div class="col-md-20">
            <base-input type="text"
                        label="Password"
                        :disabled="false"
                        placeholder="type password here"
                        v-model="input.password">
            </base-input>
          </div>
        </div>

        <div class="row">
          <div class="row">
            <base-checkbox></base-checkbox>
          </div>
            
            Remember me
          </div>

          <div class="row">
            <div class="col-xl-12 col-md-12">
              <button type="submit" @click="login()" class="btn btn-info btn-fill float-center" >
                Sign in
              </button>
            </div>
          </div>


          <div class="clearfix"></div>
          <div class="clearfix"></div>

</form>
    </card>
  </div>
</template>
<script>
  import Card from 'src/components/Cards/Card.vue'
  // put the Url here
  import Axios from "axios";
  const todoUrl = "http://localhost:3500/todo";

  export default {
    components: {
      Card
    },
    props: {
      backgroundImage: {
        type: String,
        default: 'img/adrian-sulyok-sczNLg6rrhQ-unsplash'
      }
    },
    data() {
      return {
        user_login_data: [],
        input: {
          email: "",
          password: "",
          type: "general_user"
        }
      }
    },
    methods: {
      login() {
        if(this.input.email != "" && this.input.password != ""){
          let user_type = this.getUserType();
          if(user_type == "general_user"){
            // Not secure yet
            this.$router.push('/user/overview');
          }
          else if(user_type == "admin_user"){
            this.$router.push('/admin/overview');
          }
          else{
            console.log("The email and / or password is incorrect" + user_type);
          }
        }
      },
      // Returns the type of user, either admin or general, from the server database given a username/email and password
      getUserType(){
       // First check if it is in the database, if not return -1
       let user = this.user_login_data.indexOf(this.input);
       if (user == -1){
        console.log("incorrect formatting " + toString(this.input));
        return -1;
       }
       else {
        return "general_user";
       }
      }
    },
    created(){
      Axios.get(todoUrl).then(response=>{this.user_login_data = response.data});
    }
  }


</script>
<style>
  .login {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
  }
  
</style>
