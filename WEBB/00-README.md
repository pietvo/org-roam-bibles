# World English Bible (WEB) - British spelling

Derived from the USFX version of the WEB, downloaded on Oct. 22, 2021 from
https://ebible.org/Scriptures/engwebpb_usfx.zip.

1. Download engwebpb_usfx.zip to the current directory

2. Extract `engwebpb_usfx.xml` from the zip file.

3. run `python3 makeorg.py engwebpb_usfx.xml`\
where `makeorg.py` is found in the `WEBA` directory (needs Python 3.6 or later).

**NOTE:** This requires the `lxml` package, which can be installed with\
`python3 -m pip install lxml`. It might be possible to rewrite the script to use the standard `xml.etree.ElementTree` module. I haven't tried that; I like `lxml`.

4. Move the generated `*.org` files to your `org-roam` directory.

## License:

The World English Bible is in the Public Domain. That means that it is not copyrighted. However, "World English Bible" is a Trademark of eBible.org.

See https://ebible.org/web/copyright.htm
