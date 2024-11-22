variants = (".com", ".ru", ".net", ".gmail")


def send_email(sms, recipient, *, sender='university.help@gmail.com'):
    if '@' not in recipient and '@' not in sender or sender.endswith(variants) and recipient or sender.endswith(variants) or recipient.endswith(variants):
        print('Невозможно отправить письмо с адреса ',sender,' на адрес' + recipient)
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == sender:
        print('Письмо успешно отправлено с адреса ', sender, ' на адрес ' + recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ' + sender + ' на адрес' + recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')