from diaries.DiarySample import DiarySample

from diaries.SotaDiary import SotaDiary
from diaries.onogiDiary import onogiDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), SotaDiary(), onogiDiary(),] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
