student = {1: "Akash", 2: "Saurabh", 3: "Aman"}

def name(roll):
    if roll in student:
        print("Name:", student[roll])
    else:
        print("Roll number doesn't exist")