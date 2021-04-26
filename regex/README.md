# Regular Expressions
- [Intro](#intro)
- [Literals](#literals)
- [Alternation](#alternation)
- [Character Sets](#character-sets)
- [Wildcards](#wildcards)
- [Ranges](#ranges)
- [Shorthand Character Classes](#shorthand-character-classes)
- [Grouping](#grouping)
- [Fixed Quantifiers](#fixed-quantifiers)
- [Optional Quantifiers](#optional-quantifiers)
- [Multiplicity Quantifiers](#multiplicity-quantifiers)
- [Anchors](#anchors)

## Intro
Regular expressions offer a concise way of specifying string patterns which can be used for searching and matching. You can use them to validate that an email address is valid, or to search for a sequence of characters in text (just to name a few obvious examples).

Python exposes a built-in module called `re` which can be used to work with regular expressions. After importing it using `import re`, you can "compile" a string into a regular expression pattern object which gives you access to several useful methods:
  - `match()` checks for matches at the start of a string
  - `search()` scans for matches starting from any position in the string
  - `findall()` find and return all substring matches as a list of strings
  - `finditer()` same as `findall()` but returns an iterator

```python
import re
pattern = re.compile("hello")
match = pattern.match("hello world")
```

>NOTE: See [the official Python documentation](https://docs.python.org/3/howto/regex.html) for more information on using regular expressions in Python


## Literals
A trivial regular expression is a string literal which would match exactly that literal within any string data.

```python
import re
pattern = re.compile("monkey")
matches = pattern.findall("monkey see, monkey do")
```

## Alternation
You can use the `|` character for "alternation" which will match either of the expressions on each side of the `|` (returning the first matched of the two). For example, using the pattern `A|B` (where `A` and `B` are some regular expression) would return a valid `A` match first and not evaluate `B`, but only return `B` for a valid `B` match if `A` did not match.

```python
import re
pattern = re.compile("peanut|almond|pecan")
match = pattern.search("pecan butter falcon")
```

>NOTE: To match the pipe character `|` literal, escape it with a backslash `\|` or enclose it in a character set `[|]`

## Character Sets
You can specify a set of character options using square brackets `[]`.

```python
import re
pattern = re.compile("[bdh]og")
matches = pattern.findall("bog hog dog log jog") # Returns ["bog", "hog", "dog"]
```

>NOTE: You can create a negated character set by adding the `^` symbol immediately after the first square bracket. For example, `[^lj]og` would match "fog" but not "log" or "jog".

## Wildcards
Some characters are reserved for use as placeholders with special meaning. The `.` character for example will match on ANY character in it's position.

```python
import re
pattern = re.compile("the whale weighs . tons")
matches = pattern.findall("the whale weighs 8 tons, the whale weighs 10 tons")
# Returns ["the whale weighs 8 tons"]
```

## Ranges
We can use ranges with the dash character `-` to simplify character inclusion from common sets. For example `[a-z]` matches a single alphabetical lower case character, and similarly for upper case characters `[A-Z]`. To ignore case, simply specify both ranges `[A-Za-z]`. You can use this for digits as well `[0-9]`.

>NOTE: You don't need to specify the full range, but instead specify only a subset of the range. For example, `[j-p4-7]` matches any of "j", "k", ..., "p", 4, ..., 7.

## Shorthand Character Classes
To simplify ranges and character sets even more, there are a number of shorthand specifiers known as "character classes" which represent a combination of ranges.
  - `\w` the word character, short for `[A-Za-z0-9_]` (any alphanumeric character plus underscore)
  - `\d` the digit character, short for `[0-9]` (any numeric character)
  - `\s` the whitespace character, short for `[ \t\r\n\f\v]` (any space, tab, carriage return, line break, form feed, or vertical tab)
  - `\W` the negated word, or "non-word", short for `[^A-Za-z0-9_]`
  - `\D` the negated digit, or "non-digit", short for `[^0-9]`
  - `\S` the negated whitespace, or "non-whitespace" short for `[^ \t\r\n\f\v]`

## Grouping
Extending the use of alternation, we can use grouping with parentheses `()` characters to define "capture groups".

In the example below, we need the grouping with parentheses to prevent the `A|B` alternation from appearing as though `A` represents `"It's a sunny"` and `B` represents `"rainy day!"`.

```python
import re
pattern = re.compile("It's a (sunny|rainy) day!")
match = pattern.match("It's a sunny day!)") # Returns a match
```

## Fixed Quantifiers
To avoid having to explicitly write something like `\w\w\w\w\w` to match five alphanumeric characters in a row, we can use "fixed quanitifers" with curly brackets `{lowerBound, upperBound}` (where `lowerBound` and `upperBound` are optionally provided bounds on the number of instances).

```python
import re

 # Match a digit followed by at least 5, but no more than 7 "word" characters, followed by a "z" character
pattern = re.compile("\d\w{5,7}z")
match = pattern.match("3popeyez")
```

>NOTE: Quantifiers are greedy, so if an upper bound is specified the largest possible match will be returned. For example, `hu{2,5}ge` will return `huuuuuge` (if possible) instead of `huuge` or `huuuge`.

## Optional Quantifiers
To specify that a character or group is optional (i.e. appears 0 or 1 times), use the question mark character `?` immediately after the character (or group). For example, to match "Marine" or "U.S. Marine" or "United States Marine", you can use `(US |U.S. |United States )?Marine`.

>NOTE: As with other reserved characters, you can escape the question mark to match a question mark literal `\?`.

## Multiplicity Quantifiers
You can use the asterisk `*` (also known as the Kleene star) wildcard character to denote that a character can occur 0 or more times. For example, `pow wowz*` would match `pow wow` and `pow wowz` and `pow wowzzzzz`).

There is also the plus symbol `+` (Kleene plus) which denotes one or more instances of a character or group. For example, `(very )+fast` would match `very fast`, `very very fast` but not `fast`.

## Anchors
There are additional characters for "starts with" `^` and "ends with" `$` which help narrow down even more precisely the text you want to match. For example, `^Monkeys: my mortal enemy$` matches that text but does not match `Spider Monkeys: my mortal enemy` or `Monkeys: my mortal enemy in the wild`.