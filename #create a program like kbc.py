#create a program like kbc

questions = [ ["which language was used to create fb?", "Python", "french", "Javascript", "Php", "None", 4],
            ["which language was used to create fb?", "Python", "french", "Javascript", "Php", "None", 3],
            ["which language was used to create fb?", "Python", "french", "Javascript", "Php", "None", 2],
            ["which language was used to create fb?", "Python", "french", "Javascript", "Php", "None", 2]
                ] 

levels = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000,
80000, 160000, 320000]
money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"a. {question[1]}       b. {question[2]} ")
    print(f"c. {question[3]}       d.{question[4]} ")
    reply = int(input("Enter your answer (1-4): "))
    
    if(reply == question[-1]):
        print(f"correct answer, you have won Rs.{levels[i]}")
        if(i == 2):
            money = 10000
        elif(i==3):
            money = 320000
    else:
        print("sorry Wrong answer")
        break

print(f"your take home money is: {money}")

