from texttable import Texttable
table = Texttable()
jawab = "y"
no = 0
nama = []
nim = []
ntugas = []
nuts = []
nuas = []
while (jawab =="y"):
	nama.append (input ("Nama : "))
	nim.append (input("NIM : "))
	ntugas.append (input("Nilai Tugas : "))
	nuts.append (input("Nilai UTS : "))
	nuas.append (input("Nilai UAS : "))
	jawab = input ("Tambah Data (y/t)?")
	no += 1
print ("            Daftar MAHASISWA         ")
for n in range (no):
	nt = float(ntugas[n])*30/100
	nu = float(nuts[n])*35/100
	na = float(nuas[n])*35/100
	akhir = nt+nu+na

	table.add_rows([['No','Nama', 'NIM','Tugas','UTS', 'UAS', 'Nilai Akhir'], [n+1,nama[n],nim[n],ntugas[n],nuts[n],nuas[n],akhir]])
print (table.draw())	