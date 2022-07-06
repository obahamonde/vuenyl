import { defineStore } from 'pinia'
import { Cart, Vuenyl } from './types'
import { Ref } from 'vue'

export const vueStore = defineStore('vue', () => {
    const cart = ref([])
    const items = ref([])
    const total = ref(0)
    const user = ref(null)

    const addItem = (item: Vuenyl) => {
        items.value.push(item)
        total.value += item.price
    }

    const removeItem = (item: Vuenyl) => {
        items.value = items.value.filter(i => i.title !== item.title)
        total.value -= item.price
    }

    const clearCart = () => {
        items.value = []
        total.value = 0
    }

    return {
        cart,
        items,
        total,
        user,
        addItem,
        removeItem,
        clearCart
    }
}
)