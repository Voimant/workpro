from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from sourse.get_crm import car_for_testdrive

main_menu_kb_1 = InlineKeyboardButton('📎Запись на тест-драйв📎', callback_data='button1')
# kbd_1 = InlineKeyboardMarkup().add(inline_btn_1)

main_menu_kb_2 = InlineKeyboardButton('👍отзывы👍', callback_data='review')

# inline_kb2 = InlineKeyboardMarkup().add(inline_btn_2)
main_menu_kb_3 = InlineKeyboardButton(text="Динамическая ", callback_data="user_id")
main_menu_kb_4 = InlineKeyboardButton("📎Акции📎", url='https://2gis.ru/')
# main_menu_kb_6 = InlineKeyboardButton(text='📲Контакты📲', callback_data='contacts')
main_menu_kb_7 = InlineKeyboardButton(text='🛠Узнать статус ремонта🛠', callback_data='status')
main_menu_kb_8 = InlineKeyboardButton(text='🚗Авто с пробегом🚗', url='https://t.me/probegecho')
main_menu_kb_9 = InlineKeyboardButton(text='📰Новости салона📰', url='https://t.me/avtoecho')
main_menu_kb_10 = InlineKeyboardButton(text='📲Контакты📲', callback_data='contacts')

#Админка
kba1 = InlineKeyboardButton('рассылка', callback_data='from_base')
kba2 = InlineKeyboardButton('скачать базу', callback_data='upload')
markup2 = InlineKeyboardMarkup()
markup2.add(kba1, kba2)
#рассылка
send_kb_1 = InlineKeyboardButton('Отправить', callback_data='send')
send_kb_2 = InlineKeyboardButton('Отменить', callback_data='cancel')
markup4 = InlineKeyboardMarkup()
markup4.add(send_kb_1, send_kb_2)
#объединение клавиатур row_width=2
markup = InlineKeyboardMarkup()
markup.add(main_menu_kb_9)
markup.add(main_menu_kb_1)
markup.add(main_menu_kb_7)
markup.add(main_menu_kb_8)
markup.add(main_menu_kb_2)
markup.add(main_menu_kb_10)


"""*******************ОТЗЫВЫ**********************"""

reviews_kb_1 = InlineKeyboardButton('Оставить отзыв на 2ГИС', url='https://2gis.ru/samara/firm/2533803071383702')
reviews_kb_2 = InlineKeyboardButton('Оставить отзыв на Яндекс картах', url='https://yandex.ru/maps/org/avtosalon_ekho/1063863749/reviews/?ll=50.167922%2C53.183627&z=14')
reviews_kb_3 = InlineKeyboardButton('Главное меню', callback_data='main_menu')
markup3 = InlineKeyboardMarkup()
markup3.add(reviews_kb_1)
markup3.add(reviews_kb_2)
markup3.add(reviews_kb_3)

"""**********************КОНТАКТЫ******************************"""
contacts_kb_1 = InlineKeyboardButton('Сервис GEELY', callback_data='serves')
contacts_kb_2 = InlineKeyboardButton('Отдел продаж GEELY', url='https://t.me/Oleg081')
contacts_kb_3 = InlineKeyboardButton('Поддержка GEELY', url='https://t.me/elvirasibatova')
markup5 = InlineKeyboardMarkup()
markup5.add(contacts_kb_2, contacts_kb_1)
markup5.add(contacts_kb_3, reviews_kb_3)

cont_serv_kb_1 = InlineKeyboardButton('Специалист 1', url='https://t.me/echo_geely')
cont_serv_kb_2 = InlineKeyboardButton('Специалист 2', url='https://t.me/Valeradaich')
markup6 = InlineKeyboardMarkup()
markup6.add(cont_serv_kb_1, cont_serv_kb_2)
markup6.add(reviews_kb_3)

"""**********************ТЕСТДРАЙВЫ****************************"""

def test_markup():
    testdrive_markup = InlineKeyboardMarkup(row_width=1)
    cars = car_for_testdrive()
    for car_dicts in cars:
        for key, value in car_dicts.items():
            testdrive_markup.insert(InlineKeyboardButton(key, callback_data=key))

            # print(key)
    testdrive_markup.insert(reviews_kb_3)
    return testdrive_markup
test_markup()