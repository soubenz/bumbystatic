<template>
  <!-- <section class="layouts section"> -->
  <div class="container">
    <lottie-animation
      :path="`animations/${animation}.json`"
      :loop="false"
      :width="200"
      :height="160"
      is-paddingless
    />
    <slot />
  </div>
  <!-- </section> -->
</template>


<script>
export default {
  props: {
    animation: String
  }
};
</script>

<style lang="scss">
@import "~bulma/sass/utilities/_all";
// Set your colors
$primary: rgb(197, 65, 175);
$primary-invert: findColorInvert($primary);
$twitter: rgb(197, 65, 175);
$twitter-invert: findColorInvert($twitter);
$hero-body-padding: "1rem 0.5rem";
// Setup $colors to use as bulma classes (e.g. 'is-twitter')
$colors: (
  "white": (
    $white,
    $black
  ),
  "black": (
    $black,
    $white
  ),
  "light": (
    $light,
    $light-invert
  ),
  "dark": (
    $dark,
    $dark-invert
  ),
  "primary": (
    $primary,
    $primary-invert
  ),
  "info": (
    $info,
    $info-invert
  ),
  "success": (
    $success,
    $success-invert
  ),
  "warning": (
    $warning,
    $warning-invert
  ),
  "danger": (
    $danger,
    $danger-invert
  ),
  "twitter": (
    $twitter,
    $twitter-invert
  )
);

// Links
$link: $primary;
$link-invert: $primary-invert;
$link-focus-border: $primary;

// Import Bulma and Buefy styles
@import "~bulma";
@import "~buefy/src/scss/buefy";
/* body {
  font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", Roboto,
    "Helvetica Neue", Arial, sans-serif;
  margin: 0;
  padding: 0;
  line-height: 1.5;
} */

/* .layout {
  max-width: 1000px;
  margin: 0 auto;
  padding-left: 20px;
  padding-right: 20px;
} */
/* 
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  height: 80px;
}

.nav__link {
  margin-left: 20px;
} */
</style>
