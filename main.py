class NhanVien:
    def __init__(self, ho_ten, ngay_sinh, luong_co_ban):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.luong_co_ban = luong_co_ban
        self.luong = 0

    def tinh_luong(self):
        pass

    def in_thong_tin(self):
        print(f"Họ và tên: {self.ho_ten}")
        print(f"Ngày sinh: {self.ngay_sinh}")
        print(f"Lương cơ bản: {self.luong_co_ban}")
        print(f"Lương: {self.luong}\n")


class NhanVienSanXuat(NhanVien):
    def __init__(self, ho_ten, ngay_sinh, luong_co_ban, so_san_pham):
        super().__init__(ho_ten, ngay_sinh, luong_co_ban)
        self.so_san_pham = so_san_pham

    def tinh_luong(self):
        self.luong = self.luong_co_ban + self.so_san_pham * 5000


class NhanVienVanPhong(NhanVien):
    def __init__(self, ho_ten, ngay_sinh, luong_co_ban, so_ngay_lam_viec):
        super().__init__(ho_ten, ngay_sinh, luong_co_ban)
        self.so_ngay_lam_viec = so_ngay_lam_viec

    def tinh_luong(self):
        self.luong = self.so_ngay_lam_viec * 100000


# Hàm nhập danh sách nhân viên
def nhap_danh_sach_nhan_vien():
    danh_sach = []
    so_nhan_vien = int(input("Nhập số lượng nhân viên: "))
    for i in range(so_nhan_vien):
        loai_nhan_vien = input(
            "Nhập loại nhân viên (S: Sản xuất, V: Văn phòng): "
        ).upper()
        ho_ten = input("Nhập họ và tên: ")
        ngay_sinh = input("Nhập ngày sinh (dd/mm/yyyy): ")
        luong_co_ban = float(input("Nhập lương cơ bản: "))

        if loai_nhan_vien == "S":
            so_san_pham = int(input("Nhập số sản phẩm: "))
            nhan_vien = NhanVienSanXuat(ho_ten, ngay_sinh, luong_co_ban, so_san_pham)
        elif loai_nhan_vien == "V":
            so_ngay_lam_viec = int(input("Nhập số ngày làm việc: "))
            nhan_vien = NhanVienVanPhong(
                ho_ten, ngay_sinh, luong_co_ban, so_ngay_lam_viec
            )
        else:
            print("Loại nhân viên không hợp lệ.")
            continue

        danh_sach.append(nhan_vien)

    return danh_sach


# Hàm tính lương cho từng nhân viên
def tinh_luong_cho_nhan_vien(danh_sach):
    for nhan_vien in danh_sach:
        nhan_vien.tinh_luong()


# Hàm xuất thông tin của các nhân viên
def xuat_thong_tin_nhan_vien(danh_sach):
    for nhan_vien in danh_sach:
        nhan_vien.in_thong_tin()


# Hàm tính tổng lương của công ty
def tinh_tong_luong(danh_sach):
    return sum(nhan_vien.luong for nhan_vien in danh_sach)


# Hàm tìm nhân viên có lương cao nhất và thấp nhất
def tim_nhan_vien_luong_cao_thap(danh_sach):
    luong_cao_nhat = max(danh_sach, key=lambda x: x.luong)
    luong_thap_nhat = min(danh_sach, key=lambda x: x.luong)
    return luong_cao_nhat, luong_thap_nhat


# Hàm sắp xếp danh sách nhân viên theo mức lương giảm dần
def sap_xep_theo_luong_giam_dan(danh_sach):
    return sorted(danh_sach, key=lambda x: x.luong, reverse=True)


# Main program
danh_sach_nhan_vien = nhap_danh_sach_nhan_vien()
tinh_luong_cho_nhan_vien(danh_sach_nhan_vien)

print("\nThông tin của các nhân viên:")
xuat_thong_tin_nhan_vien(danh_sach_nhan_vien)

tong_luong = tinh_tong_luong(danh_sach_nhan_vien)
print(f"\nTổng lương của công ty: {tong_luong}")

luong_cao_nhat, luong_thap_nhat = tim_nhan_vien_luong_cao_thap(danh_sach_nhan_vien)
print("\nNhân viên có lương cao nhất:")
luong_cao_nhat.in_thong_tin()
print("\nNhân viên có lương thấp nhất:")
luong_thap_nhat.in_thong_tin()

print("\nDanh sách nhân viên theo mức lương giảm dần:")
danh_sach_giam_dan = sap_xep_theo_luong_giam_dan(danh_sach_nhan_vien)
xuat_thong_tin_nhan_vien(danh_sach_giam_dan)
