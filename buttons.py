from aiogram import types


# Start menyusi
def start_buttons():
    btns = [
        [types.KeyboardButton(text="Anketa to'ldirish")],
        [types.KeyboardButton(text="Natijalarni ko'rish")]
    ]
    buttons = types.ReplyKeyboardMarkup(keyboard=btns, resize_keyboard=True)
    return buttons


def type():
    btns = [
        [types.KeyboardButton(text="O'zbekistonda | In Uzbekistan")],
        [types.KeyboardButton(text="Chet-elda | Abroad")]
    ]
    buttons = types.ReplyKeyboardMarkup(keyboard=btns, resize_keyboard=True)
    return buttons


def phone():
    btns = [
        [types.KeyboardButton(text="Raqamni jo'natish | Send phone number", request_contact=True)]
    ]
    buttons = types.ReplyKeyboardMarkup(keyboard=btns, resize_keyboard=True, one_time_keyboard=True)
    return buttons


def education_menu():
    btns = [
        [types.KeyboardButton(text="Maktabda o'qiyman | At high school")],
        [types.KeyboardButton(text="Maktabni bitirganman | In a gap year")],
        [types.KeyboardButton(text="Universitetda o'qiyman | At university")],
        [types.KeyboardButton(text="Universitetni bitirganman | Graduated university")]
    ]
    buttons = types.ReplyKeyboardMarkup(keyboard=btns, resize_keyboard=True)
    return buttons


def class_type():
    btns = [
        [types.KeyboardButton(text="9-group")],
        [types.KeyboardButton(text="10-group")],
        [types.KeyboardButton(text="11-group")]
    ]
    buttons = types.ReplyKeyboardMarkup(keyboard=btns, resize_keyboard=True)
    return buttons



def course_type():
    btns = [
        [types.KeyboardButton(text="1-course")],
        [types.KeyboardButton(text="2-course")],
        [types.KeyboardButton(text="3-course")],
        [types.KeyboardButton(text="4-course")]
    ]
    buttons = types.ReplyKeyboardMarkup(keyboard=btns, resize_keyboard=True)
    return buttons



def degree_type():
    btns = [
        [types.KeyboardButton(text="Bakalavr | Bachelor's")],
        [types.KeyboardButton(text="Magistratura | Master's")]
    ]
    buttons = types.ReplyKeyboardMarkup(keyboard=btns, resize_keyboard=True)
    return buttons


def certificate_type():
    btns = [
        [types.KeyboardButton(text="IELTS")],
        [types.KeyboardButton(text="Duolingo")],
        [types.KeyboardButton(text="Yo'q/None")]
    ]
    buttons = types.ReplyKeyboardMarkup(keyboard=btns, resize_keyboard=True)
    return buttons


def confirm():
    btns = [
        [types.KeyboardButton(text="Tasdiqlash | Confirm")],
        [types.KeyboardButton(text="Tahrirlash | Edit")]
    ]
    buttons = types.ReplyKeyboardMarkup(keyboard=btns, resize_keyboard=True)
    return buttons

