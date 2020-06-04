<template>
  <v-row dense>
    <v-col class="ma-0 pa-0">
      <v-btn block :color="icon.color" :href="account" rounded>
        <v-icon v-html="icon.icon" color="white"></v-icon>
        <span class="white--text">{{ social }}</span>
      </v-btn>
    </v-col>
  </v-row>
</template>


<script>
export default {
  props: {
    buttonColor: {
      type: String,
      default: "#1F7087"
    },
    buttonTextColor: {
      type: String,
      default: "white"
    },
    social: {
      type: String
    },
    account: {
      type: String
    }
  },
  data() {
    return {
      itemID: 1,
      isDragging: false,
      dialog: false,
      socialType: this.social,
      instagram: { color: "#C13584", icon: "mdi-instagram" },
      facebook: { color: "#4267B2", icon: "mdi-facebook" },
      twitter: { color: "#1DA1F2", icon: "mdi-twitter" },
      pinterest: { color: "#E60023", icon: "mdi-pinterest" },
      whatsapp: { color: "#25D366", icon: "mdi-whatsapp" },
      snapchat: { color: "#000000", icon: "mdi-snapchat" },
      spotify: { color: "#1DB954", icon: "mdi-spotify" },
      youtube: { color: "#FF0000", icon: "mdi-youtube" },
      soundcloud: { color: "#ff7700", icon: "mdi-soundcloud" }
    };
  },
  computed: {
    icon() {
      // console.log("changing");
      // console.log(this[this.social.toLowerCase()]);
      return this[this.socialType.toLowerCase()];
    }
  },
  methods: {
    log: function(evt) {
      window.console.log(evt);
    }
  }
};
</script>
