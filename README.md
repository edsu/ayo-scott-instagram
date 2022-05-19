This was a failed attempt to locate archived copies of [Ayo Scott]'s terminated Instagram account in the Internet Archive. I noticed that he had his Instgram set up to auto-tweet new posts. So I searched for these posts using twarc2, converted the output to CSV, and wrote a little program to look up those Instagram URLs in the Internet Archive's Wayback Machine.

    $ pip3 install requirements.txt
    $ twarc2 search --archive 'from:noyodesigns instagram.com' ayo.jsonl
    $ twarc2 csv ayo.jsonl ayo.csv
    $ python3 urls.py

Sadly, not one was archived.

