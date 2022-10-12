<!-- Top navi bar, should be able to change based on different location -->

<template>
    <nav class="navbar navbar-expand-lg">
        <div class="container-fluid">
            <!-- Show the title of the page -->
            <a class="navbar-brand" href="#">{{ pageLocation }}</a>

            <div class="collapse navbar-collapse justify-content-end">
                <ul class="navbar-nav ml-auto">
                    <b-button
                        type="submit"
                        class="btn btn-info btn-fill float-center"
                    >
                        Account
                    </b-button>
                    <b-button
                        type="submit"
                        variant="outline-secondary"
                        @click="logout()"
                        class="btn btn-info btn-fill float-center"
                    >
                        Log Out
                    </b-button>
                </ul>
            </div>
        </div>
    </nav>
</template>
<script>
export default {
    computed: {
        routeName() {
            const { name } = this.$route;
            return this.capitalizeFirstLetter(name);
        },
    },
    data() {
        return {
            pageLocation: "Product",
            activeNotifications: false,
        };
    },
    methods: {
        capitalizeFirstLetter(string) {
            return string.charAt(0).toUpperCase() + string.slice(1);
        },
        logout() {
            this.$store.dispatch("logout");
            this.$router.push("/login");
        },
    },
};
</script>
<style></style>
