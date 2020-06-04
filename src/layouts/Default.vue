<template>
  <v-app>
    <v-app-bar app :color="$page.users.appBarColor">
      <v-spacer />
      <span class="title ml-3 mr-5">{{$page.users.name}}</span>
      <v-spacer />
    </v-app-bar>
    <v-content>
      <v-container class="ma-0 pa-0" fluid>
        <v-row class="ma-0 pa-0" justify="center">
          <v-col cols="12" sm="8" md="5">
            <v-card class="elevation-12" shaped>
              <slot />
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
    <default-footer v-if="$page.paid"></default-footer>
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
    drawer: null
  }),
  methods: {}
};
</script>

