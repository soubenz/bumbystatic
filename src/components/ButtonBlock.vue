<template>
  <v-row dense>
    <v-col class="ma-0 pa-0">
      <v-btn
        block
        :color="buttonColor"
        @click="track"
        :outlined="isOutlined"
        :ripple="isRipple"
        :rounded="isRounded"
        :tile="isTile"
        :large="isLarge"
        :x-large="isExtraLarge"
        :x-small="isExtraSmall"
        :href="buttonLink"
        target="_blank"
      >
        <span :class="`${this.buttonTextColor}--text`">{{ buttonText }}</span>
      </v-btn>
    </v-col>
  </v-row>
</template>


<script>
export default {
  props: {
    blockID: String,
    buttonColor: {
      type: String,
      default: "#1F7087"
    },
    buttonTextColor: {
      type: String,
      default: "white"
    },
    buttonText: {
      type: String
    },
    buttonLink: {
      type: String
    },
    isRipple: {
      type: Boolean,
      default: false
    },
    buttonSize: {
      type: String,
      default: "classic"
    },
    buttonStyle: {
      type: String,
      default: "classic"
    }
  },
  data() {
    return {
      isRounded: false,
      isTile: false,
      isOutlined: false,
      isLarge: false,
      isExtraLarge: false,
      isExtraSmall: false
    };
  },
  mounted() {
    this.setButtonStyle();
    this.setButtonSize();
  },

  computed: {
    textColorClass() {
      return this.buttonTextColor + "--text";
    }
  },
  methods: {
    track() {
      this.$gtag.event("click", {
        event_category: "button",
        event_label: this.blockID
      });
    },
    log: function(evt) {
      window.console.log(evt);
    },
    setButtonStyle() {
      console.log("heeeeeeeeere mounted");
      console.log(this.buttonStyle);
      switch (this.buttonStyle) {
        case "rounded":
          console.log("case");
          this.isRounded = true;
          this.isTile = this.isOutlined = false;
          break;
        case "tile":
          this.isTile = true;
          this.isRounded = this.isOutlined = false;
          break;
        case "outlined":
          this.isOutlined = true;
          this.isTile = this.isRounded = false;
          break;

        default:
          this.isTile = this.isOutlined = this.isRounded = false;
          break;
      }
      console.log(this.isRounded);
    },
    setButtonSize() {
      switch (this.buttonSize) {
        case "large":
          this.isLarge = true;
          break;
        case "x-large":
          this.isExtraLarge = true;
          this.isLarge = this.isExtraSmall = false;
          break;
        case "x-small":
          this.isExtraSmall = true;
          this.isLarge = this.isExtraLarge = false;
          break;

        default:
          break;
      }
    }
  }
};
</script>
