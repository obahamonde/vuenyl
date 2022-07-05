<script setup lang="ts">
import { Icon } from '@iconify/vue'
const props = defineProps<{icon:string}>()
</script>
<template>
  <Icon :icon="props.icon" />
</template>