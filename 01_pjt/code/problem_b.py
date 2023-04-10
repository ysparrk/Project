import json
from pprint import pprint

# id,title,poster_path,vote_average,overview,genre_names
# genre_ids를 각 장르 번호에 맞는 name 값으로 대체한 genre_names 키 생성
# 새로운 딕셔너리 반환하는 함수 movie_info 완성

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
    
            

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
