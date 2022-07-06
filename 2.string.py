# 宣告一個變數，變數名字叫 string，變數值為 字串
string = "字串"

# string 因為本來就是字串，所以可以直接組合字串
print("這是字串: " + string)

# 重新給變數 string 數值為 abcdefg
string = "abcdefg"

# 在 python 中，截取字串索引值都是從 0 開始，截取
# a => 0, b => 1, c => 2 ... 以此類推
print("2 ~ 4(不含)的子字串: " + string[2:4])