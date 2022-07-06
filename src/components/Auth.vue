<script setup lang="ts">
import { initializeApp } from "firebase/app";
import {
  getAuth,
  signInWithPopup,
  signOut,
  GoogleAuthProvider,
} from "firebase/auth";
import { useUserStore } from "~/store/user";
const route = useRoute()
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
const token = ref(route.query.token);
const getUser = async () => {
const u = await fetch("/api/public/auth/",{
    method: "POST",
    headers: {
      Authorization: `Bearer ${token.value}`,
    },
  }).then((res) => res.json());
  store.setUser(u);
  user.value = u;
};

onMounted(
  ()=>{
    if(token.value){
      getUser();
    }
  }
)

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
const updateAvatar = async(e:ChangeEvent)=>{
  const file = e.target.files[0];
  const formData = new FormData();
  formData.append("file",file);
  const res = await fetch("/api/user/avatar",{
    method: "POST",
    headers: {
      Authorization: `Bearer ${token.value}`,
    },
    body: formData,
  });
  const u = await res.json();
  store.setUser(u);
  user.value = u;
}


</script>

<template>
<div>

</div>
  <div>
    <div v-if="user" col center my-8>
    <label for="avatar">
      <img r-f sh-lg m-2 :src="user.avatar"
            cursor-pointer
      
       />
       <input type="file" id="avatar" @change="updateAvatar" hidden />
       </label>
      <h1 m-2 font-sans font-bold>{{ user.name }}</h1>
      <h2 m-2 font-mono>{{ user.email }}</h2>
      <button m-2 btn bg-red-900 b-2 b-gray text-gray hover:underline hover:bg-red-500 hover:text-black hover:b-black @click="logout">Logout</button>
    </div>
    <div v-else col center>
      <a href = "https://smartprocloud.auth.us-east-1.amazoncognito.com/login?client_id=6d4rt7sphoaihhcj5on3ghb727&response_type=code&scope=aws.cognito.signin.user.admin+email+openid+phone+profile&redirect_uri=http://localhost/public/auth">
      <Ico
        icon="mdi-account-circle"
        icon-btn
        x10
        m-8
        sh-md
        r-f
        p-1
        title="Login with Google"
      /></a>
    </div>
  </div>
</template>
