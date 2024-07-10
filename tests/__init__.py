import datasift as ds

text = input( "Введи текст > ")
wt = input("Чё проверим\n\n1 - Длина текста\n2 - Ссылка\n\n> ")

if int(wt) == 1:
    if ds.length_is(value=text, length=5, condition=ds.EQUALS):
        print("Тут 5 символов")
    else:
        print("Тут не 5 символов")
elif int(wt) == 2:
    if ds.is_url(text=text):
        print("Это ссылка")
    else:
        print("Это не ссылка")