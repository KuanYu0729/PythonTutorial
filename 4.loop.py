# 迴圈: 程式一直進行同樣的行為

# while 迴圈，當while後面的「條件成立」，會一直做下去
num = 1
while num < 6:
  print("while: " + str(num))
  num += 1

# for 迴圈
# range: 一個區間，間隔為1；只有一個參數時，從0開始；有兩個參數時則是由「參數1」到「參數2」
for x in range(6):
  print("一個參數: " + str(x))

for x in range(1, 5):
  print("兩個參數: " + str(x))
