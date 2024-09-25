#Домашнее задание по теме "Оператор "with".
class WordsFinder:
    filter = [',', '.', '=', '!', '?', ';', ':', ' - ', ')', '(']

    def __init__(self, *file_names):
        self.file_names = []
        self.all_words = {}
        for item in file_names:
            self.file_names.append(item)
        self._get_all_words()

    def _get_all_words(self):
        for item in self.file_names:

            with open(item, encoding='utf-8') as file:
                words = []
                for line in file:
                    txt = line.lower()
                    for f in self.filter:
                        txt = txt.replace(f, '')
                    word_in_line = txt.split()
                    words = words + word_in_line
                self.all_words[item] = words

    def get_all_words(self):

        return self.all_words

    def find(self, word):
        word_f = word.lower()

        i = 0
        for name, words in self.all_words.items():
            for one_word in words:
                i += 1
                if one_word == word_f:
                    return {name: i}

    def count(self, word):
        word_f = word.lower()
        count = {}
        for name, words in self.all_words.items():
            i = 0
            for one_word in words:
                if one_word == word_f:
                    i = i + 1
            if i > 0:
                count[name] = i
        if len(count) == 0:
            return (f'Слово "{word}" не найдено')
        else:
            return count







if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

