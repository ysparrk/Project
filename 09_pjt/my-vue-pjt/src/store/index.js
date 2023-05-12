import Vue from 'vue'
import Vuex from 'vuex'


import axios from 'axios'
const movieTopRatedURL = 'https://api.themoviedb.org/3/movie/top_rated?api_key=5d5ba12807e444883a57039b0e2a1015&language=en-US&page=1'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: [],
    watch_list: [],
  },
  getters: {

  },
  mutations: {
    GET_MOVIES(state, movies) {
      console.log('mutataions')
      state.movies = movies
    },
    // WATCH LIST
    CREATE_MOVIE(state, movieItem) {
      state.watch_list.push(movieItem)
    },
    UPDATE_MOVIE(state, movieItem) {
      // 모든 배열을 돌면서 바꿔주어야 한다
      // 함수 -> state.todos 배열에서 클릭한 todo item을 찾고, 해당 todo.isCompleted를 반대로 뒤집는다.(토글!)
      state.watch_list = state.watch_list.map((movie) => {
        console.log(movie)
        console.log(movieItem)
        if (movie === movieItem) { // 내가 클릭한 todo item을 state.todos 배열에서 찾아서
          console.log('조건문 들어왔다')
          movie.isCompleted = !movie.isCompleted // isCompleted 뒤집기
        }
        return movie
      })
    },
  },
  actions: {
    getMovies(context) {
      console.log('store method111')      
      axios({
        method: 'get',
        url: movieTopRatedURL
      })
      .then((res) => {
        console.log('store method222')   
        context.commit('GET_MOVIES', res.data.results)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // WATCH LIST
    createMovie(context, movieTitle) {
      const movieItem = {
        title: movieTitle,
        isCompleted: false
      }
      context.commit('CREATE_MOVIE', movieItem)
      context.dispatch('saveMoviesToLocalStorage')
      console.log('create')
    },
    updateMovie(context, movieItem) {
      console.log(movieItem)
      context.commit('UPDATE_MOVIE', movieItem)
      context.dispatch('saveMoviesToLocalStorage')  // 저장
    },
    // local storage
    saveMoviesToLocalStorage(context) {
      const jsonMovies = JSON.stringify(context.state.watch_list)
      localStorage.setItem('watch_list', jsonMovies)
    },
  },
  modules: {
  }
})
