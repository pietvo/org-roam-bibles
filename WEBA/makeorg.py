#!/usr/bin/env python3

from lxml import etree
import sys
import re

bookinfo = {
    "GEN": ('Genesis',         '01-GEN'),
    "EXO": ('Exodus',          '02-EXO'),
    "LEV": ('Leviticus',       '03-LEV'),
    "NUM": ('Numbers',         '04-NUM'),
    "DEU": ('Deuteronomy',     '05-DEU'),
    "JOS": ('Joshua',          '06-JOS'),
    "JDG": ('Judges',          '07-JUD'),
    "RUT": ('Ruth',            '08-RUT'),
    "1SA": ('1 Samuel',        '09-1SA'),
    "2SA": ('2 Samuel',        '10-2SA'),
    "1KI": ('1 Kings',         '11-1KI'),
    "2KI": ('2 Kings',         '12-2KI'),
    "1CH": ('1 Chronicles',    '13-1CH'),
    "2CH": ('2 Chronicles',    '14-2CH'),
    "EZR": ('Ezra',            '15-EZR'),
    "NEH": ('Nehemiah',        '16-NEH'),
    "EST": ('Esther',          '17-EST'),
    "JOB": ('Job',             '18-JOB'),
    "PSA": ('Psalms',          '19-PSA'),
    "PRO": ('Proverbs',        '20-PRO'),
    "ECC": ('Ecclesiastes',    '21-ECC'),
    "SNG": ('Song of Songs',   '22-SON'),
    "ISA": ('Isaiah',          '23-ISA'),
    "JER": ('Jeremiah',        '24-JER'),
    "LAM": ('Lamentations',    '25-LAM'),
    "EZK": ('Ezekiel',         '26-EZE'),
    "DAN": ('Daniel',          '27-DAN'),
    "HOS": ('Hosea',           '28-HOS'),
    "JOL": ('Joel',            '29-JOE'),
    "AMO": ('Amos',            '30-AMO'),
    "OBA": ('Obadiah',         '31-OBA'),
    "JON": ('Jonah',           '32-JON'),
    "MIC": ('Micah',           '33-MIC'),
    "NAM": ('Nahum',           '34-NAH'),
    "HAB": ('Habakkuk',        '35-HAB'),
    "ZEP": ('Zephaniah',       '36-ZEP'),
    "HAG": ('Haggai',          '37-HAG'),
    "ZEC": ('Zechariah',       '38-ZEC'),
    "MAL": ('Malachi',         '39-MAL'),
    "MAT": ('Matthew',         '40-MAT'),
    "MRK": ('Mark',            '41-MRK'),
    "LUK": ('Luke',            '42-LUK'),
    "JHN": ('John',            '43-JHN'),
    "ACT": ('Acts',            '44-ACT'),
    "ROM": ('Romans',          '45-ROM'),
    "1CO": ('1 Corinthians',   '46-1CO'),
    "2CO": ('2 Corinthians',   '47-2CO'),
    "GAL": ('Galatians',       '48-GAL'),
    "EPH": ('Ephesians',       '49-EPH'),
    "PHP": ('Philippians',     '50-PHI'),
    "COL": ('Colossians',      '51-COL'),
    "1TH": ('1 Thessalonians', '52-1TH'),
    "2TH": ('2 Thessalonians', '53-2TH'),
    "1TI": ('1 Timothy',       '54-1TI'),
    "2TI": ('2 Timothy',       '55-2TI'),
    "TIT": ('Titus',           '56-TIT'),
    "PHM": ('Philemon',        '57-PHM'),
    "HEB": ('Hebrews',         '58-HEB'),
    "JAS": ('James',           '59-JAM'),
    "1PE": ('1 Peter',         '60-1PE'),
    "2PE": ('2 Peter',         '61-2PE'),
    "1JN": ('1 John',          '62-1JN'),
    "2JN": ('2 John',          '63-2JN'),
    "3JN": ('3 John',          '64-3JN'),
    "JUD": ('Jude',            '65-JUD'),
    "REV": ('Revelation',      '66-REV'),
}


def write_verse(outfile, in_verse, num, verse):
    # print(in_verse, num, verse)
    # Clean up whitespace
    verse = ''.join(verse).strip()
    verse = re.sub(r'\s+', ' ', verse)
    if verse: # Skip empty verses
        if in_verse:
            outfile.write(f'{num}. {verse}\n')
        else:
            outfile.write(f' {verse}\n')

if  len(sys.argv) != 2:
    print("Usage: makeorg.py <usfx.xmlFile>")
    sys.exit(1)
INFILE = sys.argv[1]

fileno = 0
outfile = None

root = etree.parse(INFILE)

for book in root.iter('book'):

    code = book.get('id')
    # Skip books we are not interested in (like intro)
    if code in bookinfo:
        bk = bookinfo[code]
        bookname = bk[0]
        OUT = bk[1]
        print(f'{code} => {bk}')
        verse = []
        versenum = 0
        in_verse = False

        for node in book.iter():
            tag = node.tag
            if tag == 'c':
                # New chapter
                chapter = int(node.get('id'))
                print(bookname, chapter)
                if outfile:
                    # Close previous chapter
                    outfile.close()
                # Open new file
                if code == 'PSA':
                    chaptername = f'{OUT}{chapter:03}'
                else:
                    chaptername = f'{OUT}{chapter:02}'
                filename = f'{chaptername}.org'
                outfile = open(filename, 'w')
                fileno += 1
                outfile.write(f'* {bookname} {chapter} (WEB)\n')
                outfile.write(f':PROPERTIES:\n:ID: WEB/{chaptername}\n:END:\n\n')
                verse = [] # Start new verse
                in_verse = False
                versenum = 0

            elif tag == 'v':
                # close previous verse if present
                if verse:
                    write_verse(outfile, in_verse, versenum, verse)
                verse = []
                in_verse = True
                versenum = int(node.get('id'))
                if node.tail:
                    verse.append(node.tail)

            elif tag == 've':
                write_verse(outfile, in_verse, versenum, verse)
                in_verse = False
                verse = []

            elif tag == 'w':
                verse.append(node.text)
                if node.tail:
                    verse.append(node.tail)

            elif tag in ['f', 'x']:  # footnote/crossref
                if node.tail:
                    verse.append(node.tail)

            elif tag in ['bk', 'd', 'q', 'qs', 'qt', 'wj']: # quotes/book/words of Jesus
                if node.text:
                    verse.append(node.text)
                if node.tail:
                    # Add tail to last child's tail to preserve order
                    try:
                        last_child = node[-1]
                        if last_child.tail:
                            last_child.tail += node.tail
                        else:
                            last_child.tail = node.tail
                    except IndexError: # there is no child
                        verse.append(node.tail)

            elif tag == 'p':
                if versenum > 0 and node.text:
                    verse.append(node.text)

        if outfile:
            outfile.close()


print(f'{fileno} files generated.')
