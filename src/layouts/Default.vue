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
    pageTitle: String,
  },
  data: () => ({
    items: ["Pending", "In progress", "Completed"],
  }),
  methods: {},
};
</script>

