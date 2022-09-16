from tkinter import *
from tkinter import messagebox


def start_code():
    print('=========================================================')
    print('=   Добро пожаловать в программу накрутки подписчиков   =')
    print('=    Для удобного использование создан GUI интерфейс    =')
    print('=                    Удачной работы!                    =')
    print('=                                                       =')
    print('=                                                       =')
    print('=                Автор: Rustam Kenzhali                 =')
    print('=                Instagram: @Mr_Kenzhali                =')
    print('=               Начало проекта: 16.07.2022              =')
    print('=                                                       =')
    print('=                                                       =')
    print('=                 Прибыль проекта: 0 тг                 =')
    print('=========================================================')


def interface():
    # main information
    root = Tk()
    root['bg'] = '#E0FFFF'  # background color
    root.title('Instagram Bot')
    root.geometry('560x400+250+200')
    root.resizable(width=False, height=False)  # prohibition of resizing

    def link_checker(link):
        if link[0:5] == 'https' and link[-1] == '/':
            return 1
        else:
            return 0

    def submit():
        link = user_ent.get()
        correct_link = link_checker(link)
        print(correct_link)

        if agree.get() == 1 and len(user_ent.get()) != 0 and count.get() != '0' and correct_link:
            from browser_processing import start_brows_proces
            start_brows_proces(action.get(), user_ent.get(), count.get())
            root.quit()

        else:
            messagebox.showinfo('Eror', 'Check input DATA, and push AGREE')

    actions = ['Subscribe', 'Like', 'Save']
    action = StringVar()
    action.set('Subscribe')
    for i in range(3):
        lbl = Label(root, text=actions[i], width=24, padx=3, pady=2, bd=3, bg='#E0FFFF')
        action_rd_btn = Radiobutton(variable=action, value=actions[i], bg='#E0FFFF')
        lbl.grid(row=0, column=i)
        action_rd_btn.grid(row=1, column=i)

    empty_lbl = Label(root, bg='#E0FFFF')
    empty_lbl.grid(row=2, column=0, columnspan=3)

    user_lbl = Label(root, text='User Instagram Link:', bg='#E0FFFF')
    user_ent = Entry(root, width=55, bd=2)
    user_lbl.grid(row=3, column=0, pady=5)
    user_ent.grid(row=3, column=1, columnspan=2, pady=5)
    count_lbl = Label(root, text='Followers count(1-100):', bg='#E0FFFF')
    count = Spinbox(root, from_=0, to=100)
    count_lbl.grid(row=4, column=0)
    count.grid(row=4, column=1)

    empty_lbl_1 = Label(root, height=7, bg='#E0FFFF')
    empty_lbl_1.grid(row=6, column=0, columnspan=3)

    agree = IntVar()
    agree_chk_btn = Checkbutton(variable=agree, text='Agree', onvalue=1, bg='lightblue')
    agree_chk_btn.grid(row=8, column=0)

    submit = Button(root, text='Submit', command=submit)
    submit.grid(row=8, column=2)

    root.mainloop()


start_code()
interface()
