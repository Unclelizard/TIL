# 프로젝트 2

``` 
requests라는 라이브러리.->요청하는 라이브러리
pip install로 설치한다.

URL을 구성할때 api주소를쓰고 요청 양식에 맞춰서 URL을 작성한 뒤
변수=requests.get(주소를쓴다)
json이 지원되면 .json을 붙일 수 있다.

```

# D

```
def recommendation(title):
    URL='https://api.themoviedb.org/3/search/movie?api_key=17257a665a045cdca418c3a7f455139e&query=2&region=kr&language=ko'
    BASE_URL='https://api.themoviedb.org/3'
    serchpath='/search/movie'
    params={
        'api_key':'17257a665a045cdca418c3a7f455139e',
        'region' : 'KR',
        'language': 'ko',
        'query': f'{title}'#들어간 영화를 서치하는것같음. #이곳에서 헤맸는데 f스트링으로 들어오는 변수 title을 지정해주면 title이 들어간 영화를 서치해줌
        }
    response=requests.get(BASE_URL+serchpath,params=params).json()
    #변수 리스폰=URL을 설정하고 요청한다.
    moviels=response.get('results')
    #moviels는 주소에서 받아온 값(딕셔너리로되어있음) results를 키로 갖는 리스트벨류를 뽑아옴.
    movie_id=[] #무비아이디열어주고
    name=[]#이름
    result=[]
    #print(moviedic)#무비딕내용 출력테스트
    for i in range(len(moviedic)):#무비딕(리스트속딕셔너리개수만큼 돌면서)
        movie_id.append(moviedic[i]['id'])#무비딕번호마다 id키를 갖는 벨류를 리스트에넣어줌
    #print(movie_id) #무비아이디들만을 모은 리스트
    params2={
        'api_key':'17257a665a045cdca418c3a7f455139e',
        'region' : 'KR',
        'language': 'ko',}
    for j in range(len(movie_id)):
        path=f'/movie/{movie_id[j]}/recommendations'
        response2=requests.get(BASE_URL+path,params=params2).json()
        result=response2.get('results') #추천영화를 뽑아주고 리절트리스트에 영화정보를 넣어줌. 굳이 안넣어줘도됨 원래리스트.
        if result==[]:
            return "추천 영화 없음" # 검색한 결과가 없으면? 추천영화없음
        
        for h in range(len(result)):
            name.append(result[h].get('title'))
    if name == []:
        return #검색불가영화면 None
    else:
    	return name #추천순위에있는걸 아이디에넣고 뽑아준다..
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록 구성.
    추천 영화가 없을 경우 [].
    영화 id검색에 실패할 경우 None.
    """
    pprint(recommendation('기생충'))
    # ['조커', '조조 래빗', '1917', ..., '토이 스토리 4', '스파이더맨: 파 프롬 홈']
    pprint(recommendation('그래비티'))
    # []  => 추천 영화 없음
    pprint(recommendation('검색할 수 없는 영화'))
    # => None

```

