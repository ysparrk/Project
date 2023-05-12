# PJT_09_230512

### 이번 pjt 를 통해 배운 내용

- 영화 정보를 제공하는 SPA 제작
- AJAX 통신과 JSON 구조에 대한 이해
- Vue CLI, Vue Router 플러그인 활용

---

# 0. 초기 설정

### 1. router/index.js

- router 설정

```jsx
import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/MovieView'
import RandomView from '@/views/RandomView'
import WatchListView from '@/views/WatchListView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/movies',
    name: 'MovieView',
    component: MovieView,
  },
  {
    path: '/random',
    name: 'RandomView',
    component: RandomView,
  },
  {
    path: '/watch-list',
    name: 'WatchListView',
    component: WatchListView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
```

### 2. App.vue

```jsx
<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'MovieView' }">Movie</router-link> |
      <router-link :to="{ name: 'RandomView' }">Random</router-link> |
      <router-link :to="{ name: 'WatchListView' }">WatchList</router-link>
    </nav>
    <router-view/>
  </div>
</template>
```

# A. 최고 평점 영화 출력

### 요구사항

- 네비게이션 바에서 Movie 링크(/movies)를 클릭하면 AJAX 통신을 이용하여 TMDB API로 부터 JSON 데이터를 받아와 영화 목록을 출력한다.

### 0. store/index.js

1. state에 moives 빈 리스트를 정의한다.
2. getMovies가 호출되면, url로 요청을 해서 리스트를 받아온다.
3. res가 있다면, data중 results의 값을 movies에 담는다.
4. mutations의 GET_MOVIES를 호출해 state에 반영한다.

```jsx
import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
const movieTopRatedURL = 'https://api.themoviedb.org/3/movie/top_rated?api_key=5d5ba12807e444883a57039b0e2a1015&language=en-US&page=1'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: [],
  },
  getters: {

  },
  mutations: {
    GET_MOVIES(state, movies) {
      console.log('mutataions')
      state.movies = movies
    },
  },
  actions: {
    getMovies(context) {     
      axios({
        method: 'get',
        url: movieTopRatedURL
      })
      .then((res) => {   
        context.commit('GET_MOVIES', res.data.results)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  modules: {
  }
})
```

### 1. views/MovieView.vue

- 페이지가 생성되면 getMovies 메서드를 실행시킨다.
- state의 moives를 getMovies()로 불러온다.
- v-for문으로 MovieCard의 값들을 보여준다.

```jsx
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
```

### 2. components/MovieCard.vue

- props 받은 데이터를 부트스트랩 card를 이용해 보여준다.

```jsx
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
```

📌 이 문제에서 어려웠던 점

- 함수를 다 적어 놓고, MovieView.vue에서 created로 메서드를 불러오지 않았다.

📌  내가 생각하는 이 문제의 포인트

- API 요청 보내기

---

# B. 최고 평점 영화 중 랜덤 영화 한 개 출력

## 요구사항

- 네비게이션 바에서 Random 링크(/random)를 클릭하면 저장된 최고 평점 영화 목록 중 랜덤으로 한 개를 출력한다.

### 1. views/RandomView.vue

1. filterVoteTop
    - getMovies로 전체 영화 리스트를 가져온다.
    - Math.max를 이용해 이 중에서 가장 높은 vote_average를 찾는다.
    - filter를 이용해 highestVote와 같은 vote_average를 갖는 영화의 제목을 voteTopList에 담는다.
    - random을 이용해 voteTopList 중에서 랜덤으로 인덱스 값을 추출한다.
    - template에서는 이때의 인덱스 값으로 title과 overview를 가져온다.

```jsx
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
```

📌 이 문제에서 어려웠던 점

- Life Cycle의 순서 문제 발생
    - 처음에는 가장 높은 평점이 담긴 리스트를 페이지가 생성될 때 만들어지도록 했다.
    - 하지만, 영화 목록을 불러오는 것 보다 빠르게 리스트가 생성되면서 리스트에는 어느 값도 들어가지 않았다.
        
        ➡️ 따라서 버튼이 누르면, filterVoteTop을 실행하고, 그때 리스트에 담고, 랜덤 인덱스를 추출하도록 바꿨다.
        
- error가 계속 발생
    
    ➡️ `{{ randomTopMovie?.title }}` : ?를 이용해 값이 없을 땐, 출력되지 않도록 했다.
    
- `v-if="randomTopMovie"` 를 사용해 랜덤 인덱스가 추출되지 않았다면, card 를 보여지지 않게 했다.

📌  내가 생각하는 이 문제의 포인트

- random 함수 사용

---

# C. 보고 싶은 영화 등록 및 삭제하기

## 요구사항

- 네비게이션 바에서 WathList 링크(/watch-list)를 클릭하면 보고 싶은 영화 제목을 등록할 수 있는 Form 출력
- 등록된 영화 제목을 클릭하면 취소선이 그어진다.

### 0. store/index.js

1. CREATE
    - createMovie에서 create 실시 후 localStorage에 저장한다.
    - title, isCompleted로 생성한다.
2. UPDATE
    - isCompleted을 반대로 바꾼 후 localStorage에 저장

```jsx
+import Vue from 'vue'
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
    // WATCH LIST
    CREATE_MOVIE(state, movieItem) {
      state.watch_list.push(movieItem)
    },
    UPDATE_MOVIE(state, movieItem) {
      state.watch_list = state.watch_list.map((movie) => {
        console.log(movie)
        console.log(movieItem)
        if (movie === movieItem) { 
          console.log('조건문 들어왔다')
          movie.isCompleted = !movie.isCompleted
        }
        return movie
      })
    },
  },
  actions: {
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
```

### 1. views/WatuchListView.vue

- WatchListForm과 WatchListItem을 import 한다.
- WatchListItem을 for문을 돌리며 화면에 보여주고, watch_list의 내용을 prop으로 보내준다.

```jsx
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
```

### 2. components/WatchListForm.vue

- createMovie 메서드를 불러와 form에 영화 제목을 작성한다.

```jsx
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
```

### 3. components/WatchListItem.vue

- props 받은 내용을 표시.
- updateMovie를 받아 is-completed 스타일을 표시한다.

```jsx
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
```

📌 이 문제에서 어려웠던 점

- create를 하면 생성은 되지만 바로 새로고침 되는 현상이 발생
    
    ➡️ form 태그에서의 @submit.prevent를 사용해 sumbit후 새로고침 되는 걸 막는다.
    

📌  내가 생각하는 이 문제의 포인트

- 세 페이지 간의 연결

---

## 후기

- store의 사용에 대해 익힐 수 있는 기회였던 것 같다. store를 사용하는 것이 데이터를 한 곳에서 관리하며 편하게 사용할 수 있었던 것 같다. 생성되는 데이터들을 emit과 props만을 이용해 작성해야 했다면 힘들었을 것 같다.
- 처음 url을 불러오는게 어렵다고 느껴졌는데, axios를 통해 불러오는 연습을 하니 이제는 뭔가 흐름이 느껴지는 것 같다.
- 최종 프로젝트를 위해서 생각해야 할 부분이 많은 것 같은데 지금까지 진행했던 프로젝트 처럼 명세서를 작성하고 순서대로 하면 되겠지…? 라는 생각이 들었다.