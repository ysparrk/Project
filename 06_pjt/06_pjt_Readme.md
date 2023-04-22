# PJT_06_230414

### 이번 pjt 를 통해 배운 내용

- git branch를 활용한 팀과의 협업
- Django 및 Database의 전반적인 활용

---

# A. Git workflow

- branch와 원격 저장소를 이용해 협업을 하는 방법 사용

## Fork & Pull model

1. 원격 저장소를 fork를 통해 내 원격 저장소로 복제
2. fork 이후, 복제된 내 원격 저장소를 로컬 저장소에 clone
3. 로컬 저장소와 원본 원격 저장소를 동기화 하기 위해 연결
    1. `git remote add upstream {url}`
4. 사용자는 자신이 작업할 기능에 대한 브랜치를 생성하고, 그 안에서 기능을 구현
5. 기능 구현이 완료되면, 복제 원격 저장소(origin)에 해당 브랜치를 push
6. 복제 원격 저장소(origin)에 브랜치가 반영
7. pull request를 통해 origin의 브랜치를 upstream에 반영해달라는 요청을 보냄
8. upstream에 브랜치가 병합되면 origin의 브랜치는 삭제
9. 이후 사용자는 로컬에서 master 브랜치로 switch
10. 병합으로 인해 변경된 upstream의 master 내용을 로컬에 pull
    1. `git pull upstream master`
11. upstream의 master 내용을 받았으므로, 기존 로컬 브랜치 삭제(한 사이클 종료)
12. 새로운 기능 추가를 위해 새로운 브랜치를 생성하며 위 과정을 반복

📌 이 문제에서 어려웠던 점

- git의 pull request의 사용이 처음이라 적응하는데 시간이 걸렸다.
- 계속 흐름에 따라 수정하면서 브랜치를 바꾸지 않아 원하지 않았던 브랜치에 커밋이 올라가는 경우가 발생했다.
- 상대가 model을 수정했다면 다시 `migrate` 해 주어야 하는 점을 자주 까먹었다.

📌  내가 생각하는 이 문제의 포인트

- 가장 중요한 것은 브랜치를 잘 설정하는 것이라고 생각이 들었다. 너무 브랜치를 세세하게 나누면 작업 시간이 너무 오래걸리고, 너무 크게 잡으면 상세한 수정이 보이지 않는다는 점이다.

---

# B. movies app

## 요구사항

- 영화 데이터의 생성, 조회, 수정, 삭제, 좋아요가 가능한 애플리케이션 완성

📌 이 문제에서 어려웠던 점(error 정리)

1. base.html
    1. 회원 탈퇴의 부분은 form으로 작성

```java
<form action="{% url 'accounts:delete' %}" method='POST'>
  {% csrf_token %}
  <input type="submit" value="회원탈퇴">
</form>
```

1. `@login_required()` : 로그인 한 경우에 함수 실행
2. [views.py](http://views.py) create
    1. commit=False
    - 아직 데이터베이스에 저장되지 않은 인스턴스를 반환
    - 저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 유용하게 사용한다.

```java
@require_http_methods(['GET', 'POST'])
@login_required()
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            **movie = form.save(commit=False)**
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)
```

1. 오타주의!!! ❎❎❎❎❎

📌  내가 생각하는 이 문제의 포인트

- 명세서의 흐름에 따라 정리하기
- pk가 많이 등장한다. pk의 이름 설정 및 연결되는 pk사용

---

# C. accounts app

## 요구사항

- 로그인, 로그아웃, 회원가입, 회원탈퇴, 회원정보수정, 비밀번호 변경, 팔로우가 가능한 애플리케이션

⇒ **cooperate with hun23**

---

## 후기

- 나는 movies app을, 동훈님은 accounts app을 담당했다. 하지만 두 앱이 겹치는 부분이 생길때 혼동이 발생했다.
- runserver를 하지 않고 코드만 짜야 하는 상황이 발생했을 때 어려운 부분이 생겼다.
- 하나를 만들 때마다 pull requesst를 하면 팀장이 많이 귀찮아 지는 상황이 발생하는데 여기에 코드가 잘못되서 수정까지 계속하게되면 branch 안에서 사소한 커밋 푸쉬가 계속 일어나는 것 같아 실수를 줄여야겠다는 생각이 강하게 들었다.
- 오늘은 시간의 압박을 조금(?) 느끼며 빠르게 코드를 짜려고 생각했었는데, 나중에 충분한 시간이 생긴다면 branch의 구성을 잘 생각하고 해야겠다고 생각했다. 생각보다 commit으로 남기는 메시지가 중요하다는 것을 알 수 있었다.
- 항상 계속되는 오타는 주의…!!!