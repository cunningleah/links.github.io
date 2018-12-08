---
title: "Amazon Quantum Ledger Database"
slug: amazon-quantum-ledger-database
date: 2018-11-29 20:30:05 -0600
category: 
external-url: https://aws.amazon.com/qldb/
hash: f70132f724c3250884aab80eabcd2042
year: 2018
month: 11
scheme: https
host: aws.amazon.com
path: /qldb/

---

Amazon introduced this highlighting that it was a technology they built in-house and are now making available to the public. It looks interesting.

> Amazon QLDB is a new class of database that eliminates the need to engage in the complex development effort of building your own ledger-like applications. With QLDB, your data’s change history is immutable – it cannot be altered or deleted – and using cryptography, you can easily verify that there have been no unintended modifications to your application’s data.

There is a lot of overlap with [Event Sourcing](https://www.martinfowler.com/eaaDev/EventSourcing.html) concepts, but I’m not sure it is applicable to that. This is marketed as providing the audit history trust of a blockchain, but not using decentralization.
