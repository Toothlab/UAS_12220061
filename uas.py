import pandas as pd
import json
import matplotlib.pyplot as plt
import streamlit as st

file = open("kode_negara_lengkap.json").read()
file_si_json = json.loads(file)
file_si_json
nama_negara = input("Masukkan nama negara: ")
input_nama_negara = nama_negara.capitalize()
cek = next((i for i in file_si_json if i["name"] == input_nama_negara), None)
list_input = list()
for key, val in cek.items():
    if key == "alpha-3":
        list_input.append(val)
print(list_input)

filename = "produksi_minyak_mentah.csv"
df = pd.read_csv(filename)
data_olah =df[(df["kode_negara"] == list_input[0])]
data_olah.plot(x = "tahun", y = "produksi", kind="bar", color = "black", width = 0.5, figsize = (10,5))
plt.xlabel("Tahun")
plt.ylabel("Jumlah Produksi")
judul = "Grafik Produksi Minyak Mentah per Tahun Negara {}"
plt.title(judul.format(nama_negara))
print(data_olah)

tahun = input("Masukkan tahun: ")
nilai_b = input("Masukkan b besar negara: ")
data_with_index = df.set_index("kode_negara")
data_with_index.head()
data_with_index = data_with_index.drop(["WLD", "G20", "OECD", "OEU", "EU28"])
data_tahun =data_with_index[(data_with_index["tahun"] == int(tahun))]
a = data_tahun.nlargest(int(nilai_b), ["produksi"])
a.plot(y="produksi", kind="bar", figsize = (10,5)) 
title = "{} Besar Negara Produsen Minyak di Tahun {}"
plt.title(title.format(nilai_b, tahun))
plt.xlabel("Kode Negara")
plt.ylabel("Jumlah Produksi")

data_negara = data_with_index.groupby("kode_negara")["produksi"].sum()
data_negara.sort_values(ascending=False)
b_besar_negara = data_negara.nlargest(int(nilai_b))
b_besar_negara.plot(kind="bar", figsize = (10,5)) 
title = "{} Besar Negara Produsen Minyak dari Tahun 1971-2015"
plt.title(title.format(nilai_b))
plt.xlabel("Kode Negara")
plt.ylabel("Total Produksi")