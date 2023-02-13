<template>
  <v-footer :absolute="!fixed" app style="padding:0 !important">
    <div class="bg-red d-flex w-100 align-center px-4">
      <strong class="strong">&copy; {{ new Date().getFullYear() }} - robstore</strong>
    </div>

  </v-footer>
</template>

<script>
  export default {
    props: {
      fixed: {
        type: Boolean,
        default: true,
      },
      user: {
        type: Object,
        default: null,
      },
  }
}
</script>

<style scoped>
a {
  text-decoration:none;
  font-weight: bolder;
  font-size:2rem;
}
</style>