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

  export default {
    setup() {
      const productStore = useProductStore()
      return { productStore }
    },
    data: () => ({
      filteredProducts: [],
      totalValue: 0,
      items: [],
    }),
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
        await apis.buyProducts(this.products)
        this.productStore.clearProductQuantity()
        this.$router.push({name: "thanks-for-buying"})
      }
    },
    computed: {
      ...mapState(useProductStore, ["products"])
    },
    mounted () {
      this.filterProducts()
    }
  }
</script>