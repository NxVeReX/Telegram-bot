from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    CallbackContext,
)
import time

TOKEN = '8063843029:AAFSpZ2zZZsJ4Ft09SN9ChJHQCsLf9us8lM'
URL = 'https://api.telegram.org/bot'


# Функция-обработчик команды /start
async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Билеты категории B (авто)", callback_data='button1')],
        [InlineKeyboardButton("Билеты для мототранспорта", callback_data='button2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        'Привет! Это Telegram-бот для тренировки сдачи экзаменов. Выберите нужный тип билетов:',
        reply_markup=reply_markup
    )


# Обработчик нажатия кнопок
async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    

    if query.data == 'button1':
        await query.edit_message_text(text="Выбрана категория B (авто) \nВы готовы?")
        
        # Добавление новых двух кнопок
        new_keyboard = [
            [InlineKeyboardButton("Да", callback_data='new_button_1')],
            [InlineKeyboardButton("Нет(", callback_data='new_button_2')]
        ]
        new_reply_markup = InlineKeyboardMarkup(new_keyboard)
        await query.edit_message_reply_markup(reply_markup=new_reply_markup)

    elif query.data == 'button2':
        await query.edit_message_text(text="Выбрана категория для мототранспорта \n❌НАХОДИТСЯ В РАЗРАБОТКЕ❌")

    # Вопрос 1
    if query.data == "new_button_1":
        await send_photo_url(context, 'https://storage.yandexcloud.net/pddlife/abm/n3_1.jpg')
        await query.edit_message_text(text="Вопрос 1 \nВыезжая с грунтовой дороги на перекресток, Вы попадаете: \n \n1. На главную дорогу. \n2. На равнозначную дорогу, поскольку отсутствуют знаки приоритета. \n3. На равнозначную дорогу, поскольку проезжая часть имеет твердое покрытие перед перекрестком.\n\n(см. рис.1)")
       
        answer = [
            [InlineKeyboardButton("1", callback_data = 'ans_button_1'),
             InlineKeyboardButton("2", callback_data = 'ans_button_2'),
             InlineKeyboardButton("3", callback_data = 'ans_button_3')]
        ]
        ans_reply_markup = InlineKeyboardMarkup(answer)
        await query.edit_message_reply_markup(reply_markup=ans_reply_markup)

    # Ответы 1
    elif query.data == 'ans_button_1':
        await query.edit_message_text(text="✔Ответ верный✔ \nВы выезжаете на дорогу с покрытием, которая является главной по отношению к грунтовой п. 1.2")
        time.sleep(7)
        

    elif query.data == 'ans_button_2':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 1.")
        next_quest_kb = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans_button_1')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans_button_3':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 1.")
        next_quest_kb = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans_button_1')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    # Вопрос 2
    if query.data == "ans_button_1":
        await send_photo_url(context, 'https://storage.yandexcloud.net/pddlife/abm/n3_2.jpg')
        await query.edit_message_text(text="Вопрос 2 \nГде Вы должны остановиться? \n1. Перед знаком (А). \n2. Перед перекрестком (Б). \n3. Перед краем пересекаемой проезжей части (В). \n\n(см. рис.2)")
        answer2 = [
            [InlineKeyboardButton("1", callback_data='ans2_button_1'),
             InlineKeyboardButton("2", callback_data='ans2_button_2'),
             InlineKeyboardButton("3", callback_data='ans2_button_3')]
        ]
        ans2_reply_markup = InlineKeyboardMarkup(answer2)
        await query.edit_message_reply_markup(reply_markup=ans2_reply_markup)

    # Ответы 2
    elif query.data == 'ans2_button_1':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 3.")
        next_quest_kb_2 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans2_button_3')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_2)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans2_button_2':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 3.")
        next_quest_kb_2 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans2_button_3')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_2)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans2_button_3':
        await query.edit_message_text(text="✔Ответ верный✔ \nЗнак 2.5  'Движение без остановки запрещено (STOP)' применяется при ограниченной видимости пересекаемой дороги и поэтому независимо от наличия на ней ТС требует обязательной остановки. В данном случае вы должны остановиться перед краем пересекаемой проезжей части (место В). При наличии разметки 1.12  (стоп-линия) останавливаться следует перед такой линией.")
        time.sleep(15)
        

    # Вопрос 3
    if query.data == "ans2_button_3":
        await send_photo_url(context, 'https://storage.yandexcloud.net/pddlife/abm/n3_3.jpg')
        await query.edit_message_text(text="Вопрос 3 \nВам необходимо двигаться со скоростью не более 40 км/ч: \n1. Только во время дождя. \n2. Во время выпадения осадков (дождя, града, снега). \n3. Во всех случаях, когда покрытие проезжей части влажное. \n\n(см. рис.3)")
        answer3 = [
            [InlineKeyboardButton("1", callback_data='ans3_button_1'),
             InlineKeyboardButton("2", callback_data='ans3_button_2'),
             InlineKeyboardButton("3", callback_data='ans3_button_3')]
        ]
        ans3_reply_markup = InlineKeyboardMarkup(answer3)
        await query.edit_message_reply_markup(reply_markup=ans3_reply_markup)

    # Ответы 3
    elif query.data == 'ans3_button_1':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 3.")
        next_quest_kb_3 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans3_button_3')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_3)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans3_button_2':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 3.")
        next_quest_kb_3 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans3_button_3')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_3)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans3_button_3':
        await query.edit_message_text(text="✔Ответ верный✔ \nТабличка 8.16  'Влажное покрытие' информирует о том, что запрещение движения со скоростью более 40 км/ч, вводимое знаком 3.24  'Ограничение максимальной скорости', действует только в период времени, когда покрытие проезжей части влажное, например, во время дождя или сразу после его окончания.")
        time.sleep(15)
        

    # Вопрос 4
    if query.data == "ans3_button_3":
        await send_photo_url(context, 'https://storage.yandexcloud.net/pddlife/abm/n3_4.jpg')
        await query.edit_message_text(text="Вопрос 4 \nКакой из указанных знаков устанавливается в начале дороги с односторонним движением? \n1. Только А. \n2. Только Б. \n3. Б или Г. \n4. Б или В. \n\n(см. рис.4)")
        answer4 = [
            [InlineKeyboardButton("1", callback_data='ans4_button_1'),
             InlineKeyboardButton("2", callback_data='ans4_button_2'),
             InlineKeyboardButton("3", callback_data='ans4_button_3'),
             InlineKeyboardButton("4", callback_data='ans4_button_4')]
        ]
        ans4_reply_markup = InlineKeyboardMarkup(answer4)
        await query.edit_message_reply_markup(reply_markup=ans4_reply_markup)

    # Ответы 4
    elif query.data == 'ans4_button_1':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 2.")
        next_quest_kb_4 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans4_button_2')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_4)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans4_button_2':
        await query.edit_message_text(text="✔Ответ верный✔. \nВ начале дороги с односторонним движением устанавливается знак Б (5.5  'Дорога с односторонним движением'). Знак А (5.14.1  'Полоса для маршрутных транспортных средств') обозначает полосу для маршрутных ТС, знак В (6.14.2  'Номер маршрута') указывает номер и направление маршрута на перекрестке, а знак Г (6.15.1  'Направление для грузовых автомобилей') - рекомендуемое направление движения для грузовых автомобилей.")
        time.sleep(15)
        

    elif query.data == 'ans4_button_3':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 2. \n")
        next_quest_kb_4 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans4_button_2')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_4)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans4_button_4':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 2. \n")
        next_quest_kb_4 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans4_button_2')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_4)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    # Вопрос 5
    if query.data == "ans4_button_2":
        await send_photo_url(context, 'https://storage.yandexcloud.net/pddlife/abm/n3_5.jpg')
        await query.edit_message_text(text="Вопрос 4 \nМожно ли Вам остановиться в этом месте для посадки или высадки пассажиров? \n\n1. Можно. \n2. Можно, если при этом не будут созданы помехи движению маршрутных транспортных средств. \n3. Нельзя. \n\n(см. рис.4)")
        answer5 = [
            [InlineKeyboardButton("1", callback_data='ans5_button_1'),
             InlineKeyboardButton("2", callback_data='ans5_button_2'),
             InlineKeyboardButton("3", callback_data='ans5_button_3')]
        ]
        ans5_reply_markup = InlineKeyboardMarkup(answer5)
        await query.edit_message_reply_markup(reply_markup=ans5_reply_markup)

    # Ответы 5
    elif query.data == 'ans5_button_1':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 2.")
        next_quest_kb_4 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans5_button_2')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_4)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans5_button_2':
        await query.edit_message_text(text="✔Ответ верный✔. \nРазметка 1.17.1  (в виде желтой зигзагообразной линии) применяется для обозначения мест остановок маршрутных ТС и стоянок такси. В данной ситуации Вы можете остановиться для посадки или высадки пассажиров в обозначенной разметкой 1.17.1  зоне, если не создадите помех движению маршрутных автобусов или троллейбусов п.12.4.")
        time.sleep(15)
        

    elif query.data == 'ans5_button_3':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 2. \n")
        next_quest_kb_4 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans5_button_2')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_4)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    # Вопрос 6
    if query.data == "ans5_button_2":
        await send_photo_url(context, 'https://storage.yandexcloud.net/pddlife/abm/n3_6.jpg')
        await query.edit_message_text(text="Вопрос 6 \nПри повороте направо Вы: \n\n1. Имеете право проехать перекресток первым. \n2. Должны уступить дорогу только пешеходам. \n3. Должны уступить дорогу автомобилю с включенными проблесковым маячком и специальным звуковым сигналом, а также пешеходам. \n\n(см. на рис.6)")
        answer6 = [
            [InlineKeyboardButton("1", callback_data='ans6_button_1'),
             InlineKeyboardButton("2", callback_data='ans6_button_2'),
             InlineKeyboardButton("3", callback_data='ans6_button_3')]
        ]
        ans6_reply_markup = InlineKeyboardMarkup(answer6)
        await query.edit_message_reply_markup(reply_markup=ans6_reply_markup)

    # Ответы 6
    elif query.data == 'ans6_button_1':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 3.")
        next_quest_kb_6 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans6_button_3')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_6)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans6_button_2':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 3")
        next_quest_kb_6 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans6_button_3')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_6)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans6_button_3':
        await query.edit_message_text(text="✔Ответ верный✔. \nВодитель автомобиля с включенными проблесковым маячком синего цвета и специальным звуковым сигналом имеет преимущество перед другими участниками движения п.3.1. Значит, вы должны уступить ему дорогу и только после этого можете повернуть направо, уступая дорогу также и пешеходам п.3.2 и п.13.1.")
        time.sleep(15)
        

    # Вопрос 7
    if query.data == "ans6_button_3":
        await query.edit_message_text(text="Вопрос 7 \nВ каких случаях водитель не должен подавать сигнал указателями поворота? \n\n1. Только при отсутствии на дороге других участников движения. \n2. Только если сигнал может ввести в заблуждение других участников движения. \n3. В обоих перечисленных случаях. \n\n(вопрос без рисунка)")
        answer7 = [
            [InlineKeyboardButton("1", callback_data='ans7_button_1'),
             InlineKeyboardButton("2", callback_data='ans7_button_2'),
             InlineKeyboardButton("3", callback_data='ans7_button_3')]
        ]
        ans7_reply_markup = InlineKeyboardMarkup(answer7)
        await query.edit_message_reply_markup(reply_markup=ans7_reply_markup)

    # Ответы 7
    elif query.data == 'ans7_button_1':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 2")
        next_quest_kb_7 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans7_button_2')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_7)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans7_button_2':
        await query.edit_message_text(text="✔Ответ верный✔. \nВодитель не должен подавать предупредительный сигнал указателями поворота только в том случае, если этот сигнал может ввести в заблуждение других участников движения. Во всех других случаях он обязан информировать о своих намерениях включением сигнала даже при отсутствии на дороге других участников движения п.8.2.")
        time.sleep(15)
        

    elif query.data == 'ans7_button_3':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 2")
        next_quest_kb_7 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans7_button_2')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_7)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    # Вопрос 8
    if query.data == "ans7_button_2":
        await send_photo_url(context, 'https://storage.yandexcloud.net/pddlife/abm/n3_8.jpg')
        await query.edit_message_text(text="Вопрос 8 \nВам разрешено выполнить поворот направо: \n\n1. Только по траектории А. \n2. Только по траектории Б. \n3. По любой траектории из указанных. \n\n(см. рис.7)")
        answer5 = [
            [InlineKeyboardButton("1", callback_data='ans8_button_1'),
             InlineKeyboardButton("2", callback_data='ans8_button_2'),
             InlineKeyboardButton("3", callback_data='ans8_button_3')]
        ]
        ans5_reply_markup = InlineKeyboardMarkup(answer5)
        await query.edit_message_reply_markup(reply_markup=ans5_reply_markup)

    # Ответы 8
    elif query.data == 'ans8_button_1':
        await query.edit_message_text(text="✔Ответ верный✔. \nПоворачивая направо, вы должны двигаться ближе к правому краю проезжей части, т.е. по траектории А п.8.6.")
        time.sleep(15)
        

    elif query.data == 'ans8_button_2':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 2")
        next_quest_kb_8 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans8_button_1')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_8)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans8_button_3':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 2")
        next_quest_kb_8 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans8_button_1')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_8)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    # Вопрос 9
    if query.data == "ans8_button_1":
        await send_photo_url(context, 'https://storage.yandexcloud.net/pddlife/abm/n3_9.jpg')
        await query.edit_message_text(text="Вопрос 9 \nРазрешается ли Вам выполнить разворот на перекрестке по указанной траектории? \n\n1. Разрешается. \n2. Разрешается, если видимость дороги не менее 100 м. \n3. Запрещается. \n\n(см. рис.8)")
        answer9 = [
            [InlineKeyboardButton("1", callback_data='ans9_button_1'),
             InlineKeyboardButton("2", callback_data='ans9_button_2'),
             InlineKeyboardButton("3", callback_data='ans9_button_3')]
        ]
        ans9_reply_markup = InlineKeyboardMarkup(answer9)
        await query.edit_message_reply_markup(reply_markup=ans9_reply_markup)

    # Ответы 9
    elif query.data == 'ans9_button_1':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 3")
        next_quest_kb_9 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans9_button_3')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_9)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans9_button_2':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 3")
        next_quest_kb_9 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans9_button_3')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_9)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans9_button_3':
        await query.edit_message_text(text="✔Ответ верный✔. \nНа перекрестке Вы можете совершить разворот только из крайнего левого положения п.8.5.")
        time.sleep(15)
        

    # Вопрос 10
    if query.data == "ans9_button_3":
        await send_photo_url(context, 'https://storage.yandexcloud.net/pddlife/abm/n3_10.jpg')
        await query.edit_message_text(text="Вопрос 10 \nПо какой полосе Вы имеете право двигаться с максимально разрешенной скоростью вне населенных пунктов? \n\n1. Только по правой. \n2. Только по левой. \n3. По любой. \n\n(см. рис.9)")
        answer10 = [
            [InlineKeyboardButton("1", callback_data='ans10_button_1'),
             InlineKeyboardButton("2", callback_data='ans10_button_2'),
             InlineKeyboardButton("3", callback_data='ans10_button_3')]
        ]
        ans10_reply_markup = InlineKeyboardMarkup(answer10)
        await query.edit_message_reply_markup(reply_markup=ans10_reply_markup)

    # Ответы 10
    elif query.data == 'ans10_button_1':
        await query.edit_message_text(text="✔Ответ верный✔. \nВне населенного пункта запрещается занимать левые полосы при свободной правой п.9.4. В данной ситуации вы можете двигаться только по правой полосе.")
        time.sleep(15)
        

    elif query.data == 'ans10_button_2':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 1")
        next_quest_kb_10 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans10_button_1')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_10)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans10_button_3':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 1")
        next_quest_kb_10 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans10_button_1')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_10)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    # Вопрос 11
    if query.data == "ans10_button_1":
        await query.edit_message_text(text="Вопрос 11 \nВ каком случае водитель может начать обгон, если такой маневр на данном участке дороги не запрещен? \n\n1. Только если полоса, предназначенная для встречного движения, свободна на достаточном для обгона расстоянии. \n2. Только если его транспортное средство никто не обгоняет. \n3. В случае, если выполнены оба условия. \n\n(вопрос без рисунка)")
        answer11 = [
            [InlineKeyboardButton("1", callback_data='ans11_button_1'),
             InlineKeyboardButton("2", callback_data='ans11_button_2'),
             InlineKeyboardButton("3", callback_data='ans11_button_3')]
        ]
        ans11_reply_markup = InlineKeyboardMarkup(answer11)
        await query.edit_message_reply_markup(reply_markup=ans11_reply_markup)

    # Ответы 11
    elif query.data == 'ans11_button_1':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 3")
        next_quest_kb_11 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans11_button_3')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_11)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans11_button_2':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 2")
        next_quest_kb_11 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans11_button_3')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_11)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans11_button_3':
        await query.edit_message_text(text="✔Ответ верный✔. \nВодитель может начать обгон с выездом на полосу встречного движения, если не создаст помех не только встречным, но и обгоняющим ТС п.11.1 ПДД.")
        time.sleep(15)
        

    # Вопрос 12
    if query.data == "ans11_button_3":
        await send_photo_url(context, 'https://storage.yandexcloud.net/pddlife/abm/n3_12.jpg')
        await query.edit_message_text(text="Вопрос 12 \nКто из водителей нарушил правила стоянки? \n\n1. Оба. \n2. Только водитель автомобиля. \n3. Только водитель мотоцикла. \n4. Никто не нарушил. \n\n(см. рис.10)")
        answer5 = [
            [InlineKeyboardButton("1", callback_data='ans12_button_1'),
             InlineKeyboardButton("2", callback_data='ans12_button_2'),
             InlineKeyboardButton("3", callback_data='ans12_button_3'),
             InlineKeyboardButton("4", callback_data='ans12_button_4')]
        ]
        ans5_reply_markup = InlineKeyboardMarkup(answer5)
        await query.edit_message_reply_markup(reply_markup=ans5_reply_markup)

    # Ответы 12
    elif query.data == 'ans12_button_1':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 2")
        next_quest_kb_12 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans12_button_2')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_12)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans12_button_2':
        await query.edit_message_text(text="✔Ответ верный✔. \nВ данной ситуации нарушил правила стоянки только водитель легкового автомобиля, так как использовал для стоянки тротуар п.12.2. Стоянка на расстоянии менее 3 м до прерывистой линии разметки не запрещается.")
        time.sleep(15)
        

    elif query.data == 'ans12_button_3':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 2")
        next_quest_kb_12 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans12_button_2')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_12)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans12_button_4':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 2")
        next_quest_kb_12 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans12_button_2')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_12)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    # Вопрос 13
    if query.data == "ans12_button_2":
        await send_photo_url(context, 'https://storage.yandexcloud.net/pddlife/abm/n3_13.jpg')
        await query.edit_message_text(text="Вопрос 13 \nПри движении прямо Вы: \n\n1. Должны остановиться перед стоп-линией. \n2. Можете продолжить движение через перекресток без остановки. \n3. Должны уступить дорогу транспортным средствам, движущимся с других направлений. \n\n(см. рис.11)")
        answer13 = [
            [InlineKeyboardButton("1", callback_data='ans13_button_1'),
             InlineKeyboardButton("2", callback_data='ans13_button_2'),
             InlineKeyboardButton("3", callback_data='ans13_button_3')]
        ]
        ans13_reply_markup = InlineKeyboardMarkup(answer13)
        await query.edit_message_reply_markup(reply_markup=ans13_reply_markup)

    # Ответы 13
    elif query.data == 'ans13_button_1':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 2")
        next_quest_kb_13 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans13_button_2')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_13)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans13_button_2':
        await query.edit_message_text(text="✔Ответ верный✔. \nВы приближаетесь к регулируемому перекрестку и можете проехать его без остановки, поскольку включен зеленый, разрешающий, сигнал светофора п.6.15. Выполнять требование знака 2.5  'Движение без остановки запрещено' Вы должны только в том случае, если светофор будет выключен или переведен на режим желтого мигающего сигнала п.13.3 ПДД.")
        time.sleep(15)
        

    elif query.data == 'ans13_button_3':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 2")
        next_quest_kb_13 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans13_button_2')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_13)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    # Вопрос 14
    if query.data == "ans13_button_2":
        await send_photo_url(context, 'https://storage.yandexcloud.net/pddlife/abm/n3_14.jpg')
        await query.edit_message_text(text="Вопрос 14 \nВы намерены повернуть направо. Ваши действия? \n\n1. Проедете перекресток первым. \n2. Уступите дорогу легковому автомобилю. \n3. Уступите дорогу обоим транспортным средствам. \n\n(см. рис.12)")
        answer14 = [
            [InlineKeyboardButton("1", callback_data='ans14_button_1'),
             InlineKeyboardButton("2", callback_data='ans14_button_2'),
             InlineKeyboardButton("3", callback_data='ans14_button_3')]
        ]
        ans14_reply_markup = InlineKeyboardMarkup(answer14)
        await query.edit_message_reply_markup(reply_markup=ans14_reply_markup)

    # Ответы 14
    elif query.data == 'ans14_button_1':
        await query.edit_message_text(text="✔Ответ верный✔. \nНа данном перекрестке дорогу мотоциклу уступать не надо - он не является помехой справа п.13.11 ПДД, поскольку, при повороте направо Вы не пересекаете путь его движения. Перед легковым автомобилем, поворачивающим налево, преимущество за Вами п.13.12 ПДД.")
        time.sleep(15)
        

    elif query.data == 'ans14_button_2':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 1")
        next_quest_kb_14 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans14_button_1')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_14)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans14_button_3':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 1")
        next_quest_kb_14 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans14_button_1')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_14)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    # Вопрос 15
    if query.data == "ans14_button_1":
        await send_photo_url(context, 'https://storage.yandexcloud.net/pddlife/abm/n3_15.jpg')
        await query.edit_message_text(text="Вопрос 15 \nКому Вы обязаны уступить дорогу при повороте налево? \n\n1. Трамваям А и Б. \n2. Трамваю А и легковому автомобилю. \n3. Только трамваю А. \n4. Никому. \n\n(см. рис.13)") 
        answer15 = [
            [InlineKeyboardButton("1", callback_data='ans15_button_1'),
             InlineKeyboardButton("2", callback_data='ans15_button_2'),
             InlineKeyboardButton("3", callback_data='ans15_button_3'),
             InlineKeyboardButton("4", callback_data='ans15_button_4')]
        ]
        ans15_reply_markup = InlineKeyboardMarkup(answer15)
        await query.edit_message_reply_markup(reply_markup=ans15_reply_markup)

    # Ответы 15
    elif query.data == 'ans15_button_1':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 3")
        next_quest_kb_15 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans15_button_3')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_15)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans15_button_2':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 1")
        next_quest_kb_15 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans15_button_3')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_15)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans15_button_3':
        await query.edit_message_text(text="✔Ответ верный✔. \nДвигаясь на данном перекрестке по направлению главной дороги (знаки 2.1  'Главная дорога' и 8.13  'Направление главной дороги'), для определения очередности проезда с трамваем А и легковым автомобилем Вы должны руководствоваться правилами проезда перекрестков равнозначных дорог п.13.10 ПДД. В соответствии с ними преимущество имеет трамвай А п.13.11 ПДД. По этим же правилам легковой автомобиль, находящийся от Вас слева, обязан уступить дорогу. Также уступает Вам дорогу и трамвай Б, движущийся по второстепенной дороге п.13.9 ПДД.")
        time.sleep(15)
        

    elif query.data == 'ans15_button_4':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 3")
        next_quest_kb_15 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans15_button_3')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_15)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    # Вопрос 16
    if query.data == "ans15_button_3":
        await send_photo_url(context, 'https://storage.yandexcloud.net/pddlife/abm/n3_16.jpg')
        await query.edit_message_text(text="Вопрос 16 \nКто из водителей нарушил правила остановки? \n\n1. Только водитель легкового автомобиля. \n2. Только водитель грузового автомобиля. \n3. Оба. \n\n(см. рис.14)")
        answer16 = [
            [InlineKeyboardButton("1", callback_data='ans16_button_1'),
             InlineKeyboardButton("2", callback_data='ans16_button_2'),
             InlineKeyboardButton("3", callback_data='ans16_button_3')]
        ]
        ans16_reply_markup = InlineKeyboardMarkup(answer16)
        await query.edit_message_reply_markup(reply_markup=ans16_reply_markup)

    # Ответы 16
    elif query.data == 'ans16_button_1':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 3")
        next_quest_kb_16 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans16_button_3')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_16)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans16_button_2':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 3")
        next_quest_kb_16 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans16_button_3')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_16)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans16_button_3':
        await query.edit_message_text(text="✔Ответ верный✔. \nОба водителя нарушили правила остановки, так как на автомагистралях остановка разрешена только на специальных площадках для стоянки, обозначенных знаками 6.4  «Парковка (парковочное место)» или 7.11  «Место отдыха» п.16.1.")
        time.sleep(15)
        

    # Вопрос 17
    if query.data == "ans16_button_3":
        await query.edit_message_text(text="Вопрос 17 \nКакое оборудование должно иметь механическое транспортное средство, используемое для обучения вождению? \n\n1. Дополнительные педали привода сцепления (кроме транспортных средств с автоматической трансмиссией) и тормоза.\n2. Зеркало заднего вида для обучающего вождению. \n3. Опознавательные знаки «Учебное транспортное средство». \n4. Все перечисленное оборудование. \n\n(вопрос без рисунка)")
        answer17 = [
            [InlineKeyboardButton("1", callback_data='ans17_button_1'),
             InlineKeyboardButton("2", callback_data='ans17_button_2'),
             InlineKeyboardButton("3", callback_data='ans17_button_3'),
             InlineKeyboardButton("4", callback_data='ans17_button_4')]
        ]
        ans17_reply_markup = InlineKeyboardMarkup(answer17)
        await query.edit_message_reply_markup(reply_markup=ans17_reply_markup)

    # Ответы 17
    elif query.data == 'ans17_button_1':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 4")
        next_quest_kb_17 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans17_button_4')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_17)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans17_button_2':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 4")
        next_quest_kb_17 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans17_button_4')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_17)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans17_button_3':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 4")
        next_quest_kb_17 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans17_button_4')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_17)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans17_button_4':
        await query.edit_message_text(text="✔Ответ верный✔. \nМеханическое ТС, используемое для обучения вождению, должно быть оборудовано дополнительными педалями привода сцепление (кроме ТС с автоматической трансмиссией) и тормоза, зеркалом заднего вида для обучающего вождению и опознавательными знаками «Учебное транспортное средство» п.21.5 Допуск п.5 и Допуск п.8. P.S. Новый вопрос от 2 января 2020.")
        time.sleep(15)
        

    # Вопрос 18
    if query.data == "ans17_button_4":
        await query.edit_message_text(text="Вопрос 18 \nВ каких случаях запрещается эксплуатация мотоцикла? \n\n1. Подножки или рукоятки пассажиров на седле не имеют прорезиненного покрытия. \n2. Имеется люфт в соединениях рамы мотоцикла с рамой бокового прицепа. \n3. Отсутствует огнетушитель. \n\n(вопрос без рисунка)")
        answer18 = [
            [InlineKeyboardButton("1", callback_data='ans18_button_1'),
             InlineKeyboardButton("2", callback_data='ans18_button_2'),
             InlineKeyboardButton("3", callback_data='ans18_button_3')]
        ]
        ans18_reply_markup = InlineKeyboardMarkup(answer18)
        await query.edit_message_reply_markup(reply_markup=ans18_reply_markup)

    # Ответы 18
    elif query.data == 'ans18_button_1':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 2")
        next_quest_kb_18 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans18_button_2')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_18)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans18_button_2':
        await query.edit_message_text(text="✔Ответ верный✔. \nМотоциклы относятся к категории мототранспортных средств, указанных в Приложении 1 к техническому регламенту «О безопасности колесных ТС» - «Классификация ТС по категориям», которым присвоена литера L. Запрещается эксплуатация ТС категории L, имеющих следующие неисправности: ... имеется люфт в соединениях рамы ТС с рамой бокового прицепа (Перечень п.9.8).")
        time.sleep(15)
        

    elif query.data == 'ans18_button_3':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 2")
        next_quest_kb_18 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans18_button_2')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_18)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    # Вопрос 19
    if query.data == "ans18_button_2":
        await query.edit_message_text(text="Вопрос 19 \nНа повороте возник занос задней оси переднеприводного автомобиля. Ваши действия? \n\n1. Уменьшите подачу топлива, рулевым колесом стабилизируете движение. \n2. Притормозите и повернете рулевое колесо в сторону заноса. \n3. Слегка увеличите подачу топлива, корректируя направление движения рулевым колесом. \n4. Значительно увеличите подачу топлива, не меняя положения рулевого колеса. \n\n(вопрос без рисунка")
        answer19 = [
            [InlineKeyboardButton("1", callback_data='ans19_button_1'),
             InlineKeyboardButton("2", callback_data='ans19_button_2'),
             InlineKeyboardButton("3", callback_data='ans19_button_3'),
             InlineKeyboardButton("4", callback_data='ans19_button_4')]
        ]
        ans19_reply_markup = InlineKeyboardMarkup(answer19)
        await query.edit_message_reply_markup(reply_markup=ans19_reply_markup)

    # Ответы 19
    elif query.data == 'ans19_button_1':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 3")
        next_quest_kb_19 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans19_button_3')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_19)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans19_button_2':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 3")
        next_quest_kb_19 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans19_button_3')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_19)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans19_button_3':
        await query.edit_message_text(text="✔Ответ верный✔. \nЗанос переднеприводного автомобиля может возникнуть при торможении на повороте из-за 'набегания' задних колес на передние. В этом случае целесообразно слегка увеличить подачу топлива (не вызывая пробуксовки передних колес) и дальнейшим поворотом рулевого колеса скорректировать направление движения автомобиля. Следует помнить, что на заднеприводном автомобиле увеличение скорости может только усилить возникший занос.")
        time.sleep(15)
        

    elif query.data == 'ans19_button_4':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 3")
        next_quest_kb_19 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='ans19_button_3')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_19)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)


    # Вопрос 20
    if query.data == "ans19_button_3":
        await query.edit_message_text(text="Вопрос 20 \nКакие сведения необходимо сообщить диспетчеру для вызова скорой медицинской помощи при дорожно-транспортном происшествии (ДТП)?\n\n1. Указать общеизвестные ориентиры, ближайшие к месту ДТП. Сообщить о количестве пострадавших, указать их пол и возраст. \n2. Указать улицу и номер дома, ближайшего к месту ДТП. Сообщить, кто пострадал в ДТП (пешеход, водитель автомобиля или пассажиры), и описать травмы, которые они получили. \n3. Указать место ДТП (назвать улицу, номер дома и общеизвестные ориентиры, ближайшие к месту ДТП). Сообщить: количество пострадавших, их пол, примерный возраст, наличие у них сознания, дыхания, кровообращения, а также сильного кровотечения, переломов и других травм. Дождаться сообщения диспетчера о том, что вызов принят. \n\n(вопрос без рисунка)")
        answer5 = [
            [InlineKeyboardButton("1", callback_data='ans10_button_1'),
             InlineKeyboardButton("2", callback_data='ans20_button_2'),
             InlineKeyboardButton("3", callback_data='ans20_button_3')]
        ]
        ans5_reply_markup = InlineKeyboardMarkup(answer5)
        await query.edit_message_reply_markup(reply_markup=ans5_reply_markup)

    # Ответы 20
    elif query.data == 'ans20_button_1':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 3. \nБыстрота приезда скорой медицинской помощи во многом зависит от четкости описания местонахождения ДТП. От указанного числа пострадавших зависит количество автомобилей скорой медицинской помощи, которые требуются на месте ДТП. Сведения о наличии или отсутствии у пострадавших сознания, дыхания, кровообращения, а также сильного кровотечения, переломов и других травм необходимы диспетчеру для определения специализации бригады скорой медицинской помощи.")
        next_quest_kb_20 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='end_quest_button')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_20)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans20_button_1':
        await query.edit_message_text(text="❌Ответ неверный❌, правильный ответ 3. \nБыстрота приезда скорой медицинской помощи во многом зависит от четкости описания местонахождения ДТП. От указанного числа пострадавших зависит количество автомобилей скорой медицинской помощи, которые требуются на месте ДТП. Сведения о наличии или отсутствии у пострадавших сознания, дыхания, кровообращения, а также сильного кровотечения, переломов и других травм необходимы диспетчеру для определения специализации бригады скорой медицинской помощи.")
        next_quest_kb_20 = [[InlineKeyboardButton("Перейти к следующему вопросу", callback_data='end_quest_button')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_20)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    elif query.data == 'ans20_button_3':
        await query.edit_message_text(text="✔Ответ верный✔. \nБыстрота приезда скорой медицинской помощи во многом зависит от четкости описания местонахождения ДТП. От указанного числа пострадавших зависит количество автомобилей скорой медицинской помощи, которые требуются на месте ДТП. Сведения о наличии или отсутствии у пострадавших сознания, дыхания, кровообращения, а также сильного кровотечения, переломов и других травм необходимы диспетчеру для определения специализации бригады скорой медицинской помощи.")
        next_quest_kb_20 = [[InlineKeyboardButton("Закончить тест", callback_data='end_quest_button')]]
        next_quest_reply_markup = InlineKeyboardMarkup(next_quest_kb_20)
        await query.edit_message_reply_markup(reply_markup=next_quest_reply_markup)
        

    if query.data == "end_quest_button":
        await query.edit_message_text(text=f"Вы сдали экзамен! Но учтите, что более 2-х ошибок это не сдача экзамена!")


    # эта кнопка если не готов
    elif query.data == "new_button_2":
        await query.edit_message_text(text="Иди готовься). Как подготовишься заново напиши /start)")


# Функция для отправки фотографии
async def send_photo_url(context, img_url):
    try:
        await context.bot.send_photo(chat_id=context._chat_id, photo=img_url)
    except Exception as e:
        print(f"Error sending photo: {e}")
   

# Функция-обработчик всех текстовых сообщений
async def echo(update: Update, context: CallbackContext):
    await update.message.reply_text(update.message.text)


if __name__ == '__main__':
    # Создаем приложение
    application = ApplicationBuilder().token(TOKEN).build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запускаем бота
    print("Бот запущен...")
    application.run_polling()