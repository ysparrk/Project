import json
from pprint import pprint
 
 
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


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))

