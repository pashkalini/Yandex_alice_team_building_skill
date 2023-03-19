import random
import threading
import time

# функция для отправки ответа
def make_response(text, tts=None):
    return {
        'response': {
            'text': text,
            'tts': tts,
        },
        'version': '1.0',
    }

# def repeat_message():
#     with open("text_to_repeat.txt", 'r', encoding='utf8') as f:
#         msg = f.read()
#     return msg

# def save_msg_text(msg):
#     with open("text_to_repeat.txt", 'w', encoding='utf8') as f:
#         f.write(msg)
#         return

# тексты для перебивок музыки через каждые 2 минуты
# text_18_min = "Первые две минуты прошли. Вечеринка в самом начале, продолжаем набирать обороты!"
# text_16_min = "Еще две минутки закончились. Продолжайте, у вас еще 16 минут."
text_14_min = "Первые шесть минут прошли так же быстро, как моя молодость. Но да ладно, продолжаем играть."
# text_12_min = "Ку-ку, прошло еще две минут. У вас в запасе еще 12!"
# text_10_min = "Очередные две минуты прошли! Остается - 10, дерзайте!"
text_8_min = "Вижу, все идет по плану! Но на игру осталось 8 минут."
# text_6_min = "Прошло еще две минуты! Осталось 6 минут."
text_4_min = "Кукусики! Смотрю, знакомство в самом разгаре. Поторопитесь узнать друг друга, у вас есть 4 минуты."
text_2_min = "Такс, осталась всего двухминуточка! Давайте запрыгнем в последний вагон."
text_fin_1 = "О, оу! Время вышло! Если хотите еще каких-нибудь активностей, можете спросить меня: «‎Что ты умеешь?»"
text_fin_2 = "Ну всё, время вышло! Хорошо, что познакомились! Если хотите продолжить, можете спросить меня: «‎Что ты умеешь?»"

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
    response_3 = "Ничего в голову не приходит. Надо записаться на курсы по развитию фантазии. Чтобы узнать, какие команды у меня есть скажите - \"Помощь\""
    responses = [response_1, response_2, response_3]
    random_response = random.choice(responses)
    return make_response(random_response)

# Выбирает одну из активностей для знакомства
def start_meeting_activity(event):
    bg = bg_music()
    bg_tts_1 = bg[1]
    bg_tts_2 = bg[2]
    bg_tts_3 = bg[3]
    bg_tts_4 = bg[4]
    bg_tts_5 = bg[5]
    bg_text = bg[0]
    with open("activity_1.txt", 'r', encoding='utf8') as text_1, \
            open ("activity_2.txt", 'r', encoding='utf8') as text_2, \
            open ("activity_3.txt", 'r', encoding='utf8') as text_3:
        activities = [text_1, text_2, text_3]
        random_text = random.choice(activities)
        activity_text = random_text.read() + bg_text
        return make_response(activity_text, activity_text + bg_tts_1 + text_8_min + \
                             bg_tts_2 + bg_tts_3 + text_4_min + bg_tts_4 + text_2_min + bg_tts_5 + text_fin_2)

# выбирает одну из игр
def start_game(event):
    bg = bg_music()
    bg_tts_1 = bg[1]
    bg_tts_2 = bg[2]
    bg_tts_3 = bg[3]
    bg_tts_4 = bg[4]
    bg_tts_5 = bg[5]
    bg_tts_6 = bg[6]
    bg_tts_7 = bg[7]
    bg_tts_8 = bg[8]
    bg_tts_9 = bg[9]
    bg_tts_10 = bg[10]
    bg_text = bg[0]
    with open("game_1.txt", 'r', encoding='utf8') as text_1, \
            open ("game_2.txt", 'r', encoding='utf8') as text_2, \
            open ("game_3.txt", 'r', encoding='utf8') as text_3:
        games = [text_1, text_2, text_3]
        random_text = random.choice(games)
        game_text = random_text.read() + bg_text
        return make_response(game_text, game_text + bg_tts_1 + bg_tts_2 + \
                             bg_tts_3 + text_14_min + bg_tts_4 + bg_tts_5 + \
                             bg_tts_6 + text_8_min + bg_tts_7 + bg_tts_8 + text_4_min + \
                             bg_tts_9 + text_2_min + bg_tts_10 + text_fin_1)

