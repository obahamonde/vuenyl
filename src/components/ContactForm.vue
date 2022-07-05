<template>
  <div col center>
    <label for="name">Name</label>
    <input
      type="text"
      id="name"
      required
      v-model="contact.name"
      class="bg- gray rounded"
    />
    <label for="email">Email</label>
    <input
      type="text"
      id="email"
      required
      v-model="contact.email"
      class="bg-gray-500 rounded"
    />
    <label for="message">Message</label>
    <textarea
      id="message"
      required
      v-model="contact.message"
      class="bg-gray-500 rounded"
    />
    <input
      type="submit"
      value="Send"
      @click="send"
      class="btn bg-teal-500 m-4 dark:invert"
    />
  </div>
  <p>{{event}}</p>
</template>
<script setup lang="ts">
import { Contact } from "~/types";
const contact = ref({
  name: "",
  email: "",
  message: "",
});
const event = ref("");
const URL =
  "https://e7lktfqdb4omimdggegvebs7iu0oanuy.lambda-url.us-east-1.on.aws/";

const send = async () => {
  const hello = await fetch(URL,{
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: contact.value,
  });
  event.value = JSON.stringify(await hello['body'])
};
</script>