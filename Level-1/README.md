**Write a function called answer(data, n) that takes in a list of less than 100 integers and a number n, and returns that same list but with all of the numbers that occur more than n times removed entirely. The returned list should retain the same ordering as the original list - you don't want to mix up those carefully planned shift rotations! For instance, if data was [5, 10, 15, 10, 7] and n was 1, answer(data, n) would return the list [5, 15, 7] because 10 occurs twice, and was thus removed from the list entirely.**

Constrains:

Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.

Test Cases:

Inputs:
(int list) data = [1, 2, 3]
(int) n = 0
Output:
(int list) []

Inputs:
(int list) data = [1, 2, 2, 3, 3, 3, 4, 5, 5]
(int) n = 1
Output:
(int list) [1, 4]

Inputs:
(int list) data = [1, 2, 3]
(int) n = 6
Output:
(int list) [1, 2, 3]