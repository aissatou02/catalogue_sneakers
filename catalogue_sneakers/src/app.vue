<template>
  <div class="app dark">
    
    <header class="header">
      <img class="logo" :src="logoUrl" alt="Logo Catalogue Sneakers">
      <nav class="menu">
        <button @click="filterStock('all')" :class="{ active: selectedFilter==='all' }">Tous</button>
        <button @click="filterStock('stock')" :class="{ active: selectedFilter==='stock' }">En stock</button>
        <button @click="filterStock('rupture')" :class="{ active: selectedFilter==='rupture' }">En rupture</button>
        <button @click="filterStock('commande')" :class="{ active: selectedFilter==='commande' }">Commandé</button>
        <button @click="openAddForm">Ajouter</button>
        <button @click="enableDelete = !enableDelete" :class="{ active: enableDelete }">Supprimer</button>
      </nav>
    </header>

    <h1>Catalogue Sneakers</h1>

   
    <select v-model="selectedCategory">
      <option value="all">Toutes</option>
      <option>Jordan</option>
      <option>Nocta</option>
      <option>Vomero</option>
      <option>P6000</option>
    </select>

   
    <div class="products">
      <ProductCard
        v-for="p in filteredProducts"
        :key="p.id"
        :product="p"
        @select="selectProduct"
        @delete="deleteProduct"
      />
    </div>

    
    <div v-if="showModal">
      <div class="modal" @click="closeModal">
        <div class="modal-content" @click.stop>
          <h2>{{ selectedProduct.name }}</h2>
          <div class="img-wrapper-modal">
            <img :src="selectedProduct.image" />
          </div>
          <p>{{ selectedProduct.description }}</p>
          <p><strong>Prix :</strong> {{ selectedProduct.price }} €</p>
          <p><strong>Stock :</strong> {{ selectedProduct.stock ? "En stock" : "Rupture" }}</p>
          <button @click="editProduct(selectedProduct)" class="modal-btn">Modifier</button>
          <button @click="closeModal" class="modal-btn close">Fermer</button>
        </div>
      </div>
    </div>

    
    <ProductForm
      v-if="showAddForm"
      :productData="newProduct"
      :editingId="editingId"
      @submit="addProduct"
      @close="closeAddForm"
    />

    <footer class="footer">
      <p>@ Catalogue Sneakers — Projet Vue.js</p>
      <p>Réalisé par Aicha</p>
    </footer>
  </div>
</template>

<script>
import ProductCard from "./components/ProductCard.vue";
import ProductForm from "./components/ProductForm.vue";

export default {
  components: { ProductCard, ProductForm },
  data() {
    return {
      logoUrl: "data:image/webp;base64,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", // logo Pinterest
      selectedCategory: "all",
      selectedFilter: "all",
      showModal: false,
      showAddForm: false,
      selectedProduct: null,
      editingId: null,
      enableDelete: false,
      newProduct: { name: "", price: null, category: "Jordan", image: "", description: "", stock: true, promo: false },
      products: [
        { id: 1, name: "Nike Air Max 95 Big Bubble", brand: "Nike", category: "P6000", price: 130, stock: true, promo: false, image: "https://static.nike.com/a/images/t_web_pw_592_v2/f_auto/69b72c63-d897-436e-b152-804e63195d5e/NIKE+AIR+MAX+95+BIG+BUBBLE.png", description: "Air Max 95 Big Bubble, édition classique." },
        { id: 2, name: "ShoX TL (GS)", brand: "Nike", category: "P6000", price: 140, stock: true, promo: false, image: "https://static.nike.com/a/images/t_web_pw_592_v2/f_auto/02d45724-af8d-48ce-9b85-922ed0571d0a/SHOX+TL+%28GS%29.png", description: "ShoX TL modèle pour enfants." },
        { id: 3, name: "Jordan Spizike Low", brand: "Jordan", category: "Jordan", price: 120, stock: false, promo: true, image: "https://static.nike.com/a/images/t_web_pw_592_v2/f_auto/u_126ab356-44d8-4a06-89b4-fcdcc8df0245,c_scale,fl_relative,w_1.0,h_1.0,fl_layer_apply/bae07de7-7b5e-4d5f-973c-953f1750a591/JORDAN+SPIZIKE+LOW.png", description: "Jordan Spizike Low édition spéciale." },
        { id: 4, name: "Air Jordan 4 Retro OG (GS)", brand: "Jordan", category: "Jordan", price: 150, stock: true, promo: false, image: "https://static.nike.com/a/images/t_web_pw_592_v2/f_auto/u_126ab356-44d8-4a06-89b4-fcdcc8df0245,c_scale,fl_relative,w_1.0,h_1.0,fl_layer_apply/a573e27b-12cc-4478-807d-aa044d675453/AIR+JORDAN+4+RETRO+OG+%28GS%29.png", description: "Air Jordan 4 Retro OG." },
        { id: 5, name: "Air Max TL 2.5", brand: "Nike", category: "P6000", price: 135, stock: true, promo: false, image: "https://static.nike.com/a/images/t_web_pw_592_v2/f_auto/7d121e25-ece3-4339-b1b3-113326530a37/AIR+MAX+TL+2.5.png", description: "Air Max TL version 2.5." },
        { id: 6, name: "Nike Zoom Vomero 5", brand: "Nike", category: "Vomero", price: 120, stock: false, promo: true, image: "https://static.nike.com/a/images/t_web_pw_592_v2/f_auto/67e500fb-53fd-40c5-b587-ea7adda98906/NIKE+ZOOM+VOMERO+5.png", description: "Zoom Vomero 5." },
        { id: 7, name: "Nike Zoom Vomero Roam", brand: "Nike", category: "Vomero", price: 115, stock: true, promo: false, image: "https://static.nike.com/a/images/t_web_pw_592_v2/f_auto/68bc88e4-6e72-44e5-9fd3-76d827a2cc06/NIKE+ZOOM+VOMERO+ROAM.png", description: "Zoom Vomero Roam." },
        { id: 8, name: "WMNS Nike Dunk Low", brand: "Nike", category: "Nocta", price: 125, stock: true, promo: true, image: "https://static.nike.com/a/images/t_web_pw_592_v2/f_auto/f21d1d31-5eb1-40cd-bbb2-3cb67dd3e39b/WMNS+NIKE+DUNK+LOW.png", description: "WMNS Nike Dunk Low." }
      ]
    };
  },
  computed: {
    filteredProducts() {
      let list = this.products;
      if (this.selectedCategory !== "all") list = list.filter(p => p.category === this.selectedCategory);
      if (this.selectedFilter === "stock") list = list.filter(p => p.stock);
      if (this.selectedFilter === "rupture") list = list.filter(p => !p.stock);
      return list;
    }
  },
  methods: {
    selectProduct(p) { this.selectedProduct = p; this.showModal = true; },
    closeModal() { this.showModal = false; },
    openAddForm() { this.showAddForm = true; },
    closeAddForm() { this.showAddForm = false; this.editingId = null; this.newProduct = { name: "", price: null, category: "Jordan", image: "", description: "", stock: true, promo: false }; },
    addProduct(product) {
      const idx = this.products.findIndex(p => p.id === product.id);
      if (idx > -1) this.products[idx] = product;
      else this.products.push(product);
      this.closeAddForm();
    },
    deleteProduct(id) { this.products = this.products.filter(p => p.id !== id); },
    editProduct(product) { this.newProduct = { ...product }; this.editingId = product.id; this.showAddForm = true; this.showModal = false; },
    filterStock(filter) { this.selectedFilter = filter; }
  }
};
</script>

<style src="./style.css"></style>
