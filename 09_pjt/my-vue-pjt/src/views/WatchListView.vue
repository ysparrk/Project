<template>
  <div>
    <h1>WatchList</h1>
    <WatchListForm />
    <WatchListItem v-for="(movie, index) in WatchList" :key="index" :movie=movie />
  </div>
</template>

<script>
import WatchListForm from '@/components/WatchListForm'
import WatchListItem from '@/components/WatchListItem'

export default {
  name: 'WatchListView',
  components: {
    WatchListForm,
    WatchListItem,
  },
  computed: {
    WatchList() {
      return this.$store.state.watch_list
    }
  },
}
</script>

<style>

</style>