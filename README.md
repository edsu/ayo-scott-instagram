This was a failed attempt to locate archived copies of [Ayo Scott]'s terminated Instagram account in the Internet Archive. I noticed that he had his Instgram set up to auto-tweet new posts. So I searched for these posts using twarc2, converted the output to CSV, and wrote a little program to look up those Instagram URLs in the Internet Archive's Wayback Machine.

    $ pip3 install requirements.txt
    $ twarc2 search --archive 'from:noyodesigns instagram.com' ayo.jsonl
    $ twarc2 csv ayo.jsonl ayo.csv
    $ python3 urls.py

Sadly, not one of the 1,542 Instagram URLs were archived. However it's nice to see that there have been snapshots of his [personal website][Ayo Scott]. I haven't done much in terms of seeing how complete these captures are but the [waybackprov] tool can be used to see which collections have added the homepage for his site:

```
$ waybackprov.py https://ayoscott.com/ --start 2010 --end 2022 --collapse

32 https://archive.org/details/alexacrawls
 7 https://archive.org/details/commoncrawl
 3 https://archive.org/details/survey_com00000
 2 https://archive.org/details/survey_00000
 2 https://archive.org/details/survey_00001
 2 https://archive.org/details/survey_00002
 2 https://archive.org/details/survey_00003
 2 https://archive.org/details/survey_00004
 2 https://archive.org/details/wide00014
 2 https://archive.org/details/wide00015
 2 https://archive.org/details/NO404-GDELT
 2 https://archive.org/details/wide00017
 2 https://archive.org/details/survey_00008
 2 https://archive.org/details/archiveteam_urls
 2 https://archive.org/details/mega-001
 1 https://archive.org/details/wide00011
 1 https://archive.org/details/wide00013
 1 https://archive.org/details/hackernews00000
 1 https://archive.org/details/survey_00005
 1 https://archive.org/details/survey_00007
 1 https://archive.org/details/survey_00009
 1 https://archive.org/details/GDELT_Project
```

[Ayo Scott]: https://ayoscott.com/

