import json

# 가장 높은 수익을 낸 영화를 출력하는 알고리즘 작성.
# movies.json, movies 폴더 내부 파일 활용
# 반복문을 통해 movies 폴더 내부의 파일 오픈 / 
# 수익이 같은 영화 x
# title 사용

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
        


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
