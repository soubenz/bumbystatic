<template>
  <layout>
    <v-dialog v-model="addDialog" width="500">
      <template v-slot:activator="{ on, attrs }">
        <v-btn color="red lighten-2" dark v-bind="attrs" v-on="on">Suggest New</v-btn>
      </template>
      <v-card>
        <v-card-title class="headline grey lighten-2" primary-title>Privacy Policy</v-card-title>
        <v-card-text>
          <v-text-field v-model="addingItem.title" label="Title" required></v-text-field>
          <v-text-field
            v-model="addingItem.desc"
            label="Description"
            hint="example of helper text only on focus"
          ></v-text-field>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="createFeature()">Suggest</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-tabs
      v-model="selectedTab"
      dark
      centered
      grow
      class="tab-border-left"
      background-color="brown"
      active-class="selected-tab"
    >
      <v-tab v-for="(tab) in tabs" :key="tab.name">
        <span class="hidden-sm-and-down">{{ tab.name }}</span>
        <v-icon class="d-sm-none">{{tab.icon}}</v-icon>
      </v-tab>
    </v-tabs>

    <v-tabs-items v-model="selectedTab">
      <!-- {{recent}} -->
      <features-list :items="recent" />
      <!-- <features-list /> -->
      <!-- <features-list /> -->
    </v-tabs-items>
    <!-- {{$store.getters.trendingFeatures}} -->
  </layout>
</template>


<script>
import FeaturesList from "@/components/FeaturesList";
import api from "@/ax";
export default {
  components: { FeaturesList },
  data() {
    return {
      selectedTab: null,
      addingItem: { title: "", desc: "" },
      defaultItem: { title: "", desc: "" },
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
    await this.getAllFeatures();
  },

  methods: {
    async getAllFeatures() {
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
              votes
              tags
              comments {data {text }}
              _ts
            
            }
          }
        }
      `
        }
      }).then(result => {
        console.log(result.data);
        let features = result.data.data.allFeatures.data;
        console.log(features);
        features.sort((a, b) => (a._ts > b._ts ? -1 : 1));
        this.$store.commit("setFeatures", features);
        this.recent = features;
      });
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
            votes: 0, userID: "sss", title: "${this.addingItem.title}", description: "${this.addingItem.desc}"
          }) {
            votes
            title
            description
            userID
            comments { data {text}}
            _id
            _ts
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