<template>
  <layout>
    <div class="container"></div>
  </layout>
</template>


<script>
import Layout from "~/layouts/Social.vue";

import "bulma-helpers/css/bulma-helpers.css";
export default {
  components: {
    Layout
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
