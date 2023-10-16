# split the integer for simple dividers
def get_prime_factors(number):
    factors = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number = number / divisor
        else:
            divisor +=1
    return factors

# check if the phrase is palindrome
import re
def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards

# the srting splitted into words which then returned sorted ignoring the case
def sort_words(words):
    return ' '.join(sorted(words.split(), key=str.casefold))

# find all lists items, even if lists are nested using the recursing search
def index_all(search_list, item):
    index_list = []
    for index, value in enumerate(search_list):
        if value == item:
            index_list.append([index])
        elif isinstance(search_list[index], list):
            for i in index_all(search_list[index], item):
                index_list.append([index] + i)
    return index_list

# the waiting game
import time
import random
def waiting_game():
    target = random.randint(2, 4)
    input(' ___Press Enter to Begin___ ')
    start = time.perf_counter()
    input(f'\n...Press Enter again after {target} seconds...')
    elapsed = time.perf_counter() - start
    print(f'\nElapsed time: {elapsed :.3f} seconds')
    if elapsed == target:
        print('Unbeliavable! Perfect timing!')
    elif elapsed < target:
        print(f'({target - elapsed :.3f} seconds too fast)')
    else:
        print(f'({target - elapsed :.3f} seconds too slow)')

# save a dictionary
import pickle
def save_dict(dict_to_save, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(dict_to_save, file)
def load_dict(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)
## save_dict(test_dict, 'tst.pickle') 
## recovered = load_dict('tst.pickle')
## print(recovered)

# schedule a function
import sched
import time
def schedule_function(event_time, function, *args):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(event_time, 1, function, argument=args)
    print(f'{function.__name__}() scheduled for {time.asctime(time.localtime(event_time))}')
    s.run()

# send an email
import smtplib
SENDER_EMAIL = ''
SENDER_PASSWORD = ''
def send_email(receiver_email, subject, body):
    message = f'Subject: {subject}\n\n{body}'
    with smtplib.SMTP('smtp.office365.com', 587) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message)

# simulate dice play
from random import randint
from collections import Counter
def roll_dice(*dice, num_trials=1_000_000):
    counts = Counter()
    for _ in range(num_trials):
        counts[sum((randint(1,sides) for sides in dice))] += 1
    print('\nOUTCOME\tPROBABILITY')
    for outcome in range(len(dice), sum(dice) +1):
         print(f'{outcome}\t{counts[outcome]*100 / num_trials :0.2f}%')

# count unique words
import re
import collections
def count_words(path):
    with open(path, 'r', encoding='utf-8') as file:
        all_words =  re.findall(r"[0-9a-z-A-Z-']+", file.read())
        all_words = [word.upper() for word in all_words]
        print(f'\nTotal Words: {len(all_words)}')
        words_counts = collections.Counter(all_words)
        print('\nTop 20 Words:')
        for word in words_counts.most_common(20):
            print(f'{word[0]}\t{word[1]}')

# generate a password
import secrets
def generate_passphrse(num_words, wordlist_path='diceware.wordlist.asc'):
    with open(wordlist_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[2:7778]
        word_list = [line.split()[1] for line in lines]
    words = [secrets.choice(word_list) for _ in range(num_words)]
    print(' '.join(words))
    return ' '.join(words)

# merge csv files
import csv
def merge_csv(csv_list, output_path):
    fieldnames = []
    for file in csv_list:
        with open(file, 'r', encoding='utf-8') as input_csv:
            field = csv.DictReader(input_csv).fieldnames
            fieldnames.extend(f for f in field if f not in fieldnames)
    with open(output_path, 'w', encoding='utf-8', newline='') as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        writer.writeheader()
        for file in csv_list:
            with open(file, 'r', encoding='utf-8') as input_csv:
                reader = csv.DictReader(input_csv)
                for row in reader:
                    writer.writerow(row)

# sudoku puzzle
from itertools import product
def solve_sudoku(puzzle):
    for (row, col) in product(range(0, 9), repeat=2):
        if puzzle[row][col] == 0:
            for num in range(1,10):
                allowed = True
                for i in range(0,9):
                    if num in (puzzle[i][col], puzzle[row][i]):
                        allowed = False
                        break
                for (i, j) in product(range(0, 3), repeat=2):
                    if puzzle[row - row % 3 + i][col - col % 3 + j] == num:
                        allowed = False
                        break
                if allowed:
                    puzzle[row][col] = num
                    if trial := solve_sudoku(puzzle):
                        return trial
                    puzzle[row][col] = 0
            return False
    return puzzle
def print_sudoku(puzzle):
    puzzle = [['*' if num == 0 else num for num in row] for row in puzzle]
    print()
    for row in range(0, 9):
        if ((row % 3 == 0) and (row != 0)):
            print('-' * 33)
        for col in range(0, 9):
            if ((col % 3 == 0) and (col != 0)):
                print(' | ', end='')
            print(f' {puzzle[row][col]} ', end='')
        print()
    print()
test_puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
               [6, 0, 0, 1, 9, 5, 0, 0, 0],
               [0, 9, 8, 0, 0, 0, 0, 6, 0],
               [8, 0, 0, 0, 6, 0, 0, 0, 3],
               [4, 0, 0, 8, 0, 3, 0, 0, 1],
               [7, 0, 0, 0, 2, 0, 0, 0, 6],
               [0, 6, 0, 0, 0, 0, 2, 8, 0],
               [0, 0, 0, 4, 1, 9, 0, 0, 5],
               [0, 0, 0, 0, 8, 0, 0, 7, 9]]
# if __name__ == "__main__":
#     print_sudoku(test_puzzle)
#     solution = solve_sudoku(test_puzzle)
#     print_sudoku(solution)

# a zip archive
import os
from zipfile import ZipFile
def zip_all(search_dir, extension_list, output_path):
    with ZipFile(output_path, 'w') as output_zip:
        for root, _, files in os.walk(search_dir):
            rel_path = os.path.relpath(root, search_dir)
            for file in files:
                _, ext = os.path.splitext(file)
                if ext.lower() in extension_list:
                    output_zip.write(os.path.join(root, file), arcname=os.path.join(rel_path, file))

# download sequential file
import os
import re
import urllib.parse
import urllib.request
def download_files(first_url, output_dir):
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    url_head, url_tail =os.path.split(first_url)
    first_index = re.findall(r'[0-9]+', url_tail)[-1]
    index_count, error_count = 0, 0
    while error_count < 5:
        next_index = str(int(first_index) + index_count)
        if first_index[0] == '0':
            next_index = '0' * (len(first_index) - len(next_index)) + next_index
        next_url = urllib.parse.urljoin(url_head, re.sub(first_index, next_index, url_tail))
        try:
            output_file = os.path.join(output_dir, os.path.basename(next_url))
            urllib.request.urlretrieve(next_url, output_file)
            print(f'Successfully downloaded {os.path.basename(next_url)}')
        except IOError:
            print(f'Could not retrieve {next_url}')
            error_count +=1
        index_count +=1
            

if __name__ == "__main__":
    download_files('http://699340.youcanlearnit.net/image001.jpg', 'images')
