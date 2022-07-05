<script setup lang="ts">

import { useUserStore } from '~/store/user';

useHead({
  title: "FireBook",
  meta: [
    { name: "description", content: "🔥 Likefacebook but ON FIRE 🔥" },
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
    <Avatar />
  </div>
</template>
