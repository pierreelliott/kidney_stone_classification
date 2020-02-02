<template>
    <v-app-bar
            app
            color="primary"
            dark
    >
        <div class="d-flex align-center">
<!--            <v-img-->
<!--                    alt="Vuetify Logo"-->
<!--                    class="shrink mr-2"-->
<!--                    contain-->
<!--                    src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"-->
<!--                    transition="scale-transition"-->
<!--                    width="40"-->
<!--            />-->

<!--            <v-app-bar-nav-icon></v-app-bar-nav-icon>-->

            <v-toolbar-title>Classifieur de calculs rénaux</v-toolbar-title>

<!--            <v-img-->
<!--                    alt="Vuetify Name"-->
<!--                    class="shrink mt-1 hidden-sm-and-down"-->
<!--                    contain-->
<!--                    min-width="100"-->
<!--                    src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"-->
<!--                    width="100"-->
<!--            />-->
        </div>

        <v-spacer></v-spacer>

        <template v-slot:extension>
            <v-tabs v-model="selected"
                    centered
                    fixed-tabs>
                <v-tab
                        v-for="item in items"
                        :key="item"
                        :href="'#' + item"
                >
                    {{ item }}
                </v-tab>
            </v-tabs>
        </template>


<!--        <v-btn-->
<!--                href="https://github.com/vuetifyjs/vuetify/releases/latest"-->
<!--                target="_blank"-->
<!--                text-->
<!--        >-->
<!--            <span class="mr-2">Latest Release</span>-->
<!--            <v-icon>mdi-open-in-new</v-icon>-->
<!--        </v-btn>-->
    </v-app-bar>
</template>

<script>
    export default {
        name: "Header",
        props: ['currentItem', 'items'],
        computed: {
            selected:{
                get:function () {
                    return this.currentItem
                },
                set: function(newValue){
                    // $emit is the correct way to update props:
                    this.$emit('navigate', newValue);
                }
            }
        }
    }
</script>

<style scoped>

</style>
