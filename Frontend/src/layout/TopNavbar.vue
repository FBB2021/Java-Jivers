<!-- Top navi bar, should be able to change based on different location -->

<template>
    <nav class="navbar navbar-expand-lg">
        <div class="container-fluid">
            <!-- Show the title of the page -->
            <a class="navbar-brand" href="#"></a>
            <div class="collapse navbar-collapse justify-content-end">
                <ul class="navbar-nav ml-auto">
                    <button
                        class="btn btn-default"
                        type="submit"
                        variant="primary"
                        @click="logout()"
                    >
                        Log Out
                    </button>
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
            pageLocation: "",
            activeNotifications: false,
            mypath: "",
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
        show() {
            this.pageLocation = "TADA!";
            console.log(this.$route.path);
            // path = this.$route.path;
            console.log(this.$route.path.split("/")[2]);
            // const myArray = path.split("/");
            // this.pageLocation = myArray[1];
            // console.log(myArray[1])
        },
    },
    created() {
        this.pageLocation = this.$route.path.split("/")[2].toUpperCase();
    },
};
</script>
<style></style>
