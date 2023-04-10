import requests
from pprint import pprint


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


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
