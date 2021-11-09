Experiment-3

In this experiment, the goal is to implement the tic-tac-toe game using the informed serach strategy (A*)
To find the optimal position to place the 'X' or 'O', first I calculated the difference between the winning 
combinations of current player and opponent for each choice in that round, then for the maximum values obtained, 
I then calculated which choice would not lead to opponent's victory and would lead to current user's victory by
checking the number of moves required for victory for each choice and the one with least moves is selected.
If there are similar moves then it selects at random where to place the piece.

To be able to see the demonstration, download the game.py file and run the python file. No installations required.
For user's input 0-1-2 represent the first row, 3-4-5, the 2nd row and 6-7-8 the 3rd row. 
