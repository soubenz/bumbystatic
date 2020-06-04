<template>
  <layout>
    <section class="hero is-medium">
      <div class="hero-body has-text-centered">
        <div>
          <h1 class="title has-text-primary is-size-1">{{$page.quotes.edges[0].node.series.title}}</h1>
          <h2
            class="subtitle has-text-grey-dark is-size-4"
          >Genre: {{$page.quotes.edges[0].node.series.genre}}</h2>
          <h2 class="subtitle is-size-4">Year: {{$page.quotes.edges[0].node.series.year}}</h2>
        </div>
      </div>
    </section>
    <div class="container">
      <div class="columns is-centered is-multiline is-variable is-8">
        <!-- <h1 class="title">{{$page.series.character}}</h1> -->
        <div
          class="card column is-two-fifths has-margin-30"
          v-for="edge in $page.quotes.edges"
          :key="edge.node.id"
        >
          <template v-if="edge.node.image">
            <figure class="image is-16by9">
              <g-image :src="edge.node.image.src" :alt="edge.node.text" />
            </figure>
          </template>
          <p class="has-text-centered is-family-secondary is-size-3 is-italic">{{edge.node.text}}</p>
          <p class="has-text-right is-size-4">Character: {{edge.node.character}}</p>
        </div>
      </div>
      <!-- <h2 class="subtitle">{{$page.quotes.year}}</h2>
      <h2 class="subtitle">{{$page.quotes.genre}}</h2>-->
    </div>
  </layout>
</template>

<page-query>
query ($id: ID!){
    quotes: allQuotes(filter: { series: { in: [ $id] }}) { 
    edges {
      node {
        character
        image
        series {id genre year title}
        text


  }
}}}
</page-query>

<script>
import Layout from "~/layouts/Default.vue";
import "bulma-helpers/css/bulma-helpers.css";
export default {
  components: {
    Layout
  },
  metaInfo() {
    return {
      title: this.$page.quotes.edges[0].node.series.title,
      meta: [
        {
          name: "description",
          content:
            this.$page.quotes.edges[0].node.series.title + " quotes with photos"
        },
        {
          property: "og:title",
          content: this.$page.quotes.edges[0].node.series.title
        }
      ]
    };
  },

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
