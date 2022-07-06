# 宣告一個變數，變數名字叫 number，變數值為 123
number = 123

# 因為 number 是數字，所以需要透過 str 的方法，將 number 轉成字串
print("這是數字: " + str(number))

# 數字加上另一個數字
# 別的語言支援 ++ or --
# ++ => += 1
# -- => -= 1
# 方法一
number = number + 1
print("number: " + str(number))
# 方法二 (比較常用的做法)
number += 1
print("number: " + str(number))

# 比較需要特別注意事項
# 數字除法
# 一個除號會除到小數
# 兩個除號會除到整數，剩餘的小數也不會做到四捨五入，而是無條件捨去
result1 = number / 3
print("number / 3: " + str(result1))
result2 = number // 3
print("number // 3: " + str(result2))
