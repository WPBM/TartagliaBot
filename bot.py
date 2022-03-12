import telebot
import random
import game
from arts import art
from config import TOKEN
from facts import fact

Tartaglia = telebot.TeleBot(TOKEN)

@Tartaglia.message_handler(commands=['start'])
def start(message):
    Tartaglia.send_photo(message.chat.id, "https://portalvirtualreality.ru/wp-content/uploads/2020/11/%D1%82%D0%B0%D1%80%D1%82%D0%B0%D0%BB%D1%8C%D1%8F-%D1%87%D0%B0%D0%B9%D0%BB%D1%8C%D0%B4.png", caption = "Приветсвую, Вас, Анна!\nОдин Архонт попросил меня, чтобы я, в столь тёмные времена, составил Вам компанию.\nУверен, Вы наслышаны о моей великой персоне.")
    game.start = 0
    markup = telebot.types.ReplyKeyboardMarkup()
    buttonA = telebot.types.KeyboardButton("Портрет")
    buttonB = telebot.types.KeyboardButton("Реплика")
    buttonC = telebot.types.KeyboardButton("Игра")

    markup.row(buttonA,buttonB,buttonC)

    Tartaglia.send_message(message.chat.id,'Вы можете просить меня о следующем:\n1.Продемонстрировать Вам мой случайный портрет.\n2.Услышать реплику от меня обо всём, но в первую очередь, обо мне самом.\n3.Почувстсвовать себя в моей шкуре, сыграв в приключенческую игру.', reply_markup=markup)

@Tartaglia.message_handler(commands=['help'])
def help(message):
    Tartaglia.send_photo(message.chat.id, "http://sun9-63.userapi.com/sun9-69/impg/WI-yuFn8vzTnNXgYeh8ho5baaaaF04pOpFRCdA/JzAxeeVBoLA.jpg?size=564x296&quality=96&sign=c90b7d97d60a7af4021be5df3bd2ab00&type=album", caption = 'Главная кнопка игры - "Поиск", именно с помощью неё Вы будите находить подходящих монстров для сражения и получения опыта.\nПри каждом новом уровне Вам выдают пять очков атрибутов которые Вы можите вложить в атрибуты "Сила", "Ловкость" и "Интеллект".\nАтрибут "Сила" повышает наносимый Вами урон, а также немного повышает Вашу живучесть.\nАтрибут "Ловкость" повышает шанс критического поподания, а также шанс уклонения. На уровнях атрибута 10 и 20 "Ловкость" даёт Вам дополнительный удар.\nАтрибут "Выносливость" повышает Ваше здоровье.\nНе стоит пытаться драться против противников с более высоким уровнем, особенно на первых порах.\nПри смерти Аякса прогресс сбрасывается и игра начинается с начала.')

