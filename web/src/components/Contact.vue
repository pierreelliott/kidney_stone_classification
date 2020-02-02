<template>
    <v-container>
        <div
             v-for="(items, j) in contacts"
             :key="j"
             class="mt-6"
        >
            <h2 v-if="j === 0" class="text-center">Nouvelle équipe</h2>
            <h2 v-if="j !== 0" class="text-center">Première équipe</h2>

            <v-row>
                <v-col
                        v-for="(item, i) in items"
                        :key="i"
                        :offset-lg="j === 0 && i === 0 ? 1: 0"
                        :lg="j === 0 ? 5: 4"
                        md="6"
                        cols="12"
                >
                    <v-card>
                        <div class="d-flex flex-no-wrap justify-space-between">
                            <v-avatar
                                    class="ma-3"
                                    size="125"
                                    tile
                            >
                                <v-img :src="item.avatar"></v-img>
                            </v-avatar>

                            <div>
                                <v-card-title
                                        class="headline"
                                        v-text="item.name"
                                ></v-card-title>

                                <a :href="`mailto:${item.email}`">
                                    <v-card-subtitle v-text="item.email"></v-card-subtitle>
                                </a>
                            </div>
                        </div>
                    </v-card>
                </v-col>
            </v-row>
        </div>
    </v-container>
</template>

<script>
    export default {
        name: "Contact",
        data: () => ({
            contacts: [
                [
                    {
                        name: 'Julien Perier-Camby',
                        email: 'j.perier@gmail.com',
                        avatar: require('@/assets/julien.png'),
                    },
                    {
                        name: 'Pierre-Elliott Thiboud',
                        email: 'pierre-elliott@thiboud.fr',
                        avatar: require('@/assets/pierre-elliott.png'),
                    }
                ],
                [
                    {
                        name: 'Clément Cottet',
                        email: 'clement.cottet@gmail.com',
                        avatar: require('@/assets/img/clement.png'),
                    },
                    {
                        name: 'Axel Pittore',
                        email: 'axbator@gmail.com',
                        avatar: require('@/assets/img/axel.png'),
                    },
                    {
                        name: 'Alexis Calvi',
                        email: 'alexis.calvi@yahoo.fr',
                        avatar: require('@/assets/img/alexis.png'),
                    }
                ]
            ]
        }),
    }
</script>

<style scoped>

</style>