# что ты умеешь
def what_can_you_do(event):
    text = "Я знаю, как вас познакомить или избавить от скуки. Включусь в вашу компанию, поболтаем, поиграем.\
            \nА ещё могу  предложить тему для разговора или включить песню, которую вы точно знаете.\
            \nХотите познакомиться или сыграть в игру?"
    tts = "Я знаю, как вас познакомить или избавить от скуки. Включусь в вашу компанию, поболтаем, поиграем. \
            А ещё могу  предложить тему для разговора или включить песню, которую вы точно знаете. sil <[200]>\
            Хотите познакомиться или сыграть в игру?"
    return make_response(text, tts)

# помощь (перечисление доступных команд)
def help(event):
    with open("help_commands.txt", 'r', encoding='utf8') as commands:
        return make_response(commands.read())

# выбирает рандомно игру или активность
def game_vs_activity(event):
    game = start_game(event)
    activity = start_meeting_activity(event)
    random_activity = [activity, game]
    return random.choice(random_activity)

# предлагает тему для разговора
def theme_variants(event):
    text = "Предлагаю каждому по очереди ответить на такой вопрос: "
    bg = bg_music()
    bg_tts_1 = bg[1]
    bg_tts_2 = bg[2]
    bg_tts_3 = bg[3]
    bg_tts_4 = bg[4]
    bg_tts_5 = bg[5]
    bg_text = bg[0]
    text_timer = "\n\nЯ засеку 10 минут, чтобы вы могли поболтать."
    themes = ["На какие кружки вас водили родители в детстве?", \
              "Какие неловкие ситуации у вас были?", \
              "Что бы вы не стали делать, даже за миллион долларов?", \
              "Кто каким спортом занимается?", \
              "Вы когда-нибудь сталкивались с чем-то мистическим?", \
              "Как вы относитесь к животным?", \
              "Что вы смотрите на YouTube?", \
              "Какой ваш любимый язык программирования и почему?", \
              "Любите путешествовать? Куда ездили последний раз?",
              "Вы когда-нибудь сталкивались с чем-то мистическим?"]
    theme_text = text + random.choice(themes) + text_timer + bg_text
    return make_response(theme_text, \
                         theme_text + bg_tts_1 + text_8_min + bg_tts_2 + \
                         bg_tts_3 + text_4_min + bg_tts_4 + text_2_min + bg_tts_5 + text_fin_1)

# обработка команд по типу "дальше", "давай другое"
def another_activity(event):
    game = start_game(event)
    activity = start_meeting_activity(event)
    theme = theme_variants(event)
    random_activity = [activity, game, theme]
    return random.choice(random_activity)

# NEW обход сценария - "включись в тусовку"
def start_party(event):
    text = "А я с вами! Познакомимся или повеселимся?"
    return make_response(text)

# NEW обход сценария - игра для компании
def start_team_game(event):
    game = start_game(event)
    return make_response(game)

# NEW обход сценария - включает фоновую музыку по команде "создай атмосферу для знакомства"
def create_atmosphere(event):
    bg_tts = bg_music()[1]
    text_1 = "Включаю музыку для вас."
    text_2 = "Вас познакомить?"
    return make_response(text_1, text_1 + bg_tts + text_2)

