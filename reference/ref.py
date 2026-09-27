import sys
import collections
import heapq
import bisect
import itertools
import math

sys.setrecursionlimit(300000)
sys.stdin.read().split()

dq = collections.deque()
dq.append(4)
dq.appendleft(0)
val1 = dq.pop()
val2 = dq.popleft()

c = collections.Counter()
graph = collections.defaultdict(list)

heap = []
heapq.heappush(heap, (cost, node))
cost, node = heapq.heappop(heap)

max_heap = []
heapq.heappush(max_heap, -value)
largest = -heapq.heappop(max_heap)

heapq.heapify(arr)

idx1 = bisect.bisect_left(arr, x)
idx2 = bisect.bisect_right(arr, x)

perms = list(itertools.permutations(arr))
combs = list(itertools.combinations(arr, r))
combs_r = list(itertools.combinations_with_replacement(arr, r))
prod = list(itertools.product(arr, repeat=r))
pref_sum = list(itertools.accumulate(arr))
pref_gcd = list(itertools.accumulate(arr, math.gcd))

g = math.gcd(a, b)
l = math.lcm(a, b)
root = math.isqrt(n)
c_nk = math.comb(n, k)
p_nk = math.perm(n, k)
ans = pow(base, exp, mod)
inv = pow(base, -1, mod)