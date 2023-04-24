from tkinter import *
import random

root=Tk()

root.title("Luck friend Wheel")
root.geometry("500x500")



list1 = ["Flowers" , "Cars" , "Bags" , "Stationary" , "Sana"]
print(list1)

def random_number():
    random_no = random.randint(0, 4)
    print(random_no)
    random_lucky_friend = list1[random_no]
    print("your lucky friend is: " + random_lucky_friend)
    
btn1 = Button(root)
btn1 = Button(root, text="Who is your lucky Friend? ", command = random_number)
