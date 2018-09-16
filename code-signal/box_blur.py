def boxBlur(image):
    irows =  len(image) - 2
    icols =  len(image[0]) - 2
    blurred = [[0 for x in range(icols)] for y in range(irows)]


    for i in range(irows):
        for j in range(icols):
            curr = image[i][j] + image[i][j+1] + image[i][j+2]+image[i+1][j] + image[i+1][j+1] + image[i+1][j+2]+image[i+2][j] + image[i+2][j+1] + image[i+2][j+2]
            curr = curr // 9
            blurred[i][j] = curr
    return blurred
image = [[7, 4, 0, 1],
         [5, 6, 2, 2],
         [6, 10, 7, 8],
         [1, 4, 2, 0]]

def boxBlur(image):
    row_num = len(image[0])-3+1
    col_num = len(image)-3+1
    return [ [  int(sum([ sum(k)for k in list(zip(*image[i:i+3]))[j:j+3]])/9) for j in range(row_num) ] for i in range(col_num) ]


print(boxBlur(image))


