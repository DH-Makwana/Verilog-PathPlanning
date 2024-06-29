# Verilog-PathPlanning
Here, I have showcased how a recursive algorithem of **Pyhton** can be made in hardware using **Verilog**.

The algorithem used here is of Dijkstra Path-Planning of which can be understood from Python code as showen below.

## Python
In the **DijkstrasAlgo.py** we can manually add obstacles with mouse clicks.

For Start key "S" and End key "E" will assign the source and destination.

Finally the "Space" key will start the algorithem to find the best possible path.

<img src="https://github.com/DH-Makwana/Verilog-PathPlanning/assets/107695582/c6371394-4ecb-4ea6-88b7-5fb32d9d4efd" width="350">

## Verilog
The directory **PathPlanning** has the verilog codes for the map shown below.

<img src="https://github.com/DH-Makwana/Verilog-PathPlanning/assets/107695582/99ccc22f-84d1-4fd0-81b7-6941b83bdc41" width="350">


The codes were run by a Python scripts and the compiler used was [**Iverilog**](https://github.com/steveicarus/iverilog).

Here's the output for the start node (3) and end node (19).

