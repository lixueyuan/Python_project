height = 1.75
width = 80.5
bmi = width / height
str = ''
if bmi < 18.5:
    str = '过于轻'
elif bmi < 25:
    str = '正常'
elif bmi < 28:
    str = '过重'
elif bmi < 32:
    str = '肥胖'
elif bmi > 32:
    str = '超级肥胖'
print(str)