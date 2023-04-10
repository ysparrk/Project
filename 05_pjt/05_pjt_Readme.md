# PJT_05_230407

### 이번 pjt 를 통해 배운 내용

- DB를 활용한 웹 페이지 구현 및 인증과 권한 활용
- Django의 전반적인 활용

---

# A. 사전 설정

## 1. MODEL

### 1) Movie

- 요구사항
    - 정의할 모델 클래스의 이름 : Movie

```python
# movies.modles.py

from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
```

### 2) User

- 요구사항
    - 정의할 모델 클래스의 이름 : User
    - AbstractUser 모델 클래스를 상속 받는 커스텀 모델을 사용

```python
# accounts.modles.py

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
```

- 이 문제에서 어려웠던 점
    - import
- 내가 생각하는 이 문제의 포인트
    - AbstractUser 모델 클래스 상속 커스텀 모델 사용

## 2. URL

- 요구사항
    - URL 요청에 맞는 역할 설정하기

### 1) movies app

```python
# movies.urls.py

from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),                    # 전체 영화 목록 페이지 조회
    path('create/', views.create, name='create'),           # 새로운 영화 생성 페이지 조회 & 단일 영화 데이터 저장
    path('<int:pk>/', views.detail, name='detail'),         # 단일 영화 상세 페이지 조회
    path('<int:pk>/update/', views.update, name='update'),  # 기존 영화 수전 페이지 조회 & 단일 영화 데이터 수정
    path('<int:pk>/delete/', views.delete, name='delete'),  # 단일 영화 데이터 삭제
]
```

### 2) accounts app

```python
# accounts.urls.py

from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),           # 로그인 페이지 조회 & 세션 데이터 생성 및 저장(로그인)
    path('logout/', views.logout, name='logout'),        # 세션 데이터 삭제(로그아웃)
    path('signup/', views.signup, name='signup'),        # 회원 생성 페이지 조회 & 단일 회원 데이터 생성(회원가입)
    path('delete/', views.delete, name='delete'),        # 단일 회원 데이터 삭제(회원 탈퇴)
    path('update/', views.update, name='update'),        # 회원 수정페이지 조회 & 단일 회원 데이터 수정(회원 정보 수정)
    path('password/', views.change_password, name='change_password'),  # 비밀번호 수정 페이지 조회 & 단일 비밀번호 데이터 수정(비밀번호 변경)
]
```

## 3. Admin

- 요구사항
    - 모델 Movie, User를 Admin site에 등록
    - Admin site에서 데이터의 생성, 조회, 수정, 삭제가 가능해야 한다.

### 1) user

```python
# movies.admin.py

from django.contrib import admin
from .models import Movie

# Register your models here.
admin.site.register(Movie)
```

### 2) accounts

```python
# accounts.admin.py

from django.contrib import admin
from .models import User

# Register your models here.
admin.site.register(User)
```

- 이 문제에서 어려웠던 점
    - `from django.contrib.auth.admin import UserAdmin` 를 사용했었는데 두 앱에서의  충돌이 나 에러가 발생하였다. → 삭제하여 해결
