class Jadwal:
    def __init__(self, hari, mata_kuliah, jam):
        self.hari = hari
        self.mata_kuliah = mata_kuliah
        self.jam = jam
    
    def tampilkan_jadwal(self):
        print(f"Hari: {self.hari}")
        print(f"Mata Kuliah: {self.mata_kuliah}")
        print(f"Jam: {self.jam}")
        print("-----------------")