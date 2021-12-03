# bookUniverse
## ver1.0  
 
 Mode1-Single point skipped  
 if there is no more than one node with value 1 in a column, then no (from,to) for the column.  

 Mode2-Single point preserved  
 as long as there exists node(s) with value 1 in a column, then generate (from,to) for the column.  
 if there is only one node with value 1 in the column, then point to itself.  
 eg. row 2, then (from,to) ==> (2,2)  
