"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:
- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.

What is the minimum candies you must give?

Input Format:
First line contains an integer N.
Next line contains N space separated integers.

Constraints:
1 <= N <= 106
1 <= Ai <= 103

Output Format:
Output the minimum number of candies you can give out.

Sample Input 0:
2
1 2
Sample Output 0:
3
Explanation:
The candidate with 1 rating gets 1 candy and candidate with rating cannot get 1 candy as 1 is its neighbor.
So rating 2 candidate gets 2 candies. In total, 2+1 = 3 candies need to be given out.
"""

n = int(input())
ratings = list(map(int, input().split()))
candies = [1]*n
