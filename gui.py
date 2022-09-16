from tkinter import *
from tkinter import messagebox
root = Tk()

root.geometry('240x280')
root.title('Example')

# top_frame = Frame(root).grid(row=0, column=0, columnspan=3)
# button_frame = Frame(root).grid(row=1, column=0, rowspan=2, columnspan=2)
# right_frame = Frame(root).grid(row=1,column=2, rowspan=2)
#
# text1 = Label(top_frame, bg='yellow', text='Hello world!')
# button1 = Button(button_frame, text='Button 1', fg='green', font=('Arial', 14))
# button2 = Button(button_frame, text='Button 2', fg='red', font=('Arial', 14))
# button3 = Button(button_frame, text='Button 3', fg='blue', font=('Arial', 14))
# button4 = Button(button_frame, text='Button 4', fg='black', font=('Arial', 14))
# text2 = Label(right_frame, bg='red', text='Good luck')
#
# text1.grid(row=0, column=0, columnspan=3)
# button1.grid(row=1, column=0)
# button2.grid(row=1, column=1)
# button3.grid(row=2, column=0)
# button4.grid(row=2, column=1)
# text2.grid(row=1, column=2, rowspan=2)

# def clicked():
#     display_text  = 'Hello ' + entry_text.get() + '. How are you?'
#     # print(f'Hello {display_text }! How are you?')
#     text1.config(text=display_text)
#
# text1 = Label(root, text='Enter your name here: ')
# entry_text = Entry(root)
# button = Button(root, text='Click me', command=clicked)
# text1.pack()
# entry_text.pack()
# button.pack()


# def clicked():
#     button1.config(bg='yellow', fg='blue', text='Ohh sheat')
#
# button1 = Button(root, text='Click me', command=clicked)
# button1.pack()

# def add():
#     print(info.config(text=f'Добро пожаловать {ent_name.get()} {ent_surname.get()}! Вы зарегистрированы'))
#
#
# name_frame = Frame(root)
# surname_frame = Frame(root)
# name_frame.pack()
# surname_frame.pack()
#
# Label(name_frame, text='Name:').pack(side='left')
# ent_name = Entry(name_frame)
# ent_name.pack(side='left')
# Label(surname_frame, text='Surname').pack(side='left')
# ent_surname = Entry(surname_frame)
# ent_surname.pack(side='left')
#
# Button(root, text='Submit', command=add).pack()
# info = Label(root)
# info.pack()


# def submit():
#     info_label = Label(root, text='Logged in')
#     info_label.grid(row=3, column=0, columnspan=3)
#     print(username_ent.get() + ' ' + password_ent.get())
#
#
# def clear():
#     username_ent.delete(0, 'end')
#     password_ent.delete(0, 'end')
#
#
# def close():
#     root.destroy()
#
#
# username_label = Label(root, text='Username:')
# username_ent = Entry(root)
# password_label = Label(root, text='Password:')
# password_ent = Entry(root)
# button_submit = Button(root, text='Submit', borderwidth=2, command=submit)
# button_clear = Button(root, text='Clear', borderwidth=2, command=clear)
# button_close = Button(root, text='Close', borderwidth=2, command=close)
#
#
# username_label.grid(row=0, column=0)
# username_ent.grid(row=0, column=1, columnspan=2)
#
# password_label.grid(row=1, column=0)
# password_ent.grid(row=1, column=1, columnspan=2)
#
# button_submit.grid(row=2, column=0, ipadx=15)
# button_clear.grid(row=2, column=1, ipadx=15)
# button_close.grid(row=2, column=2, ipadx=15)


# text1 = Label(root, text="0", width=10)
# button1 = Button(root, text="Counter", width= 10)
#
# text1.grid(row=0, column=0)
# button1.grid(row=1, column=0)
#
# count = 0
#
#
# def increase_value(event):
#     global count
#     count += 1
#     text1.config(text=str(count))
#
#
# def decrease_value(event):
#     global count
#     count -= 1
#     text1.config(text=str(count))
#
#
# def clear_value(event):
#     global count
#     count = 0
#     text1.config(text=str(count))
#
#
# button1.bind('<Button-1>', increase_value)
# button1.bind('<Button-2>', clear_value)
# button1.bind('<Button-3>', decrease_value)
#


