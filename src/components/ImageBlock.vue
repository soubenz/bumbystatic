<template>
  <v-row class="justify-center">
    <v-subheader v-if="imgTitle">{{ imgTitle }}</v-subheader>
    <!-- <v-img src="~/assets/images/logo.png" contain :alt="altText" :aspect-ratio="(aspectRatio) * -1"></v-img> -->
    <g-image
      :src="require(`!!assets-loader?height=400&fit=contain!!@images/${src}`)"
      :alt="altText"
    />
  </v-row>
</template>


<script>
export default {
  props: {
    src: {
      type: String,
      // default: "https://picsum.photos/510/300?random"
      default: "logo.png"
    },
    altText: {
      type: String,
      default: ""
    },
    aspectRatio: {
      type: String
    },
    imgTitle: {}
  },
  data() {
    return {
      colors: [
        "indigo",
        "warning",
        "pink darken-2",
        "red lighten-1",
        "deep-purple accent-4"
      ],
      slides: ["First", "Second", "Third", "Fourth", "Fifth"]
    };
  },
  computed: {},
  methods: {
    log: function(evt) {
      window.console.log(evt);
    }
  }
};
</script>
