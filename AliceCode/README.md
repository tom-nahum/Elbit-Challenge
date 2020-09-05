# Elbit Systems challenge, part A

Link to problem: https://codepen.io/nsxr51/full/ZEQMNRj
Alice needs our help to decode a given sequence of numbers,
which represent indexes of letters in chapter 1 of "Alice in wonderland".
The problem is we don't know in which base the numbers are. In addition, it's
given that the numbers have to be multiplied by a constant. So we have to find
the base and the number to multiply by.

## Program Workflow

* The program gets 2 parameters by the command line:
    1. A text file representing the letters stock
       (in that case, chapter 1 of "Alice in wonderland").
    2. A text file representing the pattern to decrypt.
       (in that case 36,17,17,44,12,3A,/,/,3D,9,26A,18,1B,/,58,19C,58,13,31,18)

* Then we parse the files, by removing white spaces from the text file and
  insert the pattern to an array.

* The main stage of the program, is to decode the pattern.
  I noticed that the pattern included the letters "A,B,C,D", so I thought the
  base has to be 14 or higher, were base 16 is hexadecimal.
  In order to convert the given numbers to decimal base, I created the
  function convert_to_decimal, which gets a number and return the number in
  decimal.
  In order to know in which number to multiply the number, I guessed it will
  be a number between 1-4, so i used a simple for loop to try these
  possibilities.
  Then I searched in the text for these indexes, and printed all the
  possibilities.
  Which led me to this website: https://rb.gy/uquefg