# def enter_window(event):
#     lab1.config(text='Hello, there!', bg='Yellow')
#
#
# def leave_window(event):
#     lab1.config(text='Bye!', bg='Blue')
#
#
# lab1 = Label(root, text='')
# lab1.pack()
# root.bind('<Enter>', enter_window)
# root.bind('<Leave>', leave_window)
#


# def button_1(event):
#     lab1.config(bg='Yellow')
#
#
# def button_2(event):
#     lab1.config(bg='Blue')
#
#
# lab1 = Label(root, text='LOOOOOOOOOL', bg='Yellow')
# lab1.pack()
# root.bind('<Button-1>', button_1)
# root.bind('<Button-3>', button_2)


# def print_hello():
#     print("Hello World")
#
#
# menu_bar = Menu(root)
# root.config(menu=menu_bar)
# menu_bar.add_command(label='Hello', command=print_hello)
# menu_bar.add_command(label='Quit', command=root.quit)


# def print_hello():
#     print('Hello World')
#
#
# menu_bar = Menu(root)
# root.config(menu=menu_bar)
# file_menu = Menu(menu_bar)
# save_menu = Menu(file_menu)
#
# menu_bar.add_cascade(label='File', menu=file_menu)
# file_menu.add_command(label='New', command=print_hello)
# file_menu.add_command(label='Open', command=print_hello)
#
# file_menu.add_separator()
# file_menu.add_cascade(label='Save', menu=save_menu)
# save_menu.add_command(label="Save...")
# save_menu.add_command(label="Save as...")
#
# menu_bar.add_command(label='Close', command=root.quit)
#


# def popup(event):
#     popup_menu.post(event.x_root, event.y_root)
#
#
# popup_menu = Menu(root)
# popup_menu.add_command(label='Copy')
# popup_menu.add_command(label='Past')
#
# root.bind('<Button-3>', popup)
#


# def bg_yellow():
#     root.config(bg='Yellow')
#     author_info.config(bg='Yellow')
#
#
# def bg_red():
#     root.config(bg='Red')
#     author_info.config(bg='Red')
#
#
# def contuct_number():
#     author_info.config(text='+77073503030')
#
#
# def author_name():
#     author_info.config(text='Rustam Kenzhali')
#
# menu_bar = Menu(root)
# root.config(menu=menu_bar)
#
# file_menu = Menu(menu_bar)
# menu_bar.add_cascade(label='File', menu=file_menu)
# file_menu.add_command(label='Open')
# file_menu.add_command(label='Close')
# file_menu.add_separator()
# bg_change_menu = Menu(file_menu)
# file_menu.add_cascade(label='Change bg color', menu=bg_change_menu)
# bg_change_menu.add_command(label='Yellow', command=bg_yellow)
# bg_change_menu.add_command(label='Red', command=bg_red)
#
#
# edit_menu = Menu(menu_bar)
# menu_bar.add_cascade(label='Edit', menu=edit_menu)
#
#
# view_menu = Menu(menu_bar)
# menu_bar.add_cascade(label='View', menu=view_menu)
#
#
# help_menu = Menu(menu_bar)
# menu_bar.add_cascade(label='Help', menu=help_menu)
# help_menu.add_command(label='Contact number', command=contuct_number)
# help_menu.add_command(label='Author', command=author_name)
#
# author_info = Label(root)
# author_info.pack()
#

# cnv = Canvas(root)
# cnv.pack(fill=BOTH, expand=1)
# # cnv.create_rectangle(50, 50, 300, 200, fill='Red')
# cnv.create_oval(10, 20, 150, 200,fill='Blue', outline='Grey', width=5)
#


# def brush(event):
#     cnv.create_oval(event.x - 3, event.y - 3, event.x + 3, event.y + 3, fill='red', outline='red')
#
#
# cnv = Canvas(root)
# cnv.pack(fill=BOTH, expand=1)
# cnv.bind('<Button-1>', brush)
#


