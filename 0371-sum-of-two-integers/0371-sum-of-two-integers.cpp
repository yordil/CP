class Solution {
public:
    int getSum(int a, int b) {
	  if(b <0 ){
		  for(int i = b ; i < 0 ; i++)
			  a--;
	  }
	  else{  
		  for(int i =0 ;  i < b ; i++)
	  a++; 
      }
		   
		   return a;
    }
};