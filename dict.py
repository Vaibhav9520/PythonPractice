# used of from key
def cube_finder(n):
    cube = {}
    for i in range(1,n+1):
        cube[i] = i**3
    return cube
print(cube_finder(10))