<!-- This is the entry point for the entire website, a login page. If not logged in, this page and page not found will be the only pages you can access-->

<template>
    <div class="login">
        <card>
            <h4 slot="header" class="card-title">Sign In</h4>
            <form>
                <div class="row">
                    <div class="col-md-20">
                        <base-input
                            type="text"
                            label="Email"
                            :disabled="false"
                            placeholder="type email address here"
                            v-model="input.username"
                        >
                        </base-input>
                    </div>
                </div>

                <div class="row">
                    <div class="col-md-20">
                        <base-input
                            type="text"
                            label="Password"
                            :disabled="false"
                            placeholder="type password here"
                            v-model="input.password"
                        >
                        </base-input>
                    </div>
                </div>

                <div class="row">
                    <div class="col-xl-12 col-md-12">
                        <button
                            type="submit"
                            @click="login()"
                            class="btn btn-info btn-fill float-center"
                        >
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
import Card from "src/components/Cards/Card.vue";
// put the Url here

export default {
    components: {
        Card,
    },
    data() {
        return {
            input: {
                username: "",
                password: "",
            },
            background_image: {
                image: "img/adrian-sulyok-sczNLg6rrhQ-unsplash.jpg",
            },
        };
    },
    methods: {
        /* Function that checks the input to see if it matches a password and email in the system. Currently only accepts two hard coded examples. Authentication is done in this function, then the store is called to update the state ASSUMING THAT USER TRYING TO LOGIN HAS ALREADY BEAN AUTHENTICATED */
        async login() {
            const formData = {
                username: this.input.username,
                password: this.input.password,
            };
            this.$store.dispatch("logout");

            if (this.input.username != "" && this.input.password != "") {
                try {
                    await this.$store.dispatch("login", formData);
                    this.$router.push("/admin/overview");
                } catch (error) {}
            }
        },
    },
};
</script>
<style>
.login {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    background-image: url("adrian-sulyok-sczNLg6rrhQ-unsplash.jpg");
    background-size: cover;
}
</style>
