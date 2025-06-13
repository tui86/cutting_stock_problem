import numpy as np
import math
def sapxep(chieudai, sothanh):
    for i in range(len(chieudai)-1):
        for j in range(i+1, len(chieudai)):
            if (chieudai[i]<chieudai[j]):
                chieudai[i], chieudai[j]=chieudai[j], chieudai[i]
                sothanh[i], sothanh[j]=sothanh[j], sothanh[i]
def nhapdulieu():
    try:
        L=float(input("Nhập kích thước thanh được cắt: "))
        soluong=int(input("Nhập số lượng các thanh thép: "))
        chieudai=np.empty((soluong))
        sothanh=np.empty((soluong))
        for i in range(soluong):
            a=float(input(f"Nhập chiều dài thanh thứ {i+1}: "))
            chieudai[i]=a
            if (a>L):
                print("Cảnh Báo! không thế nhập chiều dài thanh cần cắt dài hơn chiều dài thanh được cắt")
                i-=1
                continue
            b=int(input(f"Nhập số lượng thanh {i+1} cần cắt: "))
            sothanh[i]=b
    except:
        print("Lỗi, vui lòng nhập lại!")
    return L, soluong, chieudai, sothanh
def taomatran(L, soluong, chieudai, sothanh):
    matrancat=np.empty((soluong, soluong))
    for i in range(len(chieudai)):
        copy_L=L
        for k in range(i):
            matrancat[i][k]=0
        for j in range(i, len(chieudai)):
            matrancat[i][j]=copy_L//chieudai[j]
            copy_L=copy_L%chieudai[j]
    return matrancat
def tinhtoan(L, soluong, chieudai, sothanh, matrancat):
    du=0
    sothanhduocdungdecat=np.zeros_like(sothanh)
    sothanhduoccat=np.zeros_like(sothanh)
    sothanh_copy=np.copy(sothanh)
    for i in range(soluong):
        tong=np.sum(matrancat[i]*chieudai)
        if matrancat[i][i]==0:
            continue
        B=math.ceil(sothanh_copy[i]/matrancat[i][i])
        sothanhduocdungdecat[i]+=B
        sothanhduoccat+=B*matrancat[i]
        sothanh_copy-=B*matrancat[i]
        du+=B*(L-tong)
    return du, sothanhduoccat, sothanhduocdungdecat
#MAIN
L, soluong, chieudai, sothanh=nhapdulieu()
sapxep(chieudai, sothanh)
matrancat=taomatran(L, soluong, chieudai, sothanh)
du, sothanhduoccat, sothanhduocdungdecat=tinhtoan(L, soluong, chieudai, sothanh, matrancat)
print("====================KẾT QUẢ====================")
for i in range(soluong):
    print(f"Số lượng thanh {chieudai[i]}m cần cắt nhỏ nhất là: {sothanhduoccat[i]}")
print(f"Tổng số thanh được dùng để cắt là: {np.sum(sothanhduocdungdecat)}")
print(f"Chiều dài thanh còn dư là: {du}")
print(f"Phương pháp cắt:")
dem=0
dem2=1
for i in sothanhduocdungdecat:
    for j in range(int(i)):
        mota=', '.join(f"{matrancat[dem][k]}x{chieudai[k]}" for k in range(len(chieudai)) if matrancat[dem][k]>0)
        print(f"Thanh thứ {dem2} cắt {mota}")
        dem2+=1
    dem+=1
if np.any(sothanhduoccat < sothanh):
    print("Cảnh báo: Một số loại chưa được cắt đủ số lượng yêu cầu!")
    for i in range(soluong):
        if sothanhduoccat[i]<sothanh[i]:
            print(f"Loại{chieudai[i]}m: yêu cầu{sothanh[i]}, đã cắt {sothanhduoccat[i]}")
