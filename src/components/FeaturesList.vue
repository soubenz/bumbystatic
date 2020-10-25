<template>
  <v-tab-item>
    <v-dialog v-model="commentsDialog" width="500">
      <v-card>
        <!-- <v-card-title class="headline grey lighten-2"></v-card-title> -->
        <v-card-text>
          <v-btn color="primary" text @click="createFeature()">Add New</v-btn>
          <span>created on {{ transformDate(editingItem._ts) }}</span>
          <span>posted by {{ transformDate(editingItem._ts) }}</span>

          <!-- <v-text-field v-model="addingItem.title" label="Title" required></v-text-field>
          <v-text-field
            v-model="addingItem.desc"
            label="Description"
            hint="example of helper text only on focus"
          ></v-text-field>
          <v-switch v-model="addingItem.wouldPay" class="mx-2" label="Would Pay for this feature"></v-switch>-->
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="userLoginDialog" width="500">
      <v-card>
        <!-- <v-card-title class="headline grey lighten-2"></v-card-title> -->
        <v-card-text>
          <v-btn color="primary" text @click="showEmailField = true"
            >Claim Your Account</v-btn
          >
          <v-btn color="primary" text @click="createUser()"
            >Continue Anonymously</v-btn
          >
          <v-text-field
            v-if="showEmailField"
            label="Your Email Address"
            v-model="emailField"
            >Claim Your Account</v-text-field
          >
          <v-btn
            color="primary"
            left
            @click="createUser('anonymous')"
            v-if="showEmailField"
            >Create and save vote</v-btn
          >
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-snackbar v-model="snackbarVote" rounded="pill" multi-line>
      Your vote has been saved
      <v-btn color="pink" text @click="snackbarVote = false">Close</v-btn>
    </v-snackbar>
    <template v-if="items.length === 0"><empty-suggestations /></template>
    <template v-else>
      <v-card v-for="item in items" :key="item._id" class="my-6" raised shaped>
        {{ item.voted && item.payAlert }}
        <v-row>
          <v-col
            v-if="item.voted == true && payAlert == true && !!item.payAlert"
          >
            <v-alert
              prominent
              dismissible
              border="top"
              colored-border
              type="info"
              color="#DC7F9B"
              dense
              v-model="payAlert"
            >
              <v-row align="center">
                <v-col class="grow"
                  >Would you be prepared to pay for this feature ?</v-col
                >
                <v-col class="shrink">
                  <v-btn
                    @click.stop="votePay(item)"
                    class="my-2"
                    color="#94BFA7"
                    dark
                    >Yes</v-btn
                  >
                  <v-btn
                    @click="
                      payAlert = false;
                      item.payAlert = false;
                    "
                    color="#DC7F9B"
                    class="my-2"
                    >No</v-btn
                  >
                </v-col>
              </v-row>
            </v-alert>
          </v-col>
        </v-row>

        {{ isVoted(item) }}
        {{ item.voteID }}
        <v-row dense justify="center">
          <v-col
            cols="12"
            sm="1"
            class="d-flex flex-sm-column justify-sm-center justify-space-around"
          >
            <v-tooltip bottom>
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  class="ma-1 px-2 d-flex justify-space-around"
                  :outlined="!isVoted(item)"
                  color="#DC7F9B"
                  v-bind="attrs"
                  v-on="on"
                  @click="voteFeature(item, isVoted(item))"
                >
                  <v-icon class>mdi-arrow-up-drop-circle-outline</v-icon>

                  <span
                    class="d-inline justify-center font-weight-bold"
                    v-text="item.votes.data.length"
                  ></span>
                </v-btn>
              </template>
              <span>Upvote</span>
            </v-tooltip>
            <v-tooltip bottom>
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  class="ma-1 px-2 d-flex justify-space-around"
                  outlined
                  v-bind="attrs"
                  v-on="on"
                  color="#DC7F9B"
                  @click="showDetails(item)"
                >
                  <v-icon>mdi-comment-multiple-outline</v-icon>
                  <!-- <span
              class="d-inline justify-center font-weight-bold"
              v-text="item.comments.data.length"
            ></span>-->
                </v-btn>
              </template>
              <span>Add a comment</span>
            </v-tooltip>
          </v-col>
          <v-col cols="12" sm="10">
            <v-tooltip bottom>
              <template v-slot:activator="{ on, attrs }">
                <v-card-title
                  v-bind="attrs"
                  v-on="on"
                  style="cursor: pointer"
                  @click="showDetails(item)"
                  >{{ item.title }}</v-card-title
                >
              </template>
              <span>Click for more details</span>
            </v-tooltip>
            <v-card-text class="hidden-sm-and-down">{{
              item.description
            }}</v-card-text>
            <v-card-actions>
              <v-chip
                class="hidden-sm-and-down mx-1"
                :color="getTagInfo('planned').color"
                v-if="item.planned"
              >
                <v-icon left>{{ getTagInfo("planned").icon }}</v-icon>
                <span class="font-weight-bold">Planned</span>
              </v-chip>
              <v-icon
                class="d-sm-none mx-1"
                :color="getTagInfo('planned').color"
                >{{ getTagInfo("planned").icon }}</v-icon
              >

              <v-chip
                class="hidden-sm-and-down mx-1"
                :color="getTagInfo('wouldPay').color"
                v-if="item.wouldPay"
              >
                <v-icon left>{{ getTagInfo("wouldPay").icon }}</v-icon>
                <span class="font-weight-bold">wouldPay</span>
              </v-chip>
              <v-icon
                class="d-sm-none mx-1"
                dark
                :color="getTagInfo('wouldPay').color"
                >{{ getTagInfo("wouldPay").icon }}</v-icon
              >
              <!-- <template v-for="(tag, i) in item.tags">
                  <v-chip :key="i" class="hidden-sm-and-down mx-1" :color="getTagInfo(tag).color">
                    <v-icon left>{{getTagInfo(tag).icon}}</v-icon>
                    <span class="font-weight-bold">{{tag}}</span>
                  </v-chip>
                  <v-icon
                    class="d-sm-none mx-1"
                    :key="i"
                    :color="getTagInfo(tag).color"
                  >{{getTagInfo(tag).icon}}</v-icon>
            </template>-->
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
    </template>
  </v-tab-item>
