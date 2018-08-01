
empNum = 0
salaryNum = 0
salarys = []

while True:
    s = input('请输入员工的薪资（按Q或者q结束）')
    if s.upper() == 'Q':
        print("输入完成")
        break
    s = float(s)
    if s < 0:
        continue
    empNum += 1
    salarys.append(s)
    salaryNum += s

print("人数为{0}".format(empNum))
print(salarys)
print("平均工资为{0}".format(salaryNum/empNum))