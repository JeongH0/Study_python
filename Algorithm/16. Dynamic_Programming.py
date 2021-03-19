"""
조건: 1. 최적 부분 구조(Optimal Substructure) -> 부분 문제들의 최적의 답을 이용해 기존 문제의 최적의 답 구하는 것
ex) 피보나치 6의 수를 구하기 위해서는 피보나치 5의 수와 피보나치 4의 수의 합을 구하는 것과 같음
2. 중복되는 부분 문제(Overlapping Subproblem) -> 완전히 중복되는 문제들은 어떻게 처리할 것인가?
즉, 최적 부분 구조가 있고, 중복되는 부분 문제들이 있다면 Dynamic Programming을 사용. 중복되는 부분문제들을 버리지 않고 한번만.
1, Memoization  -> 중복되는 계산은 한번만 계산 후 메모 (하향식 접근, Top-down Approach) -> 재귀를 통해
2. Tabulation   -> 가장 많이 쓰이는 것 부터(Bottom-Up Approach) -> 반복문을 통해

공간 최적화 또한 고려해봐라!
"""