# 正则表达式验证身份证号是否合法

import re


def is_id_number(id_number):
    if len(id_number) != 18 and len(id_number) != 15:
        print('身份证号码长度错误')
        return False
    regularExpression = "(^[1-9]\\d{5}(18|19|20)\\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\\d{3}[0-9Xx]$)|" \
                        "(^[1-9]\\d{5}\\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\\d{3}$)"
    if re.match(regularExpression, id_number):
        return True
    else:
        return False


id_number = input('请输入您的身份证号：')
print(is_id_number(id_number))
