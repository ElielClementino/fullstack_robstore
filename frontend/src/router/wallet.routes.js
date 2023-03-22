// Composables
import DefaultLayout from "@/layouts/default/DefaultLayout.vue"
import DigitalWalletView from "@/views/wallet/DigitalWalletView.vue"

export default [
  {
    path: "/wallet",
    component: DefaultLayout,
    children: [
      {
        path: "/digital-wallet",
        name: "digital-wallet",
        component: DigitalWalletView,
      }
    ],
  },
]
