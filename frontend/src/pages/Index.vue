<template>
  <q-page class="q-pa-md">
    <q-list>
      <q-item tag="label" v-for="product in products" :key="product.title">
        <q-item-section avatar>
          <q-btn dense round color="red" glossy text-color="black" icon="delete" />
        </q-item-section>
        <q-item-section>
          <q-item-label>{{ product.title }}</q-item-label>
        </q-item-section>
        <q-item-section avatar>
          <q-btn dense round color="green" icon="shopping_cart" />
        </q-item-section>
      </q-item>
      <q-item tag="label">
        <q-item-section>
          <q-input dense outlined v-model="newProductInput" label="Product name" />
        </q-item-section>
        <q-item-section avatar>
          <q-btn label="+" @click="addProduct" />
        </q-item-section>
      </q-item>
    </q-list>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'PageIndex',
  data () {
    return {
      products: [],
      realized: [],

      newProductInput: ''
    }
  },
  methods: {
    async loadData () {
      const response = await this.$axios.get('http://127.0.0.1:8854/api/carts/cart')
      this.products = response.data.products
      console.log(response)
    },
    async addProduct () {
      this.products.push({ title: this.newProductInput })
      this.newProductInput = ''
    },
    async removeProduct () {

    },
    async putProduct () {

    }
  },
  async mounted () {
    await this.loadData()
  }
})
</script>
