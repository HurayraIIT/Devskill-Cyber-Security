# Introduction

Regular expressions can extract information from text such as code or log files. We need to recognize that everything is essentially a character and we write patterns to match a specific sequence of characters. Mosyt patterns use normal ASCII but unicode can also be used. 

> Patterns: 

- `abc` - matches all occurences of the string **abc** in the target file

- `\d` - matches any digit from **0 - 9**

-  `d` - matches the letter **d**

-  `.` - dot is a wildcard metacharacter. It matches any single character

-  `\.` - this matches the period character

-  `...\.` - this will match 3 characters ending with a dot. Like: **a9D.**

-  `[abc]def` - this will match any sequence that starts with "a" or "b" or "c" and ends with "def". Like: adef, cdef

-  `[^abc]` - this will match any single character except a, b and c

-  `[0-6]` - this will match any character in the range 0 - 6

-  `[a-fP-T2-8] - this will match any character in the range a - f, P - T and 2 - 8

-  `[^A-Ca-c]` - this will match a single character excluding A-C and a-c

 