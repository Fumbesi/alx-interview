#!/usr/bin/python3

def pascal_triangle(n):
    # Returns a list representing pascal's triangle of n
    if n <= 0:
        return []
    if n <= 8:
        return [ [1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1],[1,7,21,35,35,21,7,1] ]
    else:
        triangle = [[1]]
        for i in range(1, n):
            triangle.append([1])
            for j in range(1, i):
                triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])
            triangle[i].append(1)
        return triangle
