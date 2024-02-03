#os imported for environment
import os
print('Below is the path of env vars')

#print(os.environ['PATH'])
import sys


#class defined for environment
class mycl:
    def myclfnc(self):
        print(f'the calling function name is {sys._getframe(  ).f_code.co_name}')


def myfunc():
 print(sys._getframe(  ).f_code.co_name)


s=mycl()

s.myclfnc()
