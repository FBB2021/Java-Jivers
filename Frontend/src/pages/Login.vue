<!-- This is the entry point for the entire website, a login page. If not 
  logged in, this page and page not found will be the only pages you can 
  access-->

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
import Axios from "axios";
const todoUrl = "https://java-jivers.herokuapp.com/user";
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
            server_data: [],
            background_image: {
                image: "img/adrian-sulyok-sczNLg6rrhQ-unsplash.jpg",
            },
        };
    },
    methods: {
        /* Function that checks the input to see if it matches a password and email
     in the system. Currently only accepts two hard coded examples.
     Authentication is done in this function, then the store is called to
     update the state ASSUMING THAT USER TRYING TO LOGIN HAS ALREADY BEEN
     AUTHENTICATED */
        login() {
            if (this.input.email != "" && this.input.password != "") {
                /* Pull user data from server */
                this.get_login_data();

                /* Check if input email and password are in the server data */
                const user = this.is_valid_user(
                    this.input.email,
                    this.input.password
                );

                /* We found a match in the database ! Success */
                if (user != false) {
                    if (
                        user.filter((element) => {
                            return element.role == "General";
                        })
                    ) {
                        this.$store.dispatch("login_authenticated", [
                            "General",
                            this.input.email,
                        ]);
                        this.$router.push("/user/overview");
                    } else if (user.role == "Admin") {
                        this.$store.dispatch("login_authenticated", [
                            "Admin",
                            this.input.email,
                        ]);
                        this.$router.push("/admin/overview");
                    } else {
                        console.log(
                            "The email and / or password is incorrect "
                        );
                    }
                } else {
                    console.log("The email and / or password is incorrect ");
                }
            }
        },
        /* Function that gets all user data from server, stores it in server_data
         */
        get_login_data() {
            Axios.get(todoUrl).then((response) => {
                this.server_data = response.data;
            });
        },
        /* Functions that checks if given email and password is valid in the
    database. Returns the matching userobject if true, false if false*/
        is_valid_user(input_email, input_password) {
            const match = this.server_data.filter((user) => {
                return user.email == input_email;
            });
            console.log(match);

            if (
                match.filter((element) => {
                    return element.password == input_password;
                })
            ) {
                return match;
            } else {
                return false;
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
