# PJT_01_230120

### 이번 pjt 를 통해 배운 내용

- json에서 필요한 데이터 추출하기
- 딕셔너리의 사용법

---

## A. 제공되는 영화 데이터의 주요내용 수집

- 요구 사항 : 영화데이터에서 서비스 구성에 필요한 정보만 추출해 반환하는 함수 단계적 완성
- 결과 : 성공
    - 문제 접근 방법 및 코드 설명
    
    ```python
    def movie_info(movie):
        # 1
        # result 딕셔너리를 만들고, 필요한 정보를 가져온다. .get() 사용해 value 값 가져오기
        # pprint(movie)      # pprint는 import를 해야 사용이 가능하다. print는 보기 불편하다.
        result = {
            'id' : movie['id'], 
            'title' : movie['title'],
            'poster_path' : movie.get('poster_path'),     
            'vote_average' : movie.get('vote_average'),
            'overview': movie.get('overview'),
            'genre_ids' : movie.get('genre_ids')
        }
        return result
    ```
    
    - 이 문제에서 어려웠던점
        - json에서 자료를 파악하는 것이 어려움
    - 내가 생각하는 이 문제의 포인트
        - result 딕셔너리 정의하기

---

## B. 제공되는 영화 데이터의 주요내용 수정

- 요구 사항 : genre_ids를 장르 번호가 아닌 장르 이름 리스트 genre_names로 바꿔 반환
- 결과 : 성공
    - 문제 접근 방법 및 코드 설명
    
    ```python
    def movie_info(movie, genres):
        # 1
        # movie.json에서 필요한 값 추출해서 딕셔너리 만들기
        result = {
            'id' : movie['id'], 
            'title' : movie['title'],
            'poster_path' : movie.get('poster_path'),     
            'vote_average' : movie.get('vote_average'),
            'overview': movie.get('overview'),
            'genre_names' : movie.get('genre_ids')
        }
    
        # 2
        # result의 'genre_names' value값을 추출해 ids_list 만들기 / 
        # for문 1 : ids_list의 모든 요소 돌린다/ids_list는 숫자가 두개 있는 리스트/
        # for문 2 : genre의 모든 id의 value값을 1번 for문의 해당하는 ids와 같다면 add_list에 추가
        # result 딕셔너리의 'genre_names'의 value 값을 add_list로 바꾼다
        ids_list = result['genre_names']
        add_list = []
        
        for ids in ids_list:
            for i in range(0, len(genres)):
                if genres[i]['id'] == ids:
                    add_list.append(genres[i]['name'])
    
                result['genre_names'] = add_list
                    
    
        return result
    ```
    
    - 이 문제에서 어려웠던점
        - 리스트 안의 딕셔너리 안의 위치 설정. [i]넣는 부분이 가장 어려웠다.
    - 내가 생각하는 이 문제의 포인트
        - for문 두번 사용하기

---

## C. 다중 데이터 분석 및 수정

- 요구 사항 : 평점 높은 20개의 영화 데이터를 바탕으로 서비스 구성에 필요한 정보만 추출해 반환
- 결과 : 성공
    - 문제 접근 방법 및 코드 설명
    
    ```python
    def movie_info(movies, genres):
        # 1
        # 반환할 리스트 선언
        top20_list = []
    
        # 2
        # B와 비슷하게 result를 가져오지만 for문 활용해 movies의 모든 것들 딕셔너리로 추가하기
        for idx in range(0, len(movies)):
            result = {
                'id' : movies[idx]['id'], 
                'title' : movies[idx]['title'],
                'poster_path' : movies[idx]['poster_path'],    
                'vote_average' : movies[idx]['vote_average'],
                'overview': movies[idx]['overview'],
                'genre_names' : movies[idx]['genre_ids']
            }
    
            ids_list = result['genre_names']
            add_list = []
                
            for ids in ids_list:
                for i in range(0, len(genres)):
                    if genres[i]['id'] == ids:
                        add_list.append(genres[i]['name'])
    
                    result['genre_names'] = add_list
    
            top20_list.append(result)
    
        return top20_list
    ```
    
    - 이 문제에서 어려웠던점
        - B를 이해했다면 괜찮았다.
    - 내가 생각하는 이 문제의 포인트
        - for문 활용해 movies의 모든 값 적용해서 리스트에 추가

---

## D. 알고리즘을 사용한 데이터 출력

