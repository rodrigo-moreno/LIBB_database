#import pylab


def ld(s1, s2):
  '''
  A FUNCTION THAT CALCULATES THE DIFFERENCE BETWEEN TWO STRINGS WITH
  THE LEVENSHTEIN DISTANCE. LEVENSHTEIN DISTANCE IS CALCULATED BY
  FILLING OUT A MATRIX DEPENDING ON THE IDENTITY OR LACK THEREOF
  IN THE DIFFERENT POSSITIONS OF TWO STRINGS. THE TOTAL DISTANCE IS
  GIVEN BY THE BOTTOM-RIGHT ELEMENT OF THE MATRIX. FOR MORE INFORMATION:
  http://people.cs.pitt.edu/~kirk/cs1501/Pruhs/Fall2006/Assignments/editdistance/Levenshtein%20Distance.htm
  '''
  mat = [[0 for x in range(len(s1)+1)] for x in range(len(s2)+1)]
  mat[0] = range(len(s1)+1)
  for i in range(len(mat)):
    mat[i][0] = i
#  print mat
  for n in range(1, len(mat)):            ### ITERATES THROUGH THE ROWS OF THE MATRIX
    for m in range(1, len(mat[n])):       ### ITERATES THROUGH THE "COLUMNS" OF THE MATRIX
      i = m - 1                           ### THE ITERATOR OF THE FIRST WORD
      j = n - 1                           ### THE ITERATOR OF THE SECOND WORD
      up = mat[n - 1][m]
      left = mat[n][m - 1]
      diag = mat[n - 1][m - 1]
#      print s1[i], s2[j]
      if s1[i] == s2[j]:
        cost = 0
#        print "As the values are the same, the cost is nill."
      else:
        cost = 1
#        print "As the values are different, the cost is 1."
      mat[n][m] = min([up+cost, left+cost, diag+cost])
#    print mat
  distance = mat[n][m]
  
  for i in range(len(mat)):
    print mat[i]
  return distance
