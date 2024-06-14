# week-07 -> compute.py

import math

def main():

    expr1 = abs(1.6 + -4)
    print(f"abs(1.6 + -4) = {expr1}")  # Expected: 2.4

    expr2 = math.pow(6, 2)
    print(f"math.pow(6, 2) = {expr2}")  # Expected: 36.0

    expr3 = math.pow(5 // 2, 6)
    print(f"math.pow(5 // 2, 6) = {expr3}")  # Expected: 64.0

    expr4 = math.ceil(9.1)
    print(f"math.ceil(9.1) = {expr4}")  # Expected: 10

    expr5 = math.ceil(115.8)
    print(f"math.ceil(115.8) = {expr5}")  # Expected: 116

    expr6 = max(7, 4)
    print(f"max(7, 4) = {expr6}")  # Expected: 7

    expr7 = min(8, 3 + 2)
    print(f"min(8, 3 + 2) = {expr7}")  # Expected: 5

    expr8 = min(-2, -5)
    print(f"min(-2, -5) = {expr8}")  # Expected: -5

    expr9 = math.sqrt(49)
    print(f"math.sqrt(49) = {expr9}")  # Expected: 7.0

    expr10 = math.sqrt(76 + 45)
    print(f"math.sqrt(76 + 45) = {expr10}")  # Expected: 11.0

    expr11 = 100 + math.log10(100)
    print(f"100 + math.log10(100) = {expr11}")  # Expected: 102.0

    expr12 = 13 + abs(-7) - math.pow(2, 3) + 5
    print(f"13 + abs(-7) - math.pow(2, 3) + 5 = {expr12}")  # Expected: 13

    expr13 = math.sqrt(16) * max(abs(-5), abs(-3))
    print(f"math.sqrt(16) * max(abs(-5), abs(-3)) = {expr13}")  # Expected: 20.0

    expr14 = 7 - 2 + math.log10(1000) + math.log(math.pow(math.e, 5))
    print(f"7 - 2 + math.log10(1000) + math.log(math.pow(math.e, 5)) = {expr14}")  # Expected: 15.0
 
    expr15 = max(18 - 5, math.ceil(4.6 * 3))
    print(f"max(18 - 5, math.ceil(4.6 * 3)) = {expr15}")  # Expected: 18

if __name__ == "__main__":
    main()