seq = input().split(" ")
seq = [int(i) for i in seq]

longest_path = 1
current_path = 1
current_diff = seq[1] - seq[0]

for idx, i in enumerate(seq):
    if idx == 0:
        continue
    if current_diff == i - seq[idx - 1]:
        current_path += 1
    else:
        longest_path = max(longest_path, current_path)
        current_path = 2
        current_diff = i - seq[idx - 1]

longest_path = max(longest_path, current_path)

print(longest_path)