<template>
  <v-container class="fill-height">
    <v-responsive class="d-flex align-center text-center fill-height">
      <blockquote class="blockquote text-h4">
        <v-img contain height="310" src="@/assets/logo.png" />
        Bem Vindo a robstore, sua loja de aplicações web!
        <footer >
          <small>
            <em>Nossa missão é te entregar aplicações de alto nível </em>
          </small>
        </footer>
      </blockquote>

      <div class="py-6" />

      <v-row class="d-flex align-center justify-center">
        <v-col cols="auto">
          <v-btn
            color="#C62828"
            rel="noopener noreferrer"
            v-if="!loggedUser"
            size="x-large"
            variant="flat"
            class="my-4 ms-2"
            :to="{ name: 'accounts-register' }">
            <v-icon icon="mdi-account-arrow-right-outline" size="large" start />
            Cadastre-se
          </v-btn>
          <v-btn
            v-if="!loggedUser"
            color="#C62828"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            :to="{ name: 'accounts-login' }"
            class="my-4 ms-2">
            <v-icon icon="mdi-account-arrow-right-outline" size="large"/>
            Login
          </v-btn>
          <v-btn
            v-else
            color="#C62828"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            class="my-4 ms-2"
            :to="{ name: 'accounts-logout' }">
            <v-icon icon="mdi-account-arrow-right-outline" size="large"/>
            Logout
          </v-btn>
          <v-btn
            color="#C62828"
            :to="{ name: 'products-list' }"
            size="x-large"
            variant="flat"
            class="ms-2">
            Ver aplicações disponíveis
          </v-btn>
        </v-col>
      </v-row>
    </v-responsive>
  </v-container>
</template>

<script>
import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"

export default {
  computed: {
    ...mapState(useAccountsStore, ["loggedUser"]),
  },
}
</script>
