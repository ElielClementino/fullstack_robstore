<template>
  <v-container class="fill-height">
      <blockquote class="blockquote text-h4">
        <em> Cadastre novos produtos </em>
      </blockquote>
      <new-product-form/>
  </v-container>
</template>

<script>

import Products from "@/components/Products.vue"
import NewProductForm from "@/components/NewProductForm.vue"

export default {
  name: "ProductCreation",
  components: {
    Products,
    NewProductForm
  },
  data() {
    return {
      loading: false,
    }
  },
  methods: {

  },
}
</script>

<style scoped>

</style>
