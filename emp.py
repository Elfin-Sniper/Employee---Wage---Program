                                                                                  
import random

def atd():
        print("Welcome")
        attendance = random.choice([0,1])
        if (attendance == 1):
               print("Present")
        else:
                print("Absent")

if __name__ == "__main__":
        atd()
