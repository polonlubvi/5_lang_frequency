import os
import re
import logging
import logging.config
import argparse
import sys


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
    lower_case_text = text.lower()
    numberless_text = re.sub(r"\d", " ", lower_case_text)
    tokenized_word_list = re.findall(r'\w+', numberless_text)
    logging.debug(tokenized_word_list)
    return tokenized_word_list


def get_most_frequent_words(tokenized_word_list):
    words_frequency_dictionary = {}
    for word in tokenized_word_list:
        if word not in words_frequency_dictionary:
            words_frequency_dictionary[word] = 1
        else:
            words_frequency_dictionary[word] += 1
    logging.debug("get_most_frequent_words")
    sorted_word_frequency = sorted(
        words_frequency_dictionary.items(),
        key=lambda x: x[1], reverse=True)
    logging.debug(sorted_word_frequency)
    logging.debug(type(sorted_word_frequency))
    print(sorted_word_frequency[1:10])


def get_console_args():
    parser = argparse.ArgumentParser(
        prog='Words frequency',
        description='Get ten most frequent words from a given text.'
    )

    parser.add_argument(
        '--file_path',
        default='test.txt',
        help='You need to specify the path to the text file from which'
        'the script will count the frequency of the words'
    )

    return parser.parse_args()


if __name__ == '__main__':
    parse_args = get_console_args()
    text = load_data(parse_args.file_path)
    if text is None:
        sys.exit('File not found or path is incorrect')
    tokenized_word_list = get_words_from_text(text)
    get_most_frequent_words(tokenized_word_list)
