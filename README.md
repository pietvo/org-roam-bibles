# Bibles in org-roam (v2) format #

This repository contains a collection of Bibles in Org-Roam (version 2)
format.

## License ##

All Bibles have a license that allows them to be freely used under certain circumstances, usually for non-commercial use. To be sure check the individual licenses. I have just passed on the licenses of the sources that I used to construct the files. I don't put any additional license for my own contribution.

**NOTE: I am not a lawyer. This is not a legal advise. If you want to be sure if you can use these Bibles in other products, consult the original sources or consult a lawyer.**

All the Bibles have been generated from downloaded files, with a Python program, that I usually called `makeorg.py`. Each directory has it own Python program. These programs are free to be used in whatever way you want.

## Structure ##

The structure of the Bibles is the same for all of them. Each chapter is a separate `.org` file.
The file name is of the form `<number>-<BOK><chapter>`, eg. `45-ROM12` for Romans 12.

  * The `<number>` is the ordinal number of the book in the traditional Protestant Bibles, 1-39 for the Old testament, 40-66 for the New Testament.
  * `<BOK>` is a three-letter abbreviation of the book, or one digit followed by a two-letter abbreviation (e.g. `1JN`).
  * `<chapter>` is the chapter number, with two digits, except for Psalms, which for obvious reasons uses three-digit numbers. Books that have only a single chapter, still use chapter number 1 for reasons of consistency. 

The file starts with a heading that is the bookname followed by the chapter number and, between parentheses, an abbreviation of the version. For example `* Romans 12 (WEB)`, where `WEB` denotes the 'World English Bible'.

See below for a list of the booknames and the codes.

The heading is followed by the `org-roam` version 2 ID:

    :PROPERTIES:
    :ID: WEB/45-ROM12
    :END:
    
This is followed by the verses as a numbered list.

Normally `org-roam` uses random IDs. I have chosen to use structured IDs, which consists of an abbreviation of the version (often the same or similar as the one in the heading), followed by the filename, separated by a slash. This way, I can write commands to easily switch from one version to another while staying in the same chapter/verse, using `org-roam-node-find`, or to go to the next or previous chapter. This can be done by manipulating the ID. The filename doesn't matter, as `org-roam` v2 uses ID's, not filenames to access the files.

This whole setup has been largely copied from Abe Peters (https://github.com/bc-abe/plain-text-bibles) with some modifications.

In my own setup I have put each Bible in a separate directory within my `org-roam` directory. This isn't necessary, but if you want to put them all in the same directory, and you have several Bible versions, it can become unwieldy, as each Bible that contains both the Old and the New Testament contains 1189 files. Moreover, if you do this with more than one Bible version, you will have to rename the files, to prevent filename clashes.

## List of Bible book names and codes ##

I use the same booknames for all English Bibles. Also for the Hebrew and Greek Bibles I have used the same names to make selecting them easier. For my Dutch Bibles (not included here) I use Dutch names, however.

| Book name       |  code    |
|:--              |:--       |
| Genesis         | `01-GEN` |
| Exodus          | `02-EXO` |
| Leviticus       | `03-LEV` |
| Numbers         | `04-NUM` |
| Deuteronomy     | `05-DEU` |
| Joshua          | `06-JOS` |
| Judges          | `07-JUD` |
| Ruth            | `08-RUT` |
| 1 Samuel        | `09-1SA` |
| 2 Samuel        | `10-2SA` |
| 1 Kings         | `11-1KI` |
| 2 Kings         | `12-2KI` |
| 1 Chronicles    | `13-1CH` |
| 2 Chronicles    | `14-2CH` |
| Ezra            | `15-EZR` |
| Nehemiah        | `16-NEH` |
| Esther          | `17-EST` |
| Job             | `18-JOB` |
| Psalms          | `19-PSA` |
| Proverbs        | `20-PRO` |
| Ecclesiastes    | `21-ECC` |
| Song of Songs   | `22-SON` |
| Isaiah          | `23-ISA` |
| Jeremiah        | `24-JER` |
| Lamentations    | `25-LAM` |
| Ezekiel         | `26-EZE` |
| Daniel          | `27-DAN` |
| Hosea           | `28-HOS` |
| Joel            | `29-JOE` |
| Amos            | `30-AMO` |
| Obadiah         | `31-OBA` |
| Jonah           | `32-JON` |
| Micah           | `33-MIC` |
| Nahum           | `34-NAH` |
| Habakkuk        | `35-HAB` |
| Zephaniah       | `36-ZEP` |
| Haggai          | `37-HAG` |
| Zechariah       | `38-ZEC` |
| Malachi         | `39-MAL` |
| Matthew         | `40-MAT` |
| Mark            | `41-MRK` |
| Luke            | `42-LUK` |
| John            | `43-JHN` |
| Acts            | `44-ACT` |
| Romans          | `45-ROM` |
| 1 Corinthians   | `46-1CO` |
| 2 Corinthians   | `47-2CO` |
| Galatians       | `48-GAL` |
| Ephesians       | `49-EPH` |
| Philippians     | `50-PHI` |
| Colossians      | `51-COL` |
| 1 Thessalonians | `52-1TH` |
| 2 Thessalonians | `53-2TH` |
| 1 Timothy       | `54-1TI` |
| 2 Timothy       | `55-2TI` |
| Titus           | `56-TIT` |
| Philemon        | `57-PHM` |
| Hebrews         | `58-HEB` |
| James           | `59-JAM` |
| 1 Peter         | `60-1PE` |
| 2 Peter         | `61-2PE` |
| 1 John          | `62-1JN` |
| 2 John          | `63-2JN` |
| 3 John          | `64-3JN` |
| Jude            | `65-JUD` |
| Revelation      | `66-REV` |
