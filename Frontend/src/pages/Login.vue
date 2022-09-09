<template>
  <div class="login">
    <card>
      <h4 slot="header" class="card-title">Sign In</h4>
      <form>
        <div class="row">
          <div class="col-md-20">
            <base-input type="text"
                        label="Email"
                        :disabled="false"
                        placeholder="type email address here"
                        v-model="user.email">
            </base-input>
          </div>
        </div>

        <div class="row">
          <div class="col-md-20">
            <base-input type="text"
                        label="Password"
                        :disabled="false"
                        placeholder="type password here"
                        v-model="user.password">
            </base-input>
          </div>
        </div>

        <div class="row">
          <div class="col-xl-6 col-md-6">
            <button type="submit" class="btn btn-info btn-fill float-center">
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
    data () {
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
        }
      }
    },
    methods: {
      updateProfile () {
        alert('Your data: ' + JSON.stringify(this.user))
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
