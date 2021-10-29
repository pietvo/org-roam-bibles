# World English Bible (WEB) - U.S. spelling

Derived from the USFX version of the WEB, downloaded on Oct. 19, 2021 from
https://ebible.org/Scriptures/engwebp_usfx.zip.

1. Download engwebp_usfx.zip to the current directory

2. Extract `engwebp_usfx.xml` from the zip file.

3. run `python3 makeorg.py engwebp_usfx.xml`\
(needs Python 3.9 or later).

**NOTE:** This requires the `lxml` package, which can be installed with\
`python3 -m pip install lxml`. It might be possible to rewrite the script to use the standard `xml.etree.ElementTree` module. I haven't tried that; I like `lxml`.

4. Move the generated `*.org` files to your `org-roam` directory.

## License:

The World English Bible is in the Public Domain. That means that it is not copyrighted. However, "World English Bible" is a Trademark of eBible.org.

See https://ebible.org/web/copyright.htm
