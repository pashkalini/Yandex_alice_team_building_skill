import random


# функция для отправки ответа
def make_response(text, tts=None):
    return {
        'response': {
            'text': text,
            'tts': tts,
        },
        'version': '1.0',
    }


# приветствует пользователя
def welcome_message(event):
    text = "Сегодня были пары? Кажется, я стала прогульщицей...\
    Ну ладно, хоть до вас дошла. Хотите познакомиться поближе или повеселиться?"
    tts = "sil <[300]> Сегодня были пары? Кажется, я стала прогульщицей...sil <[300]>\
    Ну ладно, хоть до вас дошла. Хотите познакомиться поближе или повеселиться?"
    return make_response(text, tts)


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
    bg = bg_music()
    bg_tts = bg[1]
    bg_text = bg[0]
    with open("activity_1.txt", 'r', encoding='utf8') as text_1, \
            open("activity_2.txt", 'r', encoding='utf8') as text_2, \
            open("activity_3.txt", 'r', encoding='utf8') as text_3:
        activities = [text_1, text_2, text_3]
        random_text = random.choice(activities)
        activity_text = random_text.read() + bg_text
        return make_response(activity_text, activity_text + bg_tts)


# выбирает одну из игр
def start_game(event):
    bg = bg_music()
    bg_tts = bg[1]
    bg_text = bg[0]
    with open("game_1.txt", 'r', encoding='utf8') as text_1, \
            open("game_2.txt", 'r', encoding='utf8') as text_2, \
            open("game_3.txt", 'r', encoding='utf8') as text_3:
        games = [text_1, text_2, text_3]
        random_text = random.choice(games)
        game_text = random_text.read() + bg_text
        return make_response(game_text, game_text + bg_tts)


# что ты умеешь
def what_can_you_do(event):
    text = "Я знаю, как вас познакомить или избавить от скуки. Включусь в вашу компанию, поболтаем, поиграем. \
            А ещё могу  предложить тему для разговора.\
            Хотите познакомиться или сыграть в игру?"
    tts = "Я знаю, как вас познакомить или избавить от скуки. Включусь в вашу компанию, поболтаем, поиграем. \
            А ещё могу  предложить тему для разговора. sil <[200]>\
            Хотите познакомиться или сыграть в игру?"
    return make_response(text, tts)


# помощь (перечисление доступных команд)
def help(event):
    with open("help_commands.txt", 'r', encoding='utf8') as commands:
        return make_response(commands.read())


#  выбирает рандомно игру или активность
def game_vs_activity(event):
    game = start_game(event)
    activity = start_meeting_activity(event)
    random_activity = [activity, game]
    return random.choice(random_activity)


# предлагает тему для разговора
def theme_variants(event):
    text = "Предлагаю поболтать на такую тему: "
    bg = bg_music()
    bg_tts = bg[1]
    bg_text = bg[0]
    themes = ["На какие кружки вас водили родители в детстве?",
              "Неловкие ситуации.",
              "Что бы вы не стали делать, даже за миллион долларов?",
              "Кто каким спортом занимается?",
              "Мистические истории.",
              "Животные.",
              "Что вы смотрите на YouTube?",
              "Любимый язык программирования.",
              "Любите путешествовать? Куда ездили последний раз?"]
    theme_text = text + random.choice(themes) + bg_text
    return make_response(theme_text, theme_text + bg_tts)


# обработка команд по типу "дальше", "давай другое"
def another_activity(event):
    game = start_game(event)
    activity = start_meeting_activity(event)
    theme = theme_variants(event)
    random_activity = [activity, game, theme]
    return random.choice(random_activity)


# включает песню, которую знают все
def play_music(event):
    text = "Включаю, эту песню вы точно знаете!"
    tts_1 = "<speaker audio=\"dialogs-upload/9298f90d-da88-42dd-bafc-253e0505f2f6/2d3ac5af-13a5-4586-bba2" \
            "-8522512d8f4a.opus\">"
    tts_2 = "<speaker audio=\"dialogs-upload/9298f90d-da88-42dd-bafc-253e0505f2f6/9a8114c7-6428-4835-a9c2" \
            "-8dd3ab41c490.opus\">"
    tts_3 = "<speaker audio=\"dialogs-upload/9298f90d-da88-42dd-bafc-253e0505f2f6/8e6febcd-0972-4f67-a095" \
            "-2f622350858e.opus\">"
    tts_4 = "<speaker audio=\"dialogs-upload/9298f90d-da88-42dd-bafc-253e0505f2f6/6615efee-4ee3-4fb9-863b" \
            "-35932ec3e5d0.opus\">"
    tts_5 = "<speaker audio=\"dialogs-upload/9298f90d-da88-42dd-bafc-253e0505f2f6/2c6ce01b-7668-4130-9a84" \
            "-991db17f6bcd.opus\">"
    music_tts = [tts_1, tts_2, tts_3, tts_4, tts_5]
    return make_response(text, text + random.choice(music_tts))


# фоновая музыка
def bg_music():
    text = "\n\nА чтобы вы про меня не забыли, включу фоновую музыку."
    tts_1 = "<speaker audio=\"dialogs-upload/9298f90d-da88-42dd-bafc-253e0505f2f6/7ea00568-2068-453f-949f" \
            "-e03258f55f02.opus\">"
    tts_2 = "<speaker audio=\"dialogs-upload/9298f90d-da88-42dd-bafc-253e0505f2f6/d851b591-671c-4534-8e53" \
            "-3dea98483853.opus\">"
    tts_3 = "<speaker audio=\"dialogs-upload/9298f90d-da88-42dd-bafc-253e0505f2f6/cf64664f-31f7-47d5-92e3" \
            "-1e3b2cca9576.opus\">"
    bg_tts = [tts_1, tts_2, tts_3]
    bg = [text, random.choice(bg_tts)]
    return bg


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
    elif 'game_vs_activity' in intents:
        return game_vs_activity(event)
    elif 'theme_variants' in intents:
        return theme_variants(event)
    elif 'another_activity' in intents:
        return another_activity(event)
    elif 'play_music' in intents:
        return play_music(event)
    else:
        return fallback(event)
