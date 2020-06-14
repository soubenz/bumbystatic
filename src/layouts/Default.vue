<template>
  <v-app>
    <v-app-bar app>
      <v-spacer />
      <v-spacer />
    </v-app-bar>
    <v-main>
      <v-container class="ma-0 pa-0" fluid>
        <v-row class="ma-0 pa-0" justify="center">
          <v-col cols="12" sm="9" md="7">
            <slot />
          </v-col>
        </v-row>
      </v-container>
    </v-main>
    <!-- <default-footer v-if="$page.paid"></default-footer> -->
  </v-app>
</template>

<script>
import DefaultFooter from "~/components/DefaultFooter";
export default {
  components: { DefaultFooter },
  props: {
    pageTitle: String
  },
  data: () => ({
    tab: null,
    items: ["Pending", "In progress", "Completed"],
    text:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",

    drawer: null
  }),
  methods: {}
};
</script>

