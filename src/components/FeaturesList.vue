<template>
  <v-tab-item>
    <!-- {{features}} -->
    <v-card v-for="item in items" :key="item._id" class="my-6" id="rounded-card" raised>
      <v-row dense justify="center">
        <v-col
          cols="12"
          sm="1"
          class="d-flex flex-sm-column justify-sm-center justify-space-around"
        >
          <v-btn
            class="ma-1 px-2 d-flex justify-space-around"
            :outlined="!item.voted"
            color="blue lighten-2"
            @click="vote(item, !item.voted)"
          >
            <v-icon class>mdi-arrow-up-drop-circle-outline</v-icon>
            <span class="d-inline justify-center font-weight-bold" v-text="item.votes"></span>
          </v-btn>
          <span class="d-inline justify-center mx-2 px-2 font-weight-bold" v-text="item.votes"></span>
          <v-btn class="mx-2" text icon color="blue lighten-2" @click="snackbarVote = true">
            <v-icon>mdi-comment-multiple-outline</v-icon>
          </v-btn>
        </v-col>
        <v-col cols="12" sm="10">
          <v-card-title primary-title>{{ item.title }}</v-card-title>
          <v-card-text class="hidden-sm-and-down">{{ item.description }}</v-card-text>
          <v-card-actions>
            <template v-for="(tag, i) in item.tags">
              <v-chip :key="i" class="hidden-sm-and-down mx-1" :color="getTagInfo(tag).color">
                <v-icon left>{{getTagInfo(tag).icon}}</v-icon>
                <span class="font-weight-bold">{{tag}}</span>
              </v-chip>
              <v-icon
                class="d-sm-none mx-1"
                :key="i"
                :color="getTagInfo(tag).color"
              >{{getTagInfo(tag).icon}}</v-icon>
            </template>
          </v-card-actions>
        </v-col>
        <!-- <v-col
          cols="12"
          sm="1"
          class="d-flex flex-sm-column justify-sm-center justify-space-around"
        >
          <v-snackbar v-model="snackbarVote">
            Your vote has been saved
            <v-btn color="pink" text @click="snackbarVote = false">Close</v-btn>
          </v-snackbar>

          <v-btn class="mx-2" text icon color="blue lighten-2" @click="snackbarVote = true">
            <v-icon>mdi-comment-plus-outline</v-icon>
          </v-btn>
          <span class="d-inline justify-center mx-2 px-2 font-weight-bold">23</span>
          <v-btn class="mx-2" text icon color="blue lighten-2">
            <v-icon>mdi-comment-multiple-outline</v-icon>
          </v-btn>
        </v-col>-->
      </v-row>
    </v-card>
  </v-tab-item>
</template>

<script>
export default {
  data() {
    return {
      snackbarVote: false,
      //   snackbarVoteDown: false,
      pending: [
        {
          id: 1,
          text: "Add the ability to embed Kampsite as a widget on a website",
          tags: [
            "Popular",
            // "Enhancement"
            "Bug",
            "Would Pay",
            "Very Important",
            "Planned"
          ],
          desc:
            "Add the ability on kampsite to add more questions under the 'would you...",
          comments: [],
          votes: 12
        },
        {
          id: 2,
          text: "Support other languages",
          tags: [],
          desc:
            "Allow users to choose the language the feedback page displays in",
          comments: [],
          votes: 5
        },
        {
          id: 3,
          text: "Add public Kampsite API",
          tags: [],
          desc:
            "With an API I could build an interface within my app for my users to i...",
          comments: [],
          votes: 454
        },
        {
          id: 4,
          text: "Bulk delete",
          tags: [],
          desc: "Add integration with JIRA",
          comments: [],
          votes: 22
        }
      ],
      icons: {
        planned: {
          icon: "mdi-view-agenda-outline",
          color: "deep-purple lighten-3",
          dark: false
        },
        popular: {
          icon: "mdi-trending-up",
          color: "teal lighten-3",
          dark: false
        },
        bug: {
          icon: "mdi-alert-circle-outline",
          color: "deep-orange lighten-3",
          dark: true
        },
        "would pay": {
          icon: "mdi-currency-usd",
          color: "yellow lighten-3",
          dark: false
        },
        // enhancement: { icon: "mdi-currency-usd", color: "", dark: true },
        "very important": {
          icon: "mdi-currency-usd",
          color: "blue-grey lighten-3",
          dark: true
        }
      }
      // features: this.items
    };
  },
  props: {
    items: { type: Array, required: true }
  },
  // async mounted() {
  //   this.$store.commit("setPending", pending);
  // },

  methods: {
    getTagInfo(tag) {
      // console.log(tag);
      // console.log(this.icons.enhancement);
      return this.icons[tag.toLowerCase()];
    },
    vote(item, status) {
      this.$store.commit("vote", { item: item, status: status });
      this.snackbarVote = true;
    },
    }
  }
};
</script>

<style>
</style>