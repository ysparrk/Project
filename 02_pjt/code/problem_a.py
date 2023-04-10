import requests

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


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
