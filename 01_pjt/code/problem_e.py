import json


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
            
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
