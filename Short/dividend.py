"""

· (nx1)xn.nn %
· 参酌(?)の住所 : https://tariat.tistory.com/1604

By. 倉井ルナ @Luna0x00

"""
from itertools import chain
import sys
import math

def calculate_dividend(stock_price ,shares_owned, dividend_yield):        
    dividend = (stock_price * shares_owned) * (dividend_yield / 1000)
    return dividend

# ユーザー入力を受ける | 사용자 입력 받기
stock_price = float(input("保有株式の価格を入力してください: ")) # 보유한 주식 가격을 입력하세요
shares_owned = float(input("保有している株式の数を入力してください: ")) # 보유한 주식 수를 입력하세요
dividend_yield = float(input("配当利回りを入力してください(ex: n.nn): ")) # 배당 이율을 입력하세요

# 配当金の計算結果 | 배당금 계산결과
dividend = calculate_dividend(stock_price,shares_owned, dividend_yield)
print("予想配当金: ${:.2f}".format(dividend)) # 예상 배당금
