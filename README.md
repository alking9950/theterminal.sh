# theterminal.sh Bitcoin Puzzle Workbook

This repository contains information in regards to solving the puzzle
"thetherminal.sh"

http://www.theterminal.sh

[Original reddit
thread](https://www.reddit.com/r/Bitcoin/comments/6r316b/there_is_1btc_hidden_in_the_terminal_it_is_yours/)
[Original
Removeddit](https://www.removeddit.com/r/Bitcoin/comments/6r316b/there_is_1btc_hidden_in_the_terminal_it_is_yours/)
[Current reddit
thread](https://www.reddit.com/r/bitcoinpuzzles/comments/7vphjz/theterminalsh/)

Current Prize: [2 BTC](http://www.theterminal.sh/components/motd.html)

## Commands

### cat PATH

Outputs the contents of a file.

For example:

    cat /home/user1/__addr.sql

Outputs:

    SELECT w_addr, w_id, w_owner
    FROM HRIManagementAccounts
    WHERE department_id = 4;

Without any arguments `cat` outputs:

    MISSING TARGET

With a path that is a directory, e.g., `cat /`, outputs:

    / IS A DIRECTORY

With any path that doesn't exist, e.g., `cat /foo` outputs:

    NO SUCH FILE OR DIRECTORY


### help

Outputs:

    ERROR

Responds from http://theterminal.sh/components/help.html.

### ls PATH

Outputs the contents of the listed directory.

For example:

    ls /home

Ouputs:

    ..
    admin
    martin
    unknown
    user1

**Worth Noting**
One thing that's interesting is that `..` is added to the response, but `..`
does not appear to be usable in any paths. Also note that `.` is not included.

Without any arguments `ls` outputs:

    MISSING PATH

With any path that doesn't exist, or the addition of a trailing `/`, e.g., `ls
//`, or `ls /bin/` outputs:

    *

With a path that is not a directory, e.g., `ls /bin/ls.bin`, outputs:

    /bin/ls.bin IS NOT A DIRECTORY

With a path that is not accessible, e.g., `ls /home/martin`, outputs:

    ACCESS DENIED

Interestingly one maybe can probe for files within the directory as `ls
/home/martin/key` outputs `*` which again seems to indicate the file is not
found.

### me

This command appears to only output `127.0.0.1`, localhost.

### motd

Outputs the message of the day:

    FEB 10 2018 UPDATE:
    AS BTC PRICES HAVE FALLEN DOWN, THERE ARE 2 BTC ON THIS TERMINAL

This output comes from the URL: http://theterminal.sh/components/motd.html

Unsure if there was anything here before 2018/02/10.

The `Last-Modified` header returns: Tue, 13 Feb 2018 17:56:06 GMT which is the
exact same time as the file for `help`. This could be used to track updates to
the server if all the files are updated at the same time when deploying.

### stat PATH

Outputs `File`, `Size`, `Owner`, `Created`, and `Permissions` of a given PATH.

For example:

    stat /bin/stat.bin

Outputs:

    File: /bin/stat.bin
    Size: 143
    Owner: system
    Created: 19/11/1983
    Permissions: rx

Without an argument outputs:

    MISSING TARGET

With an invalid argument outputs:

    NO SUCH FILE OR DIRECTORY

### su

This command was added 2018/02/13. This could indicate that it's not necessary
to solve the puzzle.

Appears to always output:

    INSUFFICIENT PRIVILEGES

---

The commands under `/bin` appear in the order `cat`, `ls`, `stat`, `me`. Note
that this is not alphabetical order, all files have the same dates, and this
order does not correlate with the size order.

**2018/02/13 Update**

`su.bin` now appears first in the `ls /bin` order. Everything else appears in
the same order.

## API

### Single Character Behavior

I ran a program to make network requests with all the single characters
representing ascii values 0 to 255 as the parameters for
http://theterminal.sh/repl?command={} replacing `{}` with the character.

All responses came back with 200 status codes and and the `<p>:{} not
found.</p>` response, except for the characters `#`, and `&` which both
responded with 204 status codes.

**2018/02/13 Update**

The responses no longer repeat the invalid command and instead generically
respond with `<p>command not found.</p>`.

### Etags

Requesting http://theterminal.sh/repl?command=me+{} with all 256 characters
consistently resulted in the exact same response as simply requesting
http://theterminal.sh/repl?command=me, including the etag response header,
`W/"10-lqFXmgc8eKYuSwVD65bAqqDwpDk"`.

The only exception was http://theterminal.sh/repl?command=me+% which resulted
in the not found response which is interesting because there still clearly is a
space after `me`.


### Server Side Parsing

Hexidecimal numbers representations are being parsed as numbers (from frownupon
on discord):

    curl -D- "http://theterminal.sh/repl?command=0xFFFFFFFFFFFFFFFFFF"

Outputs

    <p>4.722366482869645e+21: not found.</p>

However, binary numbers do not:

    curl -D- "http://theterminal.sh/repl?command=0b101"

    <p>0b101: not found.</p>

**2018/02/13 Update**

The input command is no longer reflected, thus this likely was just a
coincidence and has no impact on the challenge.

### duplicate query parameters

    curl -D- "http://theterminal.sh/repl?command=me&command=me"

Returns 409 conflict:

    HTTP/1.1 409 Conflict
    Date: Mon, 12 Feb 2018 04:28:35 GMT
    Content-Length: 0
    Connection: keep-alive
    X-Powered-By: ASP.NET
    Server: Microsoft-IIS/6.0

The same response occurs when trying to use the array-like syntax:

    curl -v -D- "http://theterminal.sh/repl?command\[\]=me"


## sql_out.txt

* The first line is missing the '1' from 1PAnAkYDHQn83AZHEnoXvvDnuPgKkwpvPc

* First column is the address second column is the hash 160

* This output Seems to correspond to the query in __addr.sql
    + via /u/rezpkt
    + https://www.reddit.com/r/bitcoinpuzzles/comments/7vphjz/theterminalsh/dtw5x6r/

The following are the corresponding block numbers and their respective nonce
values:

```
Addr   Block  Nonce
1PAnA  2773   1391322658
1NwC7  2774   1983279132
1GEbV  2775   65349048
1GYUZ  2776   3790112039
1jngx  2777   1949148959
1K68U  2778   1225964035
```
