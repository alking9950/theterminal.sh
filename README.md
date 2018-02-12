## API


### Single Character Behavior

I ran a program to make network requests with all the single characters
representing ascii values 0 to 255 as the parameters for
http://theterminal.sh/repl?command={} replacing `{}` with the character.

All responses came back with 200 status codes and and the `'<p>:{} not
found.</p>'` response, except for the characters `#`, and `&` which both
responded with 204 status codes.

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

## sql_out.txt

* The first line is missing the '1' from 1PAnAkYDHQn83AZHEnoXvvDnuPgKkwpvPc

* First column is the address second column is the hash 160

* This output Seems to correspond to the query in __addr.sql
    + via /u/rezpkt
    + https://www.reddit.com/r/bitcoinpuzzles/comments/7vphjz/theterminalsh/dtw5x6r/

The following are the corresponding block numbers and their respective nonce
values:

Addr   Block  Nonce
1PAnA  2773   1391322658
1NwC7  2774   1983279132
1GEbV  2775   65349048
1GYUZ  2776   3790112039
1jngx  2777   1949148959
1K68U  2778   1225964035

## Other Observations

### duplicate query parameters

    curl -H -D- "http://theterminal.sh/repl?command=me&command=me"

Returns 409 conflict:

    HTTP/1.1 409 Conflict
    Date: Mon, 12 Feb 2018 04:28:35 GMT
    Content-Length: 0
    Connection: keep-alive
    X-Powered-By: ASP.NET
    Server: Microsoft-IIS/6.0

The same response occurs when trying to use the array-like syntax:

    curl -v -D- "http://theterminal.sh/repl?command\[\]=me"
