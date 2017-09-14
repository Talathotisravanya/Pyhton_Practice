import os
import git
from git import Repo


class checkout:
    def gitFun(self,folder,repository,project,tcList):
        #e=os.environ['HOME']
        #clon=Repo.clone_from('https://github.com/Talathotisravanya/Pyhton_Practice.git',folder)
        #need to add checkout
        l1=os.listdir(folder)
        if repository in l1:
            l2=os.listdir(folder+'/'+repository)
            if project in l2:
                l3=os.listdir(folder+'/'+repository+'/'+project)
                l=[]
                for i in tcList:
                    if i in l3:
                        path=folder+'/'+repository+'/'+project+'/'
                        f=open(path+i,'r')
                        data=f.read()
                        print data
                        print ("********************************")
                        l.append(data)
                print l
            else:
                print "Branch does not exist"
                raise Exception
        else:
            print "Project does not exist"
            raise Exception
