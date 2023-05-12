<template>
  <div>
    <nav class="navbar bg-body-tertiary">
      <div class="container-fluid">
        <form class="d-flex" role="search" @submit.prevent="createMovie">
          <input class="form-control me-2" v-model.trim="movieTitle" type="text" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success" type="submit">Add</button>
        </form>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'WatchListForm',
  data() {
    return {
      movieTitle: null,
    }
  },
  methods: {
    createMovie() {
      if (this.movieTitle) {
        this.$store.dispatch('createMovie', this.movieTitle)
        console.log('create method')
      } else {
        alert('영화 제목을 입력하세요!')
      }
      this.movieTitle = null
    }
  },
}
</script>

<style>

</style>