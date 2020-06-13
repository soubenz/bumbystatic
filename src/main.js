// This is the main.js file. Import global CSS and scripts here.
// The Client API can be used here. Learn more: gridsome.org/docs/client-api

import DefaultLayout from '~/layouts/Default.vue'
import LottieAnimation from 'lottie-vuejs'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import SequentialEntrance from 'vue-sequential-entrance'
import 'vue-sequential-entrance/vue-sequential-entrance.css'
import VueGtag from "vue-gtag";
import Vuex from 'vuex'

export default function (Vue, {
  appOptions,
  head,
  router
}) {
  head.link.push({
    rel: 'stylesheet',
    href: 'https://use.fontawesome.com/releases/v5.2.0/css/all.css',
  }, {
    rel: 'stylesheet',
    href: "https://cdn.jsdelivr.net/npm/@mdi/font@4.x/css/materialdesignicons.min.css"
  }, {
    rel: 'stylesheet',
    href: "https://fonts.googleapis.com/css?family=Material+Icons"
  })
  Vue.use(LottieAnimation);
  Vue.use(SequentialEntrance);
  Vue.use(VueGtag, {
    config: {
      id: "UA-163710881-1",
    }
  }, router);

  Vue.use(Vuetify)
  const opts = {
    icons: {
      iconfont: 'mdi',
    },
  }
  // Set default layout as a global component
  Vue.component('Layout', DefaultLayout)


  appOptions.vuetify = new Vuetify(opts);
  Vue.use(Vuex);
  appOptions.store = new Vuex.Store({
    state: {
      voted: [],
      features: [],
      pending: []
    },
    getters: {
      trendingFeatures: state => {
        return state.features
      },
      votedFeatures: state => {
        return state.voted
      }
    },
    mutations: {
      vote(state, id) {
        state.voted.push({
          id
        });
      },
      setFeatures(state, features) {
        Vue.set(state, 'features', features)
      }
    }
  });
}