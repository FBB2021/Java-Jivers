<template>
  <card>
    <h4 slot="header" class="card-title">Sign In</h4>
    <form>
      <div class="row">
        <div class="col-md-5">
          <base-input type="text"
                    label="item name"
                    :disabled="true"
                    placeholder="type item name here "
                    v-model="user.company">
          </base-input>
        </div>
      </div>

      <div class="row">
        <div class="col-md-5">
          <base-input type="text"
                    label="Address"
                    :disabled="true"
                    placeholder="Home Address"
                    v-model="user.address">
          </base-input>
        </div>
      </div>

      <div class="text-center">
        <button type="submit" class="btn btn-info btn-fill float-right" @click.prevent="updateProfile">
          Update Profile
        </button>
      </div>
      <div class="clearfix"></div>
    </form>
  </card>
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

</style>
