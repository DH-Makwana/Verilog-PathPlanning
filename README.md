# Verilog-PathPlanning
Here, I have showcased how a recursive algorithm of **Pyhton** can be made in hardware using **Verilog**.

The algorithm used here is Dijkstra Path-Planning which can be understood from Python code as shown below.

## Python
In the **DijkstrasAlgo.py** we can manually add obstacles with mouse clicks.

The start key "S" and the End key "E" will assign the source and destination.

Finally, the "Space" key will start the algorithm to find the best possible path.

<img src="https://github.com/DH-Makwana/Verilog-PathPlanning/assets/107695582/c6371394-4ecb-4ea6-88b7-5fb32d9d4efd" width="350">

## Verilog
The directory **PathPlanning** has the Verilog codes for the map below.

<img src="https://github.com/DH-Makwana/Verilog-PathPlanning/assets/107695582/99ccc22f-84d1-4fd0-81b7-6941b83bdc41" width="350">


The codes were run by a Python script and the compiler was [**Iverilog**](https://github.com/steveicarus/iverilog).

Here's the output for the start node (3) and end node (25).

<img src="https://github.com/DH-Makwana/Verilog-PathPlanning/assets/107695582/85f2e9cc-eb6a-4fc4-a7a8-5c2f531cfae9" width="350">
