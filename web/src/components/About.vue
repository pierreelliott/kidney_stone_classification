<template>
    <v-container fluid>
        <v-row align="center"
               justify="center"
               class="mt-5"
        >
            <v-col class="text-center" cols="12" md="6" sm="8">
                <h2 class="display-2 mb-4 master-title">Objectif du projet</h2>
                <p class="text-justify">Ce projet a été réalisé dans un cadre scolaire à Polytech Lyon section
                    informatique, dans le cadre
                    d'un projet libre de co-développement. L'idée a été suggérée aux étudiants par Christian VIAL et les
                    docteurs Etienne DENIS et Vincent ESTRADE. L'objectif était de développer une application web
                    permettant de classifier un calcul urinaire. Pour cela, nous avons entrainé un modèle de deep
                    learning avec une base de données de photos déja classifiées (par les docteurs DENIS et ESTRADE). Le
                    modèle a été entraîné via la librairie TensorFlow en Python.</p>
                <p class="text-justify">Notre modèle ne reconnait que les trois types de calculs urinaires les plus
                    répendus (Ia, IIb et
                    IIIb) à partir d'images de coupe et de sections. Plus bas vous trouverez deux exemples de ses
                    photos. En machine learning, la précision, la variété et l'abondance de données améliorent les
                    résultats de l'algorithme. Ainsi, nous avons également ajouté un module qui permet d'envoyer sur le site des
                    images de calculs urinaires (uniquement pour les spécialistes car il faut préciser la classe). Vous avez
                    besoin de lui, il a besoin de vous !</p>
            </v-col>
        </v-row>

        <v-row align="center"
               justify="center"
               class="my-12"
        >
            <v-col class="text-center"
                   cols="12" order="2"
                   md="4" order-md="1">
                <v-img
                        src="@/assets/img/Va_SEC_2.png"
                        gradient="to bottom, rgba(22, 22, 22, 0.1) 0%, rgba(22, 22, 22, 0.5) 75%, #161616 100%"
                />
            </v-col>
            <v-col md="1" order-md="2"/>
            <v-col class="text-center"
                   cols="12" order="1"
                   md="4" order-md="3">
                <h1>Exemple de section</h1>
                <p>Notre algorithme a été entrainé avec des photos prises par le même appareil (avec cette qualité et
                    cette luminosité). Si jamais votre photo a des caractéristiques très différentes, il est possible
                    que ce calcul dupe notre modèle !</p>
            </v-col>
        </v-row>

        <v-spacer></v-spacer>

        <v-row align="center"
               justify="center"
               class="my-12"
        >
            <v-col class="text-center"
                   cols="12"
                   md="4">
                <h1>Exemple de surface</h1>
                <p>Si votre photo est celle d'une surface, voici un exemple.</p>
            </v-col>
            <v-col md="1"/>
            <v-col class="text-center"
                   cols="12"
                   md="4">
                <v-img
                        src="@/assets/img/Va_SUR_4.png"
                        gradient="to bottom, rgba(22, 22, 22, 0.1) 0%, rgba(22, 22, 22, 0.5) 75%, #161616 100%"
                />
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    export default {
        name: "About"
    }
</script>

<style scoped>

</style>
