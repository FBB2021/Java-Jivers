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
          <div class="col-md-3">
            <base-checkbox></base-checkbox>
          </div>
          
          <div class="col-md-9">
            <div class="row">
              <div class="col-md-9">
                Remember me
                </div>
              </div>
            </div>

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

  export default {
    components: {
      Card
    },
    props: {
      backgroundImage: {
        type: String,
        default: 'img/adrian-sulyok-sczNLg6rrhQ-unsplash'
      },
    },
    data() {
      return {
        user: {
          company: 'input item name here ',
          username: '',
          email: '',
          firstName: '',
          lastName: '',
          address: '',
          city: '',
          country: '',
          postalCode: '',
          aboutMe: ` Mercy, Your chick she so thirsty, I'm in that two seat Lambo.`
        },
        input: {
          email: "",
          password: ""
        },
        login_details : {
          user: {email: 'useremail', password: 'password'},
         admin: {email: 'adminemail', password: 'password'}
      }
      }
    },
    methods: {
      login() {
        if(this.input.email != "" && this.input.password != ""){
          if(this.input.email == 'useremail' && this.input.password == 'password'){
            // Not secure yet
            this.$router.push('/user/overview');
          }
          else{
            console.log("The email and / or password is incorrect");
          }
        }
        else{
        }
      }
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
