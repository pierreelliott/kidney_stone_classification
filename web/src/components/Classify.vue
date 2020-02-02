<template>
    <v-container fluid>
        <v-row>
            <v-col cols="12" sm="5" offset-sm="1">
                <v-img :src="image" class="mb-4"></v-img>
                <div v-if="response">
                    <h3>Résultat du classifieur</h3>
                    <p v-html="response"></p>
                </div>
                <div class="red--text lighten-4" v-if="error">
                    <h3>Erreur</h3>
                    <p v-html="error"></p>
                </div>
            </v-col>
            <v-col cols="12" sm="5" class="">
                <h2>Je veux classifier ce calcul</h2>
                <p>Sélectionnez votre image et nous allons tenter de déterminer sa classe.</p>

                <v-divider class="my-4"></v-divider>

                <v-form
                        ref="form"
                        v-model="valid"
                        lazy-validation
                        @input="resetMessages"
                >
                    <v-file-input
                            label="Charger l'image"
                            filled
                            outlined
                            show-size
                            solo
                            prepend-icon="mdi-camera"
                            @change="onSelectImage"
                            required
                            :rules="[v => !!v || 'Choisissez une image']"
                    ></v-file-input>

                    <v-select
                            v-model="select"
                            :items="items"
                            :rules="[v => !!v || 'Il faut choisir le type de calcul']"
                            label="Type de calcul"
                            required
                    ></v-select>

                    <div class="mt-5">
                        <v-btn
                                :disabled="!valid"
                                color="success"
                                class="mr-4"
                                @click="validate"
                                v-bind:class="{ disabled: !image }"
                        >
                            Classifier
                        </v-btn>

                        <v-btn
                                color="error"
                                outlined
                                class="mr-4"
                                @click="reset"
                        >
                            Réinitialiser
                        </v-btn>
                    </div>
                </v-form>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    import { sendForm } from '../services/classifierAPI';

    export default {
        name: "Classify",
        data: () => ({
            valid: true,
            select: null,
            items: [
                {text: 'Section', value: 'SEC'},
                {text: 'Surface', value: 'SUR'},
            ],
            imageSource: '',
            imageFile: undefined,
            responseData: undefined,
            errorData: undefined,
        }),
        computed: {
            image: function() {
                return this.imageSource;
            },
            response: function() {
                return this.responseData;
            },
            error: function() {
                return this.errorData;
            }
        },
        methods: {
            validate () {
                if (this.$refs.form.validate()) {
                    sendForm(`/classification_cristaux/classerCristal/${this.select}`, {
                        image: this.imageFile
                    })
                        .then(response => {
                            // eslint-disable-next-line no-console
                            console.log(response);
                            let classe = response.data; // TODO Send a more detailed response
                            this.responseData = `D'après notre classifieur, le calcul rénal en question appartient
                            à la classe <b>${classe}.</b>`;
                        })
                        .catch(error => {
                            // eslint-disable-next-line no-console
                            console.log(error);
                            this.errorData = `Le service a rencontré une erreur lors de la classification de ce calcul rénal.
                            Veuillez réessayer dans quelques instants. Si le problème persiste, veuillez contacter
                             l'administrateur du site.`;
                        })
                }
            },
            reset () {
                this.$refs.form.reset();
            },
            resetMessages() {
                this.responseData = undefined;
                this.errorData = undefined;
            },
            onSelectImage (files) {
                this.resetMessages();
                if(Array.isArray(files)) {
                    // TODO Handle multiple files input
                } else {
                    this.imageFile = files;
                    this.displaySelectedImage(files);
                }
            },
            displaySelectedImage (image) {
                if(image) {
                    const reader = new FileReader();

                    reader.onload = (event) => {
                        this.imageSource = event.target.result;
                    };

                    reader.readAsDataURL(image);
                } else {
                    this.imageSource = '';
                }
            }
        },
    }
</script>

<style scoped>

</style>
