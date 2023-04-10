# PJT 02_230127

### 이번 pjt 를 통해 배운 내용

- API 요청하여 데이터를 가져오는 방법을 배웠다.
- 받은 데이터를 활용해 반복문과 조건문을 활용해 문제 해결

---

## A. 인기 영화 조회

- 요구 사항 : 인기 영화 목록을 응답 받아 개수 출력
- 결과 : 성공
    - 문제 접근 방법 및 코드 설명
    
    ```python
    def popular_count():
        # 1
        # 데이터 가져오기
        URL = 'https://api.themoviedb.org/3/movie/popular'
    
        params = {
            'api_key' : '5d5ba12807e444883a57039b0e2a1015',
            'language' : 'ko-KR',
            'region' : 'KR',
        }
        
        response = requests.get(URL, params=params).json()
    
        # 2
        # 가져온 데이터 안의 키값 results인 value값 리스트로 가져오기
        results_list = response.get('results')
        title_list = []
    
        # 3
        # 리스트의 딕셔너리 중 하나의 key값을 title_list에 모으고 리스트의 길이 => 영화목록 개수 반환!
        for idx in range(len(results_list)):
            title_list.append(results_list[idx]['original_title'])
    
        return len(title_list)
    ```
    
    - 이 문제에서 어려웠던점
        - API 요청하여 데이터 가져오기
        - 가져온 데이터에서 내가 필요한 데이터 찾기
    - 내가 생각하는 이 문제의 포인트
        - 데이터 요청하기

---

## B. 특정 조건에 맞는 인기 영화 조회 1

- 요구 사항 : 인기 영화 목록 중 평점이 8점 이상인 영화 목록 출력
- 결과 : 성공
    - 문제 접근 방법 및 코드 설명
    
    ```python
    def vote_average_movies():   
        # 1
        # 데이터 가져오기
        URL = 'https://api.themoviedb.org/3/movie/popular'
    
        params = {
            'api_key' : '5d5ba12807e444883a57039b0e2a1015',
            'language' : 'ko-KR',
            'region' : 'KR',
        }
        
        response = requests.get(URL, params=params).json()
        
        # 2
        # 가져온 데이터 안의 키값 results인 value값 리스트로 가져오기
        results_list = response.get('results')
    
        # 3
        # vote_average가 8이상인 영화 목록 넣을 리스트 선언
        # for문 + if문 활용해 'vote_average'가 8 이상이라면/results_list의 같은 인덱스 자료 추가 = > 반환!
        title_list_8 = []
        for idx in range(len(results_list)):
            if results_list[idx]['vote_average'] >= 8:
                title_list_8.append(results_list[idx])
            
        return title_list_8
    ```
    
    - 이 문제에서 어려웠던점
        - 내가 필요한 데이터 찾기(results)
    - 내가 생각하는 이 문제의 포인트
        - for문 + if문 활용해 조건에 맞는 영화 목록 리스트 작성

---

## C. 특정 조건에 맞는 인기 영화 조회 2

- 요구 사항 : 인기 영화 목록을 평점이 높은 순으로 5개의 영화 데이터 목록 출력
- 결과 : 성공
    - 문제 접근 방법 및 코드 설명
    
    ```python
    def ranking():  
        # 1
        # 데이터 가져오기
        URL = 'https://api.themoviedb.org/3/movie/popular'
    
        params = {
            'api_key' : '5d5ba12807e444883a57039b0e2a1015',
            'language' : 'ko-KR',
            'region' : 'KR',
        }
        
        response = requests.get(URL, params=params).json()
        
        # 2
        # 가져온 데이터 안의 키값 results인 value값 리스트로 가져오기
        results_list = response.get('results')
        
        # 3
        # results_list의 idx를 key, vote_average를 value로 하는 딕셔너리 선언
        # for문으로 results_list의 모든 vote_average 가져오기
        title_dict = {}
        for idx in range(len(results_list)):
            title_dict[idx] = results_list[idx]['vote_average']
    
        # 4
        # value 값 기준으로 정렬하기, sort되면서 key값이 value를 따라가야 한다/람다 이용
        sort_dict = sorted(title_dict.items(), key=lambda x:x[1], reverse=True)
    
        # 5
        # 슬라이싱 이용해서 sort_dict의 앞에서 5번째까지 자른다.
        # key값인 results_list의 인덱스를 이용해 해당하는 위치의 results_list 값 가져와 title_list_top5에 넣기 => 반환!
        title_top5_idx = sort_dict[0:5]
        title_list_top5 = []
        for i in range(5):
            title_list_top5.append(results_list[title_top5_idx[i][0]])
    
        return title_list_top5
    ```
    
    - 이 문제에서 어려웠던점
        - 딕셔너리의 value 값을 기준으로 sort 하기
    - 내가 생각하는 이 문제의 포인트
        - 인덱스를 key값으로 딕셔너리를 만들고 평점을 value로 활용해 sort해서 원하는 자료 찾기

---

## D. 특정 추천 영화 조회

