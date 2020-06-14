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
import VuexPersist from 'vuex-persist';
// import VueScroller from 'vue-scroller'

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
  // Vue.use(VueScroller)
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

  appOptions.vuexLocalStorage = new VuexPersist({
    key: 'vuex', // The key to store the state on in the storage provider.
    storage: window.localStorage, // or window.sessionStorage or localForage
    // Function that passes the state and returns the state with only the objects you want to store.
    // reducer: state => state,
    // Function that passes a mutation and lets you decide if it should update the state in localStorage.
    // filter: mutation => (true)
  })
  Vue.use(Vuex);

  appOptions.store = new Vuex.Store({
    plugins: [appOptions.vuexLocalStorage.plugin],
    state: {
      voted: [],
      features: [],
      pending: []
    },
    getters: {
      features: state => {
        state.features.sort((a, b) => (a._ts > b._ts ? -1 : 1));
        return state.features
      },
      plannedFeatures: state => {
        return state.features.filter(
          feature => {
            return feature.planned == true
          }
        )
      }
    },
    mutations: {
      vote(state, payload) {
        const index = state.features.indexOf(payload.item);
        Vue.set(state.features[index], 'voted', payload.status)
        // state.features = [...state.features, feature];
        // state.voted.push({
        //   id
        // });
      },
      setFeatures(state, features) {
        Vue.set(state, 'features', features)
      }
    },
    addFeatures(state, feature) {
      state.features = [...state.features, feature];
      // state.features.push(feature)
    }

  });
}