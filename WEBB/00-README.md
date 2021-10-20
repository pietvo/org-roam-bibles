# World English Bible (WEB) - British spelling

Derived from the USFX version of the WEB, downloaded on Dec. 8, 2020 from
https://ebible.org/Scriptures/engwebpb_usfx.zip.

1. Download engwebpb_usfx.zip to the current directory

2. Extract `engwebpb_usfx.xml` from the zip file.

3. run `python3 makeorg.py engwebpb_usfx.xml`\
where `makeorg.py` is found in the `WEBA` directory (needs Python 3.9 or later).

4. Move the generated `*.org` files to your `org-roam` directory.

NOTE: I have made two manual corrections after step 3:\
a) In 2 Chronicles 3:15 (14-2CH03.org), the word 'heigh' was replaced by 'high'.\
b) In Zephaniah 1:17 (file 36-ZEP01.org), a full stop (.) was added between 'LORD' and 'Their'

## License:

The World English Bible is in the Public Domain. That means that it is not copyrighted. However, "World English Bible" is a Trademark of eBible.org.

See https://ebible.org/web/copyright.htm
