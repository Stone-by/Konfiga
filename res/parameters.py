from random import randint
from questions_basa import question_1, question_2, question_3, question_4, question_5, question_6
from question_answer import answer_1, answer_2, answer_3, answer_4, answer_5, answer_6
from email_post import send_mail
from time import time


def param():
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

    sum_ball = 0

    sum_ball += answer_1(list_param[0], ques_1)
    sum_ball += answer_2(list_param[1], ques_2)
    sum_ball += answer_3(list_param[2], ques_3)
    sum_ball += answer_4(list_param[3], ques_4)
    sum_ball += answer_5(list_param[4], ques_5)
    sum_ball += answer_6(list_param[5], ques_6)

    return sum_ball


def start_test():
    start_time = time()
    fio_student = "FIO_text"
    res = param()
    end_time = int((time() - start_time))
    sec = int(end_time)
    min = int(end_time / 60)
    hour = int(end_time / 60 / 60)
    mail_send = ("Student: " + str(fio_student) + "\n" +
          "Time: " + str(hour) + ":" + str(min) + ":" + str(sec) + "\n" +
          "Mark: " + str(res))
    # send_mail(mail_send)
