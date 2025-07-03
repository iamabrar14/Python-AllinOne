questions = [
    ["Who is the inventor of Facebook?", "Mark Zuckerberg", "Bill Gates",
     "Steve Jobs", "Elon Musk", 1],
    ["Which one is an OOP language?", "HTML", "CSS",
     "Python", "C", 3],
    ["Who won 2022 FIFA World Cup?", "Portugal", "Argentina",
     "France", "Germany", 2],
    ["Who is the inventor of Windows?", "Shakib Al Hasan", "Bill Gates",
     "Mustafa Zabbar", "Elon Musk", 2],
    ["Which animal is a pet animal?", "Tiger", "Lion",
     "Whale", "Cat", 4],
     ["Who won a noble prize from that following list", "Dr. Muhammad Younus", "Donald Trump",
     "Narendra Modi", "Benjamin Netaniahu", 1],
      ["Which language is used for developing Facebook?", "Bengali", "English",
     "PHP", "Assembly", 3],
       ["Who is a boxer among them", "Mohammad Ali", "Lionel Messi",
     "Undertaker", "Steve Smith", 1],
        ["Which Country is an Asian Country", "Russia", "Ukraine",
     "Mali", "Taiwan", 4],
         ["Who is a movie director among them", "Christopher Nolan", "Steve Jobs",
     "Tarek Zia", "Andre Onana", 1]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,640000]
money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\nQuestion for TK {levels[i]}")
    print(question[0])  
    print(f"a. {question[1]}          b. {question[2]}")
    print(f"c. {question[3]}          d. {question[4]}")
    reply = int(input("Enter your answer (1-4): "))
    
    if reply == question[-1]:
        print(f"✅ Correct Answer! You have won TK. {levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000
    else:
        print("❌ Wrong Answer!")
        break

print(f"\n🎉 You won total money: TK {money}")
