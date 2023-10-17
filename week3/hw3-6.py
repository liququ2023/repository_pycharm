# 百分制转等级制

num = float(input("请输入学生的考试成绩："))
if num < 60:
    print('不合格')
elif 60 <= num < 75:
    print('合格')
elif 75 <= num < 90:
    print('良好')
else:
    print('优秀')
