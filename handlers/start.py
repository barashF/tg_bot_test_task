from urllib import response
from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards import replykeyboards, inlinekeyboards
from create_bot import bot, dp
from payment.yoomoney import bill
from Google_sheets.manager_sheets import get_value_from_sheet
from views import start_view


start_router = Router()



class CallbackOnStart(StatesGroup):
    Q1 = State()

#стартовое сообщение бота
@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Надеюсь быть полезным для вас)', 
                         reply_markup=replykeyboards.main_kb())


#вызов ссылки на яндекс карты
@start_router.message(F.text.lower() == 'яндекс карты')
async def call_inline(message: Message):
    await message.answer('Ссылка на карту:',
                         reply_markup=inlinekeyboards.yandex_map_inline())


#вызов ссылки на яндекс карты
@start_router.message(F.text.lower() == 'ссылка на оплату')
async def get_url_bill(message: Message):
    await message.answer('Ссылка на оплату:',
                         reply_markup=inlinekeyboards.url_bill_inline(bill()))
    
#получение значения из поля А2
@start_router.message(F.text == 'Значение из А2')
async def get_value(message: Message):
    await message.answer(get_value_from_sheet())


#отправка изображения
@start_router.message(F.text.lower() == 'картинка')
async def answer_image(message: Message):
    photo = FSInputFile("путь к картинке")
    await bot.send_photo(chat_id=message.chat.id, photo=photo)

#запрос на запись даты
@start_router.message(F.text.lower() == 'внести дату')
async def inp_date(message: Message, state: FSMContext):
    await message.answer('Введите дату')
    await state.set_state(CallbackOnStart.Q1)


#проверка даты на корректность и внос в таблицу
@start_router.message(CallbackOnStart.Q1)
async def write_date(message: types.Message):
    date = message.text
    response = await start_view.input_date(date)
    await message.answer(response)
