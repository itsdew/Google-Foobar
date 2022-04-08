# Minion Task Schedule
**Write a function called <code>answer(data, n)</code> that takes in a list of less than 100 integers and a number n, and returns that same list but with all of the numbers that occur more than n times removed entirely. The returned list should retain the same ordering as the original list - you don't want to mix up those carefully planned shift rotations! For instance, if data was <code>[5, 10, 15, 10, 7]</code> and n was <code>1</code>, <code>answer(data, n)</code> would return the list <code>[5, 15, 7]</code> because <code>10</code> occurs twice, and was thus removed from the list entirely.**

**Constrains:**

Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.

**Test Cases:**

Inputs:
(int list) data = <code>[1, 2, 3]</code> </br>
(int) n = <code>0</code> </br>
Output: </br>
(int list) <code>[]</code>

Inputs: </br>
(int list) data = <code>[1, 2, 2, 3, 3, 3, 4, 5, 5]</code> </br>
(int) n = <code>1</code> </br>
Output: </br>
(int list) <code>[1, 4]</code>

Inputs: </br>
(int list) data = <code>[1, 2, 3]</code> </br>
(int) n = <code>6</code> </br>
Output: </br>
(int list) <code>[1, 2, 3]</code> </br>
