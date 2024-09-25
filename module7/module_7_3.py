# Домашнее задание по теме "Оператор "with".

class WordsFinder:
    filter = [',', '.', '=', '!', '?', ';', ':', ' - ']

    def __init__(self, *files_name):
        self.file_names = []
        for item in files_name:
            self.file_names.append(item)

    def get_all_words(self):
        all_words = {}
        for item in self.file_names:

            with open(item, encoding='utf-8') as file:
                words = []
                for line in file:
                    txt = line.lower()
                    for f in self.filter:
                        txt = txt.replace(f, '')
                    word_in_line = txt.split()
                    words = words + word_in_line
                all_words[item] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        word_f = word.lower()

        i = 0
        for name, words in all_words.items():
            for one_word in words:
                i += 1
                if one_word == word_f:
                    return {name: i}

    def count(self, word):
        all_words = self.get_all_words()
        word_f = word.lower()
        count = {}
        for name, words in all_words.items():
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
    # finder1 = WordsFinder('Mother Goose - Monday’s Child.txt', )
    # print(finder1.get_all_words())
    # print(finder1.find('Child'))
    # print(finder1.count('Child'))



