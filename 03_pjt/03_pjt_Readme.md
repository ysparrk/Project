### 이번 pjt 를 통해 배운 내용

- 커뮤니티 웹 서비스 개발을 위한 화면 구성 단계를 배웠다.
- CSS와 Bootstrap 사용 방법을 배웠다.

---

## A. nav_footer.html

- 요구 사항
    1. Navigation Bar
        1. bootstrap navbar 사용
        2. 상단 고정
        3. 로고 삽입 및 하이퍼링크
        4. 로그인 화면 bootstrap modal component 및 form component 사용
    2. Footer
        1. 하단 고정
        2. 수직, 수평 가운데 정렬
- 결과
    1. Navigation Bar
        1. 부트스트랩의 nav_bar를 가져온다.
        2. Login에서 modal을 위한 botton을 설정한다.
        
        ```html
        <div class="sticky-top">
            <nav class="navbar navbar-expand-md navbar-dark bg-dark p-4">
              <!-- container -->
              <div class="container-fluid">
                <a href="./01_nav_footer.html"><img src="./images/logo.png" width="120" height="48"></a>
                <!-- button right -->
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
                  <span class="navbar-toggler-icon"></span>
                </button>
                <!-- list -->
                <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
                  <ul class="navbar-nav">
                    <li class="nav-item">
                      <a class="nav-link active mt-2" aria-current="page" href="./02_home.html">Home</a>
                    </li>
                    <li class="nav-item">
                      <a class="nav-link mt-2" href="./03_community.html">Community</a>
                    </li>
                    <!-- login -->
                    <li class="nav-item">
                      <a class="nav-link" href="#"><button type="button" class="btn nav-link" data-bs-toggle="modal" data-bs-target="#staticBackdrop">Login</button></a>
                    </li>
                  </ul> 
                </div>
        
              </div>
            </nav>
            </div>
        
            <!-- Modal -->
            <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h1 class="modal-title fs-5" id="staticBackdropLabel">Modal title</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <form>
                      <div class="mb-3">
                        <label for="exampleInputEmail1" class="form-label">Email address</label>
                        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                        <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
                      </div>
                      <div class="mb-3">
                        <label for="exampleInputPassword1" class="form-label">Password</label>
                        <input type="password" class="form-control" id="exampleInputPassword1">
                      </div>
                      <div class="mb-3 form-check">
                        <input type="checkbox" class="form-check-input" id="exampleCheck1">
                        <label class="form-check-label" for="exampleCheck1">Check me out</label>
                      </div>
                    </form>
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary">Submit</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        ```
        
    2. footer
        
        ```html
        <footer>
            <div class="fixed-bottom d-flex justify-content-center align-items-center">
            <h5>Web-bootstrap PJT, by Youngseo Park</h5>
            </div>
          </footer>
        ```
        
    - 이 문제에서 어려웠던점
        - nav_bar의 정렬 문제 → margin top을 통해 해결
    - 내가 생각하는 이 문제의 포인트
        - 적절한 bootstrap component 가져오기

---

## B. home.html

- 요구 사항
    1. Header
        1. bootstrap carousel component 사용
        2. 이미지 자동 전환
    2. Section
        1. bootstrap card component 사용
        2. viewport의 크기에 따라 이미지 개수 표시 변경
