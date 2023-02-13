<template>
  <v-container>
    <v-row align="center" class="mt-10" no-gutters>
      <v-col cols="12" sm="6" offset-sm="3">
        <v-sheet class="pa-2"> <h1>Cadastre-se</h1> </v-sheet>
        <v-form>
            <v-text-field
                v-model="username"
                label="Nome de usuário"
                type="text"
                prepend-inner-icon="mdi-account"
                variant="outlined"
                required
            />

            <v-text-field
                v-model="email"
                type="email"
                label="E-mail"
                prepend-inner-icon="mdi-email-fast-outline"
                variant="outlined"
                required
            />

            <v-text-field
                v-model="password"
                type="password"
                label="Senha"
                prepend-inner-icon="mdi-key-outline"
                variant="outlined"
                required
            />

            <v-btn
                :disabled="canRegister()"
                block
                size="large"
                rounded="pill"
                color="#C62828"
                append-icon="mdi-chevron-right"
                :to="{ name: 'accounts-login' }"
                @click="register"
                >
                    Cadastre-se
            </v-btn>
            <v-btn
                class="my-2"
                block
                size="large"
                rounded="pill"
                color="#C62828"
                variant="outlined"
                :to="{ name: 'base-home' }">
                Início
            </v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

import AccountsApi from "@/api/accounts.api.js"

export default {
  name: "RegisterView",
  data: () => {
    return {
      email: null,
      username: null,
      password: null,
      userForm: {}
    }
  },
  methods: {
    async register(){
        this.userForm = {
            "email": this.email,
            "username": this.username,
            "password": this.password
        }
        await AccountsApi.register(this.userForm)
    },
    canRegister(){
        if(!!this.email && !!this.username && !!this.password){
            return false
        }
        return true
    },
  },
}
</script>
