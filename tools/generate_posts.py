#!/usr/bin/python

import pinboard
from datetime import datetime
from dateutil import tz
from slugify import slugify
import os
from urlparse import urlparse, parse_qsl

pb = pinboard.Pinboard(os.environ['PINBOARD_API'])

def make_post(p, timestamp):

    url_parts = urlparse(p.url)
    if url_parts.query:
        qsl = parse_qsl(url_parts.query)
        qstring = 'query:'
        for q in qsl:
            qstring = qstring + '\n    {}: "{}"'.format(q[0], q[1])
    else:
        qstring = ''

    data = {
        "title": p.description.replace('"', '\\"'),
        "slug": slugify(p.description, max_length=70, word_boundary=True),
        "date": timestamp.strftime('%Y-%m-%d %H:%M:%S %z'),
        "category": ",".join(p.tags),
        "external-url": p.url,
        "hash": p.hash,
        "year": timestamp.strftime('%Y'),
        "month": timestamp.strftime('%m'),
        "scheme": url_parts.scheme,
        "host": url_parts.netloc,
        "path": url_parts.path,
        "qstring": qstring,
        "body": p.extended.replace('{', '&#123;').replace('}', '&#125;')
    }

    return u"""---
title: "{title}"
slug: {slug}
date: {date}
category: {category}
external-url: {external-url}
hash: {hash}
year: {year}
month: {month}
scheme: {scheme}
host: {host}
path: {path}
{qstring}
---

{body}
""".format(**data)
    


def write_file(p, timestamp):

    # Make directories
    dname = "_posts/{}".format(timestamp.strftime('%Y/%m'))
    if not os.path.exists(dname):
        print "Creating %s directory" % dname
        os.makedirs(dname)

    fname = "{}/{}-{}.md".format(
        dname,
        timestamp.strftime('%Y-%m-%d'),
        slugify(p.description, max_length=70, word_boundary=True))

    if not os.path.isfile(fname):

        print "Writing %s" % fname

        file = open(fname,"w") 
        file.write(make_post(p, timestamp).encode('utf8'))      
        file.close() 

    else:

        print "ERROR: %s exists!" % (fname)


def main():
    if 'PINBOARD_API' not in os.environ:
        print "Please set PINBOARD_API environment variable."
        exit(1)

    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('America/Chicago')

    #pins = pb.posts.recent()['posts']
    pins = pb.posts.all()

    for p in pins:
        if p.shared and not p.toread:
            # Convert date from UTC to CDT
            utc = p.time.replace(tzinfo=from_zone)
            central = utc.astimezone(to_zone)

            write_file(p, central)


main()

