<script setup lang="ts">
import { initializeApp } from "firebase/app";
import {
  getAuth,
  signInWithPopup,
  signOut,
  GoogleAuthProvider,
} from "firebase/auth";
import { useUserStore } from "~/store/user";

const auth = getAuth(
  initializeApp({
    apiKey: "AIzaSyC-EWWaIHK_yLZMM9EAMhzSH7cyYc6exls",
    authDomain: "intaas-880b3.firebaseapp.com",
    databaseURL: "https://intaas-880b3-default-rtdb.firebaseio.com",
    projectId: "intaas-880b3",
    storageBucket: "intaas-880b3.appspot.com",
    messagingSenderId: "244469163250",
    appId: "1:244469163250:web:2fd9dc63e68510a6e4dc6b",
    measurementId: "G-DCT8N5SDFE",
  })
);
const store = useUserStore();
const user = ref(store.getUser());
const login = async () => {
  const result = await signInWithPopup(auth, new GoogleAuthProvider());
  user.value = {
    uid: result.user.uid,
    email: result.user.email,
    name: result.user.displayName,
    avatar: result.user.photoURL,
  };
  store.setUser(user.value);
};
const logout = () => {
  signOut(auth);
  user.value = null;
  store.setUser(null);
};
</script>

<template>
  <div>
    <div v-if="user" col center my-8>
      <img r-f sh-lg m-2 :src="user.avatar" />
      <h1 m-2 font-sans font-bold>{{ user.name }}</h1>
      <h2 m-2 font-mono>{{ user.email }}</h2>
      <button m-2 btn bg-red-900 b-2 b-gray text-gray hover:underline hover:bg-red-500 hover:text-black hover:b-black @click="logout">Logout</button>
    </div>
    <div v-else col center>
    <h1 text-lg font-sans font-bold mt-8  text-red-700>Login with Google</h1>
      <Ico
        icon="logos:google-icon"
        @click="login"
        icon-btn
        x10
        m-8
        sh-md
        r-f
        p-1
        title="Login with Google"
      />
    </div>
  </div>
</template>
