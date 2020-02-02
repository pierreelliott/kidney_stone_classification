<template>
  <v-app>
    <Header :current-item="currentItem" :items="items" @navigate="onNavigate"/>

    <v-content>
      <component
              v-bind:is="currentTabComponent"
      ></component>
<!--      <v-tabs-items v-model="currentItem">-->
<!--        <v-tab-item-->
<!--                v-for="item in items"-->
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
<!--      </v-tabs-items>-->
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

export default {
  name: 'App',

  components: {
    Header,
    Send,
    About,
    Classify,
    Contact,
    // HelloWorld,
  },

  data: () => ({
    currentItem: 'about',
    items: [
      'about', 'classify', 'send', 'contact',
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
