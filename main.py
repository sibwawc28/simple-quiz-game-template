questions=[
    "1", "2", "3", "4", "5"
]

options=[
    ['a', 'b', 'c', 'd'],
    ['a', 'b', 'c', 'd'],
    ['a', 'b', 'c', 'd'],
    ['a', 'b', 'c', 'd'],
    ['a', 'b', 'c', 'd']
]

answer=['a', 'c', 'b', 'a', 'd']


print("omg queen welcome to the grand quiz game ")
correct=0 

for i in range(len(questions)):

    print(f"question {i+1}")
    print(questions[i])

    print("the answer options are: ")
    for each in options[i]:
        print(each)

    choice=input("enter your answer ")

    if (choice.lower() == answer[i]) :
        print("omg congos queen. that was correct")
        correct=correct+1

    else:
        print("oopsie daisy. better luck next time")


print(f"you got {correct} questions correct")


