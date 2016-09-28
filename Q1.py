'''
Input Output

201604 APR16

200001 JAN00

000112 DEC01

123405 MAY34
'''

month = ['','JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
yyyymm = int(input())
mm = yyyymm % 100
yyyymm = yyyymm // 100
yyyymm = yyyymm % 100
print(month[mm]+str(yyyymm).zfill(2))
