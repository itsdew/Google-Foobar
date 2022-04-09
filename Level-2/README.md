# 1. Please Pass the Coded Messages

You need to pass a message to the bunny workers, but to avoid detection, the code you agreed to use is... obscure, to say the least. The bunnies are given food on standard-issue plates that are stamped with the numbers <code>0-9</code> for easier sorting, and you need to combine sets of plates to create the numbers in the code. The signal that a number is part of the code is that it is divisible by <code>3</code>. You can do smaller numbers like <code>15</code> and <code>45</code> easily, but bigger numbers like <code>144</code> and <code>414</code> are a little trickier. Write a program to help yourself quickly create large numbers for use in the code, given a limited number of plates to work with.

You have L, a list containing some digits <code>(0 to 9)</code>. Write a function solution(L) which finds the largest number that can be made from some or all of these digits and is divisible by <code>3</code>. If it is not possible to make such a number, return <code>0</code> as the solution. L will contain anywhere from <code>1</code> to <code>9</code> digits.  The same digit may appear multiple times in the list, but each element in the list may only be used once.

**Test Cases:**

Input: <br>
(int list) <code>[3, 1, 4, 1]</code> <br>
Output:<br>
    (int) <code>4311</code>

Input:<br>
(int list) <code>[3, 1, 4, 1, 5, 9]</code> <br>
Output: <br>
    (int) <code>94311</code>


<br>


# 2. Power Hungry

Commander Lambda's space station is HUGE. And huge space stations take a LOT of power. Huge space stations with doomsday devices take even more power. To help meet the station's power needs, Commander Lambda has installed solar panels on the station's outer surface. But the station sits in the middle of a quasar quantum flux field, which wreaks havoc on the solar panels. You and your team of henchmen have been assigned to repair the solar panels, but you'd rather not take down all of the panels at once if you can help it, since they do help power the space station and all!

You need to figure out which sets of panels in any given array you can take offline to repair while still maintaining the maximum amount of power output per array, and to do THAT, you'll first need to figure out what the maximum output of each array actually is. Write a function <code>solution(xs)</code> that takes a list of integers representing the power output levels of each panel in an array, and returns the maximum product of some non-empty subset of those numbers. So for example, if an array contained panels with power output levels of <code>[2, -3, 1, 0, -5]</code>, then the maximum product would be found by taking the subset: <code>xs[0] = 2, xs[1] = -3, xs[4] = -5</code>, giving the product <code>2*(-3)*(-5) = 30</code>.  So <code>solution([2,-3,1,0,-5])</code> will be <code>"30"</code>.

Each array of solar panels contains at least <code>1</code> and no more than <code>50</code> panels, and each panel will have a power output level whose absolute value is no greater than <code>1000</code> (some panels are malfunctioning so badly that they're draining energy, but you know a trick with the panels' wave stabilizer that lets you combine two negative-output panels to produce the positive output of the multiple of their power values). The final products may be very large, so give the solution as a string representation of the number.

**Test Cases:**

Input: <br>
(int list) <code>[2, 0, 2, 2, 0]</code> <br>
Output: <br>
    (int) <code>8</code>

Input: <br>
(int list) <code>[-2, -3, 4, -5]</code> <br>
Output: <br>
    (int) <code>60</code>

