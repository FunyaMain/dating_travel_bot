from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👤 Мой профиль")],
        [KeyboardButton(text="💌 Анонимное сообщение")],
        [KeyboardButton(text="📜 О нас / Соглашение")],
        [KeyboardButton(text="💎 Поддержать")]
    ],
    resize_keyboard=True
)

confirm_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Подтвердить", callback_data="confirm")],
    [InlineKeyboardButton(text="✏️ Редактировать", callback_data="edit")]
])
