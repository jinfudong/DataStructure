pass
'''
第一步：数据填充，假如数据长度为 x (单位：位)，使得：
   X % 512 == 448  (即X的长度要填充到512的倍数减64)

   填充方法：第一位为1，其余为0
   需要注意的是，即使原消息长度刚好为与448模512同余，仍需要填充；即使原消息长度刚好为512的整数倍，仍需要填充。
'''


# import re
#
# str = '（香港）上海诚信工业有限公司'
#
# str = re.sub('（.*?）', '', str)
# print('hero is a break in the w')
# print('zhouri')
# print('')
# print(str)
