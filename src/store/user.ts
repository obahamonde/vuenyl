import { acceptHMRUpdate, defineStore } from "pinia";
import { User } from "~/types";
import { Ref } from "vue";

export const useUserStore = defineStore("user", () => {
  const user: Ref<User | null> = ref(
    null
  );

  function setUser(u: User | null) {
    user.value = u;
  }
  function getUser(): User | null {
    return user.value;
  }

  return {
    user,
    setUser,
    getUser
     
  };
});

if (import.meta.hot)
  import.meta.hot.accept(acceptHMRUpdate(useUserStore, import.meta.hot));
