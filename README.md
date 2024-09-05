Pathfinding Algorithm Visualization

This project implements and visualizes two pathfinding algorithms, A* and Dijkstra, using Python and the Pygame library. 
The goal is to show how these algorithms work in real time, enabling users to create start and end points, set up barriers, and watch the algorithm find the shortest path.

The grid is represented by cells that change color to indicate different states:
1. Orange: Start point
2. Turquoise: End point
3. Black: Barrier/Obstacle
4. Green: Cells turn green when they are added to the open set
5. Red: Closed cells that have already been evaluated
6. Purple: Final path from start to end

How it works: 
Choose Algorithm: Press A for A* and D for Dijkstra.
Set Start & End: Left-click to place the start and end points on the grid. The first click will set the start (orange) and the second will set the end (turquoise).
Add Barriers: Continue left-clicking to create barriers (black) on the grid.
Start the Algorithm: Press Space to start the selected algorithm.
Reset: Press C to clear the grid and start again.

