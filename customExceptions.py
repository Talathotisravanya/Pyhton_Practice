

class testlinkExceptions(Exception):
        pass
    
class branchDoesNotExist(testlinkExceptions):

    def __init__(self,msg):
        """
        """
        super(branchDoesNotExist, self).__init__(msg)
        self.msg=msg
        
class projectDoesNotExist(testlinkExceptions):

    def  __init__(self,msg):
        super(projectDoesNotExist, self).__init__(msg)
        self.msg=msg
        
class testCaseDoesNotExist(testlinkExceptions):

    def __init__(self,msg):
        super(testCaseDoesNotExist, self).__init__(msg)
        self.msg=msg

class invalidTestCase(testlinkExceptions):

    def __init__(self,msg):
        super(invalidTestCase, self).__init__(msg)
        self.msg=msg
        

        
