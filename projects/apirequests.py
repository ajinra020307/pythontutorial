import requests
import random
import os

url='https://opentdb.com/api.php?amount=10&type=multiple'
originaldata={}
choicearray=[]
userchoice=[]
def getUsers(url):
    print('......loading')
    response=requests.get(url=url)
    data=response.json()
    originaldata=data['results']
    return data['results']

originaldata=getUsers(url)

def ask(data,choicearray):
    
    for index in range(len(data)):
        q='''
         Question.no:{qno}\n
         Category:{category}\n
         question:{question}\n
         choices \n
         1.{one}\n
         2.{two}\n
         3.{three}\n
         4.{four}>>\n
        '''
        answerarray=[]
        correct_answer=data[index]['correct_answer']
        answerarray.append(data[index]['correct_answer'])
        for a in data[index]['incorrect_answers']:
            answerarray.append(a)
        correctchoice=0
    
        one=answerarray[random.randint(0,len(answerarray)-1)]
        answerarray.remove(one)
        if one==correct_answer:
            correctchoice=1
        two=answerarray[random.randint(0,len(answerarray)-1)]
        answerarray.remove(two)
        if two==correct_answer:
            correctchoice=2
        three=answerarray[random.randint(0,len(answerarray)-1)]
        answerarray.remove(three)
        if three==correct_answer:
            correctchoice=3
        four=answerarray[0]
        answerarray.remove(four)
        if four==correct_answer:
            correctchoice=4
        choicearray.append(correctchoice)
        os.system('cls')
        print(q.format(qno=index+1,question=data[index]['question'],category=data[index]['category'],one=one,two=two,three=three,four=four))

        answer=int(input(' '))
        userchoice.append(answer)
        


ask(originaldata,choicearray)
userscore=0

for num in range(len(choicearray)):
  if(choicearray[num]==userchoice[num]):
      userscore+=1

print('You have answered {score} questions correctly'.format(score=userscore))