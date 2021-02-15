from macro import Macro

stu_no = input('stu_no: ')
pw = input('pw: ')
grade = int(input('grade: '))
index = int(input('index: '))
method = int(input('method(0:전공, 1:장바구니): '))

flag = True
while flag:
    macro = Macro(stu_no, pw, grade, index, method)
    try:
        flag = macro.run()
    except:
        macro.driver.close()
        flag = True