# scale = Scale(root, from_=10, to=20, orient=HORIZONTAL)
# spinbox = Spinbox(root, width=5, values=('One', 'Two', 'Three'))
# scale.pack()
# spinbox.pack()
#


# def confirm():
#     print(clr.get())
#     from tkinter import messagebox
#     if yes_no.get() == 1:
#
#         messagebox.showinfo("Hello", "You have chosen "+clr.get())
#     else:
#         messagebox.showinfo("No no", "Please put a tick")
#
#
# values = ['Red', 'Green', 'Blue', 'Yellow', 'Black']
# yes_no = IntVar()
# clr = StringVar()
# clr.set('Red')
#
# for i in range(5):
#     lbl = Label(root, text=values[i])
#     c = Radiobutton(variable=clr, value=values[i])
#     lbl.grid(row=i+1, column=0)
#     c.grid(row=i+1, column=1)
#
# yes_no_lbl = Label(root, text='Yes/No')
# yes_no_cbut = Checkbutton(variable=yes_no, onvalue=1)
# yes_no_lbl.grid(row=6, column=0)
# yes_no_cbut.grid(row=6, column=1)
#
# button = Button(root, text='Confirm', command=confirm)
# button.grid(row=7, column=0, columnspan=2)
#


# def create_rectangle_in_xy_possition(event):
#     cnv.create_rectangle(event.x, event.y, event.x+100, event.y+150)
#
#
# cnv = Canvas(root)
# cnv.pack(fill=BOTH, expand=1)
#
# root.bind('<Button-1>', create_rectangle_in_xy_possition)


# def submit():
#     if agree.get() == 1:
#         print('Hello ' + ent_name.get(), ent_surname.get() + '. Info about you: ' + gender.get(), math.get(),
#               phisic.get(), pe.get(), chemistry.get())
#     else:
#         from tkinter import messagebox
#         messagebox.showinfo("No no", "Please put a tick")
#
#
# name = Label(root, text='Name:')
# ent_name = Entry(root)
# surname = Label(root, text='Surname:')
# ent_surname = Entry(root)
# day_spinpox = Spinbox(root, from_=0, to=31, width=3)
# month_spinpox = Spinbox(root, from_=0, to=12, width=3)
# year_spinpox = Spinbox(root, from_=1990, to=2022, width=5)
# genders = ['Men', 'Women']
#
# name.grid(row=0, column=0)
# ent_name.grid(row=0, column=1)
# surname.grid(row=1, column=0)
# ent_surname.grid(row=1, column=1)
# # day_spinpox.grid(row=0, column=2)
# # month_spinpox.grid(row=1, column=2)
# # year_spinpox.grid(row=2, column=2)
#
# gender = StringVar()
# gender.set('Men')
# for i in range(2):
#     lbl = Label(root, text=genders[i])
#     gender_rd_btn = Radiobutton(variable=gender, value=genders[i])
#     lbl.grid(row=i, column=3)
#     gender_rd_btn.grid(row=i, column=4)
#
# math = StringVar()
# math_chk_btn = Checkbutton(variable=math, text='Math', onvalue='Math', offvalue='')
# math_chk_btn.deselect()
#
# phisic = StringVar()
# phisic_chk_btn = Checkbutton(variable=phisic, text='Physics', onvalue='Physics', offvalue='')
# phisic_chk_btn.deselect()
#
# pe = StringVar()
# pe_chk_btn = Checkbutton(variable=pe, text='P.E.', onvalue='P.E.', offvalue='')
# pe_chk_btn.deselect()
#
# chemistry = StringVar()
# chemistry_chk_btn = Checkbutton(variable=chemistry, text='chemistry', onvalue='chemistry', offvalue='')
# chemistry_chk_btn.deselect()
#
# math_chk_btn.grid(row=2, column=0)
# phisic_chk_btn.grid(row=2, column=1)
# pe_chk_btn.grid(row=3, column=0)
# chemistry_chk_btn.grid(row=3, column=1)
#
# agree = IntVar()
# agree_chk_btn = Checkbutton(variable=agree, text='Agree', onvalue=1)
# agree_chk_btn.grid(row=5, column=0)
#
# submit = Button(text='Submit', command=submit)
# submit.grid(row=5, column=4)
#
#
#
#
#

