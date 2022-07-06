

<style scoped>
.submit {
 @apply bg-blue-500 hover:bg-lime-300 hover:text-blue-900 hover:border-2 hover:border-blue-900 hover:shadow-lg @apply animate_animated hover:shadow-gray-500 text-white font-bold py-2 px-4 rounded cursor-pointer;
}
</style>
<template>
  <form @submit.prevent="onSubmit" col center>
    <div>
      <div col m-4>
        <label for="from" mx-4 p="x4 y2" text="center" font-mono >Email</label>
        <input
          type="email"
          id="from"
          v-model="from"
          placeholder="Tu correo, por ejemplo: john.doe@example.com"
          input
          p="x4 y2"
          text="center"
          bg="transparent"
          border="~ rounded gray-900 dark:gray-700"
          outline="none active:none"
        />
        <label for="name" mx-4 mt-4 p="x4 y2" text="center" font-mono >Name</label>
        <input
          type="text"
          id="name"
          v-model="name"
          placeholder="Tu nombre, por ejemplo: John Doe"
          input
          p="x4 y2"
          text="center"
          bg="transparent"
          border="~ rounded gray-900 dark:gray-700"
          outline="none active:none"
          
        />
      </div>  
      <div col center>
        <label for="message" p="x4 y2" text="center" mx-8 mt-4 font-mono>Message</label>
        <div col m-4 mt-0 w-full center>
          <textarea
            id="message"
            v-model="message"
            rows="8"
            cols=" 60"
            placeholder="Tu mensaje, por ejemplo: Hola, estoy interesado en tu producto"
            input
            p="x4 y2"
            text="center"
            bg="transparent"
            b-2 border="~ rounded gray-900 dark:gray-700"
            outline="none active:none"
          ></textarea>
        </div>
      </div>
    </div>
    <input type="submit" value="Send" class="submit" gray-900 dark:gray-700 />
  </form>
  <Toast bg="lime-300" toast="Email sent successfully!" timeout="10" v-if="toast" />
  </template>
  <script setup lang="ts">
import { Ref } from 'vue'

const from = ref("");
const name = ref("");
const message = ref("");
const toast = ref(false);

const onSubmit = async () => {
  const res = await fetch('/api/', {
    method: "POST",
    body: {
      name: name.value,
      email: from.value,
      message: message.value,
    }
  });
    toast.value = true;
};
</script>