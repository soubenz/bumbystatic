<template>
  <layout>
    <v-card active-class="class" color="#F3A738" raised height="200">
      <v-card-title>
        <v-row justify="center">{{ this.$page.user.companyName }}</v-row>
      </v-card-title>
      <v-card-text>
        <v-row justify="center">
          <p class="text-h5">{{ $page.user.boardCaption }}</p>
          <!-- <v-img
            src="https://dataimpact.io/wp-content/uploads/2019/04/data-impact-1.png"
            max-width="250"
          ></v-img> -->
        </v-row>
        <v-row justify="center">
          <v-btn text color="#DC7F9B" :href="$page.user.companyWebsite"
            >Company's Website</v-btn
          >
        </v-row>
        <v-dialog v-model="announcementDialog" width="500" height="400">
          <v-card>
            <v-card-title class="text-h5 grey lighten-2"
              ><v-icon large>mdi-bullhorn-outline</v-icon>
              Announcement</v-card-title
            >
            <v-card-text class="mt-4">
              <span class="text-body-1">{{ announcementText }} </span>
            </v-card-text>
            <v-divider></v-divider>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="primary" left text @click="closeAnnouncement"
                >close</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-row justify="space-between">
          <p>{{ loggedinUser }}</p>

          <v-dialog v-model="addDialog" width="500">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="#2F2F2F" dark v-bind="attrs" v-on="on"
                >Give feedback</v-btn
              >
            </template>

            <v-card>
              <v-card-title class="headline grey lighten-2" primary-title
                >Suggest new Feature</v-card-title
              >
              <v-card-text>
                <new-feedback-form
                  :email="loggedinUser"
                  :inputData.sync="addingItem"
                />
                <!-- <v-text-field
                  v-model="addingItem.title"
                  label="Title"
                  required
                ></v-text-field>
                <v-text-field
                  v-model="addingItem.desc"
                  label="Description"
                  hint="example of helper text only on focus"
                ></v-text-field>
                <v-switch
                  v-model="addingItem.wouldPay"
                  class="mx-2"
                  label="Would Pay for this feature"
                ></v-switch> -->
              </v-card-text>
              <!-- <v-divider></v-divider> -->
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="primary" text @click="createFeature()"
                  >Suggest</v-btn
                >
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-row>
      </v-card-text>
    </v-card>
    <v-app-bar dark fixed>
      <v-tabs
        v-model="selectedTab"
        dark
        centered
        grow
        class="my-6"
        background-color="#2F2F2F"
        active-class="selected-tab"
      >
        <v-tab v-for="tab in tabs" :key="tab.name">
          <span class="hidden-sm-and-down">{{ tab.name }}</span>
          <v-icon class="d-sm-none">{{ tab.icon }}</v-icon>
        </v-tab>
      </v-tabs>
    </v-app-bar>
    <v-tabs-items v-model="selectedTab">
      <features-list :items="recent" />
      <features-list :items="planned" />
      <completed-list :items="completed" />
    </v-tabs-items>
  </layout>
</template>
<page-query>
query ($id: ID!) {
  user(id: $id) {
    id
    announcement
    companyName
    companyWebsite
    boardCaption
  }
}
</page-query>

<script>
import newFeedbackForm from "@/components/newFeedbackForm";
import FeaturesList from "@/components/FeaturesList";
import CompletedList from "@/components/CompletedList";
import api from "@/ax";
export default {
  components: { FeaturesList, CompletedList, newFeedbackForm },
  data() {
    return {
      selectedTab: null,
      addingItem: { title: "", desc: "", wouldPay: false },
      defaultItem: { title: "", desc: "", wouldPay: false },
      addDialog: false,
      trending: [],
      completed: [],
      announcementText: "",
      planned: [],
      recent: [],
      announcementDialog: false,
      tabs: [
        { name: "Most Recent", icon: "mdi-trending-up" },
        { name: "Planned", icon: "mdi-view-agenda-outline" },
        { name: "Completed", icon: "mdi-check" },
      ],
    };
  },
  metaInfo() {},
  async mounted() {
    // if (this.$store.getters.features.length != 0) {
    //   console.log("from vuex");
    //   this.recent = this.$store.getters.features;
    // } else {
    await this.getAllFeatures();
    if (!this.$store.getters.announcement) {
      this.announcementDialog = true;
    }
    // }
  },

  methods: {
    closeAnnouncement() {
      this.announcementDialog = false;
      this.$store.commit("setAnnouncement", true);
    },
    async getAllFeatures() {
      // console.log(this.$store.getters.features.length);
      // if (this.$store.getters.features.length != 0) {
      //   console.log("in vuex");
      // } else {
      // console.log("from api");
      await api({
        url: "https://graphql.fauna.com/graphql",
        method: "post",
        data: {
          query: `
       query findUser {
          usersByUsername(username: "${this.$page.user.id}") {
          _id
          _ts
          announcement
          features { data {title _id completed planned
          description  votes {data {rating wouldPay like _id user  {_id}}}}}
        }  
          }
        `,
        },
      }).then((result) => {
        console.log(result.data);
        let features = result.data.data.usersByUsername.features.data;

        this.completed = features.filter((feature) => {
          return feature.completed == true;
        });
        this.planned = features.filter((feature) => {
          return feature.planned == true;
        });
        this.announcementText = result.data.data.usersByUsername.announcement;
        // console.log(this.completed);
        // if (this.$store.getters.user != null){
        //   features.map( (feature) => { if(vote.user._id == this.$store.getters.user._id) {} })

        // }

        // console.log(features);
        // features.sort((a, b) => (a._ts > b._ts ? -1 : 1));
        // this.$store.commit("setFeatures", features);
        this.recent = features;
      });
      // }
    },
    createFeature() {
      api({
        url: "https://graphql.fauna.com/graphql",
        method: "post",
        data: {
          query: `
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
        `,
        },
      }).then((result) => {
        this.addDialog = false;

        // Vue.set(...this.recent, "avatar", avatar);
        // this.recent = [...this.recent, result.data.data.createFeature];
        console.log(this.recent);
        // this.recent = [];
        this.recent.push(result.data.data.createFeature);
        this.recent.sort((a, b) => (a._ts > b._ts ? -1 : 1));
        this.addingItem = this.defaultItem;
        this.$store.commit("setFeatures", features);

        // this.$forceUpdate();
      });
    },
  },
  computed: {
    loggedinUser() {
      const user = this.$store.getters.user;
      if (user != null) {
        if (!!user.email) {
          return user.email;
        } else {
          return true;
        }
      }
      // console.log(this.$store.getters);
      return false;
      // if (this.$store.getters.user != null) {
      //   if (this.$store.getters.user.email == "") {
      //     return "anonymous";
      //   } else {
      //     return $store.getters.user.email;
      //   }
      // }
      // return false;
    },
    // trending() {
    //   console.log(this.$store.getters.trending);
    //   return this.$store.getters.trending;
    // }
  },
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
  background-color: #dc7f9b;

  /* border-end-end-radius: 25px; */
  /* border-start-start-radius: 60px; */
  /* border-radius: 60px; */

  /* border-end-end-radius: ; */
}
</style>