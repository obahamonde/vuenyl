<script setup lang="ts">
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
</script>

<template>
  <div h-screen w-screen >
    <RouterView bg-light dark:bg-info text-info dark:text-light /> 
  </div>
</template>
