<script setup lang="ts">
import { vueStore } from '~/store/shop'
import { useUserStore } from '~/store/user'
const { cart,
        items,
        total,
        user,
        addItem,
        removeItem,
        clearCart } = vueStore()



const vinyls = ref([])

onMounted(
    async()=>{
        const res = await fetch("/api/vinyls")
        const data = await res.json()
        vinyls.value = data
        data.map(vinyl=>{
            vinyl.image.startsWith("//") ? vinyl.image = "https:" + vinyl.image : vinyl.image = vinyl.image
        })
    }
)


function addToCart(vinyl){
    vinyl.quantity = vinyl.quantity ? vinyl.quantity++ : 1
    addItem(vinyl)
}

function removeFromCart(vinyl){
    vinyl.quantity = vinyl.quantity ? vinyl.quantity-- : 0
    removeItem(vinyl)
}




</script>

<template>
    <div col center>
        <div
            bg-gray-200 dark:bg-gray-500 sh-lg  w-full  col center shadow-black dark:shadow-white 
            grid cols-2 gap-0 row-gap-0 rows-auto  
         v-for="vinyl in vinyls" :key="vinyl.id">
            <img :src="vinyl.img" border-black b-2 self-center margin-auto />
            <div w-full col center bg-gray-500 text-white rounded-lg p-1 m-1>
            <h2
              text-xs text-teal bg-black w-20 m-auto rounded-lg
            >{{ vinyl.title }}</h2>
            <h3 text-sm font-mono>{{ vinyl.category }}</h3>
            <h4 text-xs font-thin font-serif>{{ vinyl.price }}</h4>  
            <Ico icon="mdi-cart"
                @click="addToCart(vinyl)"
             size="1.5em" text-xl text-teal cursor-pointer />         
        </div>
        </div>
    </div>
</template>