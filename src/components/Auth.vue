<script setup lang="ts">
import { useUserStore } from "~/store/user";
import { useRoute } from "vue-router";
import { onMounted } from "vue";
import { User } from "~/types";

const user = ref(useUserStore().user);
const route = useRoute();
const token = ref(route.query.token);

onMounted(async () => {
  if (token.value) {
    const response = await fetch("/api/user?token=" + token.value, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    }).then((res) => res.json());
    response.token = token.value;
    user.value = response;
    useUserStore().setUser(response);
  }
});
const logout = async () => {
  const res = await fetch("/logout?token=" + token.value, {
    method: "GET",
  });
  console.log(res);
  user.value = null;
  useUserStore().setUser(null);
  router.push("/");
};

const updateAvatar = async (e:ChangeEvent) => {
  const file = e.target.files[0];
  const formData = new FormData();
  formData.append("avatar", file);
  const res = await fetch("/api/user/avatar?token=" + token.value, {
    method: "POST",
    body:formData,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PATCH, PUT, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'Origin, Content-Type, X-Auth-Token'
    }
  });
  const response = await res.json();
  user.value.avatar = response.avatar;
  useUserStore().setUser(user.value);
};  
</script>

<template>
  <div v-if="user" col center my-8>
    <label for="avatar">
      <img r-f sh-lg m-2 x16 :src="user.avatar" cursor-pointer />
      <input type="file" id="avatar" @change="updateAvatar" hidden />
    </label>
    <h1 m-2 font-sans font-bold>{{ user.name }}</h1>
    <h2 m-2 font-mono>{{ user.email }}</h2>
    <button
      m-2
      btn
      bg-red-700
      b-2
      b-gray
      text-gray
      hover:underline
      hover:bg-red-500
      hover:text-black
      hover:b-black
      @click="logout"
    >
      Logout
    </button>
  </div>
  <div v-else col center>
    <a
      href="https://smartprocloud.auth.us-east-1.amazoncognito.com/login?client_id=6d4rt7sphoaihhcj5on3ghb727&response_type=code&scope=aws.cognito.signin.user.admin+email+openid+phone+profile&redirect_uri=http://localhost/auth"
    >
      <Ico icon="mdi-account-circle" icon-btn x10 m-8 sh-md r-f p-1
    /></a>
    <strong row font-extrabold>Click en el icono <Ico icon="mdi-arrow-up"/></strong>
    <h1 font-extrabold>Inicia sesion en nuestra página de manera segura y rápida</h1>
    <h2 w-72 m-4 font-serif>Serás redirigido al servidor en la nube de nuestro proveedor de privacidad y seguridad informática, velamos por tu seguridad y la de tu bolsillo!</h2>
    <h3 m-4>Trabajamos con los mejores partners tecnológicos para ofrecerte la mejor experiencia digital</h3>
  <div col center> <Ico my-4 icon="logos:aws" text-3xl/> <Ico my-4 icon="logos:google" text-3xl/><Ico my-4 icon="simple-icons:fauna" text-purple-900 text-4xl/></div>
  <span text-purple-900 font-extrabold>FaunaDB</span>
  </div>
</template>
