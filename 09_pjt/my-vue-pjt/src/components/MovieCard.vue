<template>
  <div>
    <div class="card custom-card" style="width: 20rem; height: 40rem;">
      <div class="card-body">
        <img :src="`https://www.themoviedb.org/t/p/original${movie.poster_path}`" class="card-img-top" alt="#">
        <br>
        <br>
        <h4 class="card-title">{{ movie.title }}</h4>
        <p class="card-text">{{ movie.overview }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  computed: {
    movies() {
      return this.$store.state.movies
    },
  },
  props: {
    movie: Object,
  }

}
</script>

<style>
.custom-card {
  overflow: auto;
  white-space: normal;
}
</style>