Anime List
==========


This README file provides an example of how an anime list should look like. In the file itself, a semi-colon (`;`) in the beggining of a line may be used to indicate a comment, which will be ignored by the software. This is a very basic syntax that has been imaginated to help organizing titles and queries. The website used to search for titles is [AnimeCalendar](http://animecalendar.net/).

### What exactly are these titles and queries?
A title is what the show is called, and also what you want your screen to show. A query is what you want the software to search on the website. Queries should differ from titles somehow.

### Why organizing titles and queries?
There are some titles on [AnimeCalendar](http://animecalendar.net/) that are misspelled, e.g., Nanatsu no Taizai. If you look for Nanatsu no Taizai, you'll find Nanatsu no Taiza instead. That means, searching for 'Nanatsu no Taizai' won't show any results.

### How can I tell title from query?
As said earlier, the syntax is very basic. All you have to do is separate a title from a query using a right arrow: `->`. So, `Nanatsu no Taizai -> nanatsu no taiza` will search for `nanatsu no  taiza` and show `Nanatsu no Taizai` when found. Leading and trailing spaces are stripped, which means `title->query` will be treated just like  
`  title         ->      query` would be.

### May I omit queries?
Yes. If the query is the exact same thing as the title, then you can omit the query and the title will be used as the query as well, which means that `Isuca -> Isuca` is essentially the same thing as just `Isuca`.

***

**Queries are case-insensitive.** It doesn't matter if you write `dog days`, or `DOG DAYS`, or even `DoG DaYS`they will be treated the same way.
Insert a question mark when you don't know how to represent a certain character. For example, `Shinmai Maō no Testament`: in this case, the query should (but doesn't need to) be `shinmai ma? no testament`, without the quotes. These question marks will then be converted to the `.*` regex pattern.

***

**The displaying of the message will be different for Linux and Windows.** On Linux, `notify-send` will be used to show titles airing in the current day; on Windows, a small `.vbs` script will be created, and the function `MsgBox` will be used. There will also be a terminal alternative for Linux, which will use ANSI color codes to "prettify" generated output.

***

Example list: anime_list.txt
----------------------------

    ; Use semi-colons to write comments,
    ; which will be ignored by the software.
    ;
    ; Remember to use the title->query syntax
    ; when the search term differs from the title.
    ;
    Cross Ange
    Dog Days" -> dog days
    Isuca
    Junketsu no Maria
    Log Horizon
    Nanatsu no Taizai -> nanatsu no taiza
    ; Remember also to use a question mark when you
    ; don't know how to represent a character.
    Shinmai Maou no Testament -> shinmai ma? no testament
    Seiken Tsukai no World Break
    Tokyo Ghoul √A -> tokyo ghoul

**Final note:** prefer to place the software in a place where you have write permissions  
(somewhere like `$HOME` (linux) or `%USERPROFILE%` (windows))
