import json

revenu_list =[]
titlelist=[]
def max_revenue(movies):
    for moviedic in movies:
        a = moviedic['id']
        file_json = open(f'data/movies/{a}.json', encoding='UTF8')
        dict_json= json.load(file_json)
            
        revenu_list.append(dict_json['revenue'])
        titlelist.append(dict_json['title'])
    maxvalue = revenu_list[0]
    for i in range(len(revenu_list)):
        if revenu_list[i] > maxvalue:
            maxvalue=revenu_list[i]
    return titlelist[revenu_list.index(maxvalue)]

        
 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))