<template>
  <v-row dense>
    <v-col class="ma-0 pa-0">
      <v-btn
        block
        color="#f96854"
        @click="track"
        ripple
        rounded
        :href="patreonPledge"
        target="_blank"
      >
        <v-icon color="white" left>mdi-patreon</v-icon>Become a Patron!
      </v-btn>
    </v-col>
  </v-row>
</template>


<script>
export default {
  props: {
    blockID: String,
    PatreonAccountID: {
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
    patreonPledge() {
      return "https://www.patreon.com/bePatron?u=" + this.PatreonAccountID;
    }
  },

  methods: {
    track() {
      this.$gtag.event("click", {
        event_category: "patreon",
        event_label: this.blockID
      });
    },
    log: function(evt) {
      window.console.log(evt);
    }
  }
};
</script>
