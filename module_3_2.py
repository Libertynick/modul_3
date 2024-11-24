def send_email(message,sender = "university.help@gmail.com",*,recipient):
    if '@' not in sender and recipient:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')

    if not sender.endswith(('.net','.com','.ru')) and recipient.endswith(('.net','.com','.ru')):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    elif sender == recipient:
        print(f'Невозможно отправить сообщение самому себе')

    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')

    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', recipient='vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', recipient='urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', recipient='urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', recipient='urban.teacher@mail.ru', sender='urban.teacher@mail.ru')