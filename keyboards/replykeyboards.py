from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


#Создаём главную клавиатуру
def main_kb():
    kb_list = [
        [KeyboardButton(text='Яндекс карты'), 
         KeyboardButton(text='Ссылка на оплату')],
        [KeyboardButton(text='Картинка'), 
         KeyboardButton(text='Значение из А2')],
        [KeyboardButton(text='Внести дату')],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list, 
                                   resize_keyboard=True, 
                                   one_time_keyboard=True, 
                                   input_field_placeholder='Выберите пункт меню')

    return keyboard