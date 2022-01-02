from aiogram.dispatcher.filters.state import StatesGroup, State


class OrderProduct(StatesGroup):
    # Состояние для добавления нового продукта в список.
    waiting_for_product_name_to_add = State()

    # Состояния для изменения названия продукта в списке.
    waiting_for_product_name_to_update = State()
    waiting_for_product_new_name_to_update = State()

    # Состояние для изменения названия предыдущего продукта в списке.
    waiting_for_product_name_to_update_prev = State()

    # Состояния для изменения количества продукта в списке.
    waiting_for_product_amount_to_update = State()

    # Состояние для изменения количества предыдущего продукта в списке.
    waiting_for_product_amount_to_update_prev = State()

    # Состояния для изменения категории продукта в списке.
    waiting_for_product_type_to_update = State()

    # Состояние для удаления продукта из списка.
    waiting_for_product_name_to_del = State()
