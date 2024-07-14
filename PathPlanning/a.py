# s = ""
# for i in range(19, 0, -1):
# 	s = s + "o["+ str(5*(i))+":"+str(5*(i+1)-1)+"],"
# print(s)

import os

#Executing the Testbench
os.system("iverilog tb.v")
os.system("vvp a.out")
