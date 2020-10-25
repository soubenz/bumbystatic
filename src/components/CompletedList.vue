<template>
  <v-tab-item>
    <!-- {{features}} -->
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
    <template v-if="items.length === 0"> <empty-suggestations /></template>
    <template v-else>
      <v-row>
        <v-col cols="12" sm="6" v-for="item in items" :key="item._id">
          <v-card class="my-6" raised shaped height="250">
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
                  dense
                  v-model="payAlert"
                >
                  <v-row align="center">
                    <v-col class="grow"
                      >Would you be prepared to pay for this feature ?</v-col
                    >
                    <v-col class="shrink">
                      <v-btn @click.stop="votePay(item)">Yes</v-btn>
                      <v-btn
                        @click="
                          payAlert = false;
                          item.payAlert = false;
                        "
                        >No</v-btn
                      >
                    </v-col>
                  </v-row>
                </v-alert>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="12" sm="10">
                <v-card-title
                  style="cursor: pointer"
                  @click="showDetails(item)"
                  >{{ item.title }}</v-card-title
                >
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
            </v-row>
            <v-row dense justify="center">
              {{ isVoted(item) }}
              <!-- {{ item }} -->
              <v-col class="d-flex justify-center ma-1">
                <v-btn-toggle group tile v-model="item.rating" color="#A02C4F">
                  <v-tooltip bottom v-for="icon in emojis" :key="icon.text">
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn
                        transition="fade-transition"
                        :icon="false"
                        x-large
                        @click.native="voteFeature(item, isVoted(item))"
                        class="mx-1"
                        v-bind="attrs"
                        v-on="on"
                      >
                        <v-img
                          class="py-4"
                          max-height="50"
                          max-width="50"
                          :src="icon.img"
                        />
                      </v-btn>
                    </template>
                    <span>{{ icon.text }}</span>
                  </v-tooltip>
                </v-btn-toggle>
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
        </v-col>
      </v-row>
    </template>
  </v-tab-item>
</template>

<script>
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
      showRatingButtons: true,
      emojis: [
        {
          img: require("@/assets/images/dislike.svg"),
          text: "Dislike",
          amount: 0,
        },
        {
          img: require("@/assets/images/neutral.svg"),
          text: "Neutral",
          amount: 0,
        },
        {
          img: require("@/assets/images/like.svg"),
          text: "Like",
          amount: 0,
        },
        {
          img: require("@/assets/images/love.svg"),
          text: "Love",
          amount: 0,
        },
      ],
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
    };
  },
  props: {
    items: { type: Array, required: true },
  },

  methods: {
    rateEntry(item, icon) {
      item.rated = true;
      // icon.color = "green";
      // icon.deactivated = false;
      this.showRatingButtons = false;
    },
    votePay(item) {
      api({
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
      });
    },
    async removeVote(item) {
      await api({
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
      });
    },
    async addVote(item) {
      let user = this.$store.getters.user;

      await api({
        data: {
          query: `
      mutation createVote($feature: ID, $user: ID,  $rating: Float) {
        createVote(data: {
        like: true,
          wouldPay: false,
         rating: $rating,
          feature: {connect :$feature}
          user: {connect: $user}
        }) {
            rating
              _id wouldPay like
          user {_id email}
        }
      }
        `,
          variables: {
            feature: item._id,
            user: user._id,
            rating: item.rating,
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
        item.rating = isVoted[0].rating;
        return true;
      }
      return false;
    },
    async createUser() {
      await api({
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

        this.clickedFeature.voted = true;
        this.clickedFeature.voteID = vote._id;
        this.clickedFeature.payAlert = true;
        this.clickedFeature.votes.data.push(vote);
      });
    },
    getTagInfo(tag) {
      return this.icons[tag.toLowerCase()];
    },

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
    },
  },
};
</script>

<style>
</style>