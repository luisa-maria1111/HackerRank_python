"""
Arithmetic Operators

Task:
Read two integers from STDIN and print three lines where:
1.The first line contains the sum of the two numbers.
2.The second line contains the difference of the two numbers (first - second).
3.The third line contains the product of the two numbers.

Input Format:
The first line contains the first integer, a. 
The second line contains the second integer, b.

Constraints:
    1 <= a <= 10**10
    1 <= b <= 10**10

Output Format:
Print the three lines as explained above.

Sample Input:
3
2

Sample Output:
5
1
6

Explanation:
3 + 2 = 5
3 - 2 = 1
3 * 2 = 6

@author: Luísa Maria Mesquita
"""
def arithmetic_operators():
    a = int(input("A: "))
    b = int(input("B: "))
    
    print(a+b)
    print(a-b)
    print(a*b)
