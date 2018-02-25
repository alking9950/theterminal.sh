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

### mem ADDRESS

ADDRESS appears that it should be in hexidecimal between 0 and FFFFFFFF,
however, it doesn't really error out with other characters.

For HEX values of ADDRESS between 0 and 3E7 `mem` responds with:

    ERROR: ADDRESS IS LOCKED.

For many addresses `mem` responds with:

    0000 0000 0000 0000 0000 0000 0000 0000

The HEX contents of a zip file is returned for addresses between B105F00D and
B105F026.

`mem B105F027` returns:

    undefined


Note: While `B105F00D` returns the same result as `b105f00d`, `3E7` returns a
different result than `3e7`. ~~I'm not sure what to make of that.~~

Note Update: It turns out the parser on the server interprets `3e7` as `3 *
10^7`, or `30000000` hence why it doesn't respond as locked. Another example is
`1e7`, or `10000000`, the evaluated string is no more than 8 characters long so
it is a valid address. `1e8` (`100000000`) is 9 characters long so `ERROR:
INVALID MEMORY ADDRESS` is returned. Finally `1e20` is an invalid memory
address because the resulting number is 21 characters long, however, `1e21`
results in `ERROR: ADDRESS IS LOCKED` because Javascript converts `1e21` into
`1e+21` which is only 5 characters long.

`mem D15EA5E` returns a list of links whose output looks like:

