<template> <div text-4xl col center>
      <img :src="logo" x16  dark:invert duration-100 hover:animate-pulse cursor-pointer />
    </div></template>
<script setup lang="ts">
const props = defineProps<{
  logo: string;
}>();
</script>