@Tartaglia.message_handler(content_types=['text'])
def arts(message):        
    if message.text == "Портрет":
        Tartaglia.send_photo(message.chat.id, random.choice(art))

    if message.text == "Реплика":
        Tartaglia.send_message(message.chat.id, random.choice(fact))


    if message.text == "Игра":
        if game.start == 0:
            markup = telebot.types.ReplyKeyboardMarkup()
            buttonA = telebot.types.KeyboardButton("Отправиться в Мондштадт")
            markup.row(buttonA)
            Tartaglia.send_photo(message.chat.id, "https://vgtimes.ru/uploads/posts/2021-05/77507_4_3.jpg",)
            Tartaglia.send_message(message.chat.id, "Вы - Аякс «Чайльд» Тарталья одинадцатый из Предвестников Фатуи. Будучи непревзойдённым воином, именно Вам достаются самые сложные и опасные задания. Так произошло и в этот раз.\nТейват на пороге Великой Войны Архонтов. В последние месяцы участились конфликты между Вашей родиной, могущественным и воинственным королевством Крио Архонта Царицы, и двумя державами - Мондштадтом, городом-государством под покровительством Анемо Архонта Барбатоса и Ли Юэ, королевством Гео Архонта Моракса.\nВследствие этого, Фатуи решила направить разведчиков в эти два королевства, с целью получения информации о военном положении держав, а также об их возможной готовности напасть на Снежную. \nК несчастью, разведчики перестали выходить на связь. Агенты Фатуи разузнали, что разведчика, направленного в Мондштадт, захватили в плен хиличурлы и держут его в заложиниках, охраняя большим числом войск. Второго же разведчика, отправленного в Ли Юэ, постигла участь ни чуть не лучше - его схватили геовишапы.\nИменно Вам поручено освободить разведчиков, дабы Царица смогла увидеть картину целиком и предпринять верные действия в эти непростые времена.\nСперва отправляйтесь в Мондштадт, а после - в Ли Юэ. Не медлите, Аякс, да прибудет с Вами Царица!", reply_markup=markup)

       
        if game.start > 0:    
            markup = telebot.types.ReplyKeyboardMarkup()
            buttonA = telebot.types.KeyboardButton("Поиск")
            buttonB = telebot.types.KeyboardButton("Аякс")
            buttonC = telebot.types.KeyboardButton("Локация")
            buttonN = telebot.types.KeyboardButton("В главное меню")

            markup.row(buttonA,buttonB,buttonC,buttonN)

            Tartaglia.send_message(message.chat.id,'Поиск - поиск противника.\nАякс - информация о герое.\nЛокация - информация о нынешней локации.\nВернуться назад - вернуться в главное меню.', reply_markup=markup)

    if message.text == "Отправиться в Мондштадт":
        Tartaglia.send_photo(message.chat.id, "https://st.renderu.com/image/1200x/532193",caption = "Вы прибыли в Мондштадт.\nАгент Фатуи направил Вас по следу хиличурлов.")
        markup = telebot.types.ReplyKeyboardMarkup()
        buttonA = telebot.types.KeyboardButton("Поиск")
        buttonB = telebot.types.KeyboardButton("Аякс")
        buttonC = telebot.types.KeyboardButton("Локация")
        buttonN = telebot.types.KeyboardButton("В главное меню")

        markup.row(buttonA,buttonB,buttonC,buttonN)

        Tartaglia.send_message(message.chat.id,'Поиск - поиск противника.\nАякс - информация о герое.\nЛокация - информация о нынешней локации.\nВернуться назад - вернуться в главное меню.', reply_markup=markup)
        game.start+=1

    if message.text == "В главное меню":
        markup = telebot.types.ReplyKeyboardMarkup()
        buttonA = telebot.types.KeyboardButton("Портрет")
        buttonB = telebot.types.KeyboardButton("Реплика")
        buttonC = telebot.types.KeyboardButton("Игра")

        markup.row(buttonA,buttonB,buttonC)

        Tartaglia.send_message(message.chat.id,'Вы можете просить меня о следующем:\n1.Продемонстрировать Вам мой случайный портрет.\n2.Услышать реплику от меня обо всём, но в первую очередь, обо мне самом.\n3.Почувстсвовать себя в моей шкуре, сыграв в приключенческую игру.', reply_markup=markup)


    if message.text == "Поиск":
        markup = telebot.types.ReplyKeyboardMarkup()
        buttonA = telebot.types.KeyboardButton("Атаковать")
        buttonB = telebot.types.KeyboardButton("Пропустить")
        buttonN = telebot.types.KeyboardButton("Назад")

        markup.row(buttonA,buttonB,buttonN)
        game.Ayaks.find(game.loc1)
        Tartaglia.send_photo(message.chat.id, game.warrior.photo, caption = f"\nВы наткнулись на {game.warrior.name} {game.warrior.level} уровня.", reply_markup=markup)

    if message.text == "Пропустить":
        Tartaglia.send_message(message.chat.id, 'Вы решили избежать битвы.')
        game.Ayaks.find(game.loc1)
        Tartaglia.send_photo(message.chat.id, game.warrior.photo, caption = f"\nВы наткнулись на {game.warrior.name} {game.warrior.level} уровня.")
        
    if message.text == "Атаковать":
        markup = telebot.types.ReplyKeyboardMarkup()
        buttonA = telebot.types.KeyboardButton("Нанести удар")

        markup.row(buttonA)

        Tartaglia.send_message(message.chat.id, "\nВы нападаете на ошеломлённого противника.", reply_markup=markup)

    if message.text == "Нанести удар":
        c = 0
        e = 0
        crit = random.randint(1,100)
        evasion = random.randint(1,100)
        for i in range(1,game.Ayaks.characteristic["Шанс критического удара"]+1):
            if i == crit:
                game.Ayaks.characteristic["Урон"]*=2
                c = 1     
        game.warrior.health-=game.Ayaks.characteristic["Урон"]
        if c == 1:
            Tartaglia.send_message(message.chat.id,f'\nАякс ударил {game.warrior.name} и нанёс ему критический урон! {game.Ayaks.characteristic["Урон"]} урона.\nУ {game.warrior.name} осталось {game.warrior.health} здоровья.')
            c = 0
            game.Ayaks.characteristic["Урон"]//=2
        elif c == 0:
            Tartaglia.send_message(message.chat.id, f'\nАякс ударил {game.warrior.name} и нанёс ему {game.Ayaks.characteristic["Урон"]} урона.\nУ {game.warrior.name} осталось {game.warrior.health} здоровья.')
        if game.Ayaks.attributes["Ловкость"] >= 10:
            crit = random.randint(1,100)
            for i in range(1,game.Ayaks.characteristic["Шанс критического удара"]+1):
                if i == crit:
                    game.Ayaks.characteristic["Урон"]*=2
                    c = 1
            game.warrior.health-=game.Ayaks.characteristic["Урон"]
            Tartaglia.send_message(message.chat.id, f'\nБлагодаря своей ловкости Аякс наносит дополнительный удар.')
            if c == 1:
                Tartaglia.send_message(message.chat.id, f'\nАякс ударил {game.warrior.name} и нанёс ему критический урон! {game.Ayaks.characteristic["Урон"]} урона.\nУ {game.warrior.name} осталось {game.warrior.health} здоровья.')
                c = 0
                game.Ayaks.characteristic["Урон"]//=2
            elif c == 0:
                Tartaglia.send_message(message.chat.id, f'\nАякс ударил {game.warrior.name} и нанёс ему {game.Ayaks.characteristic["Урон"]} урона.\nУ {game.warrior.name} осталось {game.warrior.health} здоровья.')
        if game.Ayaks.attributes["Ловкость"] >= 20:
            crit = random.randint(1,100)
            for i in range(1,game.Ayaks.characteristic["Шанс критического удара"]+1):
                if i == crit:
                    game.Ayaks.characteristic["Урон"]*=2
                    c = 1
            game.warrior.health-=game.Ayaks.characteristic["Урон"]
            Tartaglia.send_message(message.chat.id, f'\nБлагодаря своей ловкости Аякс наносит дополнительный удар.')
            if c == 1:
                Tartaglia.send_message(message.chat.id, f'\nАякс ударил {game.warrior.name} и нанёс ему критический урон! {game.Ayaks.characteristic["Урон"]} урона.\nУ {game.warrior.name} осталось {game.warrior.health} здоровья.')
                c = 0
                game.Ayaks.characteristic["Урон"]//=2
            elif c == 0:
                Tartaglia.send_message(message.chat.id, f'\nАякс ударил {game.warrior.name} и нанёс ему {game.Ayaks.characteristic["Урон"]} урона.\nУ {game.warrior.name} осталось {game.warrior.health} здоровья.')

        if game.warrior.health>0:
            for i in range(1,game.Ayaks.characteristic["Шанс уклонения"]+1):
                    if i == evasion:
                        e = 1
            if e == 0:
                game.Ayaks.characteristic["Нынешнее здоровье"]-=game.warrior.atack       
                Tartaglia.send_message(message.chat.id, f'\n{game.warrior.name} ударил Аякса и нанёс ему {game.warrior.atack} урона.\nУ Аякса осталось {game.Ayaks.characteristic["Нынешнее здоровье"]} здоровья.\n')
            elif e == 1:
                Tartaglia.send_message(message.chat.id, f'\nБлагодаря ловкости, Аякс смог увернуться от удара {game.warrior.name}.\n')
                e = 0           

        if game.Ayaks.characteristic["Нынешнее здоровье"]<=0:
            markup = telebot.types.ReplyKeyboardMarkup()
            buttonA = telebot.types.KeyboardButton("Начать сначала")
            markup.row(buttonA)
            Tartaglia.send_message(message.chat.id, "Аякс умер.\nВы проиграли.", reply_markup=markup)

        if game.warrior.health <= 0:
            game.Ayaks.level["Опыт"] += game.warrior.level*2
            game.Ayaks.characteristic["Нынешнее здоровье"] = game.Ayaks.characteristic["Максимальное здоровье"]
            game.warrior.treatment()
            
            markup = telebot.types.ReplyKeyboardMarkup()
            buttonA = telebot.types.KeyboardButton("Поиск")
            buttonB = telebot.types.KeyboardButton("Аякс")
            buttonC = telebot.types.KeyboardButton("Локация")
            buttonN = telebot.types.KeyboardButton("В главное меню")

            markup.row(buttonA,buttonB,buttonC,buttonN)
            
            Tartaglia.send_message(message.chat.id,f"\nАякс победил. За победу он получил {game.warrior.level*2} опыта.\nЗдоровье восстановленно божественной благодатью.", reply_markup=markup)
            if game.Ayaks.level["Опыт"] >= game.Ayaks.level["Опыт до следующего уровня"]:
                 Tartaglia.send_message(message.chat.id, "Полученного опыта достаточно для повышения уровня.\n(Повысить уровень можно во вкладке «Аякс»)")


    if message.text == "Начать сначала":
        markup = telebot.types.ReplyKeyboardMarkup()
        buttonA = telebot.types.KeyboardButton("Отправиться в Мондштадт")
        markup.row(buttonA)
        Tartaglia.send_photo(message.chat.id, "https://vgtimes.ru/uploads/posts/2021-05/77507_4_3.jpg",)
        Tartaglia.send_message(message.chat.id, "Вы - Аякс «Чайльд» Тарталья одинадцатый из Предвестников Фатуи. Будучи непревзойдённым воином, именно Вам достаются самые сложные и опасные задания. Так произошло и в этот раз.\nТейват на пороге Великой Войны Архонтов. В последние месяцы участились конфликты между Вашей родиной, могущественным и воинственным королевством Крио Архонта Царицы, и двумя державами - Мондштадтом, городом-государством под покровительством Анемо Архонта Барбатоса и Ли Юэ, королевством Гео Архонта Моракса.\nВследствие этого, Фатуи решила направить разведчиков в эти два королевства, с целью получения информации о военном положении держав, а также об их возможной готовности напасть на Снежную. \nК несчастью, разведчики перестали выходить на связь. Агенты Фатуи разузнали, что разведчика, направленного в Мондштадт, захватили в плен хиличурлы и держут его в заложиниках, охраняя большим числом войск. Второго же разведчика, отправленного в Ли Юэ, постигла участь ни чуть не лучше - его схватили геовишапы.\nИменно Вам поручено освободить разведчиков, дабы Царица смогла увидеть картину целиком и предпринять верные действия в эти непростые времена.\nСперва отправляйтесь в Мондштадт, а после - в Ли Юэ. Не медлите, Аякс, да прибудет с Вами Царица!", reply_markup=markup)

        game.Ayaks.rang = "Крошка Аякс"
        game.Ayaks.level["Уровень"] = 1
        game.Ayaks.level["Опыт"] = 0
        game.Ayaks.level["Опыт до следующего уровня"] = 10
        game.Ayaks.level["Очки для повышения атрибутов"] = 0
        game.Ayaks.characteristic["Нынешнее здоровье"] = 120
        game.Ayaks.characteristic["Максимальное здоровье"] = 120
        game.Ayaks.characteristic["Урон"] = 20
        game.Ayaks.characteristic["Шанс критического удара"] = 5
        game.Ayaks.characteristic["Критический удар"] = 200
        game.Ayaks.characteristic["Шанс уклонения"] = 5
        game.Ayaks.attributes["Сила"] = 1
        game.Ayaks.attributes["Ловкость"] = 1
        game.Ayaks.attributes["Выносливость"] = 1

        game.start=0

    if message.text == "Назад":
        markup = telebot.types.ReplyKeyboardMarkup()
        buttonA = telebot.types.KeyboardButton("Поиск")
        buttonB = telebot.types.KeyboardButton("Аякс")
        buttonC = telebot.types.KeyboardButton("Локация")
        buttonN = telebot.types.KeyboardButton("В главное меню")

        markup.row(buttonA,buttonB,buttonC,buttonN)

        Tartaglia.send_message(message.chat.id,'Поиск - поиск противника.\nАякс - герой.\nЛокация - информация о нынешней локации.\nВернуться назад - вернуться в главное меню.', reply_markup=markup)

    if message.text == "Аякс":
        markup = telebot.types.ReplyKeyboardMarkup()
        buttonA = telebot.types.KeyboardButton("Информация")
        buttonB = telebot.types.KeyboardButton("Повышение уровня")
        buttonN = telebot.types.KeyboardButton("Назад")

        markup.row(buttonA,buttonB,buttonN)

        Tartaglia.send_message(message.chat.id,'Информация - информация об Аяксе.\nПовышение уровня - прокачка героя.', reply_markup=markup)

    if message.text == "Информация":
        Tartaglia.send_photo(message.chat.id, game.Ayaks.photo[game.Ayaks.level["Уровень"]-1], caption = game.Ayaks.AboutMe())

    if message.text == "Повышение уровня" and game.Ayaks.level["Уровень"]<10:
        if game.Ayaks.level["Опыт"] >= game.Ayaks.level["Опыт до следующего уровня"]:
            game.Ayaks.level["Опыт"] = game.Ayaks.level["Опыт"]-game.Ayaks.level["Опыт до следующего уровня"]
            game.Ayaks.levelup()
            Tartaglia.send_message(message.chat.id, f'Аякс повысил свой уровень до {game.Ayaks.level["Уровень"]}.\nТеперь он не {game.Ayaks.rang}, а настоящий {game.Ayaks.rangs[game.Ayaks.level["Уровень"]]}.')
            game.Ayaks.rangup()
                    
            markup = telebot.types.ReplyKeyboardMarkup()

            buttonA = telebot.types.KeyboardButton("Сила")
            buttonB = telebot.types.KeyboardButton("Ловкость")
            buttonC = telebot.types.KeyboardButton("Выносливость")

            markup.row(buttonA,buttonB,buttonC)

            Tartaglia.send_message(message.chat.id, f'Вам доступно {game.Ayaks.level["Очки для повышения атрибутов"]} очков для  распределения.', reply_markup=markup)

        else:
            Tartaglia.send_message(message.chat.id, "Аякс недостаточно опытен для повышения уровня.")

    if message.text == "Повышение уровня" and game.Ayaks.level["Уровень"]==10:
        Tartaglia.send_message(message.chat.id, "Вы достигли максимального уровня.")
    
    if message.text == "Сила" and game.Ayaks.level["Очки для повышения атрибутов"]>0:
        game.Ayaks.attributes["Сила"]+=1
        game.Ayaks.characteristic["Урон"] = game.Ayaks.characteristic["Урон"]+game.Ayaks.characteristic["Урон"]//2
        game.Ayaks.characteristic["Максимальное здоровье"] = game.Ayaks.characteristic["Максимальное здоровье"]+game.Ayaks.characteristic["Максимальное здоровье"]//8
        game.Ayaks.characteristic["Нынешнее здоровье"] = game.Ayaks.characteristic["Нынешнее здоровье"]+game.Ayaks.characteristic["Нынешнее здоровье"]//8
        game.Ayaks.level["Очки для повышения атрибутов"]-=1
        Tartaglia.send_message(message.chat.id, f'Вы повысили силу на 1 пункт.\nВаша сила составляет {game.Ayaks.attributes["Сила"]} очков.\nОчков для распределения осталось: {game.Ayaks.level["Очки для повышения атрибутов"]}.')

        if game.Ayaks.level["Очки для повышения атрибутов"]==0:
            markup = telebot.types.ReplyKeyboardMarkup()
            buttonA = telebot.types.KeyboardButton("Информация")
            buttonB = telebot.types.KeyboardButton("Повышение уровня")
            buttonN = telebot.types.KeyboardButton("Назад")

            markup.row(buttonA,buttonB,buttonN)

            Tartaglia.send_message(message.chat.id,'Вы закончили распределять очки атрибутов.', reply_markup=markup)
            
    if message.text == "Ловкость" and game.Ayaks.level["Очки для повышения атрибутов"]>0:
        game.Ayaks.attributes["Ловкость"]+=1
        game.Ayaks.characteristic["Шанс критического удара"]+=5
        if game.Ayaks.characteristic["Шанс уклонения"]<80:
            game.Ayaks.characteristic["Шанс уклонения"]+=5
        game.Ayaks.level["Очки для повышения атрибутов"]-=1
        Tartaglia.send_message(message.chat.id, f'Вы повысили ловкость на 1 пункт.\nВаша ловкость составляет {game.Ayaks.attributes["Ловкость"]} очков.\nОчков для распределения осталось: {game.Ayaks.level["Очки для повышения атрибутов"]}.')

        if game.Ayaks.level["Очки для повышения атрибутов"]==0:
            markup = telebot.types.ReplyKeyboardMarkup()
            buttonA = telebot.types.KeyboardButton("Информация")
            buttonB = telebot.types.KeyboardButton("Повышение уровня")
            buttonN = telebot.types.KeyboardButton("Назад")

            markup.row(buttonA,buttonB,buttonN)

            Tartaglia.send_message(message.chat.id,'Вы закончили распределять очки атрибутов.', reply_markup=markup)
            
    if message.text == "Выносливость" and game.Ayaks.level["Очки для повышения атрибутов"]>0:
        game.Ayaks.attributes["Выносливость"]+=1
        game.Ayaks.characteristic["Максимальное здоровье"] = game.Ayaks.characteristic["Максимальное здоровье"]+game.Ayaks.characteristic["Максимальное здоровье"]//4
        game.Ayaks.characteristic["Нынешнее здоровье"] = game.Ayaks.characteristic["Нынешнее здоровье"]+game.Ayaks.characteristic["Нынешнее здоровье"]//4
        
        game.Ayaks.level["Очки для повышения атрибутов"]-=1
        Tartaglia.send_message(message.chat.id, f'Вы повысили выносливость на 1 пункт.\nВаша выносливость составляет {game.Ayaks.attributes["Выносливость"]} очков.\nОчков для распределения осталось: {game.Ayaks.level["Очки для повышения атрибутов"]}.')

        if game.Ayaks.level["Очки для повышения атрибутов"]==0:
            markup = telebot.types.ReplyKeyboardMarkup()
            buttonA = telebot.types.KeyboardButton("Информация")
            buttonB = telebot.types.KeyboardButton("Повышение уровня")
            buttonN = telebot.types.KeyboardButton("Назад")

            markup.row(buttonA,buttonB,buttonN)

            Tartaglia.send_message(message.chat.id,'Вы закончили распределять очки атрибутов.', reply_markup=markup)

    if game.Ayaks.level["Уровень"] >= 5 and game.Ayaks.level["Уровень"]<9:
        game.loc1 = game.LiYue.mobs_list[1]
    if game.Ayaks.level["Уровень"] >= 9:
        game.loc1 = game.Snowy.mobs_list[2]

    if game.Ayaks.level["Уровень"] == 5 and game.start == 1 and game.Ayaks.level["Очки для повышения атрибутов"] == 0:
        game.start += 1
        markup = telebot.types.ReplyKeyboardMarkup()
        buttonA = telebot.types.KeyboardButton("Отправиться в Ли Юэ")
        markup.row(buttonA)
        Tartaglia.send_photo(message.chat.id, "https://consejosjuegospro.com/wp-content/uploads/2021/06/Ubicaciones-de-los-agentes-Pyro-de-Genshin-Impact-Fatui.png", caption = "Уничтожив всех хиличурлов, Вы освободили разведчика.\nОн рассказал Вам, что Мондштадт не готов к войне, более того, никаких военных настроений не было обнаружено. Армия Мондштадта значительно уступают армии Снежной и в случае военного конфликта взять Мондштадт будет не проблема. \nВы отправили разведчика в Снежную. Чтож, половина задания выполнена. Следующая остановка Ли Юэ!", reply_markup=markup)

    if message.text == "Отправиться в Ли Юэ":
        Tartaglia.send_photo(message.chat.id, game.LiYue.photo)
        markup = telebot.types.ReplyKeyboardMarkup()
        buttonA = telebot.types.KeyboardButton("Поиск")
        buttonB = telebot.types.KeyboardButton("Аякс")
        buttonC = telebot.types.KeyboardButton("Локация")
        buttonN = telebot.types.KeyboardButton("В главное меню")

        markup.row(buttonA,buttonB,buttonC,buttonN)

        Tartaglia.send_message(message.chat.id,"Вы прибыли в Ли Юэ.\nСтранно, но агент Фатуи, который должен был показать вам путь к логову геовишапов, не выходит на связь.\nПроявив характерный авантюризм, Вы наткнулись на след геовишапов самостоятельно.", reply_markup=markup)

    if game.Ayaks.level["Уровень"] == 9 and game.start == 2 and game.Ayaks.level["Очки для повышения атрибутов"] == 0:
        game.start += 1
        markup = telebot.types.ReplyKeyboardMarkup()
        buttonA = telebot.types.KeyboardButton("Отправиться в Снежную")
        markup.row(buttonA)
        Tartaglia.send_photo(message.chat.id, "https://consejosjuegospro.com/wp-content/uploads/2021/06/Ubicaciones-de-los-agentes-Pyro-de-Genshin-Impact-Fatui.png", caption = "Разделавшись с геовишапами, Вы освободили разведчика.\nОн сообщил Вам ошеломительную новость: Моракс - Гео Архонт, правитель Ли Юэ - собрал многотысячное войско и направил его на Снежную. Более того, он подчинил своей воле могущественных гео существ. За эту информацию разведчик был вынужден поплатиться своей свободой, так как его обнаружили. \nВ общем-то, тот факт, что его охраняли геовишапы полностью подтверждает изложенные им сведения. Всё-таки, такое поведение не свойственно геовишапам в обыденной жизни.\nОпомнившись от услышанного, Вы мигом отправились Снежную, дабы успеть предупредить Фатуи о готовящимся нападении.", reply_markup=markup)

    if message.text == "Отправиться в Снежную":
        Tartaglia.send_photo(message.chat.id, "https://kartinkin.net/uploads/posts/2021-07/1626172568_10-kartinkin-com-p-razrushennii-zamok-art-art-krasivo-18.jpg")
        markup = telebot.types.ReplyKeyboardMarkup()
        buttonA = telebot.types.KeyboardButton("Поиск")
        buttonB = telebot.types.KeyboardButton("Аякс")
        buttonC = telebot.types.KeyboardButton("Локация")
        buttonN = telebot.types.KeyboardButton("В главное меню")

        markup.row(buttonA,buttonB,buttonC,buttonN)

        Tartaglia.send_message(message.chat.id,"Снежная встретила Вас пламенем горящих домов и руинами замков. Армия Моракса была разрушительной и беспощадной.\nДобравшись с боем до столично замка, Вы попали на заседание Царицы с Предвестниками Фатуи. Объектом обсуждений было внезапное вторжение Ли Юэ.\nНа момент Вашего прихода велись громкие дискуссии, предлагались самые разные планы обороны и контрнаступления. Но в связи с Вашим докладом о том, что Мораксу удалось подчинить своей воле могущественных гео созданий, главная задача была ясна для всех.\nЕдинственный путь к спасению Снежной - убить Моракса.\nВы доказали свою преданность, храбрость и исполнительность. Более того, Вас по праву можно назвать самым искусным воином во всей Снежной. Именно поэтому, лично Царица назначила Вас исполнителем этого непростого задания. Именно Вы должны схлеснуться с Мораксом в смертельной схватке.\nУдачи, Аякс. Судьба Снежной зависит от Вас.", reply_markup=markup)
    
    if message.text == "Локация":
        if game.Ayaks.level["Уровень"]<5:
            Tartaglia.send_photo(message.chat.id, game.Monshtad.photo, caption = f'{game.Monshtad.name}\n{game.Monshtad.description}')

        if game.Ayaks.level["Уровень"]>=5 and game.Ayaks.level["Уровень"]<9:
            Tartaglia.send_photo(message.chat.id, game.LiYue.photo, caption = f'{game.LiYue.name}\n{game.LiYue.description}')

        if game.Ayaks.level["Уровень"]==9:
            Tartaglia.send_photo(message.chat.id, game.Snowy.photo, caption = f'{game.Snowy.name}\n{game.Snowy.description}')
    
    if game.Ayaks.level["Уровень"]==10 and game.Ayaks.level["Очки для повышения атрибутов"] == 0 and game.boss == 0:
        game.boss = 1 
        markup = telebot.types.ReplyKeyboardMarkup()
        buttonA = telebot.types.KeyboardButton("Атаковать!")

        markup.row(buttonA)

        Tartaglia.send_photo(message.chat.id, "https://abrakadabra.fun/uploads/posts/2022-01/1641282208_3-abrakadabra-fun-p-oboi-na-pk-tartalya-6.jpg", caption = "Пробераясь сквозь толпы могучих монстров, Вы наконец встречаете Моракса. \nВот он, этот миг, который сделает Вас великим, достойным божественного титула, или же похоронит под руинами собственного отечества. Не мешка, вы скрещиваете с ним оружие.", reply_markup=markup)

    if message.text == "Атаковать!":
        c = 0
        e = 0
        cm = 0
        em = 0
        crit = random.randint(1,100)
        evasion = random.randint(1,100)
        critm = random.randint(1,100)
        evasionm = random.randint(1,100)             

        for i in range(1,game.Li.characteristic["Шанс уклонения"]+1):
            if i == evasionm:
                em = 1

        if em == 0:
            for i in range(1,game.Ayaks.characteristic["Шанс критического удара"]+1):
                if i == crit:
                    game.Ayaks.characteristic["Урон"]*=2
                    c = 1
            game.Li.characteristic["Здоровье"]-=game.Ayaks.characteristic["Урон"]
            if c == 1:
                Tartaglia.send_message(message.chat.id,f'\nАякс ударил Моракса и нанёс ему критический урон! {game.Ayaks.characteristic["Урон"]} урона.\nУ Моракса осталось {game.Li.characteristic["Здоровье"]} здоровья.')
                c = 0
                game.Ayaks.characteristic["Урон"]//=2
            elif c == 0:
                Tartaglia.send_message(message.chat.id, f'\nАякс ударил Моракса и нанёс ему {game.Ayaks.characteristic["Урон"]} урона.\nУ Моракса осталось {game.Li.characteristic["Здоровье"]} здоровья.')

            if game.Ayaks.attributes["Ловкость"] >= 10:
                crit = random.randint(1,100)
                for i in range(1,game.Ayaks.characteristic["Шанс критического удара"]+1):
                    if i == crit:
                        game.Ayaks.characteristic["Урон"]*=2
                        c = 1
                game.Li.characteristic["Здоровье"]-=game.Ayaks.characteristic["Урон"]
                Tartaglia.send_message(message.chat.id, '\nБлагодаря своей ловкости Аякс наносит дополнительный удар.')
                if c == 1:
                    Tartaglia.send_message(message.chat.id, f'\nАякс ударил Моракса и нанёс ему критический урон! {game.Ayaks.characteristic["Урон"]} урона.\nУ Моракса осталось {game.Li.characteristic["Здоровье"]} здоровья.')
                    c = 0
                    game.Ayaks.characteristic["Урон"]//=2
                elif c == 0:
                    Tartaglia.send_message(message.chat.id, f'\nАякс ударил Моракса и нанёс ему {game.Ayaks.characteristic["Урон"]} урона.\nУ Моракса осталось {game.Li.characteristic["Здоровье"]} здоровья.')
            if game.Ayaks.attributes["Ловкость"] >= 20:
                crit = random.randint(1,100)
                for i in range(1,game.Ayaks.characteristic["Шанс критического удара"]+1):
                    if i == crit:
                        game.Ayaks.characteristic["Урон"]*=2
                        c = 1
                game.Li.characteristic["Здоровье"]-=game.Ayaks.characteristic["Урон"]
                Tartaglia.send_message(message.chat.id, '\nБлагодаря своей ловкости Аякс наносит дополнительный удар.')
                if c == 1:
                    Tartaglia.send_message(message.chat.id, f'\nАякс ударил Моракса и нанёс ему критический урон! {game.Ayaks.characteristic["Урон"]} урона.\nУ Моракса осталось {game.Li.characteristic["Здоровье"]} здоровья.')
                    c = 0
                    game.Ayaks.characteristic["Урон"]//=2
                elif c == 0:
                    Tartaglia.send_message(message.chat.id, f'\nАякс ударил Мораска и нанёс ему {game.Ayaks.characteristic["Урон"]} урона.\nУ Моракса осталось {game.Li.characteristic["Здоровье"]} здоровья.')

        elif em == 1:
            Tartaglia.send_message(message.chat.id, '\nБлагодаря ловкости, Моракс смог увернуться от удара Аякса.')
            em = 0    

        if game.Li.characteristic["Здоровье"]>0:            
            for i in range(1,game.Ayaks.characteristic["Шанс уклонения"]+1):
                if i == evasion:
                    e = 1
            if e == 0:
                    for i in range(1,game.Li.characteristic["Шанс критического удара"]+1):
                        if i == critm:
                            game.Li.characteristic["Урон"]*=2
                            cm = 1      
                    game.Ayaks.characteristic["Нынешнее здоровье"]-=game.Li.characteristic["Урон"]
                    if cm == 1:
                        Tartaglia.send_message(message.chat.id, f'\nМоракс ударил Аякса и нанёс ему критический урон! {game.Li.characteristic["Урон"]} урона.\nУ Аякса осталось {game.Ayaks.characteristic["Нынешнее здоровье"]} здоровья.')
                        сm = 0
                        game.Li.characteristic["Урон"]//=2
                    elif cm == 0:
                        Tartaglia.send_message(message.chat.id, f'\nМоракс ударил Аякса и нанёс ему {game.Li.characteristic["Урон"]} урона.\nУ Аякса осталось {game.Ayaks.characteristic["Нынешнее здоровье"]} здоровья.')
            elif e == 1:
                Tartaglia.send_message(message.chat.id, '\nБлагодаря ловкости, Аякс смог увернуться от удара Моракса.')
                e = 0           

        elif game.Li.characteristic["Здоровье"]<=0:
            markup = telebot.types.ReplyKeyboardMarkup()
            buttonA = telebot.types.KeyboardButton("Портрет")
            buttonB = telebot.types.KeyboardButton("Реплика")
            buttonC = telebot.types.KeyboardButton("Игра")

            game.Ayaks.rang = "Крошка Аякс"
            game.Ayaks.level["Уровень"] = 1
            game.Ayaks.level["Опыт"] = 0
            game.Ayaks.level["Опыт до следующего уровня"] = 10
            game.Ayaks.level["Очки для повышения атрибутов"] = 0
            game.Ayaks.characteristic["Нынешнее здоровье"] = 120
            game.Ayaks.characteristic["Максимальное здоровье"] = 120
            game.Ayaks.characteristic["Урон"] = 20
            game.Ayaks.characteristic["Шанс критического удара"] = 5
            game.Ayaks.characteristic["Критический удар"] = 200
            game.Ayaks.characteristic["Шанс уклонения"] = 5
            game.Ayaks.attributes["Сила"] = 1
            game.Ayaks.attributes["Ловкость"] = 1
            game.Ayaks.attributes["Выносливость"] = 1
            markup.row(buttonA,buttonB,buttonC)
            Tartaglia.send_photo(message.chat.id, "https://avatars.mds.yandex.net/get-images-cbir/369811/y3dUPtGxTePKx4DCEe3uMw3449/ocr", caption = "Вы одолели Моракса!\nПоразительно, Вы смогли убить Бога! Этот момент войдёт в историю как триумф человеческой воли.\nПоздравляю! Войска Моракса потеряв лидера дезориентированы и в спешке покидают поле боя. Снежная спасена исключительно благодаря Вам, Аякс, Вы герой!",reply_markup = markup)
            game.loc1 = game.Monshtad.mobs_list[0]
            game.start = 0

        if game.Ayaks.characteristic["Нынешнее здоровье"]<=0:
            game.Ayaks.rang = "Крошка Аякс"
            game.Ayaks.level["Уровень"] = 1
            game.Ayaks.level["Опыт"] = 0
            game.Ayaks.level["Опыт до следующего уровня"] = 10
            game.Ayaks.level["Очки для повышения атрибутов"] = 0
            game.Ayaks.characteristic["Нынешнее здоровье"] = 120
            game.Ayaks.characteristic["Максимальное здоровье"] = 120
            game.Ayaks.characteristic["Урон"] = 20
            game.Ayaks.characteristic["Шанс критического удара"] = 5
            game.Ayaks.characteristic["Критический удар"] = 200
            game.Ayaks.characteristic["Шанс уклонения"] = 5
            game.Ayaks.attributes["Сила"] = 1
            game.Ayaks.attributes["Ловкость"] = 1
            game.Ayaks.attributes["Выносливость"] = 1
            game.start = 0
            game.loc1 = game.Monshtad.mobs_list[0]
            markup = telebot.types.ReplyKeyboardMarkup()
            buttonA = telebot.types.KeyboardButton("Начать сначала")
            buttonB = telebot.types.KeyboardButton("В главное меню")
            markup.row(buttonA, buttonB)
            Tartaglia.send_photo(message.chat.id, "https://pbs.twimg.com/media/E3YHj7qXMAoQsEB.jpg","Моракс одолел Вас!\nНе удивительно. Человеку не по силам тягаться с Богом. И в это успешно продемонстрировали.\nАякс мертв, а вместе с ним и многовековая держава.   ", reply_markup = markup)
            
    if message.text == "Зигани":
        Tartaglia.send_photo(message.chat.id,"https://avatars.mds.yandex.net/get-images-cbir/1780006/IY3c6ek6NzikWvxKYbN5JQ7174/ocr", caption = "ХАИЛЬ ЦАРИЦА")
    
if __name__ == "__main__":
    Tartaglia.infinity_polling()
    