- 결과
    1. Header
        1. 자동으로 전환되는 carousel 가져오기
        
        ```html
        <header>
        
            <div id="carouselExampleAutoplaying" class="carousel slide" data-bs-ride="carousel">
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img src="./images/header1.jpg" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                  <img src="./images/header2.jpg" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                  <img src="./images/header3.jpg" class="d-block w-100" alt="...">
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
        
          </header>
        ```
        
    2. Section
        1. viewport의 가로 크기가 576px 미만일 경우 한 행에 1개씩 표시
        2. viewport의 가로 크기가 576px 이상일 경우 한 행에 2개 이상 표시
        3. `<div class=”container”> → <section class=”row”>`후 각 article 별로 `col-sm-4`를 이용
        
        ```html
        <h1 class="text-center fw-bold my-5">Boxoffice</h1>
        
          <div class="container">
            <section class="row">
              <!-- 1 -->
              <div class="col-sm-4">
                <article>
                  <div class="card">
                    <img src="./images/movie1.jpg" class="card-img-top" alt="...">
                    <div class="card-body">
                      <h5 class="card-title">Card title</h5>
                      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                    </div>
                  </div>
                </article>
              </div>
              <!-- 2 -->
              <div class="col-sm-4">
                <article>
                  <div class="card">
                    <img src="./images/movie2.jpg" class="card-img-top" alt="...">
                    <div class="card-body">
                      <h5 class="card-title">Card title</h5>
                      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                    </div>
                  </div>
                </article>
              </div>
              <!-- 3 -->
              <div class="col-sm-4">
                <article>
                  <div class="card">
                    <img src="./images/movie3.jpg" class="card-img-top" alt="...">
                    <div class="card-body">
                      <h5 class="card-title">Card title</h5>
                      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                    </div>
                  </div>
                </article>
              </div>
              <!-- 4 -->
              <div class="col-sm-4">
                <article>
                  <div class="card">
                    <img src="./images/movie4.jpg" class="card-img-top" alt="...">
                    <div class="card-body">
                      <h5 class="card-title">Card title</h5>
                      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                    </div>
                  </div>
                </article>
              </div>
              <!-- 5 -->
              <div class="col-sm-4">
                <article>
                  <div class="card">
                    <img src="./images/movie5.jpg" class="card-img-top" alt="...">
                    <div class="card-body">
                      <h5 class="card-title">Card title</h5>
                      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                    </div>
                  </div>
                </article>
              </div>
              <!-- 6 -->
              <div class="col-sm-4">
                <article>
                  <div class="card">
                    <img src="./images/movie6.jpg" class="card-img-top" alt="...">
                    <div class="card-body">
                      <h5 class="card-title">Card title</h5>
                      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                    </div>
                  </div>
                </article>
              </div>      
            </section>
          </div>
        ```
        
    - 이 문제에서 어려웠던점
        - nav_bar에 의해 이미지가 사라지는 현상 발생 → fixed-top이 아닌 sticky-top 사용
    - 내가 생각하는 이 문제의 포인트
        - viewport에 대한 이해가 필요하다.

---

## C. community.html

- 요구 사항
    1. Aside
        1. bootstrap list group component 사용
        2. viewport 설정
    2. Section
        1. viewport에 따라 전혀 다른 요소 표시
        2. 가로 크기가 992px 미만일 경우, HTML article 요소의 집합
        3. 가로 크기가 992px 이상일 경우, bootstrap tables content로 구성
    3. Paignation
        1. bootstrap pagination component 구성
        2. 수평 중앙 정렬
