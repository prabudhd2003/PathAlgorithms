**Pathfinding Algorithm Visualization**

This project visualizes two pathfinding algorithms, Dijkstra's and A*, using Python and the PyGame library. The goal is to let users interactively create start and end points, set barriers, and watch the algorithm find the shortest path in real-time.

https://github.com/user-attachments/assets/594be966-5e59-4992-8852-ed19b288da8b

How It Works:
1. Choose Algorithm: Press A for A* or D for Dijkstra.
2. Set Start & End: Left-click to place the start (coral color) and end (steel blue color) points on the grid. The first click will set the start point, and the second click will set the end point.
3. Add Barriers: Left-click to add barriers (dark gray color) to the grid after setting the start and end points.
4. Run the Algorithm: Press Space to start the selected algorithm and visualize the process.
5. Reset: Press C to clear the grid and start again.

Color Guide:
1. Lime: Nodes that are in the open set and are currently being evaluated.
2. Crimson: Closed nodes that have already been evaluated.
3. Purple: Final path from start to end.
4. White: Unvisited nodes, representing empty space.
