<template>
  <!-- https://forum.vuejs.org/t/dynamic-components-with-dynamic-imports/20703/7 -->
  <component :animation="$page.links1.animation" v-bind:is="componentFile">
    <div>
      <div class="hero-body has-text-centered has-padding-top-10">
        <div>
          <h1 class="title has-text-primary is-size-1">{{$page.links1.name}}</h1>
          <h2 class="subtitle has-text-grey-dark is-size-4">{{$page.links1.bio}}</h2>
        </div>
      </div>
      <div
        class="links columns is-centered is-multiline"
        v-for="edge in $page.links1.items"
        :key="edge.id"
      >
        <div class="column is-half">
          <g-link :to="edge.href">
            <b-button class="is-primary" expanded size="is-large">Click here</b-button>
          </g-link>
        </div>
        <!-- <b-button class="is-primary" expanded size="is-large">Click here2</b-button> -->
        <!-- <b-button class="card column is-half is-primary" size="is-medium" expanded>Click here</b-button> -->
      </div>
    </div>
  </component>
</template>

<page-query>
query ($id: ID!){
    links1(id: $id) {
    id
    bio
    name
    profileImg
    theme
    header
    animation
    
  }}
</page-query>

<script>
import Layout from "~/layouts/Social.vue";

import "bulma-helpers/css/bulma-helpers.css";
export default {
  components: {
    Layout
  },
  computed: {
    componentFile() {
      return () => import(`~/layouts/${this.$page.links1.header}.vue`);
    }
  },

  metaInfo() {},

  methods: {
    getImage(imageUrl) {
      let hashed = require.resolve(
        "../assets/images/0a07c859915761d54cf049a1c771873a30d3b563.jpg"
      );

      return hashed;
    },
    sortData(data) {
      const sortedData = data.sort((a, b) => (a.id > b.id ? 1 : -1));
      list.sort((a, b) => (a.color > b.color ? 1 : -1));
      return sortedData;
    },
    getTitle() {
      return this.$page.quotes.edges[0].node.series.title;
    }
  }
};
</script>

<style>
.home-links a {
  margin-right: 1rem;
}
</style>
