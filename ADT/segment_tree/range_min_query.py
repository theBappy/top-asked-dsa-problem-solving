import math
from typing import List

def build_segment_tree(i: int, l: int, r: int, segment_tree: List[int], arr: List[int]) -> None:
    if l == r:
        segment_tree[i] = arr[l]
        return
    mid = l + (r - l) // 2
    build_segment_tree(2 * i + 1, l, mid, segment_tree, arr)
    build_segment_tree(2 * i + 2, mid+1,r, segment_tree, arr)
    segment_tree[i] = min(segment_tree[2*i + 1], segment_tree[2*i + 2])
    
def construct_st(arr: List[int]) -> List[int]:
    n = len(arr)
    segment_tree = [math.inf] * (4 * n)
    build_segment_tree(0, 0, n-1, segment_tree, arr)
    return segment_tree

def query(start: int, end: int, i: int, l: int, r: int, segment_tree: List[int]) -> int:
    if l > end or r < start:
        return math.inf
    if l >= start and r <= end:
        return segment_tree[i]
    mid = l + (r - l) // 2
    return min(
        query(start, end , 2 * i + 1, l, mid, segment_tree),
        query(start, end , 2 * i + 2, mid+1, r, segment_tree)
    )

def rmq(st: List[int], n: int, a: int, b: int) -> int:
    return query(a, b, 0, 0, n - 1, st)
