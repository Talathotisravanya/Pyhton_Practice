import os
class creation:
   def create(self,folder,project,branches):
        #clon_1=Repo.clone_from('https://github.com/Talathotisravanya/Pyhton_Practice','/home/nexii/Desktop/gitRep')
        #clone_repo=Repo.clone('/home/nexii/10Aug17','/home/nexii/12Aug17')
        #clon=Repo.clone_from('/home/nexii/Desktop/gitRepo/','/home/nexii/Desktop/SravMy')
        #os.system('git clone /home/nexii/10Aug17 /home/nexii/myFol')
        env=os.environ['HOME']
        #g=env+'/'+folder
        #print g
        l2=os.listdir(env+'/'+folder)
        #print l2
        if project in l2:
            print "Project exist"
            l3=os.listdir(env+'/'+folder+'/'+project)
            #print l3
            if branch in l3:
                l4=os.listdir(env+'/'+folder+'/'+project+'/'+branch)
            subdir = []
            #for dirName,subdirList,fileList in os.walk(env+'/'+folder+'/'+project):
                if dirName.split('/')[-1] not in branches:
                    continue
                for i in fileList:
                    print i                        
                #for i in fileList:
                    #print i
                    #for j in lis:
                        #if j in fileList:
                            #print j
                            #print "success"       
                #l4=os.listdir(env+'/'+folder+'/'+project+'/'+i)
                #if i==branch:
                    #l5=os.listdir(env+'/'+folder+'/'+project+'/'+i)
                    #print l5

        '''
            if branch in l3:
                print branch
                #print "branch exist"
                l4=os.listdir(env+'/'+folder+'/'+project+'/'+branch+'')
                print l4
                l5=[]
                os.chdir(folder+'/'+project+'/'+branch)
                if tc in l4:
                    for i in l4:
                        print i
                        #f=open(i,'r')
                        #s=f.read()
                        #print s
                        #l5.append(s)
                #return l5
            else:
                print "branch does not exist"
                raise Exception
    
        else:
            print "project does not exist"
            raise Exception
        '''

   def save(self):
c=creation()
c.create('12Aug17','FLAS_TCASES',['comptel.robot','Project-2', 'sds'])
