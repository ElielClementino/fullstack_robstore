<template>
  <v-container class="fill-height">
      <blockquote class="blockquote text-h1 text-user">
        <em> Carteira Digital </em>
      </blockquote>
    <digital-wallet/>
  </v-container>
</template>

<script>

import DigitalWallet from "@/components/DigitalWallet.vue"

export default {
  name: "DigitalWalletView",
  components: {
    DigitalWallet
  }
}
</script>

<style scoped>
.text-user {
    display:flex;
    justify-content: space-around;
}
</style>