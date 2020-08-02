class Data:
    currLogin_id=0
    currLogin_password=''
    isLogin=False
    branchList=["ICT","CE","ME","EC","Civil","IT"]
    SemesterList=[1,2,3,4,5,6,7,8]
class Faculty:
    def __init__(self,name,uid,password):
        self.f_Name=name
        self.f_Id=uid
        self.f_Password=password
        
    def getName(self):
        return self.f_Name
        
    def getId(self):
        return self.f_Id
        
    def getPassword(self):
        return self.f_Password
        
    def __str__(self):
        return "{} {} {}".format(self.f_Name,self.f_Id,self.f_Password)

    
def getObject(ls):
        #ls=str1.split(",")
    return Faculty(ls[1],int(ls[0]),ls[2])




