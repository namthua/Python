# print('Hello world!, this is the first time I am here')
# name = 'Thuan'
# age = 20
# print(f'My name is {name}, I am {age} years old')

# address = 'Binh Duong'
# country = 'Viet Nam'
# print(f'My address is {address} province, {country}')
# print('Nice to meet you!')
# import itertools
# def pow_lst(lst, level):
#     return [x**level for x in lst]

# if __name__ == '__main__':
#     with open('Input_MaxIt_Hackerank.txt', 'r') as file:
#         k, m = map(int, file.readline().strip().split())

#         lst = []
#         for _ in range(k):
#             lst.append(list(map(int, file.readline().strip().split()))[1:])

#     lst_combination = list(itertools.product(*lst))
#     lst_pow_sum = [sum(pow_lst(list(element), 2))%m for element in lst_combination]

#     Max = 0
#     for element in lst_pow_sum:
#         if (element > Max):
#             Max = element

#     print(Max)


# import re

# if __name__ == '__main__':
#     pattern = r'^[+-]?[0-9]*\.[0-9]+$'
#     n = int(input())

#     result = []
#     for _ in range(n):
#         number = input()
#         result.append(True if re.match(pattern, number) else False)

#     for e in result:
#         print(e, end='\n')


# import re

# # Define function 
# def Search_pattern(pattern, string):
#     result = re.findall(pattern, string) 
#     if not result:
#         print(-1)
#     else:
#         for element in result:
#             print(element, end='\n')

# if __name__ == "__main__":
#     pattern = r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])([aeiouAEIOU]{2,})(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])'
#     string = input()
    
#     Search_pattern(pattern, string)

# import re

# string = '123456789'
# m = re.search('45', string)
# print(m.end())
# print(m.start())

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

if __name__ == '__main__':
    string = input()
    sub_str = input()
    
    l = len(sub_str)
    result = []
    pos = re.search(sub_str, string)
    if pos:
        start = pos.start()
        end = pos.end()-1
        result.append(tuple([start, end]))
        while (len(string) >= l):
            new_string = string[start+1:]
            pos = re.search(sub_str, new_string)
            if pos:
                start = start + pos.start() + 1
                end = end + pos.end() - 1
                result.append(tuple([start, end]))
            else:
                break
        
    if not result:
        result.append(tuple([-1, -1]))
    else:
        for e in result:
            print(e, end='\n')