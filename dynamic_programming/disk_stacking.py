from typing import List

def disk_stacking(disks: List[List[int]]):
    disks.sort(key=lambda item: item[2])
    print(disks)
    parent = [-1] * len(disks)
    height_arr = [item[2] for item in disks]
    result = []

    for idx in range(1, len(disks)):
        width, depth, height = disks[idx]
        for inner_idx in range(idx):
            c_width, c_depth, c_height = disks[inner_idx]
            if c_width < width and c_depth < depth and c_height < height:
                if height_arr[idx] < height + height_arr[inner_idx]:
                    parent[idx] = inner_idx
                    height_arr[idx] = height + height_arr[inner_idx]

    idx_height, max_height = None, -float('inf')
    for i, height in enumerate(height_arr):
        if max_height < height:
            max_height = height
            idx_height = i

    if idx_height is not None:
        if parent[idx_height] == -1:
            result.append(disks[idx_height])
        else:
            curr = idx_height
            while curr != -1:
                result.append(disks[curr])
                curr = parent[curr]

    return result[::-1]





disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]

print(disk_stacking(disks))