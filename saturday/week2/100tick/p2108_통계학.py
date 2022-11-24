##########################################
#
# p2108 [통계학]
#
# [문제]
# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다.
# 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다.
# 단, N은 홀수라고 가정하자.
# 1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 3.최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
#
# [입력]
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다.
# 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다.
# 입력되는 정수의 절댓값은 4,000을 넘지 않는다.
#
# [출력]
# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
# 둘째 줄에는 중앙값을 출력한다.
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 넷째 줄에는 범위를 출력한다.
#
# [https://www.acmicpc.net/problem/2108]
#
#
##########################################
# IMPORT
##########################################
from typing import List, Dict, Tuple
from collections import Counter
import sys
#
#
# FOR FAST INPUT
#
#
input = sys.stdin.readline
##########################################
# INPUT
##########################################
N = int(input())
nums = []

# N회 만큼 숫자 Input, nums List에 저장
for _ in range(N):
    nums.append(int(input()))

##########################################
# MAIN LOGIC
##########################################
# 1. 산술평균
avg: int = round(sum(nums) / N)
#
# 중앙값, 범위를 구하기 위해서 정렬 필요
nums.sort()
#
# 2. 중앙값
# N은 항상 홀수이므로 N//2는 항상 nums의 중간 index
# nums = [1,2,3]
# 3(length) // 2(N) = 1
# nums[1] = 2
median: int = nums[N//2]
#
# 3. 범위(출력은 4번째)
rng: int = nums[-1] - nums[0]
#
# 4. 최빈값
#
# Cpp에서 최빈값을 구하기 위해서는 Counting Sort,
# 혹은 Map으로 각 숫자의 누적 출현 빈도를 저장한 뒤,
# Vector로 변환하여 Sort하는 등의 과정이 필요했지만
# Python은 그러한 과정을 생략하고 최빈값을 구할 수 있는 Library를 기본적으로 제공
#
cnt = Counter(nums).most_common()  # 모든 최빈값을 (값, 출현 빈도)를 담은 List 형태로 return
# cnt[n][0]: 수
# cnt[n][1]: 출현 빈도
# len(cnt)로 최빈값의 갯수를 검사하여 최빈값이 여러 개인 경우 2번째 수 반환
# 최빈값이 하나인 경우 1번째 요소의 수 반환
mean = cnt[1][0] if len(cnt) > 1 and cnt[0][1] == cnt[1][1] else cnt[0][0]
#
# ternary operator와 비슷한 식
# <condition> ? <expression1> : <expression2>;
# Python에서는 <expression1> if <condition> else <expression2>와 같이 사용
# 조건에서 최빈값이 여러 개일 경우에는 두 번째로 작은 값을 출력하라고 했음


##########################################
# OUTPUT
##########################################
print(avg)
print(median)
print(mean)
print(rng)
