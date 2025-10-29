from collections import Counter

def solution(participant, completion):
    
    cnt = Counter(participant) - Counter(completion)
    
    return list(cnt.keys())[0]
    
#     answer = ''
#     dict_list = []
    
#     dict_list = dict(zip(range(len(participant)), participant))
    
#     n = len(dict_list)
    
#     for i in range(n):
#         if dict_list[i] in completion:
#             completion.remove(dict_list[i])
#         else:
#             answer = dict_list[i]
    
# #     default dictionary 쓰자
    
#     return answer