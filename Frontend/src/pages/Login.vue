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
          password: ""
        }
      }
    },
    methods: {
      login() {
        if(this.input.email != "" && this.input.password != ""){
          user_type = this.getUserType(this.input.email, this.input.password);
          if(user_type == general_user){
            // Not secure yet
            this.$router.push('/user/overview');
          }
          else if(user_type == admin_user){
            this.$router.push('/admin/overview');
          }
          else{
            console.log("The email and / or password is incorrect");
          }
        }
      },
      // Returns the type of user, either admin or general, from the server database given a username/email and password
      getUserType(email, password){
       // First check if it is in the database, if not return -1
       let user = this.user_login_data.find((user) => user.email == email);
       if (user == -1){
        return -1;
       }
       else {
        return this.checkIdenticalPassword(user, password);
       }
      },/*
      checkIdenticalEmail(email){
        if (this.email == email){
          return 1;
        }
        else{
          return -1;
        }
      },*/
      checkIdenticalPassword(user, password){
        if(user.password == password){
          return this.type;
        }
        else{
          return -1;
        }
      }
    },
    created(){
      Axios.get(todoUrl).then(response=>{this.user_login_data = response.data.data});
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
