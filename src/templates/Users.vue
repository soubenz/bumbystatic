<template>
  <layout>
    <v-card class="ma-0 pa-0">
      <sequential-entrance fromTop>
        <v-list-item class="list-group-item" v-for="item in blockList" :key="item.id" dense>
          <v-list-item-content>
            <keep-alive>
              <component class="ma-0 pa-0" :is="item.type" v-bind="item">{{item.buttonText}}</component>
            </keep-alive>
          </v-list-item-content>
        </v-list-item>
      </sequential-entrance>
    </v-card>
  </layout>
</template>


<page-query>
query ($id: ID!){
    users(id: $id) {
    id
    name
    appBarColor
    paid
    layout {type hidden blockID aspectRatio isRipple buttonText buttonLink buttonTextcolor buttonColor buttonStyle buttonSize galleryImages {src alt} textTitle textDescription
    descAlign titleAlign descFormat titleFormat titleColor descColor textTitle social account PatreonAccountID SpotifyAccountID}
    
  }}
</page-query>
<script>
import AvatarBlock from "~/components/AvatarBlock";
import ImageBlock from "~/components/ImageBlock";
import GalleryBlock from "~/components/GalleryBlock";
import DividerBlock from "~/components/DividerBlock";
import ButtonBlock from "~/components/ButtonBlock";
import TextBlock from "~/components/TextBlock";
import SocialBlock from "~/components/SocialBlock";
import OptinBlock from "~/components/OptinBlock";
import PatreonBlock from "~/components/PatreonBlock";
import SpotifyBlock from "~/components/SpotifyBlock";

export default {
  components: {
    AvatarBlock,
    ButtonBlock,
    DividerBlock,
    SocialBlock,
    GalleryBlock,
    ImageBlock,
    OptinBlock,
    TextBlock,
    PatreonBlock,
    SpotifyBlock
  },
  metaInfo() {},

  methods: {},
  computed: {
    blockList() {
      return this.$page.users.layout.filter(block => {
        return !block.hidden;
      });
    }
  }
};
</script>

