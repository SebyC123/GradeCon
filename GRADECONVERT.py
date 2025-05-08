tyq = input("Enter A to convert a letter grade to %, Enter 00 to conver % to letter grade: ")
if tyq == "A":
    userlg = input("What grade did you get: ")
    if userlg == "F":
        print("you got 0-49% that means you FAIL")
        input("Press Enter to close the program...")
    elif userlg == "D":
        print("you got 50-54% that is a realy bad mark")
        input("Press Enter to close the program...")
    elif userlg == "D+":
        print("you got 57-59% that is a realy bad mark")
        input("Press Enter to close the program...")
    elif userlg == "C-":
        print("you got 60-62% that is a bad mark")
        input("Press Enter to close the program...")
    elif userlg == "C":
        print("you got 63-66% that is not a good mark")
        input("Press Enter to close the program...")
    elif userlg == "C+":
        print("you got 67-69% that is close to the ontario provincial standerd mark")
        input("Press Enter to close the program...")
    elif userlg == "B-":
        print("you got 70-72% that is the normal mark in ontario but its not the best but not the worst")
        input("Press Enter to close the program...")
    elif userlg == "B":
        print("you got 73-76% that is a tiny bit over the normal mark in ontario but its not the best but not the worst")
        input("Press Enter to close the program...")
    elif userlg == "B+":
        print("you got 77-79% that is almost a good mark and you are almost in a good mark zone!")
        input("Press Enter to close the program...")
    elif userlg == "A-":
        print("you got 80-84% that is a good mark!")
        input("Press Enter to close the program...")
    elif userlg == "A":
        print("you got 85-89% that is a GREAT mark!")
        input("Press Enter to close the program...")
    elif userlg == "A+":
        print("you got 90-100% this is the best MARK! Good Job!!!")
        input("Press Enter to close the program...")
    else:
        print("ERRORRRRRRRR")
        input("press enter to close the program and next time enter a valid mark with capatials!...")
elif tyq =="00":
    percent = input("What grade did you get: ")
    usernumg = float(percent)
    if usernumg <= 49:
        print("you got an F")
        input("Press Enter to close the program...")
    elif 50 <= usernumg <= 54:
        print("you got a D")
        input("Press Enter to close the program")
    elif 57 <= usernumg <= 59:
        print("you got a D+")
        input("Press Enter to close the program")
    elif 60 <= usernumg <= 62:
        print("you got a C-")
        input("Press Enter to close the program")
    elif 63 <= usernumg <= 66:
        print("you got a C")
        input("Press Enter to close the program")
    elif 67 <= usernumg <= 69:
        print("you got a C+")
        input("Press Enter to close the program")
    elif 70 <= usernumg >= 72:
        print("you got a B-")
        input("Press Enter to close the program")
    elif 73 <= usernumg <= 76:
        print("you got a B")
        input("Press Enter to close the program")
    elif 77 <= usernumg <= 79:
        print("you got a B+")
        input("Press Enter to close the program")
    elif 80 <= usernumg <= 84:
        print("you got a A-")
        input("Press Enter to close the program")
    elif 85 <= usernumg <= 89:
        print("you got a A")
        input("Press Enter to close the program")
    elif 90 <= usernumg <= 100:
        print("you got a A+")
        input("Press Enter to close the program")
    else:
        print("ERROR")
        print("invalid input")
        input("Press Enter to close the program")