```
**WARNING:** This memory address has been infected.
Please select reboot sequence key to reload permission table.
[E3F0EA4C707](/reboot/6803ad/e3f0ea4c707)[F93F2CD2062](/reboot/6803ad/f93f2cd2062)[E139FA822D6](/reboot/6803ad/e139fa822d6)[EE5F2C8F3D2](/reboot/6803ad/ee5f2c8f3d2)
[E6E9EE7F757](/reboot/6803ad/e6e9ee7f757)[F443B3C7BB5](/reboot/6803ad/f443b3c7bb5)[DAAA5B87770](/reboot/6803ad/daaa5b87770)[EE68D4A98EE](/reboot/6803ad/ee68d4a98ee)
[E2D08A23AC3](/reboot/6803ad/e2d08a23ac3)[FDFF48C8744](/reboot/6803ad/fdff48c8744)[E84119A4F01](/reboot/6803ad/e84119a4f01)[F666A541C46](/reboot/6803ad/f666a541c46)
[FCF7795571E](/reboot/6803ad/fcf7795571e)[F6D913EAC34](/reboot/6803ad/f6d913eac34)[FD52AFD054D](/reboot/6803ad/fd52afd054d)[FC3F6B8BDA4](/reboot/6803ad/fc3f6b8bda4)
[F98686F1165](/reboot/6803ad/f98686f1165)[F35B71BC785](/reboot/6803ad/f35b71bc785)[F7670142F96](/reboot/6803ad/f7670142f96)[F579513B608](/reboot/6803ad/f579513b608)
[F2FE2669E57](/reboot/6803ad/f2fe2669e57)[DBC264530C5](/reboot/6803ad/dbc264530c5)[FD86800A849](/reboot/6803ad/fd86800a849)[E3B3D427860](/reboot/6803ad/e3b3d427860)
[E9832327F23](/reboot/6803ad/e9832327f23)[E29D17CAD61](/reboot/6803ad/e29d17cad61)[F9A1A8B1A2C](/reboot/6803ad/f9a1a8b1a2c)[E084EE75BA0](/reboot/6803ad/e084ee75ba0)
[EEFA0C654E5](/reboot/6803ad/eefa0c654e5)[E2D83E4604A](/reboot/6803ad/e2d83e4604a)[EEB69EDC2DC](/reboot/6803ad/eeb69edc2dc)[EC1374C3DE4](/reboot/6803ad/ec1374c3de4)
[F3B500E5094](/reboot/6803ad/f3b500e5094)[E3BA612558B](/reboot/6803ad/e3ba612558b)[F0FC90B3C0E](/reboot/6803ad/f0fc90b3c0e)[EA6A3BF1534](/reboot/6803ad/ea6a3bf1534)
[ECD567E411C](/reboot/6803ad/ecd567e411c)[E5B403F9FD6](/reboot/6803ad/e5b403f9fd6)[E95E9F928FC](/reboot/6803ad/e95e9f928fc)[FA883921BC9](/reboot/6803ad/fa883921bc9)
[E10DC337382](/reboot/6803ad/e10dc337382)[E709F91C502](/reboot/6803ad/e709f91c502)[F5B96E6392A](/reboot/6803ad/f5b96e6392a)[F416B42F5A3](/reboot/6803ad/f416b42f5a3)
[FFE84AFE215](/reboot/6803ad/ffe84afe215)[F9296EBCEE3](/reboot/6803ad/f9296ebcee3)[F1DCE7B3B73](/reboot/6803ad/f1dce7b3b73)[F49CD46CFFD](/reboot/6803ad/f49cd46cffd)
[EA82D0BA2B8](/reboot/6803ad/ea82d0ba2b8)[DBB443B6183](/reboot/6803ad/dbb443b6183)[E02794E4A6F](/reboot/6803ad/e02794e4a6f)[E1D9C4F7248](/reboot/6803ad/e1d9c4f7248)
[FA4C69D955D](/reboot/6803ad/fa4c69d955d)[FC774A1F301](/reboot/6803ad/fc774a1f301)[FA671484C0F](/reboot/6803ad/fa671484c0f)[DF19CE5F596](/reboot/6803ad/df19ce5f596)
[E82E86AC4B5](/reboot/6803ad/e82e86ac4b5)[FB7DFB27A89](/reboot/6803ad/fb7dfb27a89)[F49E50D5A0A](/reboot/6803ad/f49e50d5a0a)[E6018DD7F14](/reboot/6803ad/e6018dd7f14)
[E3FF7C59262](/reboot/6803ad/e3ff7c59262)[F1C9A258BEF](/reboot/6803ad/f1c9a258bef)[EF21BEA7A53](/reboot/6803ad/ef21bea7a53)[F0FF7322C2B](/reboot/6803ad/f0ff7322c2b)
[F5F45EAC1BB](/reboot/6803ad/f5f45eac1bb)[E982029341C](/reboot/6803ad/e982029341c)[F334A6F1B91](/reboot/6803ad/f334a6f1b91)[E21DA87204B](/reboot/6803ad/e21da87204b)
[DDBA3036ECC](/reboot/6803ad/ddba3036ecc)[EAE318BB624](/reboot/6803ad/eae318bb624)[E9AA1B94912](/reboot/6803ad/e9aa1b94912)[FF2A0059147](/reboot/6803ad/ff2a0059147)
[FA93F5E21B4](/reboot/6803ad/fa93f5e21b4)[F524E2A9406](/reboot/6803ad/f524e2a9406)[E2D6F13A94C](/reboot/6803ad/e2d6f13a94c)[DE6EB50E649](/reboot/6803ad/de6eb50e649)
[E6895139BCE](/reboot/6803ad/e6895139bce)[E9D31F1A43E](/reboot/6803ad/e9d31f1a43e)[F60ACA25048](/reboot/6803ad/f60aca25048)[F9F4ED7EC6D](/reboot/6803ad/f9f4ed7ec6d)
[DEC35BD2C1C](/reboot/6803ad/dec35bd2c1c)[DD1796EA70C](/reboot/6803ad/dd1796ea70c)[EBEB81C1E8C](/reboot/6803ad/ebeb81c1e8c)[EFEF35FB9DD](/reboot/6803ad/efef35fb9dd)
```

As far as we know all links at this point redirect with a body containing
`Found. Redirecting to /reboot.html`.

User ludu discovered a set of duplicate "key" value (first part of url), which
may be of interest. Those can be found in `generated/duplicate_keys.txt`.

* `D15EA5E` address discovered by mapleleaffan_09 in discord channel.
* `mem` command discovered by ludu in discord channel.

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