# ******************************************


# color = (0, 'Red')
#
#
# def choose_color():
#     global color
#     from tkinter import colorchooser
#     color = colorchooser.askcolor('Red')
#
#
# shape = 'R'
#
#
# def choose_rectangle():
#     global shape
#     shape = 'R'
#
#
# def choose_oval():
#     global shape
#     shape = 'O'
#
#
# def choose_line():
#     global shape
#     shape = 'L'
#
#
# def draw_shape(event):
#     global shape
#     w = width_scale.get()
#     h = height_scale.get()
#     xy = event.x - w/2, event.y - h/2, event.x + w/2, event.y + h/2
#     if shape == 'R':
#         cnv.create_rectangle(xy, fill=color[1])
#     elif shape == 'O':
#         cnv.create_oval(xy, fill=color[1])
#     elif shape == 'L':
#         cnv.create_line(xy, fill=color[1])
#
#
# def paint(event):
#     width_scale.set(height_scale.get())
#     h = height_scale.get()
#     xy = event.x - h / 2, event.y - h / 2, event.x + h / 2, event.y + h / 2
#     cnv.create_oval(xy, fill=color[1], width=0)
#
#
# def clear_art():
#     cnv.delete('all')
#
#
# toolbarPane = Frame(root)
# canvasPane = Frame(root, relief=RAISED, bd=3, cursor='cross')
# toolbarPane.pack(side='left')
# canvasPane.pack()
#
# cnv = Canvas(canvasPane, width=500, height=600)
# cnv.pack()
#
# rec_button = Button(toolbarPane, text='Rectangle', width=15, command=choose_rectangle)
# oval_button = Button(toolbarPane, text='Oval', width=15, command=choose_oval)
# line_button = Button(toolbarPane, text='Line', width=15, command=choose_line)
# color_button = Button(toolbarPane, text='Color', width=15, command=choose_color)
# height_lbl = Label(toolbarPane, text='Height')
# height_scale = Scale(toolbarPane, from_=0, to=300, orient=HORIZONTAL)
# width_lbl = Label(toolbarPane, text='Width')
# width_scale = Scale(toolbarPane, from_=0, to=300, orient=HORIZONTAL)
# clear_btn = Button(toolbarPane, text='Clear art', width=15, command=clear_art)
#
# rec_button.pack()
# oval_button.pack()
# line_button.pack()
# color_button.pack()
# height_lbl.pack()
# height_scale.pack()
# width_lbl.pack()
# width_scale.pack()
# clear_btn.pack()
#
# cnv.bind('<Button-1>', draw_shape)
# cnv.bind('<B3-Motion>', paint)
#
#
#


# import datetime
# from PIL import Image, ImageTk    # photo library
#
#
# class Person:
#     def __init__(self, name, birthdate):
#         self.name = name
#         self.birthdate = birthdate
#
#     def age(self):
#         today = datetime.date.today()
#         age = today.year - self.birthdate.year
#         month = today.month - self.birthdate.month
#         day = today.day - self.birthdate.day
#         return age, month, day
#
#
# def get_input():
#     person_name = name_ent.get()
#
#     monkey = Person(person_name, datetime.date(int(year_ent.get()), int(month_ent.get()), int(date_ent.get())))
#
#     text_area = Text(master=root, height=5, width=15)
#     text_area.grid(row=6, column=1)
#
#     ans_year, ans_month, ans_day = monkey.age()
#     answer = f'Hey {person_name}!!!. You are {ans_year} years, {ans_month} month, {ans_day} day old!!!'
#
#     text_area.insert(END,answer)
#
#
# image = Image.open('tree-736885__480.jpg')
# image.thumbnail((420, 280))
# photo = ImageTk.PhotoImage(image)
# label_img = Label(root, image=photo)
# label_img.grid(row=0, column=1)
#
# name = Label(root, text='Name')
# name.grid(row=1, column=0)
# name_ent = Entry(root)
# name_ent.grid(row=1, column=1)
#
# year = Label(root, text='Year')
# year.grid(row=2, column=0)
# year_ent = Entry(root)
# year_ent.grid(row=2, column=1)
#
# month = Label(root, text='month')
# month.grid(row=3, column=0)
# month_ent = Entry(root)
# month_ent.grid(row=3, column=1)
#
# date = Label(root, text='Day')
# date.grid(row=4, column=0)
# date_ent = Entry(root)
# date_ent.grid(row=4, column=1)
#
# button = Button(root, text='Calculate Age', command=get_input, bg='Pink')
# button.grid(row=5, column=1)
#
#
#
# ********************************************


