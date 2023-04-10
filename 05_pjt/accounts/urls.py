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
