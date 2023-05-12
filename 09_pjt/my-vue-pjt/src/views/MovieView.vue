<template>
  <div>
    <h1>MOVIE</h1>
    <div class="row">
      <div class="col-lg-4 col-md-5 mb-3 mb-sm-01" v-for="movie in getMovies" :key="movie.id">
        <MovieCard :movie="movie"/>
      </div>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'

export default {
  name: 'MovieView',
  components: {
    MovieCard,
  },
  computed: {
    getMovies() {
      return this.$store.state.movies
    }
  },
  created() {
    this.$store.dispatch('getMovies')
  }

}
</script>

<style>

</style>