`include "path.v"
module pathDecode(clk, st_node, end_node, nodeList);
	input clk;
	input [0:4] st_node, end_node;
	output reg [0:99]nodeList;
	
	wire [0:25][0:4]o;
	wire f;
	reg ff = 0;
	
	path p(clk, st_node, end_node, o, f);
	
	integer i=1, j;
	reg [0:4] crnt, prev;
	
	always @(negedge f) ff = 0;
	
	always @(posedge f) begin
		crnt = end_node;
		prev = end_node;
		{nodeList} = {nodeList, end_node};
	end
	
	always @(posedge clk) begin
	if(ff == 0) begin
		if(f == 1) begin
			prev = o[crnt];
			{nodeList} = {nodeList, prev};
			if(prev == st_node)
				ff = 1;
		end
		else begin
			crnt = end_node;
			prev = end_node;
			i=0;
		end
	end
	end
	always @(negedge clk) begin
	if(ff == 0) begin
		if(f == 1)
			crnt = prev;
		else
			prev = end_node;
	end
	end
endmodule
