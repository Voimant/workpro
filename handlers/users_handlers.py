from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import bot
from keyboards import markup, markup2, markup3, markup4, markup5, markup6, test_markup
from pprint import pprint
from sourse.get_1C import get_request_1C
from sourse.get_crm import car_for_testdrive, create_work_list, create_lead
from sourse.get_func import get_test_re
from media.texts.texts import contacts, start_t, otziv
import re
from DB.db_main import add_client, list_id, all_id_csv
pattern = r"(8|\+7)?\s*[\(]?(\d{3})[\)-]?\s*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})\s*[\(]?(\w+\.)?\s*(\d+)?[\)]?"
class Fsm(StatesGroup):
    gos_namber = State()
    vin = State()
    
    
class Fsm1(StatesGroup):
    message_all = State()
    image_al = State()
    resl = State()

class Fsm_test(StatesGroup):
    car = State()
    name = State()
    phone = State()



#Хендлеры
#@dp.message_handler(commands=['start1'])
async def cmd_start(message: types.Message):
    add_client(message.chat.id)
    logo = 'media\\images\\main_theme.jpg'
    with open(logo, 'rb') as f:
        await bot.send_photo(message.chat.id, f, start_t,  reply_markup=markup)
    print(message.chat.id)




# простой ответ на инлайн кнопку
#@dp.callback_query_handler(text='button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, 'кнопка клацнута :)', reply_markup=markup)

#@dp.message_handler(commands=['req'])
async def in_url(message: types.Message):
    await message.answer('Главное меню', reply_markup=markup)


#Функция мой id
#@dp.callback_query_handler(text='user_id')
async def user_id_inline_callback(call):
    print(call.from_user.id)
    print(call)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_message(call.from_user.id, f"Ваш ID: {call.from_user.id}", reply_markup=markup)

#@dp.message_handler(commands=['start'])
async def hello_handler(call):
    await bot.send_message(call.from_user.id, 'Вас приветствует Автосалон ЭХО', reply_markup=markup)





#@dp.callback_query_handler(text='status')
async def auto_rep(call):
    await bot.send_message(call.from_user.id, 'Введите государственный номер автомобиля')
    await Fsm.gos_namber.set()

#@dp.message_handler(state=Fsm.gos_namber)
async def gos_namber(message: types.Message, state: FSMContext):
    await state.update_data(gos_namber=message.text)
    await bot.send_message(message.chat.id, 'Введите номер телефона')
    await Fsm.vin.set()

#@dp.message_handler(state=Fsm.vin)
async def vin(message: types.Message, state: FSMContext):
    text_1 = message.text
    subt = r"+7 (\2) \3\4\5\6\7"
    result = re.sub(pattern, subt, text_1)
    print(result)
    await state.update_data(vin=result)

    data = await state.get_data(state)
    x = get_request_1C(data['gos_namber'], data['vin'])
    x.pop('RequestStatus')
    pprint(x)
    try:
        for v in x.values():
            nakl = v['ДанныеДокумента']
            status = v['СтатусРемонта']
            mess = f'''{nakl}
            Статус ремонта: {status}'''
            await bot.send_message(message.chat.id, mess)
    except TypeError:
        await bot.send_message(message.chat.id, 'Извините ничего не нашлось😔, Нужно проверить правильность номера телефона или автомобиля', reply_markup=markup)

    print(data)

    await state.finish()

async def contact(call):
    await bot.send_message(call.from_user.id, contacts, reply_markup=markup5)


async def review(call):
    await bot.send_message(call.from_user.id, otziv, reply_markup=markup3)

async def main_menu(call):
    logo = 'media//images//main_theme.jpg'
    with open(logo, 'rb') as f:
        await bot.send_photo(call.from_user.id, f, start_t,  reply_markup=markup)

async def serves(call):
    await bot.send_message(call.from_user.id, 'Здесь вы можете задать вопрос по сервисному обслуживанию', reply_markup=markup6)



"""********************АДМИН ПАНЕЛЬ******************************"""
#@dp.message_handler(commands=['admin'])
async def admin(message: types.Message):
    await message.answer('Введите пароль:',)

#@dp.message_handler()
async def ad_key(message: types.Message):
    if message.text == 'jljbsdf.gsdfbge;sdj;nfafgad;jhnjsdgdjshn;jn':
        await message.answer('Меню админа', reply_markup=markup2)
    elif message.text == "Контакты":
        url = 'https://nb-bot.ru/#o_rasrabotchike'
        pprint(get_test_re(url))

