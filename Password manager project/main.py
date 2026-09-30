

from tkinter import *
from tkinter import messagebox

import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password =[]

    import random
    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)
    password_list = [(random.sample(letters,nr_letters), random.sample(symbols,nr_symbols),random.sample(numbers,nr_numbers))
                     for letter in letters
                     for symbol in symbols
                     for number in numbers
                     ]

    password_letters=[random.choice(letters) for letter in range(nr_letters)]
    password_symbols=[random.choice(symbols) for symbol in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for number in range(nr_numbers)]

    #Buradaki olayı biz normalde 3 tane for döngüsüyle de yapabiliriz
    # ama list comprehentionı da kullanabililriz yukarıdaki gibi


    password_list=password_letters+password_symbols+password_numbers




    random.shuffle(password_list)

    #password = ''

    #for char in password_list:
        #password += char
    #bunun yerine de şu aşağıdaki joinli şeyi kullanabilirsin

    password = "".join(password_list)
    #bu joini ben listlerde ya da tuplelarda kullanabiliyoruz ikisinde de oluyor yani anlayacağın



    password_entry.insert(0,password)


    pyperclip.copy(password)





















# ---------------------------- SAVE PASSWORD ------------------------------- #









def save_data():

    web_info = website_entry.get()
    user_info = username_entry.get()
    pass_info = password_entry.get()
    new_data = {
        web_info:{
            "email":user_info,
            "password":pass_info,


        }
    }



    if len(web_info)==0 or len(user_info)==0 or len(pass_info)==0:
        messagebox.showinfo("Oops","Please fill all fields")

    else:

        try:
            read_data = open("data.json", "r")
            # reading old dataf
            data = json.load(read_data)
            # updating old data with new data
            data.update(new_data)

            # saving updated data
            write_data = open("data.json", "w")
            json.dump(data, write_data, indent=4)

        except :
            write_data = open("data.json", "w")
            json.dump(new_data, write_data, indent=4)
            #neyi dump etmek istiyorsan parantez içine önce o yazılıyor new_data mesela
            # sonra neyin içine istiyorsan onu yazıyorsun burada write_data


        website_entry.delete(first=0, last=END)
        password_entry.delete(first=0, last=END)





def search_data():




    try:
        with open("data.json", "r") as read_data:
            data = json.load(read_data)
            web_info = website_entry.get()


        if web_info in data:
                messagebox.showinfo("info ",f"Email:{data[web_info]["email"]} \n password:{data[web_info]["password"]}")

        else:
            messagebox.showinfo("Oops",f"No details for the website exists")




    except :
        messagebox.showinfo("Oops","No data file found")











# ---------------------------- UI SETUP ------------------------------- #


from operator import length_hint



window = Tk()



window.title("Password Generator")
window.geometry("500x400")
window.configure(background="white")
window.config(padx=20, pady=20)

canvas = Canvas(window, width=200, height=200, bg="white", highlightthickness=0)
#bu direkt canvas diye bir şey oluşturuyor onunla görsel ekleyip text oluşturuabiliyoruz içine


logo=PhotoImage(file="logo.png")
#bu bizim fotoğrafı tanımamızı sağlıyor farklı dosyadan


mypass=canvas.create_image(100, 100, image=logo)
#bu da PhotoImagede kaydettiğimiz logomuzu ekranda oluşturmak için kullanıyoruz


canvas.grid(column=1, row=1)
#bu da o oluştureduğumuz şeyi ekrana yazdırmamızı sağlar,


website_entry=Entry(window, width=20, bg="white", fg="black",insertbackground="black",highlightthickness=0)
website_entry.grid(column=1, row=1,columnspan=1)
website_entry.focus()
web_info=website_entry.get()
website_label=Label(window, text="Website:", bg="white", fg="black")
website_label.grid(column=0, row=2)
website_entry.grid(row=2, column=1)


username_label=Label(window, text="Email/Username:", bg="white", fg="black")
username_label.grid(column=0, row=3)
username_entry=Entry(window, width=35, bg="white", fg="black",insertbackground="black",highlightthickness=0)
user_info=username_entry.get()
username_entry.insert(0,"ahmet@gmail.com")
#insert sayesinde o entry içine bişey koyabiliyoruz o index başlaycağımız yeri söylüyoruz



username_entry.grid(column=1, row=3,columnspan=2)
username_info=username_entry.get()


password_label=Label(window, text="Password:", bg="white", fg="black")
password_label.grid(column=0, row=4)
password_entry=Entry(window, width=21, bg="white", fg="black",insertbackground="black",highlightthickness=0)

password_entry.grid(column=1, row=4)
pass_info=password_entry.get()
pyperclip.copy(pass_info)


password_button= Button(text="generate password",width=9,highlightthickness=0,bd=0,borderwidth=0,relief="flat",command=generate_password)
password_button.grid(column=2, row=4)

add_button=Button(text="Add",width=36,command=save_data)
add_button.grid(column=1, row=5,columnspan=2)


search_button=Button(text="Search",width=9 ,
                     highlightthickness=0,bd=0,borderwidth=0,relief="flat",command=search_data)
search_button.grid(column=2, row=2)


window.mainloop()