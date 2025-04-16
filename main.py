import asyncio
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from datetime import datetime
from buttons import *


from dotenv import load_dotenv
import os
load_dotenv()
BOT_TOKEN  = os.getenv("BOT_TOKEN") 
bot = Bot(token=BOT_TOKEN)

ADMIN_ID = int(os.getenv('ADMIN_AD'))


dp = Dispatcher()

class AnketaForm(StatesGroup):
    name = State()
    birthdate = State()
    location = State()
    phone = State()
    study_year =State()
    degree = State()
    certificate = State()
    score = State()
    education_choice = State()
    confirmation = State()

from aiogram.types import BotCommand

async def set_default_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Qaytadan boshlash")
    ]
    await bot.set_my_commands(commands)


@dp.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer(text=f"Assalomu Aleykum, {message.from_user.first_name}\nTanlang:\nChoose:", reply_markup=start_buttons())

@dp.message(F.text == "Anketa to'ldirish")
async def anketa_start(msg: types.Message, state: FSMContext):
    await state.set_state(AnketaForm.name)
    await msg.answer("Iltimos, to'liq ism va familiyangizni kiriting!\nPlease, fill in your full name!")
    

@dp.message(AnketaForm.name)
async def set_name(msg: types.Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await state.set_state(AnketaForm.birthdate)
    await msg.answer("Iltimos, tug'ilgan yil, oy, va kuningizni kiriting!(2001.01.21)\nPlease, fill in your birthdate!")


@dp.message(AnketaForm.birthdate)
async def set_birthdate(msg: types.Message, state: FSMContext):
    await state.update_data(birthdate=msg.text)
    await state.set_state(AnketaForm.location)
    await msg.answer("O'zbekistonda istiqomat qilasizmi yoki chet-eldami?\nDo you live in Uzbekistan or abroad?",reply_markup=type())


@dp.message(AnketaForm.location)
async def set_location(msg: types.Message, state: FSMContext):
    await state.update_data(location=msg.text)
    await state.set_state(AnketaForm.phone)
    await msg.answer("Iltimos, telefon raqamingizni jo'nating!\n'jo'natish' tugmasini bosing yoki o'zingiz kiriting!\n\nPlease, send your phone number!\nEither press 'send' button or fill in yourself!",reply_markup=phone())
    

@dp.message(AnketaForm.phone)
async def set_phone(msg: types.Message, state: FSMContext):
    if msg.contact:
        phone_number = msg.contact.phone_number
    else:
        phone_number = msg.text
    await state.update_data(phone=phone_number)
    await state.set_state(AnketaForm.education_choice)
    await msg.answer("Tanlang:\nChoose one:", reply_markup=education_menu())

#####################################################

@dp.message(AnketaForm.education_choice, F.text == "Maktabda o'qiyman | At high school")
async def maktabda_oqiyman(msg: types.Message, state: FSMContext):
    await state.set_state(AnketaForm.study_year)
    await msg.answer("Nechinchi sinfda o'qiysiz?\nWhat grade at high school are you in?",reply_markup=class_type())


@dp.message(AnketaForm.education_choice, F.text == "Universitetda o'qiyman | At university")
async def Universitetda_oqiyman(msg: types.Message, state: FSMContext):
    await state.set_state(AnketaForm.study_year)
    await msg.answer("Nechinchi kursda o'qiysiz?\nWhat year at university are you in?",reply_markup=course_type())


@dp.message(AnketaForm.study_year)
async def set_study_year(msg: types.Message, state: FSMContext):
    await state.update_data(study_year=msg.text)
    await state.set_state(AnketaForm.degree)
    await msg.answer("Qaysi darajada o'qimoqchisiz? Tanlang:\nWhat degree do you want to study at? Choose one:",reply_markup=degree_type())


@dp.message(AnketaForm.education_choice, F.text.in_(["Maktabni bitirganman | In a gap year", "Universitetni bitirganman | Graduated university"]))
async def bitirganlar(msg: types.Message, state: FSMContext):
    if "Maktabni" in msg.text:
        await state.update_data(study_year="graduated school")
    else:
        await state.update_data(study_year="graduated university")

    await state.set_state(AnketaForm.degree)
    await msg.answer("Qaysi darajada o'qimoqchisiz? Tanlang:\nWhat degree do you want to study at? Choose one:",reply_markup=degree_type())

###############################################################


@dp.message(AnketaForm.degree)
async def set_degree(msg: types.Message, state: FSMContext):
    await state.update_data(degree=msg.text)
    await state.set_state(AnketaForm.certificate)
    await msg.answer("Sizda IELTS yoki Duolingo bormi?\nNatijasi yuqorisini tanlang!\n\nDo you have IELTS or Duolingo score?\nChoose the one you have highest score from!",reply_markup=certificate_type())


@dp.message(AnketaForm.certificate)
async def set_certificate(msg: types.Message, state: FSMContext):
    text = msg.text
    if not text == "Yo'q/None":
        await state.update_data(certificate=msg.text)
        await state.set_state(AnketaForm.score)
        await msg.answer(f'{msg.text} balingizni kiriting\nWhat is your {msg.text} score?')
    else:
        await state.update_data(certificate=msg.text)
        await state.set_state(AnketaForm.confirmation)
        data = await state.get_data()
        last_data = f'''Iltimos, shaxsiy ma'lumotingiz to'g'riligini tasdiqlang!\nPlease, confirm your personal info is correct!\n
    Toliq ism/Full name - {data.get('name')}\n
    Tug'ilgan yilingiz/Date of birth - {data.get('birthdate')}\n
    Telefon raqamingiz/Phone Number - {data.get('phone')}\n
    O'quv yilingiz/Study year - {data.get('study_year')}\n
    Tanlangan daraja/Chosen degree - {data.get('degree')}\n
    Test natijangiz/Test score - {data.get('certificate')}'''
        await msg.answer(f'{last_data}', reply_markup=confirm())
        

@dp.message(AnketaForm.score)
async def set_score(msg: types.Message, state: FSMContext):
    await state.update_data(score=msg.text)
    await state.set_state(AnketaForm.confirmation)
    data = await state.get_data()
    last_data = f'''Iltimos, shaxsiy ma'lumotingiz to'g'riligini tasdiqlang!\nPlease, confirm your personal info is correct!\n
    Toliq ism/Full name - {data.get('name')}\n
    Tug'ilgan yilingiz/Date of birth - {data.get('birthdate')}\n
    Telefon raqamingiz/Phone Number - {data.get('phone')}\n
    O'quv yilingiz/Study year - {data.get('study_year')}\n
    Tanlangan daraja/Chosen degree - {data.get('degree')}\n
    Test natijangiz/Test score - {data.get('certificate')} {data.get('score')}'''
    await msg.answer(f'{last_data}', reply_markup=confirm())
###############################################################################################################################################

@dp.message(AnketaForm.confirmation, F.text == "Tasdiqlash | Confirm")
async def final_confirmation(msg: types.Message, state: FSMContext):
    data = await state.get_data()

    if data['certificate'] == "Yo'q/None":  
        await msg.answer('''Hamkorligingiz uchun rahmat!\nUzr, bizni talablarimizga to'g'ri kelmadingiz ❌. Test natijalaringiz yetarli darajada emas, yoki o'quv yilingiz va maqsadlaringiz bizning talablarimizga mos tushmaydi.\n\nThank you for cooperation! Sorry, but you don't meet our requirements ❌. Either you have a low test score or your current education level and educational goals don't suit.''')
        await msg.answer('''Talablar:\n\n🎓 Bakalavrga hozirda 11-sinfda o’qiyotgan yoki maktabni bitirgan bo'lishingiz kerak.\nIELTS 5.5 or above\nDuolingo 100 or above\n\n🎓 Magistratura uchun esa hozirda bakalavrda 4-kursda o’qiyotgan yoki allaqachon universitetni bitirgan bo’lishingiz zarur.\nIELTS 6 or above\nDuolingo 105 or above''')
        return

    degree = data['degree']
    score1 = float(data.get('score', 0))
    study_year = data['study_year']

    if (degree == "Bakalavr | Bachelor's") and (( score1 >= 100.0 or score1 >= 5.5) and (( study_year == '11-group') or (study_year == "graduated school") )):
        await msg.answer('''Hamkorligingiz uchun rahmat!\nBizni talablarimizga to'g'ri keldingiz ✅. IELTS yoki Duolingo sertifikatingizni @kamoliddiin00o telegramga jo’nating. Sertifikatingiz haqiqatda borligini ko’rib, tekshirib, yana bir bor ishonch hosil qilib agar hammasi joyida bo’lsa shunda sizga service bo’yicha batafsil ma’lumot beramiz.\n\nThank you for cooperation!\nYou meet our requirements ✅. Please send your IELTS or Duolingo certificate to @kamoliddiin00o. We will double check if you, in fact, have a valid certificate and whether it meets the requirements. If everything is alright, then we will give you detailed information about our services. ''')            
    
    elif (degree == "Magistratura | Master's") and ((score1 >= 105 or score1 >= 6) and (study_year == "4-course" or study_year == "graduated university")) :
        await msg.answer('''Hamkorligingiz uchun rahmat!\nBizni talablarimizga to'g'ri keldingiz ✅. IELTS yoki Duolingo sertifikatingizni @kamoliddiin00o telegramga jo’nating. Sertifikatingiz haqiqatda borligini ko’rib, tekshirib, yana bir bor ishonch hosil qilib agar hammasi joyida bo’lsa shunda sizga service bo’yicha batafsil ma’lumot beramiz.\n\nThank you for cooperation!\nYou meet our requirements ✅. Please send your IELTS or Duolingo certificate to @kamoliddiin00o. We will double check if you, in fact, have a valid certificate and whether it meets the requirements. If everything is alright, then we will give you detailed information about our services. ''')            
   
    else:  
        await msg.answer('''Hamkorligingiz uchun rahmat!\nUzr, bizni talablarimizga to'g'ri kelmadingiz ❌. Test natijalaringiz yetarli darajada emas, yoki o'quv yilingiz va maqsadlaringiz bizning talablarimizga mos tushmaydi.\n\nThank you for cooperation! Sorry, but you don't meet our requirements ❌. Either you have a low test score or your current education level and educational goals don't suit.''')
        await msg.answer('''Talablar:\n\n🎓 Bakalavrga hozirda 11-sinfda o’qiyotgan yoki maktabni bitirgan bo'lishingiz kerak.\nIELTS 5.5 or above\nDuolingo 100 or above\n\n🎓 Magistratura uchun esa hozirda bakalavrda 4-kursda o’qiyotgan yoki allaqachon universitetni bitirgan bo’lishingiz zarur.\nIELTS 6 or above\nDuolingo 105 or above''')
    

    data = await state.get_data()
    last_data = f'''Foydalanuvchi malumotlari:\n
    Toliq ism/Full name - {data.get('name')}\n
    Tug'ilgan yilingiz/Date of birth - {data.get('birthdate')}\n
    Telefon raqamingiz/Phone Number - {data.get('phone')}\n
    O'quv yilingiz/Study year - {data.get('study_year')}\n
    Tanlangan daraja/Chosen degree - {data.get('degree')}\n
    Test natijangiz/Test score - {data.get('certificate')} {data.get('score')}''' 
    await bot.send_message(chat_id=ADMIN_ID ,text=last_data)
    
    
@dp.message(AnketaForm.confirmation, F.text == "Tahrirlash | Edit")
async def final_confirmation(msg: types.Message, state: FSMContext):
    await state.set_state(AnketaForm.name)
    await msg.answer("Iltimos, to'liq ism va familiyangizni kiriting!\nPlease, fill in your full name!")

        



# Ishga tushirish
async def main():
    await set_default_commands(bot)


    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
