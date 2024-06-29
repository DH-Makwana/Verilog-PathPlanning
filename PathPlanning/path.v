`include "node.v"
module path(clk, st_node, end_node, prevNode, f);
	input clk;
	input [0:4]st_node, end_node;
	//output [0:49]pth;
	
	reg [0:4]currentNode;
	wire [0:3][0:4]nextNode;
	wire [0:3][0:1]addLength;
	
	node n(currentNode, {addLength[0], nextNode[0]}, {addLength[1],nextNode[1]}, {addLength[2],nextNode[2]}, {addLength[3],nextNode[3]});
	
	reg found = 0;
	reg [0:25]explored;
	reg [0:25][0:4]exploredLength;
	output reg f;
	output reg [0:25][0:4]prevNode;
	
	reg [0:1023]que;
	
	always @(st_node, end_node) begin
		z = 0;
		found = 0;
		f = 0;
		i = 0;
		x = 0;
	end
	
	integer i=0,j,k,x=0;
	reg [0:4]nn;	
	always @(posedge clk) begin
	if(found == 0) begin
		f = 1'b0;
		if(currentNode < 26) begin
		if(explored[currentNode] == 0) begin
		
		for(j=0; j<4; j=j+1) begin
			for(k=0; k<5; k=k+1) begin
				nn=nextNode[j];
				que[20*x + 5*j + k] = nn[k];
			end
		end
		x = x + 1;
		explored[currentNode] = 1'b1;
			for(j=0; j<4; j=j+1) begin
				nn=nextNode[j];
				if(nn < 26) begin
					if(exploredLength[currentNode]+addLength[j] < exploredLength[nn]) begin
						exploredLength[nn] = exploredLength[currentNode]+addLength[j];
						prevNode[nn] = currentNode;
						if(nn == end_node)
							found = 1'b1;
					end
				end
			end
		end		
		end
		i=i+1;
	end
	else
		f=1'b1;
	end
	
	integer z=0;
	always @(negedge clk) begin
		for(j=0; j<5; j=j+1) begin
			currentNode[j] = que[5*(i-1) + j];
		end
		if(z == 0) begin
		for(j=0; j<26; j=j+1) begin
			explored[j] = 1'b0;
			exploredLength[j] = 5'b11111;
		end
		currentNode = st_node;
		exploredLength[st_node] = 5'b00000;
		z=1;
		end
	end	
endmodule
