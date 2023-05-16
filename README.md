# CS 205: Artificial Intelligence
## Project 1: The Eight Puzzle, Dr. Eamonn Keogh

Author: Anirudh Tulasi
SID: 862395278
Email: atula002@ucr.edu
Date: May 15th, 2023

This puzzle problem is a basically a 3x3 tile solving puzzle which is a shorter version of the original 15 puzzle. According to Daniel Ratner and Manfred Warmuth, "The problem has been extended to an nxn board, and finding a shortest solution for the extended puzzle is NP-hard and computationally infeasible" [1]. In our case for a 3x3 tile solving puzzle which is also called the eight puzzle, we have nine tile spaces and one empty tile meaning that a tile can only be moved up, down, left, or right depending on the availability of space on the tile’s adjacent sides. One can use a desired state as the initial and goal states. However, the generalized version assumes that the bottom right tile is empty and other tiles are in the order of one to eight.

In this project, we were asked by Dr. Keogh to write a program in any language that would solve this puzzle for which I have chosen Python 3.10. I have implemented the code in Python and compared the results for depth ranging from 0 to 31 on UCS (Uniform Cost Search Algorithm), A* Misplaced Tile Algorithm, and A* Manhattan Distance Algorithm. The code and the results for the same are attached in the report below. For the structure of the report, I have followed the sample report structure provided in the "project handout" [3].

The complete report can be found in the same repo. https://github.com/anirudhtulasi/CS205P1/blob/main/AnirudhTulasi-8Puzzle-Report.pdf
