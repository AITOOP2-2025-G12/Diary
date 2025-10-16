from diaries.DiarySample import DiarySample
from diaries.SotaDiary import SotaDiary
from diaries.onogiDiary import onogiDiary
from diaries.MaemuraD import MaemuraD

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), SotaDiary(), onogiDiary(),MaemuraD(),] 



for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
