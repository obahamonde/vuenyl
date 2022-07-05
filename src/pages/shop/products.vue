<template>
<pre>

{{}}

</pre>
</template>

<script setup lang="ts">
import { initializeApp } from 'firebase/app';
import { getFirestore } from 'firebase/firestore';
import { useUserStore } from '~/store/user';

const user = ref(useUserStore().user);

</script>