- 요구 사항 : 영화 세부 정보 중 수입 정보를 이용하여 가장 높은 수익을 낸 영화를 출력
- 결과 : 성공
    - 문제 접근 방법 및 코드 설명
    
    ```python
    def max_revenue(movies):
    
        # 1
        # title이 key, revenue가 value인 딕셔너리 선언
        movie_revenue = {}
        
        # 2
        # movies의 top20 id 값이 json폴더 명과 같다. 그래서 일단 id_list 만들기
        # for문 사용해서 moives의 모든 요소들에서 id값 담기
        id_list = []
        for idx in range(len(movies)):
            id_list.append((movies[idx])['id'])
    
        # 3
        # id_list를 활용해 해당 번호의 json폴더 열기
        # 폴더 열어서 movie_revenue에 값 추가
        for num in range(len(id_list)):
            movie_id = id_list[num]
            movie = open(f'data/movies/{movie_id}.json', encoding='utf-8')
            movie_detail = json.load(movie)
                    
            movie_revenue[movie_detail['title']] = movie_detail['revenue']
    
        # 4
        # 만들어진 딕셔너리의 value 값에서 최댓값 구하기
        value_max = max(movie_revenue.values())
        
        #5
        # 최댓값의 해당 key값 찾아서 반환하기
        # 순환이 계속 일어나다가 return key를 사용한 후 값 출력. 이유 파악 필요
        for key, value in movie_revenue.items():     
            if value == value_max:
                return key   
    
        return max_revenue(movies)
    ```
    
    - 이 문제에서 어려웠던점
        - 폴더 여는 부분이 머릿속에서 구현이 안된다.
        - 마지막에 key를 반환해야 했는데 계속 순환이 돌아 return을 저렇게 써도 되는건지 잘 모르겠었다.
    - 내가 생각하는 이 문제의 포인트
        - 폴더 열어서 json파일 확인하기.

---

## E. 알고리즘을 사용한 데이터 출력

- 요구 사항 : 영화 세부 정보 중 개봉일 정보(release_date)를 이용해 12월에 개봉한 영화들의 제목 리스트를 출력
- 결과 : 성공
    - 문제 접근 방법 및 코드 설명
    
    ```python
    def dec_movies(movies):
        # 1
        # title이 key, month가 value인 딕셔너리 선언
        # title을 모을 리스트 선언
        movie_title_dict = {}
        movie_title_list = []
    
        # 2
        # 폴더 열기/ id_list 생성
        id_list = []
        for idx in range(len(movies)):
            id_list.append((movies[idx])['id'])
    
        # 3
        # 폴더 열기
        # release_date에서 month만 넣기 위해 슬라이싱해서 month만 넣기
        for num in range(len(id_list)):
            movie_id = id_list[num]
            movie = open(f'data/movies/{movie_id}.json', encoding='utf-8')
            movie_detail = json.load(movie)
                    
            movie_title_dict[movie_detail['title']] = movie_detail['release_date'][5:7]
    
        # 4
        # movie_title_dict에서 value 값이 12라면 key값을 movie_title_list에 추가 => 반환!
        for key, value in movie_title_dict.items():
            if value == '12':
                movie_title_list.append(key)
        
        return movie_title_list
    ```
    
    - 이 문제에서 어려웠던점
        - return dec_movies(movies)를 하면 에러가 떠서 결국 return movie_title_list를 했다. 이렇게 해도 되나라는 생각이 들었다.
    - 내가 생각하는 이 문제의 포인트
        - 12월인 title을 위해 if 문 사용하기 + 리스트 만들기

---

# 후기

- 교수님의 설명을 들을 때부터 험난함이 예상되었다.
- 뭔가 이어지는 듯한 코드가 신기했다.
- 계속 상상하게 하고 눈에 보이지 않는 구현 현상들이 어렵지만 재미있었다.
- pjt는 정말 흥미로웠다. 속으로는 눈물이 났지만 재미 있었다!
- 설연휴 전날이라 4시에 끝났는데 빠른 퇴실은 정말 좋았지만 2시간이 더 있었다면 pjt를 좀 더 여유롭게, 모두 끝낼 수 있었을텐데 라는 아쉬움은 남았다.
- 정말 처음에는 길을 찾기 어려웠지만 주변 사람들에게 많은 도움을 받을 수 있어 감사했다.