class Hunian():
    def __init__(self, jenis, jml_penghuni = 1, jml_kamar = 1, hargaSewa = "Rp 1.200.000"):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.hargaSewa = hargaSewa
    
    def get_jenis(self):
        return self.jenis

    def get_hargaSewa(self):
        return self.hargaSewa

    def get_dokumen(self):
        pass

    def get_jml_kamar(self):
        return self.jml_kamar

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_summary(self):
        return " Hunian "+ self.jenis +",  ditempati oleh " + str(self.jml_penghuni) + " orang" + " dengan Harga Sewa : " + str(self.hargaSewa)
