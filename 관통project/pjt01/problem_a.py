import json
from pprint import pprint


def movie_info(movie): ####일일히 딕셔너리를 만들어야한다.... 이걸 for문으로 돌릴려면 키를뽑고 = movie.get('key')
    return_dict = {}   
     info_list = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
     for info in info_list:
         return_dict[info] = movie[info]
     return return_dict
   
    




#아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
