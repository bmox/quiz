#read 1.txt mcq question and split it single question
# like this
# database={
# {
# "q_no": "1",
# 'question':"Compromising a user’s session for exploiting the user’s data and do malicious activities or \
# misuse user’s credentials is called ___________",
# "a": "Session Hijacking" ,
# "b": "Session Fixation" ,
# "c": "Cookie stuffing",
# "d": "Session Spying",
# "answer": "a"
# },
# {
# "q_no": "2",
# 'question':"An attempt to harm, damage or cause threat to a system or network is broadly termed as \
# ______",
# "a": "Cyber-crime " ,
# "b": "Cyber Attack" ,
# "c": "System hijacking",
# "d": " Digital crime",
# "answer": "d"
# }
# }

database=[]
count=1
# with open('./data/2.txt') as f:
with open('./data/1.txt') as f:
    data = f.read()
    # split data base on starting and closing bracket (skip roman number) use regex
    data=data.split('(')
    for i in range(len(data)):
        data[i]=data[i].split(')')
        # print(data[i])
        if len(data[i])==6:
            
            print("q_no:",count)
            dash=data [i][1][:-1]
            arr = dash.split()
            for j in range(len(arr)):
                if '_' in arr[j]:
                    arr.insert(j,'dash')
                    break
            question=' '.join(arr)
            question=question.replace('_','')
            single_question={ "q_no": count,
                              "data":{
                                    "question":question,
                                    "a":data[i][2][:-1],
                                    "b":data[i][3][:-1],
                                    "c":data[i][4][:-1],
                                    "d":data[i][5][:-1],
                                    "answer":""
                              }
                             }
            
            print("question:",question)
            print("a:",data[i][2][:-1])
            print("b:",data[i][3][:-1])
            print("c:",data[i][4][:-1])
            print("d:",data[i][5][:-1])
            count +=1
            database. append(single_question)
        else:
            # print(data [i])
            pass
             
# print(database)    

import json
with open('1.json', 'w', encoding='utf-8') as f:
    json.dump(database, f, ensure_ascii=False, indent=4)
    

