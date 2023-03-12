import random


# функция для отправки ответа
def make_response(text):
    return {
        'response': {
            'text': text,
        },
        'version': '1.0',
    }


# приветствует пользователя
def welcome_message(event):
    text = "Сегодня были пары? Кажется, я стала прогульщицей...\
            Ну ладно, хоть до вас дошла. Хотите познакомиться поближе или повеселиться?"
    return make_response(text)


# обработка ошибки
def fallback(event):
    response_1 = "Ой, а что вы сказали? Не расслышала."
    response_2 = "До меня сегодня долго доходит. Что вы хотите сделать: познакомиться или повеселиться?"
    response_3 = "Ничего в голову не приходит. Надо записаться на курсы по развитию фантазии. Простите, что подвела."
    responses = [response_1, response_2, response_3]
    random_response = random.choice(responses)
    return make_response(random_response)


# Выбирает одну из активностей для знакомства
def start_meeting_activity(event):
    with open("activity_1.txt", 'r', encoding='utf8') as text_1, \
            open("activity_2.txt", 'r', encoding='utf8') as text_2, \
            open("activity_3.txt", 'r', encoding='utf8') as text_3:
        activities = [text_1, text_2, text_3]
        random_text = random.choice(activities)
        return make_response(random_text.read())


# выбирает одну из игр
def start_game(event):
    with open("game_1.txt", 'r', encoding='utf8') as text_1, \
            open("game_2.txt", 'r', encoding='utf8') as text_2, \
            open("game_3.txt.txt", 'r', encoding='utf8') as text_3:
        games = [text_1, text_2, text_3]
        random_text = random.choice(games)
        return make_response(random_text.read())


# что ты умеешь
def what_can_you_do(event):
    text = "Я знаю, как вас познакомить или избавить от скуки. Включусь в вашу компанию, поболтаем, поиграем. \
            Хотите познакомиться или сыграть в игру?"
    return make_response(text)


# помощь (перечисление доступных команд)
def help(event):
    with open("help_commands.txt", 'r', encoding='utf8') as commands:
        return make_response(commands.read())


# основной обработчик сценариев
def handler(event, context):
    intents = event['request']['nlu']['intents']
    if event['session']['new']:
        return welcome_message(event)
    elif 'start_meeting_activity' in intents:
        return start_meeting_activity(event)
    elif 'start_game' in intents:
        return start_game(event)
    elif 'what_can_you_do' in intents:
        return what_can_you_do(event)
    elif 'help' in intents:
        return help(event)
    else:
        return fallback(event)
