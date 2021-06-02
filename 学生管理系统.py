def showInfo():
    print("-"*30)
    print("      学生管理系统")
    print("1.添加学生信息")
    print("2.删改学生信息")
    print("3.修改学生信息")
    print("4.查询学生信息")
    print("5.查看所有学生信息")
    print("6.按总分降序排列")#总分取整数
    print("7.退出系统")
    print("-"*30)
def addInfo(students):
    print("您选择了添加学生信息功能")
    name=input("请输入姓名：")
    stuid=input("请输入学号（不可重复）：")
    age=input("请输入年龄：")
    score=int(input("请输入学生总分："))
    i=0
    j=0
    while len(students)!=0:
       for temp in students:
          if temp['id']==stuid:
            j=1
            break
          else:
             i=i+1
    if j==1:
           print("输入学号重复，添加失败！")
    else:
           stuInfo={}
           stuInfo['name']=name
           stuInfo['id']=stuid
           stuInfo['age']=age
           stuInfo['score']=score
           students.append(stuInfo)
           print("添加成功!")
def deleteInfo(students):
    print("您选择了删除学生功能")
    delid=input("请输入要删除的学生学号：")
    i=0
    j=0
    for temp in students:
        if temp['id']==delid:
            j=1
            break
        else:
           i=i+1
    if j==0:
        print("没有此学号，删除失败！")
    else:
        del students[i]
        print("删除成功")
def modifyInfo(students):
    print("您选择了修改学生信息")
    alterid=input("请输入你要修改的学号：")
    i=0
    j=0
    for temp in students:
        if temp['id']==alterid:
            j=1
            break
        else:
            i=i+1
    if j==0:
        print("没有此学号，修改失败")
    else:
        while True:
                print("请选择要进行修改的内容")
                alterNum=int(input("1.修改学号\n2.修改姓名\n3.修改年龄\n4.修改分数\n5.退出"))
                if alterNum==1:
                       newid=input("请输入更改后的学号：")
                       i=0
                       j1=0
                       for temp1 in students:
                           if temp1['id']==newid:
                              j1=1
                              break
                           else:
                              i=i+1
                           if j1==1:
                               print("输入学号不能重复")
                           else:
                              temp['id']=newid
                              print("学号修改成功！")
                elif alterNum==2:
                      newName=intput("请输入更改后的姓名：")
                      temp['name']=newName
                      print("姓名修改成功！")
                elif alterNum==3:
                     newAge=input("请输入更改后的年龄：")
                     temp['age']=newAge
                     print("年龄修改成功！")
                elif alterNum==4:
                     newscore=int(input("请输入更改后的分数："))
                     temp['score']=newscore
                     print("分数修改成功！")
                elif alterNum==5:
                     break
                else:
                    print("输入错误重新输入！")        
def checkInfo(students):
    check_id=input("请输入要查询的学号：")
    i=0
    j=0
    for temp in students:
        if temp['id']==check_id:
            j=1
            break
    if j==1:
        print("学号:%s\n姓名:%s\n年龄:%s\n分数:%d\n"%(temp['id'],temp['name'],temp['age'],temp['score']))
    else:
        print("查询失败，没有该学生")
    
    
def checkAll_Info(students):
    print("所有学生信息如下：")
    for temp in students:
        print("学号:%s\n姓名:%s\n年龄:%s\n分数:%d\n"%(temp['id'],temp['name'],temp['age'],temp['score']))
        print("*"*20)
    
def descending_order(students):
    print("您选择了按总分排序")
    n=len(students)
    i=0
    while i<n-1:
        j=0
        while j<n-1:
            if students[j]['score']<students[j+1]['score']:
                t=students[j]['score']
                students[j]['score']=students[j+1]['score']
                students[j+1]['score']=t
                j+=1
        i+=1
def main():
  students=[]
  while True:
        showInfo()
        num=int(input("请选择功能（序号）："))
        if num==1:
            addInfo(students)
        elif num==2:
            deleteInfo(students)
        elif num==3:
            changeInfo(students)
        elif num==4:
            checkInfo(students)
        elif num==5:
            checkAll_Info(students)
        elif num==6:
            descending_order(students)
        elif num==7:
            print("bye~~")
            break
        else:
            print("输入格式错误，请重新输入！")

main()


        
    
    
