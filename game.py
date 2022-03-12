import random


class Tartaglia:
    rang = "Крошка Аякс"
    
    photo = ["https://avatars.mds.yandex.net/get-images-cbir/137358/SFEU19K68rJCssULyjw8wQ5909/ocr", "https://pbs.twimg.com/media/EzbY-U0XEAIsdnt?format=jpg&name=large", "https://pbs.twimg.com/media/E6zFwdbUYAAiWhM?format=jpg&name=large", "https://otaku.su/wp-content/uploads/2021/07/%D0%BF%D0%BB%D0%B0%D0%BA%D0%B0%D1%82%D1%8B-213.jpg", "https://genshinpedia.ru/wp-content/uploads/2021/03/1615122901_ad61ab143223efbc24c7d2583be69251.png", "https://avatars.mds.yandex.net/get-zen_doc/1712117/pub_601420d5123cc8767c6d044e_60150b715930a614f234ee6e/scale_1200", "https://wotpack.ru/wp-content/uploads/2021/10/1152965.jpg", "https://portalvirtualreality.ru/wp-content/uploads/2021/04/%D0%B3%D0%B0%D0%B9%D0%B4-%D0%BD%D0%B0-%D1%82%D0%B0%D1%80%D1%82%D0%B0%D0%BB%D1%8C%D1%8E.jpg", "https://preview.redd.it/kls5os05ckf61.jpg?auto=webp&s=35df1bf5b12ae238bfdc498cb53489bdedd07daf", "https://preview.redd.it/kls5os05ckf61.jpg?auto=webp&s=35df1bf5b12ae238bfdc498cb53489bdedd07daf"]

    rangs = {1:"Крошка Аякс",
             2:"Малыш Аякс",
             3:"Юный Аякс",
             4:"Авантюрный Аякс",
             5:"Аякс воин",
             6:"Аякс опытный воин",
             7:"Аякс разрушитель",
             8:"Могущественный Аякс",
             9:"«Чайльд» Тарталья",
             10:"«Чайльд» Тарталья повелитель хаоса"
            }
    
    level = {"Уровень":1,
             "Опыт":0,
             "Опыт до следующего уровня":10,
             "Очки для повышения атрибутов":0
             }
    
    characteristic = {"Максимальное здоровье":120,
                      "Нынешнее здоровье":120,
                      "Урон":20,
                      "Шанс критического удара":5,
                      "Критический удар":200,
                      "Шанс уклонения":5,
                    }

    attributes = {"Сила":1,
                  "Ловкость":1,
                  "Выносливость":1,
                  }
   
    def AboutMe(self):
        return(f'Имя - Аякс\nРанг - {self.rang}\nУровень - {self.level["Уровень"]}\nОпыт - {self.level["Опыт"]}\nОпыт до следуюшего уровня - {self.level["Опыт до следующего уровня"]}\nОчки для повышения атрибутов - {self.level["Очки для повышения атрибутов"]}\nАтрибуты:\nСила - {self.attributes["Сила"]}\nЛовкость - {self.attributes["Ловкость"]}\nВыносливость - {self.attributes["Выносливость"]}\nХарактеристики:\nЗдоровье - {self.characteristic["Максимальное здоровье"]}\nУрон - {self.characteristic["Урон"]}\nКритический удар - {self.characteristic["Критический удар"]}\nШанс критического поподания - {self.characteristic["Шанс критического удара"]}\nШанс уклонения - {self.characteristic["Шанс уклонения"]}')

    def levelup(self):
        self.level["Уровень"] += 1
        self.level["Опыт до следующего уровня"] = self.level["Уровень"]*18
        self.level["Очки для повышения атрибутов"] += 5
    
    def find(self,loc):
        global warrior
        warrior = random.choice(loc)        

    def rangup(self):
        self.rang = self.rangs[self.level["Уровень"]]

                      
class Mob:
    characteristic = {"Здоровье":100,
                      "Урон":10}
    def __init__(self,n,l,p):
        self.name = n
        self.level = l
        self.photo = p
        self.health = self.characteristic["Здоровье"]*self.level
        self.atack = self.characteristic["Урон"]+(self.level*10)*self.level

    def treatment(self):
        self.health = self.characteristic["Здоровье"]*self.level


class loc:
    def __init__(self,n,d,p):
        self.name = n
        self.description = d
        self.photo = p
    mobs_list = []
    def mobs_append(self,*mob):
        self.mobs_list.append(mob)

class Morax:
    name = "Моракс разрушитель твоего ануса."
    characteristic = {"Здоровье":100000,
                      "Урон":2000,
                      "Шанс критического удара":50,
                      "Критический удар":200,
                      "Шанс уклонения":50,
                    }

Ayaks = Tartaglia()

Li = Morax()

warrior = Mob("Бот", 0, "https://i.pinimg.com/474x/5b/78/8b/5b788bb14490d8f59af6e1c12308f4b7.jpg")


