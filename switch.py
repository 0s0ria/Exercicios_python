

def case_01():
    print(1)

def case_02():
    print(1)

def case_03():
    print(3)

case={1:case_01,2:case_02,3:case_03}

i = int(input())

case[i]()
