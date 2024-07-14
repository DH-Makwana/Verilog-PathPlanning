`include "nodeList.v"
module tb;
	reg clk=0;
	reg [0:4]st_node = 5'd3;
	reg [0:4]end_node = 5'd25;
	wire [0:99]o;
	always #2 clk = ~clk;
	
	pathDecode n(clk, st_node, end_node, o); 
	
	integer i;
	initial begin
		$dumpfile("tb.vcd");
		$dumpvars;
		$monitor("%t : %d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d_%d", $time,o[95:99],o[90:94],o[85:89],o[80:84],o[75:79],o[70:74],o[65:69],o[60:64],o[55:59],o[50:54],o[45:49],o[40:44],o[35:39],o[30:34],o[25:29],o[20:24],o[15:19],o[10:14],o[5:9],o[0:4]);
		#500;
		$finish;
	end	
endmodule
