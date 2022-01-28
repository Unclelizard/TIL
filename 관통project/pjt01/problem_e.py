from calendar import month_name
import json

release_date =[]
titlelist=[]
resultlst=[]
dictlist={}
def dec_movies(movies):
    for moviedic in movies:
        a = moviedic['id']
        file_json = open(f'data/movies/{a}.json', encoding='UTF8')
        dict_json= json.load(file_json)
            
        release_date.append(dict_json['release_date'])
        titlelist.append(dict_json['title'])
    # print(titlelist)        
    cnt=0
    for month in release_date:
    
        y,m,d=month.split("-")    
        if m == "12":
            resultlst.append(titlelist[cnt])
            cnt+=0
        cnt+=1
    print(resultlst)
            

            

            

            


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))