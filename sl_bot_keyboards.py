from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

empty_kb = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

# Кнопка для связи с разработчиком
contact_dev_kb = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
contact_dev_kb.add(InlineKeyboardButton(text='Связаться с моим создателем', url='telegram.me/Interligo'))

# Кнопка для выгрузки информации из БД
show_db_kb = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
show_db_kb.add(InlineKeyboardButton(text='Показать список покупок'))

# Кнопки в стартовом меню с колбэком
start_list_callback = ["show", "add", "update", "del", "clean"]
show_db = InlineKeyboardButton('Показать список покупок', callback_data='show')
add_to_db = InlineKeyboardButton('Добавить в список покупок', callback_data='add')
update_db = InlineKeyboardButton('Изменить', callback_data='update')
del_from_db = InlineKeyboardButton('Удалить', callback_data='del')
clean_db = InlineKeyboardButton('Очистить список покупок', callback_data='clean')
start_markup = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(show_db).add(add_to_db)
start_markup.row(update_db, del_from_db).add(clean_db)

# Измененная клавиатура для функции show
show_markup = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(add_to_db)
show_markup.row(update_db, del_from_db).add(clean_db)

# Кнопки для изменения последнего введенного элемента
update_previous_button = InlineKeyboardButton('Изменить последнее', callback_data='update_previous')
update_any_button = InlineKeyboardButton('Изменить другое', callback_data='update_any')
update_prev_any_markup = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
update_prev_any_markup.add(update_previous_button).add(update_any_button)

# Кнопки для удаления последнего введенного элемента
del_previous_button = InlineKeyboardButton('Удалить последнее', callback_data='del_previous')
del_any_button = InlineKeyboardButton('Удалить другое', callback_data='del_any')
del_prev_any_markup = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
del_prev_any_markup.add(del_previous_button).add(del_any_button)

# Кнопки для функции update
update_list_callback = ["update_product", "update_amount", "update_type"]
update_name_product = InlineKeyboardButton('Изменить название', callback_data='update_product')
update_amount_product = InlineKeyboardButton('Изменить количество', callback_data='update_amount')
update_type_product = InlineKeyboardButton('Изменить категорию', callback_data='update_type')
update_markup = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(update_name_product)
update_markup.add(update_amount_product).add(update_type_product)

# Дополнительные кнопки для обработки ошибки ввода
update_amount_mistake = InlineKeyboardButton('Ввести количество ещё раз', callback_data='update_amount')
update_mistake_markup = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
update_mistake_markup.add(update_amount_mistake)

# Кнопки для функции update_previous
update_prev_list_callback = ["update_prev_product", "update_prev_amount", "update_prev_type"]
update_prev_name_product = InlineKeyboardButton('Изменить название', callback_data='update_prev_product')
update_prev_amount_product = InlineKeyboardButton('Изменить количество', callback_data='update_prev_amount')
update_prev_type_product = InlineKeyboardButton('Изменить категорию', callback_data='update_prev_type')
update_prev_markup = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(update_prev_name_product)
update_prev_markup.add(update_prev_amount_product).add(update_prev_type_product)

# Дополнительные кнопки для обработки ошибки в последнем введенном
update_prev_amount_mistake = InlineKeyboardButton('Ввести количество ещё раз', callback_data='update_prev_amount')
update_prev_mistake_markup = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
update_prev_mistake_markup.add(update_prev_amount_mistake)

# Кнопки выбора категории продукта
type_list_callback = ["Продукты", "Овощи/фрукты", "Вкусняшки", "Бытовая химия", "Алкоголь", "Другое"]
food_button = InlineKeyboardButton('Продукты', callback_data='Продукты')
vegetables_button = InlineKeyboardButton('Овощи/фрукты', callback_data='Овощи/фрукты')
delicious_button = InlineKeyboardButton('Вкусняшки', callback_data='Вкусняшки')
chemicals_button = InlineKeyboardButton('Бытовая химия', callback_data='Бытовая химия')
alcohol_button = InlineKeyboardButton('Алкоголь', callback_data='Алкоголь')
another_button = InlineKeyboardButton('Другое', callback_data='Другое')
type_markup = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
type_markup.add(food_button).row(vegetables_button, delicious_button).row(chemicals_button, alcohol_button)
type_markup.add(another_button)

# Кнопки для обновления категории продукта
type_list_callback_to_update = ["food", "vegetables", "delicious", "chemicals", "alcohol", "another"]
food_button = InlineKeyboardButton('Продукты', callback_data='food')
vegetables_button = InlineKeyboardButton('Овощи/фрукты', callback_data='vegetables')
delicious_button = InlineKeyboardButton('Вкусняшки', callback_data='delicious')
chemicals_button = InlineKeyboardButton('Бытовая химия', callback_data='chemicals')
alcohol_button = InlineKeyboardButton('Алкоголь', callback_data='alcohol')
another_button = InlineKeyboardButton('Другое', callback_data='another')
type_markup_to_update = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
type_markup_to_update.add(food_button).row(vegetables_button, delicious_button).row(chemicals_button, alcohol_button)
type_markup_to_update.add(another_button)

# Кнопки для обновления категории предыдущего продукта
type_list_callback_to_update_prev = ["food!", "vegetables!", "delicious!", "chemicals!", "alcohol!", "another!"]
food_button = InlineKeyboardButton('Продукты', callback_data='food!')
vegetables_button = InlineKeyboardButton('Овощи/фрукты', callback_data='vegetables!')
delicious_button = InlineKeyboardButton('Вкусняшки', callback_data='delicious!')
chemicals_button = InlineKeyboardButton('Бытовая химия', callback_data='chemicals!')
alcohol_button = InlineKeyboardButton('Алкоголь', callback_data='alcohol!')
another_button = InlineKeyboardButton('Другое', callback_data='another!')
type_markup_to_update_prev = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
type_markup_to_update_prev.add(food_button).row(vegetables_button, delicious_button).row(chemicals_button, alcohol_button)
type_markup_to_update_prev.add(another_button)

# Кнопки выбора количества продукта
amount_list_callback = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
button_one = InlineKeyboardButton('1', callback_data='1')
button_two = InlineKeyboardButton('2', callback_data='2')
button_three = InlineKeyboardButton('3', callback_data='3')
button_four = InlineKeyboardButton('4', callback_data='4')
button_five = InlineKeyboardButton('5', callback_data='5')
button_six = InlineKeyboardButton('6', callback_data='6')
button_seven = InlineKeyboardButton('7', callback_data='7')
button_eight = InlineKeyboardButton('8', callback_data='8')
button_nine = InlineKeyboardButton('9', callback_data='9')
amount_markup = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
amount_markup.row(button_seven, button_eight, button_nine)
amount_markup.row(button_four, button_five, button_six)
amount_markup.row(button_one, button_two, button_three)

# Кнопки для увеличения количества продукта или отмены ввода
select_list_callback = ["count_up", "cancel"]
count_up_button = InlineKeyboardButton('Увеличить количество на один', callback_data='count_up')
cancel_button = InlineKeyboardButton('Отменить ввод', callback_data='cancel')
select_markup = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(count_up_button).add(cancel_button)

# Кнопки для того, чтобы добавить продукт или отменить ввод
choice_list_callback = ["add_product", "cancel_adding"]
add_button = InlineKeyboardButton('Добавить в список', callback_data='add_product')
cancel_adding_button = InlineKeyboardButton('Отменить ввод', callback_data='cancel_adding')
choice_markup = InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(add_button).add(cancel_adding_button)
