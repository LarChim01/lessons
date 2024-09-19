#Дополнительное практическое задание по модулю: "Классы и объекты."
from time import sleep


class User():
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class UrTube:
    '''
    Видеотека
    '''

    def __init__(self):
        self.videoteka = []
        self.current_user = None
        self.users = []

    def add(self, *other):
        for item in other:
            self.videoteka.append(item)

    def get_videos(self, str):
        films = len(self.videoteka)
        found = []
        str = str.lower()
        for i in range(0, films):
            if str in self.videoteka[i].title.lower():
                found.append(self.videoteka[i].title)
        if len(found):
            return found
        else:
            return "Ничего не найдено"

    def age_user(self):
        for item in self.users:
            if item.nickname == self.current_user:
                return item.age

    def one_video(self, title):
        films = len(self.videoteka)
        for i in range(0, films):
            if title == self.videoteka[i].title:
                return i
        print(f'Фильм "{title}" не найден')

    def register(self, nickname, password, age):
        '''
        регистрация пользователя
        :param nickname:
        :param password:
        :param age:
        :return:
        '''

        if len(self.users) > 0:
            for item in self.users:
                if item.nickname == nickname:
                    print(f'Пользователь {nickname} уже существует')
                    return

        # user = {}
        # user["nickname"] = nickname
        # user["password"] = hash(password)
        # user["age"] = age
        self.users.append(User(nickname, hash(password), age))
        self.current_user = nickname

    def log_in(self, nickname, password):
        if len(self.users) > 0:
            for item in self.users:
                if item.nickname == nickname:
                    if item.password == hash(password):
                        self.current_user = nickname
                    else:
                        print('Пароль не верный')

                    return
            print(f'Пользователь {nickname} не найден')

    def watch_video(self, title):
        '''
        Воспроизведение фильма
        :param title:
        :return:
        '''
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        if self.age_user() < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
            return
        i = self.one_video(title)
        if i != None:
            duration = self.videoteka[i].duration
            time_now = self.videoteka[i].time_now
            for sek in range(time_now, duration):
                print(sek, end=' ')
                sleep(0.5)
            print("Конец видео", end='\n')
            self.videoteka[i].time_now = 0

    def log_out(self):
        self.current_user = None


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode







if __name__=='__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)
    ur.watch_video("Urban University ")
    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')

    #проверка log_in, log_out
    ur.log_out()
    print('user',ur.current_user)
    ur.log_in('vasya_pupkin', 'lolkekcheburek')
    print('user', ur.current_user)
    ur.log_in('pupkin', 'lolkekcheburek')
