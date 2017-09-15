import bugzilla
import time


s=bugzilla.Bugzilla('http://192.168.50.20/bugzilla/xmlrpc.cgi')
print ("connected")
def one():
    data={
    "product":"Sample",
    "version":"ver",
    "component":"sample_component",
    "summary":"summary",
    "description":"Description"
    }
    
    bug=s.createbug(data)
    print bug
def bugzillapro():
    createinfo = s.build_createbug(
                product="Product1",
                version="2.0",
                component="Component1",
                summary="new example python-bugzilla bug %s" % time.time(),
                description="This is comment #0 of an example bug created by "
                            "the python-bugzilla.git examples/create.py script.")
            
    newbug = s.createbug(createinfo)
    print("\nCreated a new BUG!!\nCreated new bug id=%s url=%s" % (newbug.id, newbug.weburl))
    


two()
