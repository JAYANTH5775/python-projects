quiz ={
    "question1":{
    "question":"what is the capital of karnataka",
    "answer":"bengalore"
},

"question2":{
    "question":"most popular political leader",
    "answer":"modi"
},
"question3":{
    "question":"what is the capital of INDIA",
    "answer":"delhi"
},
"question4":{
    "question":"what is the capital of INDIA",
    "answer":"delhi"
},
}

score = 0
for key,value in quiz.items():
    print(value['question'])
    answer = input("answer?")

    if answer.lower() == value['answer'].lower():
      print('correct')
      score =score+1
      print("your score is : "+str(score))

    else:
        print("wrong")
        print("the answeer is:"+value['answer'])
        print("your score is:"+str(score))
           
