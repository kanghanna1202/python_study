def solution(priorities, location):
    list_1 = priorities
    stack_list = []
    stack_index = []
    answer = 0

    for i in range(3, -1, -1):
        stack_list.append(list_1[i])
        stack_index.append(i)
    for i in range(len(stack_list)):
        num = stack_list.pop()
        stack_index.pop()
        p = 0
        for k in stack_list:
            if k > num:
                stack_list.insert(0, num)
                stack_index.insert(0, i)
                p = 1
        if p == 0:
            answer = stack_index.index(location)+1
    return answer


print(solution([2, 3, 1, 2], 2))
