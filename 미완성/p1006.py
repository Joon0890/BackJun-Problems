import sys
sys.setrecursionlimit(10**6) 

data = sys.stdin.read().splitlines()
T = int(data[0])  # 첫 번째 줄에서 T 값 가져오기

for i in range(T):
    section_list = []

    base_idx = 1 + i * 3  # 현재 테스트케이스의 시작 인덱스

    N, W = map(int, data[base_idx].split())  # N, W 추출
    second_line = list(map(int, data[base_idx + 1].split()))  # second_line 추출
    third_line = list(map(int, data[base_idx + 2].split()))  # third_line 추출

    N_list = [i for i in range(1, 2 * N + 1)]

    for i in range(N):

        if second_line[i] + third_line[i] <= W:
            section_list.append((i + 1, i + 1 + N))

        if i < N - 1 and second_line[i] + second_line[i + 1] <= W:
            section_list.append((i + 1, i + 2))

        if i == N - 1 and second_line[-1] + second_line[0] <= W:
            section_list.append((N, 1))

        if i < N - 1 and third_line[i] + third_line[i + 1] <= W:
            section_list.append((i + N + 1, i + N + 2))

        if i == N - 1 and third_line[-1] + third_line[0] <= W:
            section_list.append((N + 1, 2*N))

    # print("section_list: ", section_list)

    section_list.sort()  
    max_length = 0
    max_line = []

    def find_max_set(index, selected, used_numbers: set):
        global max_length, max_line
        if index == len(section_list):
            # print(f"DEBUG: selected = {selected}")  
            if max_length < len(selected):
                max_length = len(selected)
                max_line = selected.copy()
            return 

        num1, num2 = section_list[index]
        if num1 not in used_numbers and num2 not in used_numbers:  # ✅ O(1)
            used_numbers.update([num1, num2])
            find_max_set(index + 1, selected + [section_list[index]], used_numbers)
            used_numbers.discard(num1)
            used_numbers.discard(num2)

        find_max_set(index + 1, selected, used_numbers)

    find_max_set(0, [], set())

    max_line_set = {x for pair in max_line for x in pair} if max_line else set()
    diff = list((max_line_set | set(N_list)) - (max_line_set & set(N_list)))
    print(len(diff) + max_length)


"""
1
8 100
70 60 55 43 57 60 44 50
58 40 47 90 45 52 80 40
"""