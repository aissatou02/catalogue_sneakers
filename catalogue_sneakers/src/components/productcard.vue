<template>
  <div
    class="product-card"
    @click="$emit('select', product)"
    :class="{
      expensive: product.price > 100,
      cheap: product.price <= 100,
      out: !product.stock,
      promo: product.promo
    }"
  >
    <button class="delete-btn" @click.stop="$emit('delete', product.id)">×</button>
    <div class="img-wrapper">
      <img :src="product.image" :alt="product.name" />
    </div>
    <h3>{{ product.name }}</h3>
    <p class="brand">{{ product.brand }}</p>
    <p class="price" :style="{ color: product.stock ? '#4caf50' : '#ff5252' }">
      {{ product.price }} €
    </p>
  </div>
</template>

<script>
export default {
  name: "ProductCard",
  props: { product: Object }
};
</script>
