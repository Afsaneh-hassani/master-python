# imports modules and global variables

import numpy as np

# getting user input as a matrix

def user_input():
   
   
   rows=[]

   for i in range(3):
      row=list(map(float, (input(f'row{i+1} (please enter 3 numbers for row {i+1} and seprate them with space ) :').split(' '))))
      rows.append(row)

   A=np.array(rows)  
   return A
   





# calculation sum od rows and columns 

def sum_rows_columns(A):
   print('Row sums:')
   
   for i in range(3):
      print(f'Row {i+1}:{A[i].sum()}')
   print('Columns sums:')  
   for i in range(3):
      print(f'Column {i+1}:{A[:,i].sum()}')
      



# main function

def main():
   A=user_input()
   sum_rows_columns(A)
   
   

if __name__=="__main__":
    main()
   










