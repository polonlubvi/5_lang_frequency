import os
import re
import logging
import logging.config

logging.config.fileConfig("logging.conf")


def load_data(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r', encoding='utf8') as file:
        try:
            return file.read()
        except:
            None


def get_words_from_text(text):
    pass


def get_most_frequent_words(tokenized_word_list):
    pass


if __name__ == '__main__':
    pass
