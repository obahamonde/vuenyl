<script setup lang="ts">
import { useUserStore } from '~/store/user';

const avatar = ref(useUserStore().user.avatar);

</script>
<template>
<div fixed br><img :src="avatar" r-f x8 m-2 cursor-pointer  /></div>
</template>