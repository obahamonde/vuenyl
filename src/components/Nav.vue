<template>
  <button
    tr
    mx-6 my-4
    class="icon-btn mx-2 !outline-none"
    title="Dark"
    @click="toggleDark()" z-50
  >
    <div i="carbon-sun dark:carbon-moon" />
  </button>
  <nav text-xl mt-6 col tl m-4 z-50>
    <RouterLink class="icon-btn m-2" to="/" title="Home">
        <Ico icon="mdi-home" />
    </RouterLink>
   <RouterLink class="icon-btn m-2" to="/auth" title="About">
      <Ico icon="mdi-account" />
    </RouterLink>
    <RouterLink class="icon-btn m-2" to="/about" title="About">
       <Ico icon="mdi-post" />
    </RouterLink>

    <RouterLink class="icon-btn m-2" to="/shop" title="Shop">
       <Ico icon="mdi-store" />
    </RouterLink>
 
  
  </nav>
</template>
