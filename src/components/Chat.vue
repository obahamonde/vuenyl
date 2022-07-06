<template> 
<div sh-lg >
<div col bg-gray-200 w-64 h-72 p-1 br mb-8 rounded-t b-2 border-teal :class="{'hidden': chatOpen ? true : true}">
<div row justify-start v-for="message in messages">
{{message.text}}
</div>
</div>
<div br w-64 h-12 bg-teal-500 dark:invert row p-1>
<div row items-center>
</div>
<div row><input type="text" placeholder="Type a message" 
v-model="message" @keyup.enter="sendMessage"
text-xs w-48 bg-gray-300 rounded my-1 px-1 text-left mx-2 border-none text-black z-50 /></div>
</div>
</div>
</template>
<script setup lang="ts">
const messages = ref([])
const chatOpen = ref(true)
sendMessage = ()=>{
    if(message.value){
        messages.value.push({text:message.value})
        message.value = ""
    }
}


</script>
