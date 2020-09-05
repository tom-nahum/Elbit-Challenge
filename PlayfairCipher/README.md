# Elbit Systems challenge, part B

Another code to decrypt! This time Alice got a letter from Lyon playfair,
(Who was actually alive when the novel came out, nice one)
but the letter is encrypted. The purpose of this part is to decode Lyon's
letter. In order to decode the letter, I've used Playfair Cipher algorithm.

## Program Workflow

* The program gets 2 parameters by the command line:
    1. A text file representing the text to decode. (in this case, Lyon's
    letter).
    2. A string representing the key to decode by (in this case, "alice").

* We parse the input by removing white spaces and turn it to lower case. In
  addition, we split the text file into pairs of characters.

* Then we decode the text according to Playfair Cipher algorithm.

* Finally, we execute the decryption into a file, which called
  "decryption.txt", and we get the continuation of chapter 1 of "Alice in
  wonderland".
