from typing import List


def compute_prefix_function_table(pattern: str) -> List[int]:
    m = len(pattern)
    prefix_func = [None] * m
    prefix_func[0] = -1
    k = -1
    for q in range(1, m):
        while k > -1 and pattern[k + 1] != pattern[q]:
            k = prefix_func[k]
        if pattern[k + 1] == pattern[q]:
            k += 1
        prefix_func[q] = k
    return prefix_func


def knuth_morris_pratt(text: str, pattern: str) -> List[int]:
    matches = []
    n = len(text)
    m = len(pattern)

    if not text or not pattern or n < m:
        return matches

    prefix_function_table = compute_prefix_function_table(pattern)

    q = -1

    for i in range(n):
        while q > -1 and pattern[q + 1] != text[i]:
            q = prefix_function_table[q]
        if pattern[q + 1] == text[i]:
            q += 1
        if q == m - 1:
            matches.append(i - m + 1)
            q = prefix_function_table[q]
    return matches
