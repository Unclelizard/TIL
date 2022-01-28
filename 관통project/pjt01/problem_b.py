import json
from pprint import pprint

def movie_info(movie,genres):
    
    # 무비는 딕셔너리이다.
    # 장르스는 id와 네임을 키, 딕셔너리를 갖고있는 리스트다
    # 내가해야할것은 무비에 있는 장르아이디와
    # 장르스에 있는 id의 벨류값을 비교해서 
    # 같으면 장르스에 있는 네임의 벨류를 리스트를 만들고
    # 그 값을 넣어줄 딕셔너리에 있는 장르id의 값과 바꾸는 일이다.
    # 먼저 최종 출력될 딕셔너리를 만든다    
    
       
    
    
    # 그런다음 무비에 있는 장르아이디(딕셔너리속의 리스트로 되어있다)와 장르스에 있는 id값을
    # 비교해서. 같으면 네임값을 출력해서 리스트에 넣어준다.->둘이 동시에 비교하기가 힘들다.
    # 동시에 비교하기위해서 무비에 있는 장르아이디 값을 불러와준다
    genre_ids=movie.get('genre_ids')
    
    #[18, 80]이라는 리스트를 가져왔다.
    # 이제 값을 비교해준다.
    # 18을 넣었을때 장르이름이 나오면 된다.
    # 장르와 무비를 동시에 돌면서 비교할수 없기때문에 
    # id값을 키로->네임을 벨류로 갖는 딕셔너리를 만들어준다.
    result_dic={}
    name_list=[]
    for i in range(len(genres)):
        result_dic[genres[i]['id']] = genres[i]['name']
        

        # if genre_ids(i) = result_dit   
        #id값과 "네임을"키로 갖는 딕셔너리들이 뽑혀나왔다.
        #반복문을 빠져나가면 한번밖에 실행되지 않는다. 반복문 안에서 이 딕셔너리를 활용한다.
        #28을 넣으면 Action이 나오는 딕셔너리를 만들면 키가 id고 벨류가 name이다
        #어떻게만들지?
        #반복문을 돌려서 result_dic에 장르[원소번호]를 할당해주면
        #result_dic에는 첫번째 genre의 원소가 들어감 {{"id": 28,"name": "Action"}
        #result_dic2에 첫번쨰원소({id:28 name:action})에서 id의 값 즉 28을 키로 넣으면 값으로 i번의 네임의 값이 나오는
        #새 딕셔너리를 만들었음.
        #그럼 이제 이걸 활용해서??
        #movie에 genre_ids 값을 키로이용해서 result_dic의 값을 추출한다.
        #이걸 결과 리스트에 넣어줌.
    for j in genre_ids:
        name_list.append(result_dic.get(j)) #장르 아이디[18,80]을 돌면서 18, 80을 키로갖는 값들을 네임리스트에 추가해줌.

    resultdict = {} #새로운 딕셔너리를 만들어주고
    resultdict["genres_names"]=name_list #새딕셔너리에 장르네임즈라는 키와/값으로 아까 만들어둔 네임리스트를 넣어준다.
    info_list = ['id', 'title', 'poster_path', 'vote_average', 'overview']
    for info in info_list:
        resultdict[info] = movie[info]
    #리스트를 만들어주고 리스트를 돌면서 리스트 안에 값이 키/ 무비 인포의 벨류값이 벨류가 되도록 리절트딕셔너리에 추가해줌

    print(resultdict)
            
    


        


# def movie_info(movie, genres): ####일일히 딕셔너리를 만들어야한다.... 이걸 for문으로 돌릴려면 
#     dicta={}
#     # # 키를뽑고 = movie.get('key')
#     info_list=['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_ids']
    
#     # for i in info_list:
#     #    dicta[i]=movie[i]
#     # if type(movie[i]) == list:
#     #     info_list.remove("genre_ids")### 리스트를 순회하면서 genre_ids를 리스트에서 삭제함.
#     # print(info_list)
#     for i in genres:
#         if i['id'] == movie.get('genre_ids')[0]: #딕셔너리 장르아이디 0번값(18)
#             name1=i['name']
#         elif i['id'] == movie.get('genre_ids')[1]:#딕셔너리 장르아이디 1번값(80)
#             name2=i['name']
#     genre_name = [name2, name1] #장르네임을 만들어줬다 리스트로.
#     for i in info_list:
#        dicta[i]=movie[i]
#     if type(movie[i]) == list:
#         info_list.remove("genre_ids")
#     # print(genre_name)
                 
#     dicta['genere_name'] = genre_name #dicta에 장르네임이란 키를 추가하고 밸류는 장르네임(name2, name1)
#     return dicta# 여기까지 했는데 장르ids가 여전히 출력된다.
#     #for문에서 삭제시켰지만 밑에서 돌면서 실행이 안되기 때문? 순서를 바꿔본다->그래도 장르아이디가 출력됨.
#     # . dicta에서 삭제시켜줘야 할것 같다. 리스트에서 삭제해도 참조된


    
    # changed_info_list = ['id', 'title', 'poster_path', 'vote_average', 'overview', 'genre_names']
    # for i in range(len(info_list)):#인포리스트 값의 길이만큼 i를 반복한다
    #     if type(movie[info_list[i]]) == list: #[18, 80]
    
    #         for i in genres:
    #             if i['id'] == movie.get('genre_ids')[0]:
    #                 name1=i['name']
    #             elif i['id'] == movie.get('genre_ids')[1]:
    #                 name2=i['name']
                 
            
            
    #     for info in changed_info_list:
    #      return_dict[info] = movie[info]
        

            

    # for info in changed_info_list:
    #     # genre_names = [name2, name1]
    # # return return_dict[info] = movie[info]
    # for i in genres:
    #     if i['id'] == movie.get('genre_ids')[0]:
    #         name1=i['name']
    #     elif i['id'] == movie.get('genre_ids')[1]:
    #         name2=i['name']
    
    
## genre_ids를 손으로 삭제하지 않고 리스트에서 직접 빼주는 것을 생각.
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))