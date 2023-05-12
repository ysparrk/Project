<template>
  <div>
    <button @click="filterVoteTop" class="btn btn-primary">PICK</button>
    <div class="card custom-card" v-if="randomTopMovie" style="width: 20rem; height: 40rem;">
      <div class="card-body">
        <img :src="`https://www.themoviedb.org/t/p/original${randomTopMovie?.poster_path}`" class="card-img-top" alt="#">
        <br>
        <br>
        <h4 class="card-title">{{ randomTopMovie?.title }}</h4>
        <p class="card-text">{{ randomTopMovie?.overview }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RandomView',
  data() {
    return {
      voteTopList: [],
      randomTopMovie: null,
    }
  },
  created() {
    this.$store.dispatch('getMovies')
  },
  methods: {
    filterVoteTop() {
      console.log('save!')
      const movies = this.$store.state.movies
      console.log(movies)
      const highestVote = Math.max(...movies.map(movie => movie.vote_average))
      this.voteTopList = movies.filter(movie => movie.vote_average === highestVote)
      
      const randomIndex = Math.floor(Math.random() * this.voteTopList.length)
      this.randomTopMovie = this.voteTopList[randomIndex]  // 랜덤 영화 하나 담기
    },
  },
}
</script>

<style>
.custom-card {
  overflow: auto;
  white-space: normal;
}
</style>