---
title: "Troy Hunt: Serverless to the Max: Doing Big Things for Small Dollars with Cloudflare Workers and Azure Functions"
slug: troy-hunt-serverless-to-the-max-doing-big-things-for-small-dollars-and
date: 2018-09-08 09:07:37 -0500
category: 
external-url: https://www.troyhunt.com/serverless-to-the-max-doing-big-things-for-small-dollars-with-cloudflare-workers-and-azure-functions/
hash: e2a16f70d31df3775e28a33dfd5e8de8
year: 2018
month: 09
scheme: https
host: www.troyhunt.com
path: /serverless-to-the-max-doing-big-things-for-small-dollars-with-cloudflare-workers-and-azure-functions/

---

Deep overview of how Troy Hunt designed Have I Been Pwned? to be very cost efficient to run.

> It's costing me 2.6c per day to support 141M monthly queries of 517M records.

That is amazing! The service is using Cloudflare Workers to push a lot of cached requests off of Azure. He calculates that without Cloudflare it would cost $9.19/day to run. Both of those amounts are amazing.
