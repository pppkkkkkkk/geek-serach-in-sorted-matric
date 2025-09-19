#User function Template for python3
class Solution:
	def matSearch(self, mat, x):
	    
	    m = len(mat)
	    n = len(mat[0])
	    
	    i = 0
	    j = n-1
	    
	    while i >= 0 and j >= 0 and i<m and j<n:
	        if x == mat[i][j]:
	            return True
	        
	        if x > mat[i][j]:
	            i += 1
	        else:
	            j -= 1
	    return False
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
	    
		# Complete this function
# 		m = len(mat)
# 		n = len(mat[0])
		
# 		for i in range(m):
# 		    for j in range(n):
# 		        if mat[i][j] == x:
# 		            return True
		 
# 		return False
		
		m = len(mat)
		n = len(mat[0])
		
		cm = 0
		cn = n-1
		
# 		print(m)
# 		print(n)
# 		while cm >= 0 and cm < m and cn >= 0 and cn < n:
# 		    if mat[cm][cn] == x:
# 		        return True
# 		    elif mat[cm][cn] < x:
# 		        cm += 1
# 		    else:
# 		        cn -= 1
		        
# 		return False