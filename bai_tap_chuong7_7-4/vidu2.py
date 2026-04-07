class NhanVien:

    dem = 0

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
        NhanVien.dem += 1

        def hien_thi_so_luong(self):
            print("Tong nhan vien duoc tao: %d" % NhanVien.dem)
        def hien_thi_nhan_vien (self):
            print("Ten: ", self.name, ", luong: ", self.__salary)
        def cap_nhat (self, name=None, salary=None):
            self.__name = name
            self.__salary = salary

        Nhan_vien_dev = NhanVien ('Nguyen Van A', 1000)
        Nhan_vien_tset = NhanVien ('Nguyen Van B', 1200)

        Nhan_vien_dev.hien_thi_nhan_vien()
        Nhan_vien_tset.hien_thi_nhan_vien()
        
        print(Nhan_vien_dev.dem)
        print(Nhan_vien_dev.name)
        print(Nhan_vien_tset.name)
