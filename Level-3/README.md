Prepare the Bunnies' Escape
===========================

You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny workers, but once they're free of the work duties the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 

You have maps of parts of the space station, each starting at a work area exit and ending at the door to an escape pod. The map is represented as a matrix of <code>0s</code> and <code>1s</code>, where <code>0s</code> are passable space and <code>1s</code> are impassable walls. The door out of the station is at the top left <code>(0,0)</code> and the door into an escape pod is at the bottom right <code>(w-1,h-1)</code>. 

Write a function <code>solution(map)</code> that generates the length of the shortest path from the station door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable <code>(0)</code>. The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from <code>2</code> to <code>20</code>. Moves can only be made in cardinal directions; no diagonal moves are allowed.

**Test Cases:**

Input: <br>
(int list) <code>[[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]</code> <br>
Output: <br>
    (int) <code>7</code>

Input: <br>
(int list) <code>[[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]</code> <br>
Output: <br>
    (int) <code>11</code>


