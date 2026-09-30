import tkinter
from copyreg import constructor

from tkinter import *




# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
window= Tk()
timer=None

# ---------------------------- TIMER RESET ------------------------------- #



canvas=Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="img.png")



canvas.create_image(102, 112, image=tomato_img)

timer_text=canvas.create_text(102,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))

canvas.grid(row=1,column=1)

def reset_timer():
    global reps
    window.after_cancel(timer)
    reps=0
    tick_label.config(text="")
    timer_label.config(text="Timer",font=(FONT_NAME,35,"bold"), fg=GREEN, bg=YELLOW)

    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps+=1

    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps%8==0:
        count_down(long_break_sec)

        timer_label.config(text="Break", font=(FONT_NAME, 35, "bold"), fg=RED, bg=YELLOW)

    if reps%2==0:
        count_down(short_break_sec)

        timer_label.config(text="Break", font=(FONT_NAME, 35, "bold"), fg=PINK, bg=YELLOW)
    else:
        count_down(work_sec)


        timer_label.config(text="Work", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #













    # ---------------------------- UI SETUP ------------------------------- #


window.title("Pomodoro")
window.configure(background=YELLOW)
window.config(padx=100, pady=50)

#
# def say_somthing(a,b,c):
#     print(a)
#     print(b)
#     print(c)
#
# window.after(1000,say_somthing,"hello","hi","why")

# bak fonkun içine istediğin kadar şey ekleyebiliyorsun ama en başta
# define ederken o şeyleri yazacan mesela yukarıdaki gibi





#bu yukarıdaki class bir dosyayı okumanın ve belirli bir
# dosya konumundaki belirli bir görüntüyü ele geçirmenin bir yoludur





def count_down(count):
    global timer

    if count>0:
        min=count//60
        count_sec=count%60
        if count_sec<10:
            count_sec=f"0{count_sec}"


        if min==25:
            count_sec="00"

        if min==20:
            count_sec="00"


        if min==5:
            count_sec="00"

        #pythonun farkındasysan bir değişkeni başka bir type değiştirmeni
            # sağlayabiliyor mesel count_sec son 10 saniye string oluyor
        timer=window.after(1000,count_down,count-1)

        canvas.itemconfig(timer_text, text=f"{min}:{count_sec}")

    else:
        start_timer()

        marks=""
        work_section=int(reps/2)
        for i in range(work_section):
            marks+="✓"
        tick_label.config(text=marks)










timer_label=Label(text="Timer",font=(FONT_NAME,35,"bold"),fg=GREEN,bg=YELLOW)
timer_label.grid(row=0,column=1)



tick_label=Label(text="",font=FONT_NAME,fg=GREEN,bg=YELLOW)
tick_label.grid(row=3,column=1)







start_button=Button(text="Start",command=start_timer,highlightthickness=0)
start_button.grid(row=2,column=0)








reset_button=Button(text="Reset",command=reset_timer,highlightthickness=0)
reset_button.grid(row=2,column=2)

window.mainloop()