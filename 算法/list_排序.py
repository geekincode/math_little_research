# import random
# for i in range(1,6):
#     if i==1:
#         a=random.randint(1,100)
#     elif i==2:
#         b=random.randint(1,100)
#     elif i==3:
#         c=random.randint(1,100)
#     elif i==4:
#         d=random.randint(1,100)
#     else:
#         e=random.randint(1,100)

# list = []

# print("原列表为：\n",list)
# for i1 in range(len(list)-1):
#     for i2 in range(i1+1,len(list)):
#         if list[i1]>list[i2]:
#             list[i1],list[i2]=list[i2],list[i1]

# print("排序后列表为：\n",list)


class Take_Order():

    def __init__(self):
        import random
        for i in range(1,6):
            if i==1:
                a=random.randint(1,100)
            elif i==2:
                b=random.randint(1,100)
            elif i==3:
                c=random.randint(1,100)
            elif i==4:
                d=random.randint(1,100)
            else:
                e=random.randint(1,100)
        self.list = [a,b,c,d,e]

    def order(self):
        list = self.list
        print("原列表为：\n",list)
        for i1 in range(len(list)-1):
            for i2 in range(i1+1,len(list)):
                if list[i1]>list[i2]:
                    list[i1],list[i2]=list[i2],list[i1]

        print("排序后列表为：\n",list)

a = Take_Order()
b = Take_Order()
a.order()
b.order()