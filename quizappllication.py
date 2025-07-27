print("******* QUIZ APPLICATION *********")
score = 0
correct_answers = 0
wrong_answers = 0
print("Qno 1: What is the capital of Ireland?")
ans_1 = input("Enter a - Dublin\nb - France\nc - Japan\nd - Uk\nAnswer is : ")
if(ans_1.lower() == "a"):
    score += 5
    correct_answers += 1
else:
    print("Wrong! Correct answer is a.\n")
    wrong_answers += 1

print("Qno 2: What is the largest planet in our Solar System?")
ans_2 = input("Enter a - Mars\nb - Jupiter\nc - Saturn\nd - Uranus\nAnswer is : ")
if(ans_2.lower() == "b"):
    score += 5
    correct_answers += 1
else:
    print("Wrong! Correct answer is b.\n")
    wrong_answers += 1

print("Qno 3: What is the smallest unit of matter? ")
ans_3 = input("Enter a - Molecules\nb - Substance\nc - Atom\nd - Element\nAnswer is : ")
if(ans_3.lower() == "c"):
    score += 5
    correct_answers += 1
else:
    print("Wrong! Correct answer is c\n")
    wrong_answers += 1

print("Qno 4: Who is the founder of Microsoft?")
ans_4= input("Enter a - Steve Jobs\nb - Elon Musk\nc - Mark Zuckerberg\nd - Bill Gates\nAnswer is : ")
if(ans_4.lower() == "d"):
    score += 5
    correct_answers += 1
else:
    print("Wrong! Correct answer is d.\n")
    wrong_answers += 1

print("Qno 5: What is the national animal of Pakistan?")
ans_5=input("Enter a - Markhor \nb - Lion\nc - Leopard\nd - Eagle \nAnswer is : ")
if(ans_5.lower() == "a"):
    score += 5
    correct_answers += 1
else:
    print("Wrong! Correct answer is a\n")
    wrong_answers += 1

print("Your Result : ")
print(f"Your final score is: {score}")
print(f"Your Right answer is: {correct_answers}")
print(f"Your Wrong answer is: {wrong_answers}")