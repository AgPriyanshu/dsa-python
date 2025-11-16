# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image. Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same colour as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same colour as the starting pixel), and so on. Replace the colour of all of the aforementioned pixels with the newColor.


directions = [[[0,-1],[-1,0]],[[1,0],[0,1]]]
              

class Solution:
  def dfs(self,i,j,image,newColor):
    image[i][j] = newColor
    col,rows = len(image[0]),len(image)
    for k in range(2):
      for l in range(2):
        i2 = i + directions[k][l][0]
        j2 = j + directions[k][l][1]
        if (i2 > -1 and i2 < rows) and (j2 > -1 and j2 < col) and image[i2][j2] == 1:
          self.dfs(i2,j2,image,newColor)


  def floodFill(self, image, sr, sc, newColor):
    row,col = len(image), len(image[0])
    for i in range(row):
      for j in range(col):
        if image[i][j] == 1:
          self.dfs(sr,sc,image,newColor)
    return image

if __name__ == '__main__':
  image = [ [1, 1, 1], [1, 1, 0], [1, 0, 1] ] 
  sr = 1 
  sc = 1 
  newColor = 2
  print(Solution().floodFill(image,sr,sc,newColor))