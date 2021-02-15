from mastermind import *
import random
import sys
import io

loop = 100
count = 0
code = create_code()
test_pass = True


codestr = [str(i) for i in code]
codestr = ''.join(codestr)
#print(codestr.isdigit())

text_trap = io.StringIO()
sys.stdout = text_trap

asif = check_correctness(1, 4)

get_output = text_trap.getvalue()


sys.stdout = sys.__stdout__


#out = io.StringIO().getvalue()

print(get_output)

out = get_output

print(out)

if 'Congratulations! You are a codebreaker!\n' == out:
    print(True)
else:
    print(False)



