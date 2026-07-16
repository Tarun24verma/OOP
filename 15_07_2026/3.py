def Kwargs(**detail):
    for key,value in detail.items():
        print(key,":",value)
    print(type(detail))
Kwargs(name="tarun", Age=18,course="B.Tech")