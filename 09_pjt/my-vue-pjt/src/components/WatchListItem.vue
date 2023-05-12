<template>
  <div>
    <li @click="updateMovie" :class="{ 'is-completed' : movie.isCompleted }">{{ movie.title }}</li>
  </div>
</template>

<script>
export default {
  name: 'WatchListItem',
  props: {
    movie: Object,
  },
  methods: {
    updateMovie() {
      this.$store.dispatch('updateMovie', this.movie)
      console.log('update!')
      console.log(this.movie.isCompleted)
    }
  }
}
</script>

<style>
  .is-completed {
    text-decoration: line-through;
  }
</style>