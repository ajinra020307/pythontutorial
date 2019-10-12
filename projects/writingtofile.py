import requests

def getquiz():
    reqresponse=requests.get('https://opentdb.com/api.php?amount=10&type=multiple')
    reqdata=reqresponse.json()['results']
    return reqdata

def write():
    data=getquiz()
    file=open('quiz.txt','a+')

    for question in data:
        q=question['question']
        ans=question['correct_answer']
        file.write('Q:{q} \n\n Answer:{ans} \n\n\n'.format(q=q,ans=ans))
    file.close()
write()



