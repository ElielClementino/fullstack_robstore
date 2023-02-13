import { defineStore } from "pinia"


export const useProductStore = defineStore("productStore", {
    state: () => ({
      productQuantity: null,
      products: [],
    }),
    actions: {
      setProductQuantity(quantity, product) {
        this.productQuantity += quantity
        this.products.push(product)
      },
      clearProductQuantity() {
        this.productQuantity = null
      }
    },
  })