- 요구 사항 : 제공된 영화 제목을 검색하여 추천 영화 목록 출력
- 결과 : 성공
    - 문제 접근 방법 및 코드 설명
    
    ```python
    def recommendation(title):
        
        # 1
        # 데이터 가져오기
        URL_1 = 'https://api.themoviedb.org/3/search/movie'
        
        params = {
            'api_key' : '5d5ba12807e444883a57039b0e2a1015',
            'language' : 'ko-KR',
            'region' : 'KR',
            'query' : title
        }
        
        response_1 = requests.get(URL_1, params=params).json()
        
        # 2
        # 가져온 데이터 안의 키값 results인 value값 리스트로 가져오기
        results_list_1 = response_1.get('results')
        
        # 3
        # if문으로 먼저 조건 정하기/ 
        # results안에 id 값이 있어야 하는데, 비어있는 경우 None
        # 제목에 해당하는 영화가 있으면 else로 이어간다.
        if results_list_1 == []:
            return None
    
        # 4    
        else:
            # 4-1 첫번째 영화의 id 값
            movie_id = results_list_1[0]['id']
            
            
            # 4-2 id 기반으로 추천 영화 목록 데이터 가져오기/ f string 사용
            URL_2 = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'
    
            params = {
                'api_key' : '5d5ba12807e444883a57039b0e2a1015',
                'language' : 'ko-KR',
            }
            
            response_2 = requests.get(URL_2, params=params).json()
            
            # 4-3 가져온 데이터 안에서 results 부분 추출 
            results_list_2 = response_2.get('results')
            
            
            # 4-4
            # 반환해야 할 recommend_title 리스트 선언
            # results_list_2 가 비어있다면 => [] 반환
            # 아닌 경우 for문 활용해 recomment_title에 results_list_2의 'title' value값 추가 => 반환!
            recommend_title = []
            if results_list_2 == False:
                return []
            else:
                for idx in range(len(results_list_2)):
                    recommend_title.append(results_list_2[idx]['title'])
                return recommend_title
    ```
    
    - 이 문제에서 어려웠던점
        - 데이터를 한번 더 요청하는 것
        - if 문 활용할 때 범위를 크게 잡아야 하는 것 / None값이 계속 출력되지 않았다.
    - 내가 생각하는 이 문제의 포인트
        - 데이터 한번 더 요청할 때 f string 활용
        - 코드 작성하면서 요청받은 데이터 return해서 확인하고 코드 짜기

---

## E. 출연진, 연출진 데이터 조회

- 요구 사항 : 제공된 영화 제목을 검색하여 해당 영화의 출연진(cast)와 스태프(crew) 중 연출진(directing)의 이름 출력
- 결과 : 성공
    - 문제 접근 방법 및 코드 설명
    
    ```python
    def credits(title):
        # 1
        # 데이터 가져오기
        URL_1 = 'https://api.themoviedb.org/3/search/movie'
        
        params = {
            'api_key' : '5d5ba12807e444883a57039b0e2a1015',
            'language' : 'ko-KR',
            'region' : 'KR',
            'query' : title
        }
        
        response_1 = requests.get(URL_1, params=params).json()
        
        # 2
        # 가져온 데이터 안의 키값 results인 value값 리스트로 가져오기
        results_list_1 = response_1.get('results')
       
        # 3
        # if문으로 먼저 조건 정하기/ 
        # results안에 id 값이 있어야 하는데, 비어있는 경우 None
        # 제목에 해당하는 영화가 있으면 else로 이어간다.
        if results_list_1 == []:
            return None
    
        # 4   
        else:
            # 4-1 첫번째 영화의 id 값
            movie_id = results_list_1[0]['id']
    
            # 4-2 id 기반으로 추천 영화 목록 데이터 가져오기/ f string 사용
            URL_2 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
    
            params = {
                'api_key' : '5d5ba12807e444883a57039b0e2a1015',
                'language' : 'ko-KR',
            }
            
            response_2 = requests.get(URL_2, params=params).json()
            
            # 4-3 response_2에서 cast, crew의 value값 담은 리스트 생성
            cast_list = response_2.get('cast')
            crew_list = response_2.get('crew')
            
            # 4-4 반환할 딕셔너리 credi_dict 선언 후, key값 cast, directing의 value값이 될 리스트 cast, directing 선언
            cast = []
            directing = []
            credit_dict = {
                'cast' : cast,
                'directing' : directing
            }
            
            # 4-5
            # cast, directing 리스트 별로 for문 사용해서 조건에 해당하는 사람 채우기
            for idx in range(len(cast_list)):
                if cast_list[idx]['cast_id'] < 10:
                    cast.append(cast_list[idx]['name'])
                    
            for idx in range(len(crew_list)):
                if crew_list[idx]['department'] == 'Directing':
                    directing.append(crew_list[idx]['name'])
                   
            return credit_dict
    ```
    
    - 이 문제에서 어려웠던점
        - 반환해야 할 딕셔너리의 value 값이 response_2의 서로 다른 key값의 value에서 찾아야 하는 점
    - 내가 생각하는 이 문제의 포인트
        - cast와 crew의 데이터 받을 때 주의해서 받기
        - 각각 for문을 이용해 반환해야 할 딕셔너리에 추가하기

---

# 후기

- 처음에 api를 통해 데이터를 가져오는 방법과 그 데이터 안에서 필요한 데이터(results)를 알아채는 과정의 시간이 걸렸지만 풀리고 나니 끝까지 괜찮았다.
- 지난주 보다는 괜찮아서 속으로 울진 않았다🙂
- 리스트와 딕셔너리에 좀 가까워진 듯한 느낌… ??