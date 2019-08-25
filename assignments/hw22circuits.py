#Name: Eva Yan
#Date: Sep 17, 2018. Due: Oct 15
#This program writes a logical expression equivalent to the circuit that
#computes the majority of 3 inputs: in1, in2, in3.

#link: http://www.neuroproductions.be/logic-lab/index.php?id=92745

out = (((in1) and (in2)) or ((in2) and (in3))) or (((in1) and (in2)) or ((in1) and (in3))) or (((in2) and (in3)) or ((in1) and (in3)))
