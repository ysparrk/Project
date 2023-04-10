# PJT_04_230324

### 이번 pjt 를 통해 배운 내용

- DB를 활용한 웹 페이지 구현
- Django의 전반적인 활용

---

## A. 사전 설정

- 요구 사항
    1. Model 
        1. Movie 모델 클래스를 정의하고 원하는 정보 저장
    2. URL
        1. movies앱은 주어진 URL 요청에 맞는 역할을 가진다.
    3. View
        1. 주어진 역할을 가지는 view 함수
    4. Admin
        1. 모델 Movie를 Admin site에 등록
        2. Admin site에서 데이터의 생성, 조회, 수정, 삭제가 가능해야 한다.
    5. Form
        1. Movie 모델의 데이터 검증, 저장, 에러메시지, HTML을 관리하기 위해 ModelForm을 사용한다.
            1. genre 필드, score 필드, release_date 필드
- 결과
    1. Model
        1. 필드명, 데이터 유형을 설정한다.
        
        ```python
        # movies/models.py
        
        from django.db import models
        
        # Create your models here.
        class Movie(models.Model):
            title = models.CharField(max_length=20)
            audience = models.IntegerField()
            release_date = models.DateField()
            genre = models.CharField(max_length=30)
            score = models.FloatField()
            poster_url = models.CharField(max_length=50)
            description = models.TextField()
            actor_image = models.ImageField(blank=True)
        ```
        
    2. URL
        1. url
        
        ```python
        # articles/urls.py
        
        from django.urls import path
        from . import views
        
        app_name = 'movies'
        urlpatterns = [
            path('', views.index, name='index'),  
            path('create/', views.create, name='create'), 
            path('<int:pk>/', views.detail, name='detail'),
            path('<int:pk>/update/', views.update, name='update'),
            path('<int:pk>/delete/', views.delete, name='delete'),
        ]
        ```
        
    3. View
        1. view
        
        ```python
        # movies/views.py
        
        from django.shortcuts import render, redirect
        from .models import Movie
        from .forms import MovieForm
        from django.views.decorators.http import require_http_methods
        
        # Create your views here.
        @require_http_methods(['GET'])
        def index(request):
            movies = Movie.objects.all()
            context = {'movies' : movies}
            return render(request, 'movies/index.html', context)
        
        @require_http_methods(['GET', 'POST'])
        def create(request):
            if request.method == 'POST':
                form = MovieForm(request.POST, request.FILES)
                if form.is_valid():
                    movies = form.save()
                    return redirect('movies:detail', movies.pk)
            
            else:
                form = MovieForm()
            context = {'form' : form}
            return render(request, 'movies/create.html', context)
        
        @require_http_methods(['GET'])
        def detail(request, pk):
            movies = Movie.objects.get(pk=pk)
            context = {'movies' : movies}
            return render(request, 'movies/detail.html', context)
        
        @require_http_methods(['GET', 'POST'])
        def update(request, pk):
            movies = Movie.objects.get(pk=pk)
        
            if request.method == 'POST':
                form = MovieForm(request.POST, request.FILES, instance=movies)
                if form.is_valid():
                    form.save()
                    return redirect('movies:detail', pk=movies.pk)
            else:
                form = MovieForm(instance=movies)
        
            context = {'form' : form, 'movies' : movies}
            return render(request, 'movies/update.html', context)
        
        @require_http_methods(['POST'])
        def delete(request, pk):
            movies = Movie.objects.get(pk=pk)
            movies.delete()
            return redirect('movies:index')
        ```
        
    4. Admin
        1. admin
        
        ```python
        # movies/admin.py
        
        from django.contrib import admin
        from .models import Movie
        
        # Register your models here.
        admin.site.register(Movie)
        ```
        
    5. Form
        
        ```python
        # movies/forms.py
        
        from django import forms
        from .models import Movie
        
        class MovieForm(forms.ModelForm):
        
            genre = forms.ChoiceField(choices=[('코미디', '코미디'), ('공포', '공포'), ('로맨스','로맨스'), ('가족', '가족'), ('액션', '액션')])
         
        
            score = forms.FloatField(
                widget=forms.NumberInput(
                attrs={
                    'step' : 0.5,
                    'min' : 0,
                    'max' : 5,
                    }
                )
            )
        
            release_date = forms.CharField(
                widget=forms.TextInput(
                    attrs={
                        'type' : 'date'
                    }
                )
            )
        ```
        
    - 이 문제에서 어려웠던점
        - 
    - 내가 생각하는 이 문제의 포인트
        - 

