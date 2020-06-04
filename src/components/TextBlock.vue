<template>
  <div>
    <p :class="titleStyling">{{ textTitle }}</p>
    <p :class="descStyling">{{ textDescription }}</p>
  </div>
</template>


<script>
export default {
  props: {
    textTitle: {
      type: String
    },
    descColor: {
      type: String
    },
    titleColor: {
      type: String
    },
    titleFormat: {
      type: Array,
      default: []
    },
    descFormat: {
      type: Array,
      default: []
    },
    titleAlign: {
      type: String,
      default: "center"
    },
    descAlign: {
      type: String,
      default: "left"
    },
    textDescription: {
      type: String
    }
  },
  data() {
    return {};
  },
  computed: {
    titleStyling() {
      return [
        "title",
        "text-" + this.titleAlign,
        this.titleColor,
        ...this.titleFormat
      ];
    },
    descStyling() {
      return [
        "subtitle-1",
        "text-" + this.descAlign,
        this.descColor,
        ...this.descFormat
      ];
    }
  },
  methods: {
    log: function(evt) {
      window.console.log(evt);
    }
  }
};
</script>
