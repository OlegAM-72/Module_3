adress = ".com", ".ru", ".net"
def send_email(message, recipient, sender="university.help@gmail.com"):
    if '@' not in recipient or not recipient.endswith(adress) or '@' not in sender or not sender.endswith(adress):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
send_email('Это проверка связи', 'vasyok1337@gmail.com')
send_email('Нестандартный отправитель!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Невозможно отправить', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Письмо себе', 'urban.teacher@mail.ru',sender='urban.teacher@mail.ru')



#      1. Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение),
# recipient(получатель) и 1 обязательно именованный аргумент со значением по
# умолчанию sender = "university.help@gmail.com
# def send_email(message, recipient, sender="university.help@gmail.com"):
#       2.Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net",то вывест наэкран
# (в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
#  if '@' not in recipient or not recipient.endswith(adress) or '@' not in sender or not sender.endswith(adress):
#  print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
#       3. Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
#       4. Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: "Письмо успешно
#       отправлено с адреса <sender> на адрес <recipient>."
#       5. В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено
#       с адреса <sender> на адрес <recipient>






