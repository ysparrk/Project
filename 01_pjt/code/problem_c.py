import json
from pprint import pprint


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

        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
