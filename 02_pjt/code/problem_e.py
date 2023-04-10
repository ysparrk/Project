import requests
from pprint import pprint


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


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
