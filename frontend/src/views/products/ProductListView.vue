<template>
  <v-container class="fill-height">
    <v-row justify="center" align="center">
      <v-col cols="12">
        <v-card>
          <v-card-title class="headline"> Aplicações web disponíveis: </v-card-title>
        </v-card>
      </v-col>
    <v-divider/>
      <v-col class="mt-6" v-for="product in products" :key="product.id" cols="4">
        <products :product="product" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState } from "pinia"
import { useAppStore } from "@/stores/appStore"
import { useAccountsStore } from "@/stores/accountsStore"
import apis from "@/api/apis.js"
import Products from "@/components/Products.vue"

export default {
  name: "AppsList",
  components: {
    Products,
  },
  setup() {

    const appStore = useAppStore()
    return { appStore }
  },
  data() {
    return {
      loading: false,
      items: [],
      showDialog: false,
      products: [],
    }
  },
  mounted() {
    this.listProducts()
    this.showPopup()
  },
  computed: {
    ...mapState(useAccountsStore, ["loggedUser"]),
  },
  methods: {
    showPopup() {
      this.showDialog = false
      if (!this.loggedUser) {
        this.showDialog = true
      }
      return this.showDialog
    },
    closeDialog() {
      this.showDialog = false
      return this.showDialog
    },
    listProducts() {
      this.loading = true
      apis.listProducts().then((data) => {
        this.products = data.products
        this.loading = false
      })
    }
  },
}
</script>

<style scoped>
.done {
  text-decoration: line-through;
}
</style>
