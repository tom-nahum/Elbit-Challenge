import string

word1 = [36, 17, 17, 44, 12, '3A']
word2 = ['3D', 9, '26A', 18, '1B']
word3 = [58, '19C', 58, 13, 31, 18]


word1_14 = [48, 21, 21, 60, 16, 52, None, None]
word2_14 = [55, 9, 486, 22, 25, None]
word3_14 = [78, 334, 78, 17, 43, 22]

word1hx = [54, 23, 23, 68, 18, 58, None, None]
word2hx = [61, 9, 618, 24, 27, None]
word3hx = [88, 412, 88, 19, 49, 24]

alice = "CHAPTER I. Down the Rabbit-Hole\n\nAlice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, ‘and what is the use of a book,’ thought Alice ‘without pictures or conversations?’\n\nSo she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.\n\nThere was nothing so VERY remarkable in that; nor did Alice think it so VERY much out of the way to hear the Rabbit say to itself, ‘Oh dear! Oh dear! I shall be late!’ (when she thought it over afterwards, it occurred to her that she ought to have wondered at this, but at the time it all seemed quite natural); but when the Rabbit actually TOOK A WATCH OUT OF ITS WAISTCOAT-POCKET, and looked at it, and then hurried on, Alice started to her feet, for it flashed across her mind that she had never before seen a rabbit with either a waistcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the field after it, and fortunately was just in time to see it pop down a large rabbit-hole under the hedge.\n\nIn another moment down went Alice after it, never once considering how in the world she was to get out again."

text = alice.translate({ord(c): None for c in string.whitespace})
print(text)

word_14 = word1_14 + word2_14 + word3_14
wordhx = word1hx + word2hx + word3hx

for i in range(1, 3):
    word = str(i) + ": "
    for char in word_15:
        if char is None:
            word += '/'
        else:
            word += text[char * i]
    print(word)
