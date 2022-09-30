<template>
  <nav class="navbar">
    <RouterLink  to="/" title="Home">
      <Ico icon="mdi-home" />
    </RouterLink>
    <RouterLink  to="/auth" title="Login">
      <Ico icon="mdi-account" />
    </RouterLink>
    <RouterLink  to="/about" title="About">
      <Ico icon="mdi-post" />
    </RouterLink>
    <RouterLink  to="/shop" title="Shop">
      <Ico icon="mdi-store" />
    </RouterLink>
     <RouterLink to="/contact" title="Contact">
      <Ico icon="mdi-email" />
    </RouterLink>
    <Dark />
  </nav>
</template>
<style scoped>
  .navbar {
    @apply col center bg-primary dark:bg-secondary fixed tr w-auto px-1 py-4 rounded shadow z-50 text-2xl gap-4 text-light;
  }
</style>

