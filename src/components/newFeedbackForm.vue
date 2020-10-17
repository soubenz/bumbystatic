<template>
  <v-form>
    <v-row dense>
      <v-col>
        <v-text-field
          name="name"
          label="Title"
          hint="Short, descriptive title"
          outlined
          shaped
          v-model="editedItem.title"
        ></v-text-field>
        <v-textarea
          outlined
          shaped
          label="Description"
          v-model="editedItem.description"
        ></v-textarea>
        <v-switch
          v-model="editedItem.wouldPay"
          class="mx-2"
          label="Would Pay for this feature"
        ></v-switch>
        <v-divider></v-divider>
        <v-switch
          v-if="!email"
          v-model="anonymousPosting"
          class="mx-2"
          label="Post anonymously"
        ></v-switch>
        <v-text-field
          v-if="!anonymousPosting"
          outlined
          shaped
          :disabled="!!email"
          label="Your email address"
          v-model="editedItem.email"
          :value="email"
        ></v-text-field>

        <!-- <v-chip-group multiple active-class="primary--text">
          <v-chip v-for="tag in tags" :key="tag">{{ tag }}</v-chip>
        </v-chip-group>-->
      </v-col>
    </v-row>
  </v-form>
</template>

<script>
export default {
  data() {
    return {
      anonymousPosting: false,
      editedItem: this.inputData,
      user: this.$store.getters.user,
      // email: "",
    };
  },
  mounted() {
    this.editedItem.email = this.email;
    // let user = this.$store.getters.user;
    // if (!!this.user) {
    //   this.email = this.user.email;
    // } else {
    //   // this.user.email = "";
    // }
    // if (!!this.email) {
    //   this.editedItem.email = this.email;
    // }
  },
  props: {
    inputData: { type: Object, required: false },
    email: { type: String, required: false },
  },
  methods: {
    // save() {
    //   this.$emit("update:inputData", this.editedItem);
    // }
  },
};
</script>
<style>
</style>