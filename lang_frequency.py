import os


def load_data(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r', encoding='utf8') as file:
        try:
            return file.read()
        except:
            None


def get_most_frequent_words(text):
    pass


if __name__ == '__main__':
    text = load_data('test.txt')
    print(get_most_frequent_words(text))