Hilichurl = Mob("Хиличурл", 1, "https://static.wikia.nocookie.net/genshin-impact/images/0/0a/Enemy_Hilichurl.png/revision/latest?cb=20210828073123&path-prefix=th")
Hilichurl_fighter = Mob("Хиличурл боец", 2, "https://static.wikia.nocookie.net/gensin-impact/images/3/3f/Enemy_Hilichurl_Fighter.png/revision/latest?cb=20210528040259")
Hilichurl_berserker = Mob("Хиличурл берсерк", 3, "https://static.wikia.nocookie.net/gensin-impact/images/d/d8/Enemy_Hilichurl_Berserker.png/revision/latest/top-crop/width/360/height/360?cb=20210531023247")
Mitachurl = Mob("Митачурл", 4, "https://static.wikia.nocookie.net/genshin-impact/images/6/69/%D0%92%D1%80%D0%B0%D0%B3_%D0%9C%D0%B8%D1%82%D0%B0%D1%87%D1%83%D1%80%D0%BB_%D1%81_%D0%BE%D0%B3%D0%BD%D0%B5%D0%BD%D0%BD%D1%8B%D0%BC_%D1%82%D0%BE%D0%BF%D0%BE%D1%80%D0%BE%D0%BC.png/revision/latest/scale-to-width-down/1600?cb=20220211172701&path-prefix=ru")
Lavachurl = Mob("Лавачурл", 5, "https://static.wikia.nocookie.net/gensin-impact/images/d/dc/Enemy_Frostarm_Lawachurl.png/revision/latest?cb=20210717055543")

Geowishap_cub_five_level = Mob("Детёныш геовишапа", 5, "https://static.wikia.nocookie.net/gensin-impact/images/5/5f/Enemy_Geovishap_Hatchling.png/revision/latest?cb=20210629132452")
Geowishap_cub_six_level = Mob("Детёныш геовишапа", 6, "https://static.wikia.nocookie.net/gensin-impact/images/5/5f/Enemy_Geovishap_Hatchling.png/revision/latest?cb=20210629132452")
Geowishap_seven_level = Mob("Геовишап", 7, "https://static.wikia.nocookie.net/gensin-impact/images/b/b3/Enemy_Geovishap.png/revision/latest?cb=20210523100556")
Geowishap_eight_level = Mob("Геовишап", 8, "https://static.wikia.nocookie.net/gensin-impact/images/b/b3/Enemy_Geovishap.png/revision/latest?cb=20210523100556")
Ancient_geovishap = Mob("Древний геовишап", 9, "https://static.wikia.nocookie.net/gensin-impact/images/4/41/Enemy_Primo_Geovishap.png/revision/latest?cb=20210625221447")

Geo_hypostasis = Mob("Гео гипостазис", 9, "https://static.wikia.nocookie.net/genshin-impact/images/e/e5/%D0%92%D1%80%D0%B0%D0%B3_%D0%93%D0%B5%D0%BE_%D0%B3%D0%B8%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B7%D0%B8%D1%81.png/revision/latest?cb=20220106201123&path-prefix=ru")
Golden_wolf_leader = Mob("Золотой волчий вожак", 9, "https://static.wikia.nocookie.net/genshin-impact/images/3/3e/%D0%92%D1%80%D0%B0%D0%B3_%D0%97%D0%BE%D0%BB%D0%BE%D1%82%D0%BE%D0%B9_%D0%B2%D0%BE%D0%BB%D1%87%D0%B8%D0%B9_%D0%B2%D0%BE%D0%B6%D0%B0%D0%BA.png/revision/latest?cb=20220108203251&path-prefix=ru")

Monshtad = loc("Мондштадт", "Это город-государство, который поклоняется Анемо Архонту Барбатосу.\nВаша задача - отбить разведчика Фатуи у хиличурлов.","https://st.renderu.com/image/1200x/532193")
LiYue = loc("Ли Юэ","Богатый портовый город, расположенный в восточной части континента Тейват. Здесь властвует Архонт Моракс.\nВаша задача - отбить разведчика Фаути у геовишапов","https://download.youvteme.online/wp-content/uploads/2020/08/%E2%9C%94Genshin-Impact-iOS-758x426.jpg")
Snowy = loc("Снежная","Королевство Царицы. Страна вечного снега и льда. Ваш дом.\nВаша задача - найти и убить Моракса.","https://kartinkin.net/uploads/posts/2021-07/1626172568_10-kartinkin-com-p-razrushennii-zamok-art-art-krasivo-18.jpg")

Monshtad.mobs_append(Hilichurl, Hilichurl, Hilichurl, Hilichurl_fighter, Hilichurl_fighter, Hilichurl_fighter, Hilichurl_berserker, Hilichurl_berserker, Hilichurl_berserker, Mitachurl, Mitachurl, Lavachurl)
LiYue.mobs_append(Geowishap_cub_five_level, Geowishap_cub_six_level, Geowishap_seven_level, Geowishap_eight_level, Ancient_geovishap)
Snowy.mobs_append(Geo_hypostasis, Golden_wolf_leader, Ancient_geovishap, Ancient_geovishap)


loc1 = Monshtad.mobs_list[0]
if Ayaks.level["Уровень"] >= 5 and Ayaks.level["Уровень"]<9:
    loc1 = LiYue.mobs_list[1]
if Ayaks.level["Уровень"] >= 9:
    loc1 = Snowy.mobs_list[2]

start = 0
boss = 0
