L,R =map(int,input().split())
def la_so_palindrome(n):
    goc = n
    dao_nguoc = 0
    while n > 0:
        dao_nguoc = dao_nguoc * 10 + n % 10
        n //= 10
    return goc == dao_nguoc
def tong_cac_chu_so(n):
    tong = 0
    while n > 0:
        tong += n % 10
        n //= 10
    return tong
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def dem_palindrome_hop_le(L, R):
    dem = 0
    for so in range(L, R + 1):
        if la_so_palindrome(so) and la_so_nguyen_to(tong_cac_chu_so(so)):
            dem += 1
    return dem
print(dem_palindrome_hop_le(L, R))