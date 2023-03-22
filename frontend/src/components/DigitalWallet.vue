<template>
  <v-card
    class="mx-auto"
    max-width="800"
  >
    <v-container fluid>
      <v-row>
        <v-col>
          <v-card-title class="text-white text-h4 center">Saldo na carteira</v-card-title>
        <v-card class="text-h5 center">
          <v-container>
              <v-row justify="space-around">
              <v-col
                  cols="12"
                  md="12"
              >
                <h1 style="color:green;" class='center'>R$ {{ walletInfo?.amount_stored }}</h1>
              </v-col>
              </v-row>
          </v-container>
        </v-card>
        </v-col>
      </v-row>
      <v-row dense>
        <v-col
          v-for="card in cards"
          :key="card.title"
          :cols="card.flex"
        >
          <v-card>
            <v-img
              :src="card.src"
              class="align-end"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              height="200px"
              cover
              @click="dialog = true"
            >
              <v-card-title 
                class="text-white text-h3 pd-12" 
                style="line-height:175px;"
              >
                {{ card.title }}
              </v-card-title>
            </v-img>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    <div class="text-center">
    <v-dialog
      v-model="dialog"
      width="auto"
    >
      <v-card>
        <v-card-title>
          Escolha o método de pagamento
        </v-card-title>
        <v-divider/>
        <v-radio-group
            v-model="paymentMethod"
            column
          >
            <v-radio
              label="Cartão de crédito"
              value="credit_payment"
            ></v-radio>
        </v-radio-group>
        <v-card v-if=paymentMethod>
            <v-card-text class="text-h6">
                Qual será o valor depositado ?
            </v-card-text>
            <v-divider/>
            <v-radio-group
                v-model="amount_to_store"
                column
            >
                <v-radio
                    label="100"
                    value=100
                ></v-radio>
                <v-radio
                    label="200"
                    value=200
                ></v-radio>
                <v-radio
                    label="300"
                    value=300
                ></v-radio>
                <v-radio
                    label="500"
                    value=500
                ></v-radio>
                <v-radio
                    label="Outro valor"
                    value="other_value"
                ></v-radio>
            </v-radio-group>
        </v-card>
        <v-divider/>
        <v-card v-if="amount_to_store === 'other_value'">
            <v-text-field
                v-model="value"
                label="Valor que deseja depositar"
                placeholder="0,00"
                prefix="R$"
            />
        </v-card>
        <v-divider/>
        <v-card v-if="amount_to_store && amount_to_store != 'other_value' || value">
            <v-text-field
                v-model="credit_number"
                label="Digite o número do cartão"
                placeholder="Número"
            />
        </v-card>
        <v-card-actions>
          <v-btn 
            color="primary" 
            :disabled="!credit_number"
            @click="depositWalletMoney(amount_to_store)"
          >
            Depositar
        </v-btn>
          <v-btn color="primary" @click="dialog = false">Fechar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
  </v-card>
</template>

<script>

import AccountsApi from "~api"

  export default {
    data: () => ({
      walletInfo: {},
      dialog: false,
      paymentMethod: '',
      amount_to_store: null,
      credit_number: null,
      user_id: null,
      value: null,
      cards: [
        { title: 'Adicionar dinheiro na carteira', src: 'https://img.freepik.com/fotos-premium/muitas-centenas-e-cinquenta-reais-notas-de-dinheiro-brasileiro-salario-de-pagamento-do-grande-premio-em-fundo-branco-isolado_72932-3494.jpg', flex: 12 
        },
      ],
    }),
    async mounted(){
        await this.getLoggedUser()
        await this.getWalletAmount()
    },
    methods: {
        async depositWalletMoney (amount) {
            if (amount === 'other_value'){
                amount = this.value
            }
            await AccountsApi.depositWalletMoney(this.user_id, parseFloat(amount))
            await this.getWalletAmount()
            this.resetForm()
        },
        async getLoggedUser () {
            await AccountsApi.whoami().then((response) =>{
                this.user_id = response.user.id
            })
        },
        async getWalletAmount () {
            this.walletInfo = await AccountsApi.getWalletInfo(this.user_id)
        },
        resetForm () {
            this.paymentMethod = ''
            this.value = null
            this.credit_number = null
            this.amount_to_store = null
            this.dialog = false
        }
    }
  }
</script>

<style scoped>
.center{
    display: flex;
    justify-content: space-around;
}
</style>