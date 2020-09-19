<template>
  <layout>
    <v-card active-class="class" color="pink lighten-5" raised height="200">
      <v-card-title>
        <v-row justify="center">{{this.$page.user.companyName}}</v-row>
      </v-card-title>
      <v-card-text>
        <!-- <v-row justify="center">
        <v-col cols="3">-->
        <v-row justify="center">
          <v-img
            src="https://dataimpact.io/wp-content/uploads/2019/04/data-impact-1.png"
            max-width="250"
          ></v-img>
        </v-row>
        <v-row justify="center">
          <v-btn text color="primary" :href="$page.user.companyWebsite">Company's Website</v-btn>
        </v-row>
        <v-dialog v-model="addDialog" width="500">
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="red lighten-2" dark v-bind="attrs" v-on="on">Make Suggestion</v-btn>
          </template>
          <v-card>
            <v-card-title class="headline grey lighten-2" primary-title>Suggest new Feature</v-card-title>
            <v-card-text>
              <v-text-field v-model="addingItem.title" label="Title" required></v-text-field>
              <v-text-field
                v-model="addingItem.desc"
                label="Description"
                hint="example of helper text only on focus"
              ></v-text-field>
              <v-switch
                v-model="addingItem.wouldPay"
                class="mx-2"
                label="Would Pay for this feature"
              ></v-switch>
            </v-card-text>
            <v-divider></v-divider>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="primary" text @click="createFeature()">Suggest</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <!-- </v-col> -->
        <!-- </v-row> -->
      </v-card-text>
    </v-card>
    <v-app-bar dark fixed>
      <!-- <v-app-bar-nav-icon></v-app-bar-nav-icon> -->
      <v-tabs
        v-model="selectedTab"
        dark
        centered
        grow
        class="my-6"
        background-color="brown"
        active-class="selected-tab"
      >
        <v-tab v-for="(tab) in tabs" :key="tab.name">
          <span class="hidden-sm-and-down">{{ tab.name }}</span>
          <v-icon class="d-sm-none">{{tab.icon}}</v-icon>
        </v-tab>
      </v-tabs>
    </v-app-bar>
    <v-tabs-items v-model="selectedTab">
      <!-- {{recent}} -->
      <!-- <features-list :items="recent" />
      <features-list :items="$store.getters.plannedFeatures" />-->
      <!-- <features-list /> -->
    </v-tabs-items>

    <!-- {{$store.getters.trendingFeatures}} -->
  </layout>
</template>
<page-query>
query ($id: ID!) {
  user(id: $id) {
    id
    announcement
    companyName
    companyWebsite
  }
}
</page-query>

<script>
import FeaturesList from "@/components/FeaturesList";
import api from "@/ax";
export default {
  components: { FeaturesList },
  data() {
    return {
      selectedTab: null,
      addingItem: { title: "", desc: "", wouldPay: false },
      defaultItem: { title: "", desc: "", wouldPay: false },
      addDialog: false,
      trending: [],
      recent: [],
      tabs: [
        { name: "Most Recent", icon: "mdi-trending-up" },
        { name: "Planned", icon: "mdi-view-agenda-outline" },
        { name: "Completed", icon: "mdi-check" }
      ]
    };
  },
  metaInfo() {},
  async mounted() {
    if (this.$store.getters.features.length != 0) {
      console.log("from vuex");
      this.recent = this.$store.getters.features;
    } else {
      await this.getAllFeatures();
    }
  },

  methods: {
    async getAllFeatures() {
      console.log(this.$store.getters.features.length);
      // if (this.$store.getters.features.length != 0) {
      //   console.log("in vuex");
      // } else {
      // console.log("from api");
      await api({
        url: "https://graphql.fauna.com/graphql",
        method: "post",
        data: {
          query: `
          query FindAllFeatures {
          allFeatures {
            data {
              _id
              title
              description
              user {companyName companyWebsite announcement}
              votes { data {like wouldPay} }
              tags
              comments {data {text }}
              _ts
              planned
              completed
              wouldPay
                    
            }
          }
        }
      `
        }
      }).then(result => {
        console.log(result.data);
        let features = result.data.data.allFeatures.data;
        // console.log(features);
        // features.sort((a, b) => (a._ts > b._ts ? -1 : 1));
        this.$store.commit("setFeatures", features);
        this.recent = this.$store.getters.features;
      });
      // }
    },
    createFeature() {
      api({
        url: "https://graphql.fauna.com/graphql",
        method: "post",
        data: {
          query: `
      # Write your query or mutation here
        mutation CreateAList {
          createFeature(data: {
            votes: 1, userID: "sss", title: "${this.addingItem.title}", description: "${this.addingItem.desc}", wouldPay:${this.addingItem.wouldPay}
          }) {
            votes
            title
            description
            comments { data {text}}
            _id
            _ts
            wouldPay
          }
        }
        `
        }
      }).then(result => {
        this.addDialog = false;

        // Vue.set(...this.recent, "avatar", avatar);
        // this.recent = [...this.recent, result.data.data.createFeature];
        console.log(this.recent);
        // this.recent = [];
        this.recent.push(result.data.data.createFeature);
        this.recent.sort((a, b) => (a._ts > b._ts ? -1 : 1));
        this.addingItem = this.defaultItem;
        // this.$forceUpdate();
      });
    }
  },
  computed: {
    // trending() {
    //   console.log(this.$store.getters.trending);
    //   return this.$store.getters.trending;
    // }
  }
};
</script>

<style >
#rounded-card {
  border-radius: 25px;
}
#no-border {
  border-width: 0px;
}

.tab-border-left {
  border-style: none;
  border-top-left-radius: 25px !important;

  border-bottom-left-radius: 25px !important;
  border-top-right-radius: 25px !important;
  border-bottom-right-radius: 25px !important;
}

.tab-border-right {
  border-style: none;
  border-top-right-radius: 25px;
  border-bottom-right-radius: 25px;
}
.v-tabs-slider-wrapper {
  height: 0px;
}
.selected-tab {
  background-color: brown;

  /* border-end-end-radius: 25px; */
  /* border-start-start-radius: 60px; */
  /* border-radius: 60px; */

  /* border-end-end-radius: ; */
}
</style>