# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(x, y, z):
    return max([x, y, z])

# Write a Python function called mult_list() to multiply all the numbers in a list.


def mult_list(num_list):
    if len(num_list) == 0:
        return 0
    
    else:
        result = num_list[0]
        if len(num_list)>1:
            for num in num_list[1:]:
                result = result * num
                return result

# Write a Python function called rev_string() to reverse a string.
def rev_string(xtring):
    return xtring[::-1]

# Write a Python function called num_within() to check whether a number falls in a given range. 
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
def num_within(num, str_range, end_range):
    return num in range (str_range,end_range+1)

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)