- 내가 생각하는 이 문제의 포인트
    - [admin.py](http://admin.py) 에서의 import 문제

## 4. Form

- 요구사항
    - Movie 모델의 데이터 검증, 저장, 에러메시지, HTML을 모두 관리
    - User 모델의 데이터 검증, 저장, 에러메시지, HTML 관리

### 1) Movie

```python
# movies.forms.py

from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'
```

### 2) User

```python
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')
```

- 내가 생각하는 이 문제의 포인트
    - [admin.py](http://admin.py) 에서의 import 문제

# B. View & Template

## 0. base.html

- 요구사항
    - 공통 부모 템플릿
        - 모든 템플릿 파일은 base.html을 상속받아 사용
        - nav 태그를 사용한 상단 네비게이션 바
        - 네비게시션 바는 회원의 로그인, 비로그인 상태에 따라 다른 링크를 출력
    - 로그인 상태
        - 회원정보수정, 로그아웃, 회원 탈퇴
    - 비로그인 상태
        - 로그인, 회원가입

```python
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{% static 'base.css' %}">
    <title>MY PJT</title>
</head>
<body>
    
    <div id="nav">

        {% if user.is_authenticated %}
            <h3>Hello {{user}}</h3>
            <a href="{% url 'accounts:update' %}">회원정보 수정</a>
            <form action="{% url 'accounts:logout' %}" method="POST">
                {% csrf_token %}
                <input type="submit" value="Logout">
            </form>
            <a href="{% url 'accounts:change_password' %}">비밀번호 변경</a>
            <form action="{% url 'accounts:delete' %}" method="POST">
                {% csrf_token %}
                <input type="submit" value="회원탈퇴">
            </form>
        
        {% else %}
            <a href="{% url 'accounts:login' %}">Login</a>
            <a href="{% url 'accounts:signup' %}">Sign up</a>
        
        {% endif %}

    </div>
    
    <hr>
    <div id="content">
        {% block content %}
        {% endblock content %}
    </div>

</body>
</html>
```

- 내가 생각하는 이 문제의 포인트
    - 로그인 상태와 비로그인 상태에서의 화면 변화 → `{% if user.is_authenticated %}` 사용

## 1. movies

### 1) index

- 요구사항
    - 데이터베이스에 존재하는 모든 영화의 목록 표시
    - 제목 클릭 시 해당 영화의 상세 조회 페이지로 이동

```python
# movies.views.py

@require_http_methods(['GET'])
def index(request):
    movies = Movie.objects.all()
    context = {'movies' : movies}
    return render(request, 'movies/index.html', context)
```

```python
<!--movies.templates.index.html-->

{% extends 'base.html' %}

{% block content %}
    <h1>INDEX</h1>
    <a href="{% url 'movies:create' %}">[CREATE]</a>
    <hr>
    {% for movie in movies %}
        <a href="{% url 'movies:detail' movie.pk %}">{{movie.title}}</a>
        <hr>
    {% endfor %}
{% endblock content %}
```

- 이 문제에서 어려웠던 점
    - detail.html로 넘어가지 않았다. → `{% for movie in movies %}` 이므로 view함수에서 `movies = Movie.objects.all()` 로 나타내야 한다.
- 내가 생각하는 이 문제의 포인트
    - 데이터베이스에 존재하는 모든 영화 목록 표시

---

### 2) create

- 요구사항
    - 특정 영화를 생성하기 위한 HTML form 요소 푯
    - 모델 클래스에서 기반한 ModelForm
    - 작성한 정보는 제출(submit)시 단일 영화를 저장하는 URL로 요청과 함께 전송
    - 전체 영화 목록 조회 페이지(index.html)로 이동하는 링크 표시

```python
# movies.views.py

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {'form' : form}
    return render(request, 'movies/create.html', context)
```

```python
<!--movies.templates.create.html-->

{% extends 'base.html' %}

{% block content %}
    <h1>Create</h1>
    <hr>
    <form action="{% url 'movies:create' %}" method='POST' enctype='multipart/form-data'>
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="Submit">
    </form>

{% endblock content %}
```

- 이 문제에서 어려웠던 점
    - `movie = form.save()` 에 오타가 있어서 create가 되지 않았고, detail.html로 넘어가지 않았다.
- 내가 생각하는 이 문제의 포인트
    - pk 넣고 저장하기
    - 오타주의!

---

### 3) detail

- 요구사항
    - 특정 영화의 상세 정보 표시
    - 해당 영화의 수정 및 삭제 버튼 표시
    - 전체 영화 목록 조회 페이지로 이동하는 링크 표시

```python
# movies.views.py

@require_http_methods(['GET'])
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {'movie' : movie}
    return render(request, 'movies/detail.html', context)
```

```python
<!--movies.templates.detail.html-->

{% extends 'base.html' %}

{% block content %}

    <h1>DETAIL</h1>
    <hr/>

    <div id="movie=content">
        <h3>{{movie.title}}</h3>
        <p>Description : {{movie.description}}</p>
    </div>
    
    <a href="{% url 'movies:update' movie.pk %}">UPDATE</a>
    <form action="{% url 'movies:delete' movie.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE">
    </form>
    <a href="{% url 'movies:index' %}">BACK</a>

{% endblock content %}
```

- 이 문제에서 어려웠던 점
    - `method="POST"` 를 빠뜨려 데이터가 나타나지 않았다.
- 내가 생각하는 이 문제의 포인트
    - 모델에서 데이터 가져오기

---

### 4) update

- 요구사항
    - 특정 영화를 수정
    - 표시되는 form은 Movie 모델 클래스에 기반한 ModelForm이어야 한다.
    - HTML input요소에는 기존 데이터 출력
    - Reset 버튼으로 사용자의 모든 입력 초기 값으로 재설정
    - 작성한 정보는 제출시 단일 영화 데이터를 수정하는 URL로 요청과 함께 전송
    - 영화 상세 정보 페이지로 이동하는 링크 표시

```python
# movies.views.py

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
```

```python
<!--movies.templates.update.html-->

{% extends 'base.html' %}

{% block content %}

    <h1>UPDATE</h1>
    <hr>
    <form action="{% url 'movies:update' movies.pk %}" method="POST" enctype="multipart/form">
        {% csrf_token %}
        {{form.as_p}}
        
        <input type="reset" value="Reset">
        <input type="submit" value="Submit">        
    </form>
    <hr>
    <a href="{% url 'movies:detail' movies.pk %}">BACK</a>    

{% endblock content %}
```

- 내가 생각하는 이 문제의 포인트
    - pk 값으로 해당하는 영화의 자료 가져오기

---

### 5) delete

```python
# movies.views.py

@require_http_methods(['POST'])
def delete(request, pk):
    movies = Movie.objects.get(pk=pk)
    movies.delete()
    return redirect('movies:index')
```

- 이 문제에서 어려웠던 점
    - delete를 위해 base.html에서 form사용하기
- 내가 생각하는 이 문제의 포인트
    - delete 후 index.html로 돌아가기

## 2. accounts

### 1) login

- 요구사항
    - 로그인을 위한 HTML form 요소 표시
    - 작성한 정보는 제출시 로그인 URL로 요청과 함께 전송
    - 로그인 한 회원만 영화 정보를 생성, 수정, 삭제

```python
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            **return redirect(request.GET.get('next') or 'movies:index')**
    else:
        form = AuthenticationForm()

    context = {'form' : form}
    return render(request, 'accounts/login.html', context)
```

```python
{% extends 'base.html' %}

{% block content %}

    <h1>Login</h1>
    <form action="{% url 'accounts:login' %}" method="POST">
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="Submit">
    </form>

{% endblock content %}
```

- 이 문제에서 어려웠던 점
    - user가 로그인 되어 있는지 아닌지 확인 → `return redirect(request.GET.get('next') or 'movies:index')`
- 내가 생각하는 이 문제의 포인트
    - AuthenticationForm import

---

### 2) logout

- 요구사항
    - 로그아웃

```python
@require_http_methods(['POST'])
def logout(request):
    auth_logout(request)
    return redirect('movies:index')
```

- 이 문제에서 어려웠던 점
    - 처음에는 데코레이터에서 ‘GET’요소를 받아야 가능했다. → ‘POST’를 사용하기 위해서는 base.html에서 로그아웃 폼을 작성한다.
- 내가 생각하는 이 문제의 포인트
    - 데코레이터 활용하기

---

### 3) signup

- 요구사항
    - 회원가입을 위한 HTML form 요소 표시
    - 작성한 정보는 제출시 회원가입 URL로 요청과 함께 전송

```python
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()

    context = {'form' : form}
    return render(request, 'accounts/signup.html', context)
```

```python
{% extends 'base.html' %}

{% block content %}

    <h1>Signup</h1>

    <form action="{% url 'accounts:signup' %}" method='POST'>
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="Submit">
    </form>

{% endblock content %}
```

- 내가 생각하는 이 문제의 포인트
    - create과 같은 의미의 로직이다.

---

### 4) update

- 요구사항
    - 회원정보수정을 위한 HTML form 요소를 표시
    - 작성한 정보는 제출시 회원정보수정 URL로 요청과 함께 전송

```python
@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {'form' : form}
    return render(request, 'accounts/update.html', context)
```

```python
{% extends 'base.html' %}

{% block content %}

    <h1>회원정보 수정</h1>

    <form action="{% url 'accounts:update' %}" method='POST'>
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="Submit">
    </form>
    

{% endblock content %}
```

- 내가 생각하는 이 문제의 포인트
    - movies의 update와 비슷한 로직

---

### 5) delete

```python
@require_http_methods(['POST'])
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('movies:index')
```

- 이 문제에서 어려웠던 점
    - `method="POST"` 를 빠뜨려 데이터가 나타나지 않았다.
- 내가 생각하는 이 문제의 포인트
    - 모델에서 데이터 가져오기

---

### 6) change_password

- 요구사항
    - 비밀번호변경을 위한 HTML form 요소를 표시
    - 작성한 정보는 제출시 비밀번호 변경 URL로 요청과 함께 전송
    - 비밀번호 변경 직후 로그인 상태 유지

```python
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            **update_session_auth_hash(request, form.user)**
            return redirect('movies:index')

    else:
        form = PasswordChangeForm(request.user)
    
    context = {'form' : form}
    return render(request, 'accounts/change_password.html', context)
```

```python
{% extends 'base.html' %}

{% block content %}

    <h1>비밀번호 변경</h1>
    <form action="{% url 'accounts:change_password' %}" method='POST'>
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="Submit">

    </form>

{% endblock content %}
```

- 이 문제에서 어려웠던 점
    - 비밀번호 변경 직후 로그인 상태 유지 → `update_session_auth_hash(request, form.user)` 사용
- 내가 생각하는 이 문제의 포인트
    - 비밀번호 변경 후 로그인 상태 유지

---

## 후기

- movies의 CRUD는 지난 프로젝트와 비슷해서 수월할 것이라고 생각했다. 하지만 시간이 지나고 다시 해보니 정리한 노션을 참고하지 않으면 혼자서 하기 힘들었다.
- 하지만 반복적으로 프로젝트를 하다 보면 적응이 될 부분이라는 생각이 들었다.
- 이번에 오타가 많이 나서 에러가 발생했는데 급한 마음을 가지지 말고 하나하나 이해하며 확실히 공부를 해야겠다.