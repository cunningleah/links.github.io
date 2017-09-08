---
title: "HTTP Pipelining"
date: 2011-07-28 08:20:50 +0000
external-url: http://www.blaze.io/mobile/http-pipelining-big-in-mobile/
hash: e3a0c2f66cb702cc19921c1f0cd8ce9e
annum:
    year: 2011
    month: 07
hostname: www.blaze.io
---

HTTP pipelining has been around for quite a while – since HTTP/1.1 was introduced. When using pipelining, an HTTP client may send multiple requests on the same connection, without waiting for the server to respond. Doing so practically eliminates the round-trip time (RTT) overhead of all but the first request, especially if the server responds quickly.
