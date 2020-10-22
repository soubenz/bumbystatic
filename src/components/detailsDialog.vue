<template>
  <v-dialog v-model="commentsDialog" width="500">
    <v-card>
      <!-- <v-card-title class="headline grey lighten-2"></v-card-title> -->
      <v-card-text>
        <v-btn color="primary" text @click="createFeature()">Add New</v-btn>
        <span>created at {{item}}</span>
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
</template>

<script>
export default {};
</script>

<style>
</style>