# import random
#
# user_score = 0
# user_choice = ''
# comp_score = 0
# comp_choice = ''
#
#
# def choice_to_number(choice):
#     rps = {'rock': 1, 'paper': 2, 'scissor': 3}
#     return rps[choice]
#
#
# def number_to_choice(number):
#     rps = {1: 'rock', 2: 'paper', 3: 'scissor'}
#     return rps[number]
#
#
# def random_computer_choice():
#     return random.choice(['rock', 'paper', 'scissor'])
#
#
# def result(human_choice, camp_choice):
#     global user_score
#     global comp_score
#
#     user = choice_to_number(human_choice)
#     comp = choice_to_number(camp_choice)
#
#     if user == comp:
#         print('Tie')
#     elif (user - comp) % 3 == 1:
#         print('You win')
#         user_score += 1
#     else:
#         print('Computer win')
#         comp_score += 1
#
#     answer = f'Your choice {user_choice} \n' \
#              f'Computer choice {camp_choice} \n' \
#              f'Your score: {user_score} \n' \
#              f'Computer score: {comp_score} \n'
#
#     text_area.delete('1.0', END)
#     text_area.insert(END, answer)
#
#
# def rock():
#     global user_choice
#     global comp_choice
#
#     user_choice = 'rock'
#     comp_choice = random_computer_choice()
#
#     result(user_choice, comp_choice)
#
#
# def paper():
#     global user_choice
#     global comp_choice
#
#     user_choice = 'paper'
#     comp_choice = random_computer_choice()
#
#     result(user_choice, comp_choice)
#
#
# def scissor():
#     global user_choice
#     global comp_choice
#
#     user_choice = 'scissor'
#     comp_choice = random_computer_choice()
#
#     result(user_choice, comp_choice)
#
#
# menu_bar = Menu(root)
# root.config(menu=menu_bar)
#
# menu_bar.add_command(label='Close', command=root.quit)
#
#
# rock_btn = Button(root, text='Rock', bg='skyblue', command=rock)
# paper_btn = Button(root, text='Paper', bg='pink', command=paper)
# scissor_btn = Button(root, text='Scissor', bg='lightgreen', command=scissor)
#
# rock_btn.grid(row=1, column=0)
# paper_btn.grid(row=2, column=0)
# scissor_btn.grid(row=3, column=0)
#
# text_area = Text(master=root, height=5, width=30, bg='#FFFF99')
# text_area.grid(row=4, column=0)
#
#
#
# ********************************************