- 결과
    1. Aside
        1. viewport의 가로 크기가 992px 이상일 경우 좌측 1/6만큼의 너비 ⇒ `col-lg-2`
        
        ```html
        <main class="container">
            <div class="row">
              <h1>Community</h1>
              <!-- Aside - 게시판 목록 -->
              <div class="col-lg-2">
                <aside>
                  <ul class="list-group">
                    <li class="list-group-item text-primary"><a href="#">Boxoffice</a></li>
                    <li class="list-group-item text-primary"><a href="#">Movies</a></li>
                    <li class="list-group-item text-primary"><a href="#">Genres</a></li>
                    <li class="list-group-item text-primary"><a href="#">Actors</a></li>
                  </ul>
                </aside>
              </div>
        ```
        
    2. Section-1
        - CSS
            - viewport의 가로 크기가 992px 미만일 경우 > under
            - viewport의 가로 크기가 992px 이상일 경우 > over
            - 경우에 따라 `display : none` 사용한다.
        
        ```css
        /* 03_community.css */
        @media (min-width:992px) {
            .under {
                display: none;
            }
        }
        
        @media (max-width:992px) {
            .over {
                display: none;
            }
        }
        ```
        
        - HTML
        
        ```html
        <section class="col-lg-10">
        
                <!-- under html -->
                <div class="under">
                    <article class="border-top mt-3 py-3">
                      <h1>Best Movie Ever</h1>
                      <h2>Great Movie Title</h2>
                      <h5>user</h5>
                      <h5 class="mt-4">1 minute ago</h5>
                    </article>
                    <article class="border-top py-3">
                      <h1>Movie Test</h1>
                      <h2>Great Movie Title</h2>
                      <h5>user</h5>
                      <h5 class="mt-4">1 minute ago</h5>
                    </article>
                    <article class="border-top py-3">
                      <h1>Movie Test</h1>
                      <h2>Great Movie Title</h2>
                      <h5>user</h5>
                      <h5 class="mt-4">1 minute ago</h5>
                    </article>
                </div>
        ```
        
    3. Section-2
        - HTML
            - HTML main 요소의 영역 기준으로 우측 5/6 만큼의 너비를 가진다 → `col-lg-10` 사용
        
        ```html
        <section class="col-lg-10">		
        <!-- over table -->
            <div class="over">
              <table class="table table-striped">
                <thead class="table-dark">
                  <tr>
                    <th scope="col">영화제목</th>
                    <th scope="col">글 제목</th>
                    <th scope="col">작성자</th>
                    <th scope="col">작성 시간</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td class="fw-bold">Great Movie title</td>
                    <td>Best Movie Ever</td>
                    <td>user</td>
                    <td>1 miniute ago</td>
                  </tr>
                  <tr>
                    <td class="fw-bold">Great Movie title</td>
                    <td>Best Movie Ever</td>
                    <td>user</td>
                    <td>1 miniute ago</td>
                  </tr>
                  <tr>
                    <td class="fw-bold">Great Movie title</td>
                    <td>Best Movie Ever</td>
                    <td>user</td>
                    <td>1 miniute ago</td>
                  </tr>
                  <tr>
                    <td class="fw-bold">Great Movie title</td>
                    <td>Best Movie Ever</td>
                    <td>user</td>
                    <td>1 miniute ago</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </section>
        </div>
        ```
        
    4. Pagination
        1. boot strap pagination 가져오기
        
        ```html
        <!-- pagination -->
            <div class="d-flex justify-content-center">
              <nav aria-label="Page navigation example">
                <ul class="pagination">
                  <li class="page-item"><a class="page-link" href="#">Previous</a></li>
                  <li class="page-item"><a class="page-link" href="#">1</a></li>
                  <li class="page-item"><a class="page-link" href="#">2</a></li>
                  <li class="page-item"><a class="page-link" href="#">3</a></li>
                  <li class="page-item"><a class="page-link" href="#">Next</a></li>
                </ul>
              </nav>
            </div>
          </main>
        ```
        
    - 이 문제에서 어려웠던점
        - 가로의 크기가 커졌을때, table을 list의 옆으로 옮기기 → col 사용!
        - table과 list의 정렬이 맞지 않았을때 → 알고 보니 table에  margin을 주고 있었다.
    - 내가 생각하는 이 문제의 포인트
        - viewport에 대한 이해가 필요하다.

---

## 후기

- 지난주에 web수업을 들으면서 많은 절망을 했어서 오늘 프로젝트에 들어오기 전에 겁을 먹었었다. 하지만 생각보다 부트스트랩을 사용하면서 생각보다 어렵지 않게 해결 할 수 있어 만족스러웠다.
- 수업시간에 잘 이해하지 못했던 viewport에 관해 다시 한번 이해하고, 적용해 볼 수 있어 좋았다.
- 생각보다 웹 페이지 만드는 것이 적응되는 것 같은 느낌이다.