---

## B. base.html

- 요구 사항
    1. 공통 부모 템플릿 만들기 → 모든 템플릿 파일은 base.html을 상속받아 사용한다.
    2. header.jpg 화면 상단에 보여주기
- 결과
    1. 
        
        ```html
        <!--templates/base.html-->
        
        {% load static %}
        
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
            <link rel="stylesheet" href="{% static 'base.css' %}">
            <title>Document</title>
        </head>
        <body>
        
            <div class="container">
                <div class="row">
                    <img src="{% static 'header.jpg' %}" alt="">
                    {% block content %}{% endblock content %}
                </div>
            </div>
        
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
        </body>
        </html>
        ```
        
    - 이 문제에서 어려웠던점
        - nav_bar에 의해 이미지가 사라지는 현상 발생 → fixed-top이 아닌 sticky-top 사용
    - 내가 생각하는 이 문제의 포인트
        - 

---

## C. index.html

- 요구 사항
    1. 전체 영화 목록 조회 페이지
        1. 데이터베이스에 존재하는 모든 영화의 목록 표시
        2. 적절한 HTML 요소를 사용하여 영화 제목 및 평점을 표시하며, 제목을 클릭 시 해당 영화의 상세 조회 페이지(detail.html)로 이동
- 결과
    1. A
        
        ```html
        <!--movies/templates/movies/index.html-->
        
        {% extends 'base.html' %} 
        
        {% block content %}
            <h1>INDEX</h1>
            <a href="{% url 'movies:create' %}" class="mb-3">CREATE</a>
            <hr>
        
            {% for movie in movies %}
        
                <a href="{% url 'movies:detail' movie.pk %}" class="mb-3">{{movie.title}}</a>
                <p>{{movie.score}}</p>
                <hr>
        
            {% endfor %}
        
        {% endblock content %}
        ```
        
    2. 
    - 이 문제에서 어려웠던점
        - 가로의 크기가 커졌을때, table을 list의 옆으로 옮기기 → col 사용!
        - table과 list의 정렬이 맞지 않았을때 → 알고 보니 table에  margin을 주고 있었다.
    - 내가 생각하는 이 문제의 포인트
        - viewport에 대한 이해가 필요하다.

---

## D. detail.html

- 요구 사항
    1. 영화 상세 정보 페이지
        1. 특정 영화의 상세 정보 표시
        2. 해당 영화의 수정 및 삭제 버튼 표시
        3. 전체 영화 목록 조회 페이지(index.html)로 이동하는 링크 표시
