<template>
    <v-container fluid>
        <v-row>
            <v-col cols="12" sm="6" md="5" offset-md="1">
                <v-img :src="image" class="mb-4"></v-img>
                <div v-if="response" v-html="response">
                </div>
                <div class="red--text lighten-4" v-if="error">
                    <h3>Erreur</h3>
                    <p v-html="error"></p>
                </div>
            </v-col>
            <v-col cols="12" sm="6" md="5" class="">
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
                            v-model="type"
                            :items="types"
                            :rules="[v => !!v || 'Il faut choisir le type de calcul']"
                            label="Type de calcul"
                            required
                    ></v-select>

                    <v-select
                            v-model="classe"
                            :items="classes"
                            :rules="[v => !!v || 'Il faut choisir la classe du calcul']"
                            label="Type de calcul"
                            required
                    ></v-select>

                    <p class="mt-3">Afin de garantir la pertinence de vos données, vous êtes priés de vous identifier.</p>

                    <v-text-field
                            v-model="username"
                            :rules="[v => !!v || 'Renseignez votre identifiant']"
                            label="Identifiant"
                            required
                    ></v-text-field>

                    <v-text-field
                            v-model="password"
                            :rules="[v => !!v || 'Renseignez votre mot de passe']"
                            label="Mot de passe"
                            type="password"
                            required
                    ></v-text-field>

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
        name: "Send",
        data: () => ({
            valid: true,
            type: null,
            classe: null,
            username: '',
            password: '',
            types: [
                {text: 'Section', value: 'SEC'},
                {text: 'Surface', value: 'SUR'},
            ],
            classes: [
                {text: 'Ia', value: 'Ia'},
                {text: 'IIb', value: 'IIb'},
                {text: 'IIIb', value: 'IIIb'},
                {text: 'Autre', value: 'Autre'},
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
                    sendForm(`/classification_cristaux/chargerCristal`, {
                        image: this.imageFile,
                        classe: this.classe,
                        type: this.type,
                        username: this.username,
                        password: this.password
                    })
                        .then(response => {
                            // eslint-disable-next-line no-console
                            console.log(response);
                            // TODO Thank the user
                            this.responseData = `<h3>Merci pour cette donnée supplémentaire !</h3>`;
                        })
                        .catch(error => {
                            // eslint-disable-next-line no-console
                            console.log(error);
                            // TODO
                            if(error.response && error.response.status === 401) {
                                this.errorData = `Identifiant ou mot de passe incorrect.`
                            } else {
                                this.errorData = `Le service a rencontré une erreur. Veuillez réessayer dans quelques
                                 instants. Si le problème persiste, veuillez contacter l'administrateur du site.`;
                            }
                        })
                }
            },
            reset () {
                this.$refs.form.reset()
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