</template>

<script>
// import InfiniteLoading from "vue-infinite-loading";
import detailsDialog from "@/components/detailsDialog";
import EmptySuggestations from "@/components/EmptySuggestations";
import api from "@/ax";
export default {
  components: { detailsDialog, EmptySuggestations },
  data() {
    return {
      snackbarVote: false,
      commentsDialog: false,
      showEmailField: false,
      emailField: null,
      userLoginDialog: false,
      editingItem: {},
      clickedFeature: null,
      payAlert: false,
      user: this.$store.getters.user,
      voted: [],

      icons: {
        planned: {
          icon: "mdi-view-agenda-outline",
          color: "deep-purple lighten-3",
          dark: false,
        },
        popular: {
          icon: "mdi-trending-up",
          color: "teal lighten-3",
          dark: false,
        },
        bug: {
          icon: "mdi-alert-circle-outline",
          color: "deep-orange lighten-3",
          dark: true,
        },
        wouldpay: {
          icon: "mdi-currency-usd",
          color: "yellow lighten-3",
          dark: false,
        },
        // enhancement: { icon: "mdi-currency-usd", color: "", dark: true },
        "very important": {
          icon: "mdi-currency-usd",
          color: "blue-grey lighten-3",
          dark: true,
        },
      },
      // features: this.items
    };
  },
  props: {
    items: { type: Array, required: true },
  },
  // async mounted() {
  //   this.$store.commit("setPending", pending);
  // },

  methods: {
    votePay(item) {
      // console.log(this.getUserVote(item));
      api({
        url: "https://graphql.fauna.com/graphql",
        method: "post",
        data: {
          query: `
        mutation updateVote($id: ID!) {
          updateVote(id: $id, data: {
            wouldPay: true,
          }) {
              feature {_id}
                _id
            user {_id}
          }
        }
        `,
          variables: { id: item.voteID },
        },
      }).then((result) => {
        item.payAlert = false;
        this.payAlert = false;
        console.log(result.data);
        console.log(item.votes.data);
        // item.votes.data.push(result.data.data.createVote);
        // this.$store.commit("vote", { item: item, status: status });
        // this.snackbarVote = true;
        // item.payAlert = status;
      });
    },
    async removeVote(item) {
      console.log("removing");
      console.log(item);
      await api({
        url: "https://graphql.fauna.com/graphql",
        method: "post",
        data: {
          query: `
       mutation updateVote($vote: ID!) {
          deleteVote(id: $vote) {
                _id
          }
        }
        `,
          variables: { vote: item.voteID },
        },
      }).then((result) => {
        item.voted = false;
        item.voteID = null;
        console.log(result.data.data.deleteVote._id);
        const index = item.votes.data.indexOf(item);
        console.log(item.votes.data);
        item.votes.data = item.votes.data.filter((vote) => {
          return vote._id != result.data.data.deleteVote._id;
        });
        console.log(item.votes.data);
        // item.votes.data.push(result.data.data.createVote);
        // this.$store.commit("vote", { item: item, status: status });
        // this.snackbarVote = true;
        // item.payAlert = status;
      });
    },
    async addVote(item) {
      let user = this.$store.getters.user;
      // console.log(this.items);
      await api({
        url: "https://graphql.fauna.com/graphql",
        method: "post",
        data: {
          query: `
      
      mutation createVote($feature: ID, $user: ID) {
        createVote(data: {
        like: true,
          wouldPay: false,
          feature: {connect :$feature}
          user: {connect: $user}
        }) {
            
              _id wouldPay like
          user {_id email}
        }
      }
        `,
          variables: {
            feature: item._id,
            user: user._id,
          },
        },
      }).then((result) => {
        // console.log(result.data);
        let vote = result.data.data.createVote;
        item.voted = true;
        item.voteID = vote._id;
        item.payAlert = true;
        this.payAlert = true;
        item.votes.data.push(vote);
      });
    },

    getUserVote(item) {
      return item.votes.data.filter((vote) => {
        return (
          vote.user &&
          (vote.user._id == this.user._id ||
            vote.user.data._id == this.user._id)
        );
      });
    },
    isVoted(item) {
      if (!this.$store.getters.user) {
        return false;
      }
      let isVoted = item.votes.data.filter((vote) => {
        return !!vote.user && vote.user._id == this.$store.getters.user._id;
      });
      if (isVoted.length != 0) {
        // console.log(isVoted);
        item.voted = true;
        item.voteID = isVoted[0]._id;
        return true;
      }
      return false;
    },
    async createUser() {
      await api({
        url: "https://graphql.fauna.com/graphql",
        method: "post",
        data: {
          query: `
      
      mutation createVote($feature: ID, $email: String) {
        createVote(data: {
        like: true,
          wouldPay: false,
          feature: {connect :$feature}
          user: {create: {email: $email}}
        }) {
            
              _id wouldPay like
          user {_id email}
        }
      }
        `,
          variables: {
            feature: this.clickedFeature._id,
            email: this.emailField,
          },
        },
      }).then((result) => {
        console.log(result.data);
        this.userLoginDialog = false;
        let user = result.data.data.createVote.user;
        let vote = result.data.data.createVote;
        this.$store.commit("setUser", user);
        // this.$store.commit("vote", {
        //   item: this.clickedFeature,
        //   status: true,
        //   vote: vote,
        // });
        this.clickedFeature.voted = true;
        this.clickedFeature.voteID = vote._id;
        this.clickedFeature.payAlert = true;
        this.clickedFeature.votes.data.push(vote);
        // this.recent = this.$store.getters.features;
      });
    },
    getTagInfo(tag) {
      return this.icons[tag.toLowerCase()];
    },

    // vote(item, status) {
    //   this.$store.commit("vote", { item: item, status: status });
    //   this.snackbarVote = true;
    // },
    showDetails(item) {
      this.editingItem = item;
      this.commentsDialog = true;
    },
    transformDate(_ts) {
      var ts = new Date(_ts / 1000);
      return ts.toDateString();
    },
    voteFeature(item, status) {
      console.log(item);
      let user = this.$store.getters.user;
      if (user == null) {
        this.userLoginDialog = true;
        this.clickedFeature = item;
        return;
      }

      if (!!status) {
        this.removeVote(item);
        return;
      }
      this.addVote(item);
      // console.log("showing item after adding vote");
      // console.log(item);
      return;
      // console.log(this.isVoted(item));
      // let data = {
      //   query: `
      //   mutation createVote($feature: ID, $user: ID, $status: Boolean) {
      //     createVote(data: {
      //     like: $status,
      //       wouldPay: false,
      //       feature: {connect :$feature}
      //       user: {connect: $user}
      //     }) {
      //        wouldPay
      //        like
      //        user {_id}
      //     }
      //   }
      //   `,
      //   variables: { feature: item._id, user: user._id, status: status },
      // };
      // if (this.isVoted(item)) {
      //   data = {
      //     query: `
      //   mutation updateVote($vote: ID!) {
      //     updateVote(id: $vote, data: {
      //       wouldPay: true,
      //     }) {
      //         feature {_id}
      //           _id
      //       user {_id}
      //     }
      //   }
      //   `,
      //     variables: { vote: item.votes.data._id },
      //   };
      // }

      // api({
      //   url: "https://graphql.fauna.com/graphql",
      //   method: "post",
      //   data: {
      //     query: `
      //   mutation createVote($feature: ID, $user: ID, $status: Boolean) {
      //     createVote(data: {
      //     like: $status,
      //       wouldPay: false,
      //       feature: {connect :$feature}
      //       user: {connect: $user}
      //     }) {
      //        wouldPay
      //        like
      //        user {_id}
      //     }
      //   }
      //   `,
      //     variables: { feature: item._id, user: user._id, status: status },
      //   },
      // }).then((result) => {
      //   item.payAlert = status;
      //   console.log(result.data);
      //   console.log(item.votes.data);
      //   // item.votes.data.push(result.data.data.createVote);
      //   // this.$store.commit("vote", { item: item, status: status });
      //   this.snackbarVote = true;
      // });

      return;
      //   let nbreOfVotes = status ? 1 : -1;
      //   console.log(nbreOfVotes);
      //   api({
      //     url: "https://graphql.fauna.com/graphql",
      //     method: "post",
      //     data: {
      //       query: `
      //     mutation UpdateFeature {
      //       updateFeature(id:"${item._id}", data: {
      //         votes: ${item.votes + nbreOfVotes} , title: "${
      //         item.title
      //       }", user:{connect: "${item.userID}"}

      //       }) {
      //         votes
      //       }
      //     }
      //     `
      //     }
      //   }).then(result => {
      //     item.votes = result.data.data.updateFeature.votes;
      //     this.$store.commit("vote", { item: item, status: status });
      //     this.snackbarVote = true;
      //     item.payAlert = status;
      //   });
    },
  },
};
</script>

<style>
</style>