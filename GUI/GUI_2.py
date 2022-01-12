from tkinter import *
from functools import partial
from res.questions_basa import *
from res.question_answer import *
from res.email_post import *
from random import randint
from time import time
from tkinter import ttk


class GUI_2:
    def __init__(self):
        self.rand_1 = randint(1, 3)
        self.rand_2 = randint(1, 3)
        self.rand_3 = randint(1, 3)
        self.rand_4 = randint(1, 3)
        self.rand_5 = randint(1, 3)
        self.rand_6 = randint(1, 3)

        self.list_param = [self.rand_1, self.rand_2, self.rand_3, self.rand_4, self.rand_5, self.rand_6]

        self.ques_1 = question_1(self.list_param[0])
        self.ques_2 = question_2(self.list_param[1])
        self.ques_3 = question_3(self.list_param[2])
        self.ques_4 = question_4(self.list_param[3])
        self.ques_5 = question_5(self.list_param[4])
        self.ques_6 = question_6(self.list_param[5])

        self.list_ques = [self.ques_1, self.ques_2, self.ques_3, self.ques_4, self.ques_5, self.ques_6]

        self.FIO_txt = ""

    def window_start(self):
        def click(window):
            self.FIO_txt = txt.get()
            window.destroy()
        window = Tk()

        window.title('Тест')
        window.geometry("400x250")

        lbl = Label(window, text="Введите свою ФИО и номер группы на английском языке" + "\n"
                                                                                         "|" + "\n"
                                                                                               "|" + "\n"
                                                                                                     "V")
        lbl.pack(side=TOP)

        txt = Entry(window, width=25)
        txt.pack(side=TOP)
        txt.focus()

        button = Button(window, text="Начать тест!", command=partial(click, window))
        button.pack(side=TOP)

        window.mainloop()

    def test_window(self):
        def click_chek(start_time):
            list_text = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get()]

            ball = 0

            ball += int(answer_1(int(self.list_param[0]), str(list_text[0])))
            ball += int(answer_2(int(self.list_param[1]), str(list_text[1])))
            ball += int(answer_3(int(self.list_param[2]), str(list_text[2])))
            ball += int(answer_4(int(self.list_param[3]), str(list_text[3])))
            ball += int(answer_5(int(self.list_param[4]), str(list_text[4])))
            ball += int(answer_6(int(self.list_param[5]), str(list_text[5])))

            end_time = int((time() - start_time))
            sec = int(end_time)
            min = int(end_time / 60)
            hour = int(end_time / 60 / 60)

            mail_send = ("Student: " + str(self.FIO_txt) + "\n" +
                         "Time: " + str(hour) + ":" + str(min) + ":" + str(sec) + "\n" +
                         "Mark: " + str(ball))
            send_mail(mail_send)

            window_now.destroy()

        window_now = Tk()

        start_time = time()

        window_now.title('Тест идет!')
        window_now.geometry("400x250")

        notebook = ttk.Notebook(window_now)
        notebook.pack(fill='both', expand='yes')

        frame1 = ttk.Frame(notebook)
        frame1.pack(fill='both', expand='yes')
        frame2 = ttk.Frame(notebook)
        frame2.pack(fill='both', expand='yes')
        frame3 = ttk.Frame(notebook)
        frame3.pack(fill='both', expand='yes')
        frame4 = ttk.Frame(notebook)
        frame4.pack(fill='both', expand='yes')
        frame5 = ttk.Frame(notebook)
        frame5.pack(fill='both', expand='yes')
        frame6 = ttk.Frame(notebook)
        frame6.pack(fill='both', expand='yes')
        frame7 = ttk.Frame(notebook)
        frame7.pack(fill='both', expand='yes')

        lbl1 = Label(frame1, text=self.ques_1)
        lbl1.grid(column=0, row=0)
        lbl2 = Label(frame2, text=self.ques_2)
        lbl2.grid(column=0, row=0)
        lbl3 = Label(frame3, text=self.ques_3)
        lbl3.grid(column=0, row=0)
        lbl4 = Label(frame4, text=self.ques_4)
        lbl4.grid(column=0, row=0)
        lbl5 = Label(frame5, text=self.ques_5)
        lbl5.grid(column=0, row=0)
        lbl6 = Label(frame6, text=self.ques_6)
        lbl6.grid(column=0, row=0)

        button1 = Button(frame7, text="Проверить!", command=partial(click_chek, start_time))
        button1.grid(column=0, row=6)

        notebook.add(frame1, text='1')

        var1 = StringVar()
        var1.set("None")
        radio_1 = Radiobutton(frame1, text="1", variable=var1, value="1")
        radio_2 = Radiobutton(frame1, text="2", variable=var1, value="2")
        radio_3 = Radiobutton(frame1, text="3", variable=var1, value="3")
        radio_4 = Radiobutton(frame1, text="4", variable=var1, value="4")

        arr_column_1 = [0, 1, 2, 3]
        length = len(arr_column_1)
        for i in range(0, length):
            rnd = randint(0, length - 1)
            temp = arr_column_1[i]
            arr_column_1[i] = arr_column_1[rnd]
            arr_column_1[rnd] = temp

        radio_1.grid(column=arr_column_1[0], row=1)
        radio_2.grid(column=arr_column_1[1], row=1)
        radio_3.grid(column=arr_column_1[2], row=1)
        radio_4.grid(column=arr_column_1[3], row=1)

        notebook.add(frame2, text='2')

        var2 = StringVar()
        var2.set("None")

        radio_1 = Radiobutton(frame2, text="4", variable=var2, value="4")
        radio_2 = Radiobutton(frame2, text="5", variable=var2, value="5")
        radio_3 = Radiobutton(frame2, text="6", variable=var2, value="6")
        radio_4 = Radiobutton(frame2, text="7", variable=var2, value="7")

        arr_column_2 = [0, 1, 2, 3]
        length = len(arr_column_2)
        for i in range(0, length):
            rnd = randint(0, length - 1)
            temp = arr_column_2[i]
            arr_column_2[i] = arr_column_2[rnd]
            arr_column_2[rnd] = temp

        radio_1.grid(column=arr_column_2[0], row=1)
        radio_2.grid(column=arr_column_2[1], row=1)
        radio_3.grid(column=arr_column_2[2], row=1)
        radio_4.grid(column=arr_column_2[3], row=1)

        notebook.add(frame3, text='3')

        var3 = StringVar()
        var3.set("None")

        radio_1 = Radiobutton(frame3, text="7", variable=var3, value="7")
        radio_2 = Radiobutton(frame3, text="8", variable=var3, value="8")
        radio_3 = Radiobutton(frame3, text="9", variable=var3, value="9")
        radio_4 = Radiobutton(frame3, text="10", variable=var3, value="10")

        arr_column_3 = [0, 1, 2, 3]
        length = len(arr_column_3)
        for i in range(0, length):
            rnd = randint(0, length - 1)
            temp = arr_column_3[i]
            arr_column_3[i] = arr_column_3[rnd]
            arr_column_3[rnd] = temp

        radio_1.grid(column=arr_column_3[0], row=1)
        radio_2.grid(column=arr_column_3[1], row=1)
        radio_3.grid(column=arr_column_3[2], row=1)
        radio_4.grid(column=arr_column_3[3], row=1)

        notebook.add(frame4, text='4')

        var4 = StringVar()
        var4.set("None")

        radio_1 = Radiobutton(frame4, text="10", variable=var4, value="10")
        radio_2 = Radiobutton(frame4, text="11", variable=var4, value="11")
        radio_3 = Radiobutton(frame4, text="12", variable=var4, value="12")
        radio_4 = Radiobutton(frame4, text="13", variable=var4, value="13")

        arr_column_4 = [0, 1, 2, 3]
        length = len(arr_column_4)
        for i in range(0, length):
            rnd = randint(0, length - 1)
            temp = arr_column_4[i]
            arr_column_4[i] = arr_column_4[rnd]
            arr_column_4[rnd] = temp

        radio_1.grid(column=arr_column_4[0], row=1)
        radio_2.grid(column=arr_column_4[1], row=1)
        radio_3.grid(column=arr_column_4[2], row=1)
        radio_4.grid(column=arr_column_4[3], row=1)

        notebook.add(frame5, text='5')

        var5 = StringVar()
        var5.set("None")

        radio_1 = Radiobutton(frame5, text="13", variable=var5, value="13")
        radio_2 = Radiobutton(frame5, text="14", variable=var5, value="14")
        radio_3 = Radiobutton(frame5, text="15", variable=var5, value="15")
        radio_4 = Radiobutton(frame5, text="16", variable=var5, value="16")

        arr_column_5 = [0, 1, 2, 3]
        length = len(arr_column_5)
        for i in range(0, length):
            rnd = randint(0, length - 1)
            temp = arr_column_5[i]
            arr_column_5[i] = arr_column_5[rnd]
            arr_column_5[rnd] = temp

        radio_1.grid(column=arr_column_5[0], row=1)
        radio_2.grid(column=arr_column_5[1], row=1)
        radio_3.grid(column=arr_column_5[2], row=1)
        radio_4.grid(column=arr_column_5[3], row=1)

        notebook.add(frame6, text='6')

        var6 = StringVar()
        var6.set("None")

        radio_1 = Radiobutton(frame6, text="16", variable=var6, value="16")
        radio_2 = Radiobutton(frame6, text="17", variable=var6, value="17")
        radio_3 = Radiobutton(frame6, text="18", variable=var6, value="18")
        radio_4 = Radiobutton(frame6, text="19", variable=var6, value="19")

        arr_column_6 = [0, 1, 2, 3]
        length = len(arr_column_6)
        for i in range(0, length):
            rnd = randint(0, length - 1)
            temp = arr_column_6[i]
            arr_column_6[i] = arr_column_6[rnd]
            arr_column_6[rnd] = temp

        radio_1.grid(column=arr_column_6[0], row=1)
        radio_2.grid(column=arr_column_6[1], row=1)
        radio_3.grid(column=arr_column_6[2], row=1)
        radio_4.grid(column=arr_column_6[3], row=1)

        notebook.add(frame7, text='Закончить тест')

        window_now.mainloop()
