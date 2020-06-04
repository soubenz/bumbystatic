<template>
  <v-row dense justify="center" class="ma-0 pa-0">
    <!-- <v-spacer /> -->
    <iframe
      :src="spotifyFollow"
      width="300"
      height="56"
      scrolling="yes"
      frameborder="5"
      style="border:none; overflow:hidden"
      allowtransparency="true"
    ></iframe>
    <!-- <v-spacer /> -->
  </v-row>
</template>


<script>
export default {
  props: {
    SpotifyAccountID: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      isRounded: false
    };
  },
  computed: {
    spotifyFollow() {
      return (
        "https://open.spotify.com/follow/1/?uri=spotify:artist:" +
        this.SpotifyAccountID +
        "&size=detail&theme=light"
      );
    }
  },

  methods: {
    log: function(evt) {
      window.console.log(evt);
    }
  }
};
</script>

<style>
.spotify {
  font-size: 30px;
  color: #d33f3f;
}
</style>