- 결과
    1. A
        
        ```html
        <!--movies/templates/movies/detail.html-->
        
        {% extends 'base.html' %} 
        
        {% block content %}
          <h1>DETAIL</h1>
          <hr />
        
          <div id="article-content">
            <h3>{{movies.title}}</h3>
            <br>
            <p>Audience : {{movies.audience}}</p>
            <p>Release Dates : {{movies.release_date}}</p>
            <p>Genre : {{movies.genre}}</p>
            <p>Score : {{movies.score}}</p>
            <p>Poster URL : {{movies.poster_url}}</p>
            <p>Actor : </p>
            {% if movies.actor_image %}
            <img src="{{movies.actor_image.url}}" />
            {% endif %}
            <p>{{movies.description}}</p>
        
            <hr>
            
            <a href="{% url 'movies:update' movies.pk %}">Update</a>
            <form action="{% url 'movies:delete' movies.pk %}" method='POST'>
                {% csrf_token %}
                <input type="submit" value="DELETE">
            </form>
            <a href="{% url 'movies:index' %}">BACK</a>
        
          </div>
        {% endblock content %}
        ```
        
    2. 
    - 이 문제에서 어려웠던점
        - 가로의 크기가 커졌을때, table을 list의 옆으로 옮기기 → col 사용!
        - table과 list의 정렬이 맞지 않았을때 → 알고 보니 table에  margin을 주고 있었다.
    - 내가 생각하는 이 문제의 포인트
        - viewport에 대한 이해가 필요하다.

---

## E. create.html

- 요구 사항
    1. 영화 생성 페이지
        1. 특정 영화를 생성하기 위한 HTML form 요소를 표시
        2. 표시되는 form은 Movie 모델 클래스에 기반한 ModelForm이어야 한다.
        3. 작성한 정보는 제출(submit)시 단일 영화 데이터를 저장하는 URL로 요청과 함께 전송
        4. 전체 영화 목록 조회 페이지(index.html)로 이동하는 링크(back)를 표시
        5. actor_image에 해당하는 이미지는 직접 업로드할 수 있다.
- 결과
    1. A
        
        ```html
        <!--movies/templates/movies/create.html-->
        
        {% extends 'base.html' %}
        
        {% block content %}
        
            <h1>CREATE</h1>
            <hr>
            <form 
                action="{% url 'movies:create' %}"
                method='POST'
                enctype="multipart/form-data">
                {% csrf_token %} 
                {{form.as_p}}
                <input type="submit" value="Submit">
            </form>
        
        {% endblock content %}
        ```
        
    2. 
    - 이 문제에서 어려웠던점
        - 가로의 크기가 커졌을때, table을 list의 옆으로 옮기기 → col 사용!
        - table과 list의 정렬이 맞지 않았을때 → 알고 보니 table에  margin을 주고 있었다.
    - 내가 생각하는 이 문제의 포인트
        - viewport에 대한 이해가 필요하다.

---

## F. update.html

- 요구 사항
    1. 영화 수정 페이지
        1. 특정 영화를 수정하기 위한 HTML form 요소 표시
        2. 표시되는 form은 Movie 모델 클래스에 기반한 ModelForm이어야 한다.
        3. HTML input 요소에는 기존 데이터를 출력
        4. Reset 버튼은 사용자의 모든 입력을 초기 값으로 재설정
        5. 작성한 정보는 제출(submit)시 단일 영화 데이터를 수정하는 URL로 요청과 함께 전송
        6. 영화 상세 정보 페이지(detail.html)로 이동하는 링크(back)를 표시
- 결과
    1. A
        
        ```html
        <!--movies/templates/movies/update.html-->
        
        {% extends 'base.html' %}
        
        {% block content %}
        
          <h1>UPDATE</h1>
          <hr>
        
          <form action="{% url 'movies:update' movies.pk %}" method="POST" enctype='multipart/form-data'>
            {% csrf_token %} 
            {{form.as_p}}
            <input type="reset" value="Reset">
            <input type="submit" value="Submit">
          </form>
        
          <hr>
          <a href="{% url 'movies:detail' movies.pk %}">BACK</a>
        
        {% endblock content %}
        ```
        
    2. 
    - 이 문제에서 어려웠던점
        - 가로의 크기가 커졌을때, table을 list의 옆으로 옮기기 → col 사용!
        - table과 list의 정렬이 맞지 않았을때 → 알고 보니 table에  margin을 주고 있었다.
    - 내가 생각하는 이 문제의 포인트
        - viewport에 대한 이해가 필요하다.

---

## 후기

- Django
-