<template>
    <v-img
            src="@/assets/img/dna-1811955_1280_2.jpg"
            height="85vh"
            gradient="to bottom, rgba(22, 22, 22, 0.1) 0%, rgba(22, 22, 22, 0.5) 75%, #161616 100%"
    >
        <v-container fluid style="height: 100%">
            <v-row
                    align="center"
                    justify="center"
                    style="height: 100%"
            >
                <v-col class="text-center" cols="12">
                    <h2 class="display-4 mb-4 master-title text-uppercase">Projet CODEV</h2>
                    <p>Projet réalisé par Julien PERIER-CAMBY et Pierre-Elliott THIBOUD</p>
                    <p>Avec la collaboration des docteurs DENIS et ESTRADE, sous la tutelle de Christian VIAL</p>
                    <p>Basé sur le travail de Clément COTTET, Axel PITTORE et Alexis CALVI</p>
                </v-col>
            </v-row>
        </v-container>
    </v-img>
</template>

<script>
    export default {
        name: "Home"
    }
</script>

<style scoped>
    .master-title {
        font-family: 'Varela Round';
        letter-spacing: 0.8rem;
        background: -webkit-linear-gradient(rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0));
        -webkit-text-fill-color: transparent;
        -webkit-background-clip: text;
    }
</style>
