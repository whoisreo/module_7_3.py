class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            list = []
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    line_cls = line.lower().replace(',', '').replace('.', '').replace('=', '').replace('!', '').replace(
                        '?', '').replace(';', '').replace(':', '').replace('-', '').split()
                    list.append(line_cls)
            all_words[file_name] = sum(list, [])
        return all_words

    def find(self, word):
        find_dict = {}
        for name, words in self.get_all_words().items():
            find_dict[name] = words.index(word.lower()) + 1
        return find_dict

    def count(self, word):
        count_dict = {}
        for name, words in self.get_all_words().items():
            count_dict[name] = words.count(word.lower())
        return count_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
