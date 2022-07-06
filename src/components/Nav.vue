<template>
  <button
    tr
    mr-6
    mt-3
    class="icon-btn mx-2 !outline-none"
    title="Dark"
    @click="toggleDark()"
    z-50
  >
    <div i="carbon-sun dark:carbon-moon" />
  </button>
  <nav text-xl pt-1 text-black dark:text-white row bg-teal dark:bg-teal-800 h-12 shadow-lg w-full tl margin-auto z-40>
    <RouterLink class="icon-btn m-2" to="/" title="Home">
      <Ico icon="mdi-home" />
    </RouterLink>
    <RouterLink class="icon-btn m-2" to="/auth" title="Login">
      <Ico icon="mdi-account" />
    </RouterLink>
    <RouterLink class="icon-btn m-2" to="/about" title="About">
      <Ico icon="mdi-post" />
    </RouterLink>
    <RouterLink class="icon-btn m-2" to="/shop" title="Shop">
      <Ico icon="mdi-store" />
    </RouterLink>
     <RouterLink class="icon-btn m-2" to="/contact" title="Contact">
      <Ico icon="mdi-email" />
    </RouterLink>
  <span font-script text-3xl ml-8>Vuenyl</span>
  </nav>
</template>

