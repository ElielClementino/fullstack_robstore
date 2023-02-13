// Composables
import DefaultLayout from "@/layouts/default/DefaultLayout.vue"
import ProductListView from "@/views/products/ProductListView.vue"
import ProductCreationView from "@/views/products/ProductCreationView.vue"
import CartListView from "@/views/products/CartListView.vue"
import ThanksView from "@/views/base/ThanksView.vue"

export default [
  {
    path: "/products",
    component: DefaultLayout,
    children: [
      {
        path: "list",
        name: "products-list",
        component: ProductListView,
      },
      {
        path: "add/new-product",
        name: "new-product",
        component: ProductCreationView,
      },
      {
        path: "",
        name: "cart-products",
        component: CartListView,
      },
      {
        path: "",
        name: "thanks-for-buying",
        component: ThanksView,
      },
    ],
  },
]
