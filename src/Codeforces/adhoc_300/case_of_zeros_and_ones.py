if __name__ == '__main__':
    n = int(input().strip())
    s = input().strip()
    print(abs(s.count('1') - s.count('0')))

# if __name__ == '__main__':
#     n = int(input().strip())
#     s = input().strip()
#     st = []
#     for i in range(len(s)):
#         if s[i] == '0':
#             if len(st) > 0 and st[-1] == '1':
#                 st.pop()
#             else:
#                 st.append('0')
#         else:
#             if len(st) > 0 and st[-1] == '0':
#                 st.pop()
#             else:
#                 st.append('1')
#     print(len(st))
