#!/usr/bin/env python3

# This Python program generates an Interlinear Greek bible in org-roam format
# from a source file OpenGNT_version3_3.csv. It needs Python version at least 3.6
# This program in in the public domain.
# Author: Pieter van Oostrum, <pieter@vanoostrum.org>

import re
import csv
import sys

bookinfo = [
('Genesis',         '01-GEN'),
('Exodus',          '02-EXO'),
('Leviticus',       '03-LEV'),
('Numbers',         '04-NUM'),
('Deuteronomy',     '05-DEU'),
('Joshua',          '06-JOS'),
('Judges',          '07-JUD'),
('Ruth',            '08-RUT'),
('1 Samuel',        '09-1SA'),
('2 Samuel',        '10-2SA'),
('1 Kings',         '11-1KI'),
('2 Kings',         '12-2KI'),
('1 Chronicles',    '13-1CH'),
('2 Chronicles',    '14-2CH'),
('Ezra',            '15-EZR'),
('Nehemiah',        '16-NEH'),
('Esther',          '17-EST'),
('Job',             '18-JOB'),
('Psalms',          '19-PSA'),
('Proverbs',        '20-PRO'),
('Ecclesiastes',    '21-ECC'),
('Song of Songs',   '22-SON'),
('Isaiah',          '23-ISA'),
('Jeremiah',        '24-JER'),
('Lamentations',    '25-LAM'),
('Ezekiel',         '26-EZE'),
('Daniel',          '27-DAN'),
('Hosea',           '28-HOS'),
('Joel',            '29-JOE'),
('Amos',            '30-AMO'),
('Obadiah',         '31-OBA'),
('Jonah',           '32-JON'),
('Micah',           '33-MIC'),
('Nahum',           '34-NAH'),
('Habakkuk',        '35-HAB'),
('Zephaniah',       '36-ZEP'),
('Haggai',          '37-HAG'),
('Zechariah',       '38-ZEC'),
('Malachi',         '39-MAL'),
('Matthew',         '40-MAT'),
('Mark',            '41-MRK'),
('Luke',            '42-LUK'),
('John',            '43-JHN'),
('Acts',            '44-ACT'),
('Romans',          '45-ROM'),
('1 Corinthians',   '46-1CO'),
('2 Corinthians',   '47-2CO'),
('Galatians',       '48-GAL'),
('Ephesians',       '49-EPH'),
('Philippians',     '50-PHI'),
('Colossians',      '51-COL'),
('1 Thessalonians', '52-1TH'),
('2 Thessalonians', '53-2TH'),
('1 Timothy',       '54-1TI'),
('2 Timothy',       '55-2TI'),
('Titus',           '56-TIT'),
('Philemon',        '57-PHM'),
('Hebrews',         '58-HEB'),
('James',           '59-JAM'),
('1 Peter',         '60-1PE'),
('2 Peter',         '61-2PE'),
('1 John',          '62-1JN'),
('2 John',          '63-2JN'),
('3 John',          '64-3JN'),
('Jude',            '65-JUD'),
('Revelation',      '66-REV'),
]

def get_bookname(book):
    return bookinfo[int(book)-1][0]

def get_bookid(book):
    return bookinfo[int(book)-1][1]

INFILE = 'OpenGNT_version3_3.csv'

# options = {'strongs': False}
# for arg in sys.argv[1:]:
#     if arg in options:
#         options[arg] = True
#     else:
#         print(f'Unknown argument {arg}')

PAT_SPLIT = re.compile('[〔｜〕]')

def output_verse(outfile, verse_num, parts):
    outfile.write(f"{verse_num}. " + ' '.join(parts) + '\n')


fileno = 0
errors = 0
book = 40
prev_book = 39
prev_chapter = 0
prev_verse = 0
outfile = None
parts = []

with open(INFILE, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    next(reader) # skip header
    for row in reader:
        BkChVerse = row[6]
        Greek = row[7]
        English = row[10]
        #print (BkChVerse, Greek, English)
        #if BkChVerse == '〔40｜2｜1〕': break
        #print(PAT_SPLIT.split(BkChVerse))
        book, chapter, verse = map(int, PAT_SPLIT.split(BkChVerse)[1:-1])
        greek = PAT_SPLIT.split(Greek)[3]
        english = PAT_SPLIT.split(English)[2]

        # Check if we start a new book

        if book != prev_book:
            # New book, get info & reset previous chapter number
            bookname = get_bookname(book)
            OUT = get_bookid(book)

            # Sanity check
            if (book != prev_book + 1) or (chapter != 1) or (verse != 1):
                print('Wrong book/chapter/verse:', bookname, chapter, verse)
                errors += 1
            prev_book = book
            prev_chapter = 0

        # Check if we start a new chapter

        if chapter != prev_chapter:
            # New chapter, open file and reset previous verse number
            # Sanity check
            if (chapter != prev_chapter + 1) or (verse != 1):
                print('Wrong chapter/verse:', bookname, chapter, verse)
                errors += 1

            # If there is a verse left, output it
            if parts:
                output_verse(outfile, prev_verse, parts)
            # If there was a chapter file open, close it
            if outfile:
                outfile.close()

            if bookname == 'Psalms': # Doesn't happen in NT
                chaptername = f'{OUT}{chapter:03}'
            else:
                chaptername = f'{OUT}{chapter:02}'
            filename = f'{chaptername}.org'

            outfile = open(filename, 'w')
            fileno += 1
            outfile.write(f"* {bookname} {chapter} (GrkIL)\n")
            outfile.write(f":PROPERTIES:\n:ID: GrkIL/{chaptername}\n:END:\n\n")
            print(bookname, chapter, '=>', filename)
            prev_chapter = chapter
            prev_verse = 0
            parts = []

        # Check if we start a new verse

        if verse != prev_verse:
            # If there was a previous verse, output it
            if parts:
                output_verse(outfile, prev_verse, parts)
                parts = []
            prev_verse = verse

        parts.append(f"{greek} ({english})")

# If there is a verse left, output it
if parts:
    output_verse(outfile, prev_verse, parts)

# Close last chapter file.
if outfile:
    outfile.close()

print(f'{fileno} files generated.')
print(f'{errors} errors.')
