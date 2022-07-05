<template>
<div v-if="user">
<img :src="store.user.avatar" r-f br m-1 cursor-pointer sh-lg z-50 mb-3
    :class="isChatOpen ? 'h-6 w-6' : 'h-12 w-12'"
    @click="toggleChat"

 />
 <div :class="isChatOpen ? '' : 'hidden'">
 <Chat />
 </div>
</div>
</template>
<script setup lang="ts">
import { useUserStore } from '~/store/user';
const store = useUserStore();
const user = ref(store.getUser());
const isChatOpen = ref(false)
const toggleChat = ()=>{
    isChatOpen.value = !isChatOpen.value
}

</script>