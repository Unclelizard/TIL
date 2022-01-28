import json
from pprint import pprint


def movie_info(movies, genres):
    id = movies.get('id')#id번호 밸류
    title = movies.get('title') #title 밸류      
    genre_ids=movies.get('genre_ids')
    poster_path=movies.get('poster_path')
    vote_average=movies.get('vote_average')
    overview=movies.get('overview')
    
    for i in genres:
        if i['id'] == movies.get('genre_ids')[0]:
            name1=i['name']
        elif i['id'] == movies.get('genre_ids')[1]:
            name2=i['name']
    genre_name = [name2, name1]
    
    result = {'genere_name':genre_name,'id': id, 'title': title,'poster_path':poster_path,'vote_average':vote_average,'overview':overview}
    return result
    
    
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))