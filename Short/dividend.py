"""

· (nx1)xn.nn %
· 参酌(?)の住所 : https://tariat.tistory.com/1604

By. 倉井ルナ @Luna0x00

"""

# Defining Variables

# Current stock price
current_price = float(input("現在価格を入力してください: ")) 

# total price of the shares purchased
purchase_amount = float(input("枚数金額を入力してください: ")) 

 # dividends per share
dividends_amount = float(input("配当額を入力してください: "))

# Number of shares held
stock_share = int(input("株式数を入力してください: ")) 

# Calculation of Total Dividend
T_D = dividends_amount * stock_share

# tax calculation
TX = T_D * 0.15

# Actual dividend calculation
SS = T_D - TX

print(f"総配当額: ${T_D}") #Total dividend
print(f"ぜいきん(15%): ${TX}") #Tax
print(f"手取り配当金: ${SS}") # actual dividend
