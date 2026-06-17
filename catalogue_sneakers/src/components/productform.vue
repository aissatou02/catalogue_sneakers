<template>
  <div class="modal" @click="$emit('close')">
    <div class="modal-content" @click.stop>
      <h2>{{ editingId ? "Modifier un produit" : "Ajouter un produit" }}</h2>
      <form @submit.prevent="submitForm">
        <input v-model="product.name" placeholder="Nom" required />
        <input v-model.number="product.price" type="number" placeholder="Prix" required />
        <select v-model="product.category">
          <option>Jordan</option>
          <option>Nocta</option>
          <option>Vomero</option>
          <option>P6000</option>
        </select>
        <input v-model="product.image" placeholder="URL image" />
        <textarea v-model="product.description" placeholder="Description"></textarea>
        <label><input type="checkbox" v-model="product.promo" /> Promo</label>
        <label><input type="checkbox" v-model="product.stock" /> En stock</label>
        <button type="submit" class="modal-btn">{{ editingId ? "Modifier" : "Ajouter" }}</button>
      </form>
      <button @click="$emit('close')" class="modal-btn close">Fermer</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProductForm",
  props: { editingId: Number, productData: Object },
  data() { return { product: { ...this.productData } }; },
  methods: {
    submitForm() { this.$emit("submit", { ...this.product, id: this.editingId || Date.now() }); }
  }
};
</script>
