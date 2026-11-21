questions = [
    ["Which is the capital of India?", "Mumbai", "New Delhi", "Pune", "Chennai", 2],

    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],

    ["What is the chemical symbol of Gold?", "Ag", "Au", "Fe", "Cu", 2],

    ["Who invented the telephone?", "Thomas Edison", "Alexander Graham Bell", "Newton", "Einstein", 2],

    ["What is 12 * 8?", "86", "92", "96", "108", 3],

    ["Which language is used for web development?", "HTML", "All of these", "CSS", "JavaScript", 2],

    ["How many continents are there?", "5", "6", "7", "8", 3],

    ["Which is the largest ocean in the world?", "Atlantic", "Indian", "Arctic", "Pacific", 4],

    ["What is the brain of a computer?", "RAM", "CPU", "Hard Disk", "Monitor", 2],

    ["Which data structure follows FIFO?", "Stack", "Tree", "Queue", "Graph", 3],

    ["What is the square root of 144?", "10", "11", "12", "14", 3],

    ["Which gas do plants absorb during photosynthesis?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", 3],

    ["Which company developed Python?", "Microsoft", "Python Software Foundation", "Google", "Apple", 2],

    ["What does SQL stand for?", "Structured Query Language", "Simple Question Language", "Sequential Query Logic", "System Query Language", 1],

    ["Which keyword is used to define a function in Python?", "function", "fun", "define", "def", 4]
]

points=0
for i in range(len(questions)):
    print(f"Question {i+1}: {questions[i][0]}")
    print(f"1. {questions[i][1]}")
    print(f"2. {questions[i][2]}")
    print(f"3. {questions[i][3]}")
    print(f"4. {questions[i][4]}")
    answer=int(input("Enter your answer (1-4):"))
    if answer==questions[i][5]:
        points+=1
        print("Correct answer!")
    else:
        print("Incorrect answer!")
    print("-"*50)
score_percentage=(points/len(questions))*100

print("Total correct answers: ",points)
print("Percentage score: ",score_percentage,"%")
if score_percentage>=80:
    print("Excellent! You scored ",score_percentage,"%")
elif score_percentage>=60 and score_percentage<80:
    print("Good! You scored ",score_percentage,"%")
else:
    print("Keep practicing! You scored ",score_percentage,"%")