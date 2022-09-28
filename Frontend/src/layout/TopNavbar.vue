<!-- Top navi bar, should be able to change based on different location -->

<template>
    <nav class="navbar navbar-expand-lg">
        <div class="container-fluid">
            <!-- Show the title of the page -->
            <a class="navbar-brand" href="#">{{ pageLocation }}</a>

            <div class="collapse navbar-collapse justify-content-end">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="#"> Account </a>
                    </li>
                    <li class="nav-item">
                        <a href="#" class="nav-link"> Log out </a>
                    </li>
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
    },
};
</script>
<style></style>
