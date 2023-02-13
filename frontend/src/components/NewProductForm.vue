<template>
  <v-form @submit.prevent>
    <v-container>
      <v-row>
        <v-col
          cols="4"
          md="4"
        >
          <v-text-field
            v-model="name"
            label="Nome do produto"
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="4"
          md="4"
        >
          <v-text-field
            v-model="imageUrl"
            label="Url da imagem"
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="2"
          md="4"
        >
          <v-text-field
            v-model="description"
            label="Descrição do produto"
            required
          ></v-text-field>
        </v-col>
        <v-col
          cols="2"
          md="4"
        >
          <v-text-field
            v-model="quantity"
            label="Quantidade disponível"
            required
          ></v-text-field>
        </v-col>
        <v-col
          cols="2"
          md="4"
        >
          <v-text-field
            v-model="price"
            label="Preço do produto"
            required
          ></v-text-field>
        </v-col>
      </v-row>
    <v-btn type="submit" @click="addNewProduct()" >Adicionar Produto</v-btn>
    </v-container>
  </v-form>
</template>


<script>
import apis from "@/api/apis.js"
  export default {
    name: "NewProductForm",
    data: () => ({
      name: null,
      imageUrl: null,
      description: null,
      quantity: 0,
      price: 0,
      produto: {}
    }),
    methods: {
        addNewProduct(){
            this.produto = {
                    "name": this.name,
                    "image_url": this.imageUrl,
                    "description": this.description,
                    "quantity": this.quantity,
                    "price": this.price,
            }
            console.log(this.produto)
            apis.addNewProduct(this.produto)
        }
    }
  }
</script>