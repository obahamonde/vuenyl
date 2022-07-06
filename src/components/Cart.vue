<template>
<div z-50 text-4xl text-black bl m-4 r-f b-2 p-1>

<div bl bg-slate h-64 w-full rounded-xl :class="{'hidden': toggle}">
<ul col center overflow-y-scroll h-full w-full> 
<li text-xs row m-4 v-for="item in items">{{item.title}} <strong>{{item.price}}</strong> <i>{{item.quantity}}</i><Ico x4 icon="mdi-delete"
@click="removeFromCart(item)" /></li>

</ul>

</div>
<Ico icon="mdi-cart" bl m-4 r-f 
@click="toggle = !toggle"
dark:invert
/>
</div>
</template>
<script setup lang="ts">
import { vueStore } from '~/store/shop'
const items = vueStore().items
const toggle = ref(true)
const removeFromCart = (item)=>{
    items.remove(item)
}
</script>