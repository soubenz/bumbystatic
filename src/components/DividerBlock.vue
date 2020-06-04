<template>
  <v-divider :color="color"></v-divider>
</template>


<script>
export default {
  props: {
    blockID: String,
    color: {
      type: String,
      default: "#1F7087"
    }
  },
  data() {
    return {};
  },
  computed: {},
  methods: {
    log: function(evt) {
      window.console.log(evt);
    }
  }
};
</script>
