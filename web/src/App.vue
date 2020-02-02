<template>
  <v-app>
    <Header :current-item="currentItem" :items="items" @navigate="onNavigate"/>

    <v-content>
      <component
              v-bind:is="currentTabComponent"
      ></component>
<!--      <v-tabs-types v-model="currentItem">-->
<!--        <v-tab-item-->
<!--                v-for="item in types"-->
<!--                :key="item"-->
<!--                :value="item"-->
<!--        >-->
<!--          <v-card flat>-->
<!--            <v-card-text>-->
<!--              <h2>{{ item }}</h2>-->
<!--              {{ text }}-->
<!--            </v-card-text>-->
<!--          </v-card>-->
<!--        </v-tab-item>-->
<!--      </v-tabs-types>-->
    </v-content>
  </v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld';
import Header from "./components/Header";
import Send from "./components/Send";
import About from "./components/About";
import Classify from "./components/Classify";
import Contact from "./components/Contact";
import Home from "./components/Home";

export default {
  name: 'App',

  components: {
    Header,
    Send,
    About,
    Classify,
    Contact,
    Home,
    // HelloWorld,
  },

  data: () => ({
    currentItem: 'home',
    items: [
      {link: 'home', title: 'Accueil'},
      {link: 'about', title: 'À propos du projet'},
      {link: 'classify', title: 'Classifier un calcul rénal'},
      {link: 'send', title: 'Envoyer un calcul rénal'},
      {link: 'contact', title: 'Contact'},
    ]
  }),
  computed: {
    currentTabComponent: function () {
      return this.currentItem.toLowerCase();
    }
  },
  methods: {
    onNavigate: function (tab) {
      this.currentItem = tab;
      // // eslint-disable-next-line no-console
      // console.log("Navigated to '" + tab + "'");
    }
  }
};
</script>
