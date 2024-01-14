
quiz={
    "question1":{
        "question":"What is the capital of France?",
        "answer":"Paris"
    },
    "question2":{
        "question":"What is the capital of Germany?",
        "answer":"Berlin"
    },
    "question3":{
        "question":"What is the capital of Nepal?",
        "answer":"Kathmandu"
    },
    "question4":{
        "question":"What is the capital of Spain?",
        "answer":"Madrid"
    },
    "question5":{
        "question":"What is the capital of Portugal?",
        "answer":"Lisbon"
    },
    "question6":{
        "question":"What is the capital of Italy?",
        "answer":"Rome"
    },
    "question7":{
        "question":"What is the capital of Austria?",
        "answer":"Vienna"
    },
}

score =0
for key,values in quiz.items():
    print(values('question'))
    answer=input("Answer?")

    if answer.lower()==values['answer'].lower():
        print("Correct")
        score=score+1
        print("Your score sis: "+str(score))
    else:
        print("Wrong")    
        print("The answer is: " + values['answer'])