# включает песню, которую знают все
def play_music(event):
    text = "Включаю, эту песню вы точно знаете!"
    tts_1 = "<speaker audio=\"dialogs-upload/9298f90d-da88-42dd-bafc-253e0505f2f6/2d3ac5af-13a5-4586-bba2-8522512d8f4a.opus\">"
    tts_2 = "<speaker audio=\"dialogs-upload/9298f90d-da88-42dd-bafc-253e0505f2f6/9a8114c7-6428-4835-a9c2-8dd3ab41c490.opus\">"
    tts_3 = "<speaker audio=\"dialogs-upload/9298f90d-da88-42dd-bafc-253e0505f2f6/8e6febcd-0972-4f67-a095-2f622350858e.opus\">"
    tts_4 = "<speaker audio=\"dialogs-upload/9298f90d-da88-42dd-bafc-253e0505f2f6/6615efee-4ee3-4fb9-863b-35932ec3e5d0.opus\">"
    tts_5 = "<speaker audio=\"dialogs-upload/9298f90d-da88-42dd-bafc-253e0505f2f6/ffd20248-52d4-4070-83d0-651fdd18f666.opus\">"
    music_tts = [tts_1, tts_2, tts_3, tts_4, tts_5]
    next_text = "Вот это я понимаю классика! Аж настроение поднялось. Надеюсь и вам песенка понравилась. \
    Если хотите продолжить тусовку, спросите: «‎Что ты умеешь?»"
    return make_response(text + "\n\n 🎶 воспроизводится музыка", text + random.choice(music_tts) + next_text)

# фоновая музыка
def bg_music():
    # длительность трека - 2 минуты
    text = "\n\nА чтобы вы про меня не забыли, включу фоновую музыку."
    tts_1 = "<speaker audio=\"dialogs-upload/9298f90d-da88-42dd-bafc-253e0505f2f6/c0c15b91-4744-4561-b54b-8fce0fc5dffa.opus\">"
    tts_2 = "<speaker audio=\"dialogs-upload/9298f90d-da88-42dd-bafc-253e0505f2f6/2260fe71-abf5-4a5c-9175-0f41751b903c.opus\">"
    tts_3 = "<speaker audio=\"dialogs-upload/9298f90d-da88-42dd-bafc-253e0505f2f6/4aaf4efc-ac5a-4a74-a98b-2ab6e2db7ee4.opus\">"
    tts_4 = "<speaker audio=\"dialogs-upload/9298f90d-da88-42dd-bafc-253e0505f2f6/9446b849-a407-4f78-ab7d-cc6fc9f84935.opus\">"
    tts_5 = "<speaker audio=\"dialogs-upload/9298f90d-da88-42dd-bafc-253e0505f2f6/8eafbf56-cb54-4288-8646-6a79f3b27546.opus\">"
    tts_6 = "<speaker audio=\"dialogs-upload/9298f90d-da88-42dd-bafc-253e0505f2f6/79db73ad-67b1-4377-a7b3-b843a649c067.opus\">"
    bg_tts = [tts_1, tts_2, tts_3, tts_4, tts_5, tts_6]
    # выбираем 10 рандомных фоновых песен для чередования
    bg = [text + "\n\n 🎶 воспроизводится музыка", random.choice(bg_tts), random.choice(bg_tts), random.choice(bg_tts), random.choice(bg_tts), random.choice(bg_tts), \
          random.choice(bg_tts), random.choice(bg_tts), random.choice(bg_tts), random.choice(bg_tts), random.choice(bg_tts)]
    return bg

# основной обработчик сценариев
def handler(event, context):
    intents = event['request']['nlu']['intents']
    if event['session']['new']:
        msg = welcome_message(event)
        # save_msg_text(msg)
        return msg
    elif 'start_meeting_activity' in intents:
        msg = start_meeting_activity(event)
        return msg
    elif 'start_game' in intents:
        msg = start_game(event)
        return msg
    elif 'what_can_you_do' in intents:
        msg = what_can_you_do(event)
        return msg
    elif 'help' in intents:
        msg = help(event)
        return msg
    elif 'game_vs_activity' in intents:
        msg = game_vs_activity(event)
        return msg
    elif 'theme_variants' in intents:
        msg = theme_variants(event)
        return msg
    elif 'another_activity' in intents:
        msg = another_activity(event)
        return msg
    elif 'play_music' in intents:
        msg = play_music(event)
        return msg
    elif 'start_party' in intents:
        return start_party(event)
    elif 'start_team_game' in intents:
        return start_team_game(event)
    elif 'create_atmosphere' in intents:
        return create_atmosphere(event)
    # elif 'repeat_message' in intents:
    #     repeat_message
    else:
        return fallback(event)
