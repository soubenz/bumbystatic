<template>
  <v-row dense>
    <v-col class="ma-0 pa-0">
      <p class="text-center display-1 error--text" v-if="errorMsg">Sorry ! You are already signed up</p>
      <v-form ref="form" v-model="valid" v-else-if="!successMsg">
        <v-text-field
          v-model="email"
          :rules="emailRules"
          single-line
          filled
          rounded
          label="your@email.com"
          required
        ></v-text-field>

        <v-btn
          :disabled="!valid"
          block
          rounded
          large
          color="success"
          @click="saveEmail"
          class="mr-4"
        >{{optinText}}</v-btn>
      </v-form>
      <p class="text-center display-1 success--text" v-else>Thanks ! We'll keep you informed :)</p>
    </v-col>
  </v-row>
</template>


<script>
import api from "@/ax.js";
export default {
  props: {
    blockID: String,
    optinText: {
      type: String,
      default: "Sign Up !"
    },
    buttonTextColor: {
      type: String,
      default: "white"
    },
    buttonText: {
      type: String
      //   default: "Network Engineer"
    },
    buttonLink: {
      type: String
    }
  },
  data() {
    return {
      itemID: 1,
      successMsg: false,
      errorMsg: false,
      emailRules: [
        v => !!v || "E-mail is required",
        v => /.+@.+\..+/.test(v) || "E-mail must be valid"
      ],
      valid: true,
      email: null
    };
  },
  computed: {
    //   textColorClass(){
    //       return this.buttonTextColor + "--text"
    //   }
  },
  methods: {
    track() {
      this.$gtag.event("generate_lead", {
        event_category: "engagement",
        event_label: this.blockID
      });
    },
    log: function(evt) {
      window.console.log(evt);
    },
    async saveEmail() {
      api
        .post(
          "https://us-east-1.aws.webhooks.mongodb-stitch.com/api/client/v2.0/app/test-heyur/service/optin/incoming_webhook/optin",
          { data: { email: this.email, userID: 123 } }
        )
        .then(
          data => {
            this.track();
            this.successMsg = true;
            // console.log(data);
          },
          error => {
            this.errorMsg = true;

            console.log("error");
          }
        );
    }
  }
};
</script>