# CALCULATOR
# def make_digit_button(digit):
#     return Button(root, text=digit, bd=3, font=('Arial', 13), command=lambda: add_digit(digit))
#
#
# def make_operation_button(operation):
#     return Button(root, text=operation, bd=3, fg='Red', font=('Arial', 13), command=lambda: add_operation(operation))
#
#
# def make_calc_button(operation):
#     return Button(root, text=operation, bd=3, font=('Arial', 13), command=calculate)
#
#
# def make_clear_button(operation):
#     return Button(root, text=operation, bd=3, font=('Arial', 13), command=clear)
#
#
# def add_digit(digit):
#     value = calc.get()
#     if value[0] == '0' and len(value) == 1:
#         value = value[1:]
#     calc['state'] = NORMAL
#     calc.delete(0, END)
#     calc.insert(0, value+digit)
#     calc['state'] = DISABLED
#
#
# def add_operation(operation):
#     value = calc.get()
#     if value[-1] in '+-*/':
#         value = value[:-1]
#     elif '+' in value or '-' in value or '*' in value or '/' in value:
#         calculate()
#         value = calc.get()
#     calc['state'] = NORMAL
#     calc.delete(0, END)
#     calc.insert(0, value+operation)
#     calc['state'] = DISABLED
#
#
# def calculate():
#     value = calc.get()
#     if value[-1] in '+-*/':
#         value = value + value[:-1]
#     calc['state'] = NORMAL
#     calc.delete(0, END)
#     try:
#         calc.insert(0, eval(value))
#         calc['state'] = DISABLED
#     except ZeroDivisionError:
#         messagebox.showinfo('Внимание', 'На 0 делить нельзя!!!')
#         calc.insert(0, '0')
#         calc['state'] = DISABLED
#
#
#
# def clear():
#     calc['state'] = NORMAL
#     calc.delete(0, END)
#     calc.insert(0, '0')
#     calc['state'] = DISABLED
#
#
# def press_key(event):
#
#     if event.char.isdigit():
#         calc['state'] = NORMAL
#         add_digit(event.char)
#         calc['state'] = DISABLED
#     elif event.char in '+-*/':
#         calc['state'] = NORMAL
#         add_operation(event.char)
#         calc['state'] = DISABLED
#     elif event.char == '\r':
#         calc['state'] = NORMAL
#         calculate()
#         calc['state'] = DISABLED
#     elif event.char == '\x08':
#         calc['state'] = NORMAL
#         calc.delete(len(calc.get())-1, END)
#         calc['state'] = DISABLED
#
#
# root.config(bg='lightblue')
# calc = Entry(root, justify=RIGHT, font=('Arial', 13), width=20)
# calc.insert(0, '0')
# calc['state'] = DISABLED
# calc.grid(row=0, column=0, columnspan=4, padx=3, pady=7, sticky='we')
#
# root.bind('<Key>', press_key)
#
# # Put button on the screen
# make_digit_button('1').grid(row=1, column=0, sticky='wens', padx=2, pady=2)
# make_digit_button('2').grid(row=1, column=1, sticky='wens', padx=2, pady=2)
# make_digit_button('3').grid(row=1, column=2, sticky='wens', padx=2, pady=2)
# make_digit_button('4').grid(row=2, column=0, sticky='wens', padx=2, pady=2)
# make_digit_button('5').grid(row=2, column=1, sticky='wens', padx=2, pady=2)
# make_digit_button('6').grid(row=2, column=2, sticky='wens', padx=2, pady=2)
# make_digit_button('7').grid(row=3, column=0, sticky='wens', padx=2, pady=2)
# make_digit_button('8').grid(row=3, column=1, sticky='wens', padx=2, pady=2)
# make_digit_button('9').grid(row=3, column=2, sticky='wens', padx=2, pady=2)
# make_digit_button('0').grid(row=4, column=1, sticky='wens', padx=2, pady=2)
#
# make_operation_button('+').grid(row=1, column=3, sticky='wens', padx=1, pady=1)
# make_operation_button('-').grid(row=2, column=3, sticky='wens', padx=1, pady=1)
# make_operation_button('/').grid(row=3, column=3, sticky='wens', padx=1, pady=1)
# make_operation_button('*').grid(row=4, column=3, sticky='wens', padx=1, pady=1)
#
# make_calc_button('=').grid(row=4, column=2, sticky='wens', padx=1, pady=1)
#
# make_clear_button('C').grid(row=4, column=0, sticky='wens', padx=1, pady=1)
#
# root.grid_rowconfigure(1, minsize=60)
# root.grid_rowconfigure(2, minsize=60)
# root.grid_rowconfigure(3, minsize=60)
# root.grid_rowconfigure(4, minsize=60)
#
# root.grid_columnconfigure(0, minsize=60)
# root.grid_columnconfigure(1, minsize=60)
# root.grid_columnconfigure(2, minsize=60)
# root.grid_columnconfigure(3, minsize=60)
#
# *****************************************



mainloop()
