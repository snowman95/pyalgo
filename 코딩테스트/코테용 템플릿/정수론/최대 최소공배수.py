import math

# 최대공배수
math.gcd([1,2,3])

# 최소공약수
math.lcm([1,2,3]) # 3.9 버전이상 제공

def lcm(a,b): #3.8 버전이하 직접구현
    return a*b//math.gcd(a,b)