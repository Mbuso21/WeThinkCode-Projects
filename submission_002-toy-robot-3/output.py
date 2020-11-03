from robot import do_replay_limit_silent


boolean  = do_replay_limit_silent()

# numList = ['forward 3','forward 2', 'forward 1']
# alpha_num = '3-1'

# alpha_num = alpha_num.split('-')
# alpha_num = [int(i) for i in alpha_num]
# # decrement_num_list = [i-1 for i in alpha_num]
# # print(decrement_num_list)
# #print(alpha_num)
# #print()
# alpha_num = [i - 1 for i in alpha_num]
# print(alpha_num)
# print()
# print(numList[alpha_num[1]:alpha_num[0]])
# print()
# print(numList[:])

string = 'replay silent 2'

if string.split(' ')[0] == 'replay':
    print(True)
else:
    print(False)