async def mess_all(call):
    await bot.send_message(call.from_user.id, 'Отправьте текст рассылки')
    await Fsm1.message_all.set()

async def image_all(message: types.Message, state: FSMContext):
    await state.update_data(message_all=message.text)
    await bot.send_message(message.chat.id, 'Добавьте картинку для рассылки')
    await Fsm1.image_al.set()

async def res(message: types.Message, state: FSMContext):
    photos = message.photo[-1].file_id
    await state.update_data(image_al=photos)
    data = await state.get_data(state)

    await bot.send_photo(message.chat.id, photo=data['image_al'], caption=data['message_all'])
    # await bot.send_message(message.chat.id, data['message_all'])
    await bot.send_message(message.chat.id, 'Проверяйте правильность сообщения и нажмите отправить', reply_markup=markup4)
    await Fsm1.resl.set()

async def sends_all(callback: types.CallbackQuery, state:FSMContext):
    if callback.data == 'send':
        data = await state.get_data(state)
        for user_ids in list_id():
            print(f'{data["image_al"]} и {data["message_all"]}')
            await bot.send_photo(user_ids, photo=data['image_al'], caption=data['message_all'])
            # await bot.send_message(user_ids, data['message_all'])
        await state.finish()
    elif callback.data == 'cancel':
        await bot.send_photo(callback.from_user.id, 'возврат в главное меню', reply_markup=markup)
        await state.finish()

async def upload_csv(call):
    x = all_id_csv()
    doc = open('clients.csv', 'rb')
    await bot.send_document(call.from_user.id, doc)
    await bot.send_message(call.from_user.id, 'файл отправлен', reply_markup=markup)

async def testdrive(call):
    await bot.send_message(call.from_user.id, 'Выберете машину     ', reply_markup=test_markup())
    await Fsm_test.car.set()

async def name_1(callback: types.CallbackQuery, state:FSMContext):
    print(callback.data)
    await bot.send_message(callback.from_user.id, callback.data)
    await state.update_data(car=callback.data)
    await bot.send_message(callback.from_user.id, 'Введите ваше имя')
    await Fsm_test.name.set()

async def phone_1(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await bot.send_message(message.chat.id, 'Введите номер телефона без дополнительных знаков 89921111222')
    await Fsm_test.phone.set()

async def all_info(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    data = await state.get_data(state)
    cars = car_for_testdrive()
    for car in cars:
        for key, value in car.items():
            if key == data['car']:
                # create_work_list(value['brand_id'], value['model_id'])
                resp = create_lead(data['name'], data['phone'], value['brand_id'], value['model_id'])
                if resp['success'] == False:
                    await bot.send_message(message.chat.id, 'Номер введен неверно. Попробуйте еще раз', reply_markup=markup)
                else:
                    await bot.send_message(message.chat.id, 'Менеджер получил заявку на тест-драйв, в ближайшее время с вами свяжуться. Спасибо!', reply_markup=markup)
                    break
            else:
                pass
    await state.finish()
    print(data)


def register_handlers(dp: Dispatcher):
    """*****************************testdrive************************************"""
    dp.register_callback_query_handler(testdrive, text='button1')
    dp.register_callback_query_handler(name_1, state=Fsm_test.car)
    dp.register_message_handler(phone_1, state=Fsm_test.name)
    dp.register_message_handler(all_info, state=Fsm_test.phone)

    """**************************ADMIN**********************************"""

    dp.register_callback_query_handler(upload_csv,text='upload')
    dp.register_message_handler(admin, commands=['admin'])
    dp.register_callback_query_handler(mess_all, text='from_base')
    dp.register_message_handler(image_all, state=Fsm1.message_all)
    dp.register_message_handler(res, content_types=['photo'], state=Fsm1.image_al)
    dp.register_callback_query_handler(sends_all, state=Fsm1.resl)
    """**************************USER*********************************"""
    dp.register_callback_query_handler(serves, text='serves')
    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_callback_query_handler(auto_rep, text='status')
    dp.register_message_handler(gos_namber, state=Fsm.gos_namber)
    dp.register_message_handler(vin, state=Fsm.vin)
    dp.register_callback_query_handler(contact, text='contacts')
    dp.register_message_handler(ad_key)
    dp.register_callback_query_handler(review, text='review')
    dp.register_callback_query_handler(main_menu, text='main_menu')
