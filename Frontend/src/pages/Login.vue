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
                            v-model="input.email"
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
                    <td>
                        <base-checkbox></base-checkbox>
                    </td>
                    <td>Remember me</td>
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
                email: "",
                password: "",
            },
            login_details: {
                general: { email: "useremail", password: "password" },
                admin: { email: "adminemail", password: "password" },
            },
            background_image: {
                image: "img/adrian-sulyok-sczNLg6rrhQ-unsplash.jpg",
            },
        };
    },
    methods: {
        /* Function that checks the input to see if it matches a password and email in the system. Currently only accepts two hard coded examples. Authentication is done in this function, then the store is called to update the state ASSUMING THAT USER TRYING TO LOGIN HAS ALREADY BEAN AUTHENTICATED */
        login() {
            if (this.input.email != "" && this.input.password != "") {
                if (
                    this.input.email == this.login_details.general.email &&
                    this.input.password == this.login_details.general.password
                ) {
                    // Not secure yet
                    this.$store.dispatch("login_authenticated", [
                        "General",
                        "useremail",
                    ]);
                    this.$router.push("/user/overview");
                } else if (
                    this.input.email == this.login_details.admin.email &&
                    this.input.password == this.login_details.admin.password
                ) {
                    // Not secure yet
                    this.$store.dispatch("login_authenticated", [
                        "Admin",
                        "adminemail",
                    ]);
                    this.$router.push("/admin/overview");
                } else {
                    console.log("The email and / or password is incorrect ");
                }
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
