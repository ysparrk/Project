import requests
from pprint import pprint


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
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
    """
    [{'adult': False,
      'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
      'genre_ids': [28, 18],
      'id': 361743,
      'original_language': 'en',
      'original_title': 'Top Gun: Maverick',
      'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
                  '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
                  '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
                  '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
      'popularity': 911.817,
      'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
      'release_date': '2022-06-22',
      'title': '탑건: 매버릭',
      'video': False,
      'vote_average': 8.4,
      'vote_count': 1463},
    ..생략..,
    }]
    """
