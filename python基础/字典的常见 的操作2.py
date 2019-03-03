




student = {
    "name" : "卡卡罗特",
    "age" : 1,
    "imagUrl" : "腾讯",
}


if __name__ == "__main__":
   k =  student.keys()
   print(k)

   v = student.values()
   print(v)

   y = student.items()
   print(y)

   # ss = y[0]
   # print(ss)
   # ss = y[1]
   # print(ss)

   for temp in y:
       print(temp,end= "")
       print()
       print("key = %s ,value =%s"%(temp[0],temp[1]))
       # print()

   print("=========================")
   for a , b in student.items():
       print("key = %s ,value =%s"%(a,b))


   # k1 = student.keys(0)
   # v1 = student.values(0)
   # i1 = student.items(0)
   # print(k1)
   # print(v1)
   # print(i1)