<template>
<v-container>
  <v-card
    class="mx-auto"
  >
    <v-toolbar color="#212121">
      <v-toolbar-title>Aplicações adicionadas:</v-toolbar-title>
    </v-toolbar>

    <v-list
      :items="items"
      item-props
      lines="three"
    >
    </v-list>
    <v-toolbar color="#C62828">
    <v-toolbar-title >Total: R$ {{ totalValue }}</v-toolbar-title>
    <v-btn
    size="large"
    rounded="pill"
    dense
    append-icon="mdi-chevron-right"
    :disabled="totalValue <= 0"
    @click="buyProducts()"
    >
      FINALIZAR COMPRA
    </v-btn>
    </v-toolbar>
  </v-card>
</v-container>
</template>

<script>
import apis from "@/api/apis.js"
import { mapState } from "pinia"
import { useProductStore } from "@/stores/productsStore"
import { useAppStore } from "@/stores/appStore"
import AccountsApi from "@/api/accounts.api.js"

  export default {
    setup() {
      const productStore = useProductStore()
      const appStore = useAppStore()
      return { productStore, appStore }
    },
    data: () => ({
      filteredProducts: [],
      totalValue: 0,
      items: [],
      user_id: null,
      walletInfo: {}
    }),
    async mounted (){
      await this.getLoggedUser()
      await this.filterProducts()
      await this.getWalletAmount()
    },
    computed: {
      ...mapState(useProductStore, ["products"])
    },
    methods: {
      async filterProducts () {
        if (!this.products) return

        this.filteredProducts = await apis.filterProducts(this.products)
        for (let idx=0; idx < this.products.length; idx++){
          this.totalValue += this.products[idx][0].price
        }
        this.filteredProducts.products.map((item, idx) =>
          this.items.push(
                {
                  prependAvatar:item["image_url"],
                  title: item["name"],
                  subtitle: `Você adicionou ${this.products[idx][0].quantity} unidades, custando ${item["price"]} cada.`,
                },
                { type: 'divider', inset: true },
              )
        )
      },
      async buyProducts () {
        if (this.walletInfo?.amount_stored < this.totalValue) {
          this.appStore.showSnackbar("Saldo insuficiente", "danger")
          return
        }
        await AccountsApi.withdrawWalletMoney(this.user_id, this.totalValue)
        await apis.buyProducts(this.products)
        this.productStore.clearProductQuantity()
        this.$router.push({name: "thanks-for-buying"})
      },
      async getLoggedUser () {
          await AccountsApi.whoami().then((response) =>{
              this.user_id = response.user.id
          })
      },
      async getWalletAmount () {
            this.walletInfo = await AccountsApi.getWalletInfo(this.user_id)
        }
    }
  }
</script>