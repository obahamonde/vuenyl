<script setup lang="ts">

import { useUserStore } from '~/store/user';

useHead({
  title: "Vuenyl",
  meta: [
    { name: "description", content: "Vinyl Records E-Store" },
    {
      name: "theme-color",
      content: computed(() => (isDark.value ? "#00aba9" : "#ffffff")),
    },
  ],
  link: [
    {
      rel: "icon",
      href: "/favicon.ico",
    },
  ],
});

const user = ref(useUserStore().user);
</script>

<template>
  <div col center>
    <RouterView /> 
      <ChatBox/>
  </div>
<Cart />
</template>
