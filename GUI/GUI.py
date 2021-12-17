from tkinter import *
from functools import partial
from res.questions_basa import *
from res.question_answer import *
from random import randint
from time import time
from res.email_post import *


def GUI():
    def click(window):
        def click_chek(list_param, start_time, FIO_txt):
            list_text = [txt1.get(), txt2.get(), txt3.get(), txt4.get(), txt5.get(), txt6.get()]

            ball = 0

            ball += int(answer_1(int(list_param[0]), str(list_text[0])))
            ball += int(answer_2(int(list_param[1]), str(list_text[1])))
            ball += int(answer_3(int(list_param[2]), str(list_text[2])))
            ball += int(answer_4(int(list_param[3]), str(list_text[3])))
            ball += int(answer_5(int(list_param[4]), str(list_text[4])))
            ball += int(answer_6(int(list_param[5]), str(list_text[5])))

            end_time = int((time() - start_time))
            sec = int(end_time)
            min = int(end_time / 60)
            hour = int(end_time / 60 / 60)

            mail_send = ("Student: " + str(FIO_txt) + "\n" +
                         "Time: " + str(hour) + ":" + str(min) + ":" + str(sec) + "\n" +
                         "Mark: " + str(ball))

            window_now.destroy()

            send_mail(mail_send)

        start_time = time()

        FIO_txt = txt.get()

        rand_1 = randint(1, 3)
        rand_2 = randint(1, 3)
        rand_3 = randint(1, 3)
        rand_4 = randint(1, 3)
        rand_5 = randint(1, 3)
        rand_6 = randint(1, 3)

        list_param = [rand_1, rand_2, rand_3, rand_4, rand_5, rand_6]

        ques_1 = question_1(list_param[0])
        ques_2 = question_2(list_param[1])
        ques_3 = question_3(list_param[2])
        ques_4 = question_4(list_param[3])
        ques_5 = question_5(list_param[4])
        ques_6 = question_6(list_param[5])

        list_ques = [ques_1, ques_2, ques_3, ques_4, ques_5, ques_6]

        window.destroy()

        window_now = Tk()

        window_now.title('Тест идет!')
        window_now.geometry("400x250")

        lbl1 = Label(window_now, text=ques_1)
        lbl1.grid(column=0, row=0)
        lbl2 = Label(window_now, text=ques_2)
        lbl2.grid(column=0, row=1)
        lbl3 = Label(window_now, text=ques_3)
        lbl3.grid(column=0, row=2)
        lbl4 = Label(window_now, text=ques_4)
        lbl4.grid(column=0, row=3)
        lbl5 = Label(window_now, text=ques_5)
        lbl5.grid(column=0, row=4)
        lbl6 = Label(window_now, text=ques_6)
        lbl6.grid(column=0, row=5)

        txt1 = Entry(window_now, width=25)
        txt1.grid(column=1, row=0)
        txt2 = Entry(window_now, width=25)
        txt2.grid(column=1, row=1)
        txt3 = Entry(window_now, width=25)
        txt3.grid(column=1, row=2)
        txt4 = Entry(window_now, width=25)
        txt4.grid(column=1, row=3)
        txt5 = Entry(window_now, width=25)
        txt5.grid(column=1, row=4)
        txt6 = Entry(window_now, width=25)
        txt6.grid(column=1, row=5)

        button1 = Button(window_now, text="Проверить!", command=partial(click_chek, list_param, start_time, FIO_txt))
        button1.grid(column=0, row=6)

        window_now.mainloop()

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
