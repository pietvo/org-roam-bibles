#!/usr/bin/env python3

# This Python program generates a Lexham English Bible bible in org-roam
# format from a Sword module LEB.zip. It needs Python version at least 3.9
# It needs the pysword module which can be installed with pip:
# python3 -m pip install pysword
# or download it from https://gitlab.com/tgc-dk/pysword/
# This program in in the public domain.
# Author: Pieter van Oostrum, <pieter@vanoostrum.org>

from pysword.modules import SwordModules
import re

bookinfo = {
'Genesis':            ('Genesis',         '01-GEN'),
'Exodus':             ('Exodus',          '02-EXO'),
'Leviticus':          ('Leviticus',       '03-LEV'),
'Numbers':            ('Numbers',         '04-NUM'),
'Deuteronomy':        ('Deuteronomy',     '05-DEU'),
'Joshua':             ('Joshua',          '06-JOS'),
'Judges':             ('Judges',          '07-JUD'),
'Ruth':               ('Ruth',            '08-RUT'),
'I Samuel':           ('1 Samuel',        '09-1SA'),
'II Samuel':          ('2 Samuel',        '10-2SA'),
'I Kings':            ('1 Kings',         '11-1KI'),
'II Kings':           ('2 Kings',         '12-2KI'),
'I Chronicles':       ('1 Chronicles',    '13-1CH'),
'II Chronicles':      ('2 Chronicles',    '14-2CH'),
'Ezra':               ('Ezra',            '15-EZR'),
'Nehemiah':           ('Nehemiah',        '16-NEH'),
'Esther':             ('Esther',          '17-EST'),
'Job':                ('Job',             '18-JOB'),
'Psalms':             ('Psalms',          '19-PSA'),
'Proverbs':           ('Proverbs',        '20-PRO'),
'Ecclesiastes':       ('Ecclesiastes',    '21-ECC'),
'Song of Solomon':    ('Song of Songs',   '22-SON'),
'Isaiah':             ('Isaiah',          '23-ISA'),
'Jeremiah':           ('Jeremiah',        '24-JER'),
'Lamentations':       ('Lamentations',    '25-LAM'),
'Ezekiel':            ('Ezekiel',         '26-EZE'),
'Daniel':             ('Daniel',          '27-DAN'),
'Hosea':              ('Hosea',           '28-HOS'),
'Joel':               ('Joel',            '29-JOE'),
'Amos':               ('Amos',            '30-AMO'),
'Obadiah':            ('Obadiah',         '31-OBA'),
'Jonah':              ('Jonah',           '32-JON'),
'Micah':              ('Micah',           '33-MIC'),
'Nahum':              ('Nahum',           '34-NAH'),
'Habakkuk':           ('Habakkuk',        '35-HAB'),
'Zephaniah':          ('Zephaniah',       '36-ZEP'),
'Haggai':             ('Haggai',          '37-HAG'),
'Zechariah':          ('Zechariah',       '38-ZEC'),
'Malachi':            ('Malachi',         '39-MAL'),
'Matthew':            ('Matthew',         '40-MAT'),
'Mark':               ('Mark',            '41-MRK'),
'Luke':               ('Luke',            '42-LUK'),
'John':               ('John',            '43-JHN'),
'Acts':               ('Acts',            '44-ACT'),
'Romans':             ('Romans',          '45-ROM'),
'I Corinthians':      ('1 Corinthians',   '46-1CO'),
'II Corinthians':     ('2 Corinthians',   '47-2CO'),
'Galatians':          ('Galatians',       '48-GAL'),
'Ephesians':          ('Ephesians',       '49-EPH'),
'Philippians':        ('Philippians',     '50-PHI'),
'Colossians':         ('Colossians',      '51-COL'),
'I Thessalonians':    ('1 Thessalonians', '52-1TH'),
'II Thessalonians':   ('2 Thessalonians', '53-2TH'),
'I Timothy':          ('1 Timothy',       '54-1TI'),
'II Timothy':         ('2 Timothy',       '55-2TI'),
'Titus':              ('Titus',           '56-TIT'),
'Philemon':           ('Philemon',        '57-PHM'),
'Hebrews':            ('Hebrews',         '58-HEB'),
'James':              ('James',           '59-JAM'),
'I Peter':            ('1 Peter',         '60-1PE'),
'II Peter':           ('2 Peter',         '61-2PE'),
'I John':             ('1 John',          '62-1JN'),
'II John':            ('2 John',          '63-2JN'),
'III John':           ('3 John',          '64-3JN'),
'Jude':               ('Jude',            '65-JUD'),
'Revelation of John': ('Revelation',      '66-REV'),
}

modules = SwordModules('LEB.zip')
found_modules = modules.parse_modules()
bible = modules.get_bible_from_module('LEB')

biblestruct = bible.get_structure()
books = biblestruct.get_books()
books = books['ot'] + books['nt']

fileno = 0

for book in books:
    num_chap = book.num_chapters
    bookname = bookinfo[book.name][0]
    OUT = bookinfo[book.name][1]
    chapters = book.chapter_lengths
    for chapnum, verses in enumerate(chapters):
        num = chapnum+1
        print(bookname, 'Chapter', num)
        chaptername = f'{OUT}{num:03}' if bookname == 'Psalms' else f'{OUT}{num:02}'
        filename = f'{chaptername}.org'
        print(bookname, num, '=>', filename)

        with open(filename, 'w') as outfile:
            fileno += 1
            outfile.write(f'* {bookname} {num} (LEB)\n')
            outfile.write(f':PROPERTIES:\n:ID: LEB/{chaptername}\n:END:\n\n')
            for v in range(1, verses+1):
                verse = bible.get(books=[book.name], chapters=[num], verses=[v])
                verse = verse.strip()
                verse = re.sub('\s+', ' ', verse)
                outfile.write(f"{v}. {verse}\n")

print(f'{fileno} files generated.')
