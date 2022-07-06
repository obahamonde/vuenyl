<template>
<pre>

{{products}}

</pre>
</template>

<script setup lang="ts">
import { initializeApp } from 'firebase/app';
import { getFirestore } from 'firebase/firestore';
import { useUserStore } from '~/store/user';
import { Product } from '~/types';
import { Ref } from 'vue';

const user:Ref<User|null> = ref(useUserStore().user);

const products:Ref<Product[]> = ref([]);

</script>   