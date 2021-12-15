import pandas as pd
import json
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib import cm

st.title("Data Produksi Minyak Mentah Negara Tahun 1971-2015")
st.header("UAS Pemrograman Komputer (IF-2112) Institut Teknologi Bandung")
st.subheader("Devanto Wicaksono Soekardi (12220061)")

#input user
nama_negara = st.sidebar.text_input("Masukkan nama negara")
tahun = st.sidebar.number_input("Masukkan tahun", min_value=1971, max_value=2015, value = 2001, step = 1)
nilai_b = st.sidebar.number_input("Masukkan nilai B-besar negara", min_value=1, max_value=200, value = 10, step = 1)

#input user

#membuka file json dan mencocokan dengan nama negara inputan user
file = open("kode_negara_lengkap.json").read()
file_si_json = json.loads(file)
input_nama_negara = nama_negara
cek = [i for i in file_si_json if i["name"].lower() == input_nama_negara.lower()]
list_input = [i["alpha-3"] for i in cek]
#membuka file json dan mencocokan dengan nama negara inputan user

#plotting untuk soal A dengan membuka csv dan inputan diambil dari part di atas
filename = "produksi_minyak_mentah.csv"
df = pd.read_csv(filename)
data_olah =df[(df["kode_negara"] == list_input[0])]
fig, ax = plt.subplots()
ax.bar(data_olah["tahun"], data_olah["produksi"], color="black")
ax.set_xlabel("Tahun", fontsize=12)
ax.set_ylabel("Total Produksi Minyak Mentah", fontsize=12)
st.subheader("Grafik Produksi Minyak Mentah per Tahun Negara "+nama_negara.title())
st.pyplot(fig)
#plotting untuk soal A

#plotting untuk soal B
data_with_index = df.set_index("kode_negara")
data_with_index = data_with_index.drop(["WLD", "G20", "OECD", "OEU", "EU28"]) #menghapus value yang bukan negara
data_with_index = data_with_index.reset_index("kode_negara") #mengembalikan format dataframe pada kolom kode_negara
data_tahun = data_with_index[(data_with_index["tahun"] == int(tahun))] 
b_besar_negara_tahun = data_tahun.nlargest(int(nilai_b), ["produksi"])
fig, ax = plt.subplots()
cmap_name = 'Set1'
cmap = cm.get_cmap(cmap_name)
colors = cmap.colors[:len(b_besar_negara_tahun["kode_negara"])]
fig, ax = plt.subplots()
ax.bar(b_besar_negara_tahun["kode_negara"], b_besar_negara_tahun["produksi"], color=colors)
ax.set_xlabel("Kode Negara", fontsize=12)
ax.set_ylabel("Total Produksi Minyak Mentah", fontsize=12)
st.subheader(str(nilai_b) + " Besar Negara Produsen Minyak di Tahun " + str(tahun))
st.pyplot(fig)
#plotting untuk soal B

#plotting untuk soal C
data_total_produksi = data_with_index.groupby(["kode_negara"])["produksi"].sum()
data_total_produksi.sort_values(ascending=False)
b_besar_negara_total = data_total_produksi.nlargest(int(nilai_b))
b_reset = b_besar_negara_total.reset_index()
fig, ax = plt.subplots()
cmap_name = 'Set2'
cmap = cm.get_cmap(cmap_name)
colors = cmap.colors[:len(b_reset["kode_negara"])]
fig, ax = plt.subplots()
ax.bar(b_reset["kode_negara"], b_reset["produksi"], color=colors)
ax.set_xlabel("Kode Negara", fontsize=12)
ax.set_ylabel("Total Produksi Minyak Mentah", fontsize=12)
st.subheader(str(nilai_b) + " Besar Negara Produsen Minyak dari Tahun 1971-2015")
st.pyplot(fig)
#plotting untuk soal C

#tabel untuk soal D (terbesar) pada tahun T
produsen_terbesar_tahun = b_besar_negara_tahun[0:1]
negara_terbesar_tahun = produsen_terbesar_tahun.iloc[0]["kode_negara"]
besar_produksi_tahun = produsen_terbesar_tahun.iloc[0]["produksi"]
cek2 = [i for i in file_si_json if i["alpha-3"] in negara_terbesar_tahun]
list_negara = [i["name"]for i in cek2]
list_kode = [i["alpha-3"] for i in cek2]
list_region = [i["region"]for i in cek2]
list_subregion = [i["sub-region"] for i in cek2]
data_d = {"Nama Negara" : list_negara, "Kode Negara": list_kode, "Region": list_region, "Sub-region": list_subregion}
data_frame_d = pd.DataFrame(data_d)
st.write("Data Negara dengan Jumlah Produksi Terbesar di Tahun", tahun, "dengan total produksi", besar_produksi_tahun)
st.table(data_frame_d)
#tabel untuk soal D (terbesar) pada tahun T

#tabel untuk soal D (terbesar) pada keseluruhan tahun
data_terbesar = b_reset["kode_negara"][0]
besar_produksi = b_reset["produksi"][0]
cek3 = [i for i in file_si_json if i["alpha-3"] in data_terbesar]
list_negara2 = [i["name"]for i in cek3]
list_kode2 = [i["alpha-3"] for i in cek3]
list_region2 = [i["region"]for i in cek3]
list_subregion2 = [i["sub-region"] for i in cek3]
data_besar = {"Nama Negara" : list_negara2, "Kode Negara": list_kode2, "Region": list_region2, "Sub-region": list_subregion2}
data_frame_besar = pd.DataFrame(data_besar)
st.write("Data Negara dengan Jumlah Produksi Terbesar dari tahun 1971-2015 dengan total produksi", besar_produksi)
st.table(data_frame_besar)
#tabel untuk soal D (terbesar) pada keseluruhan tahun

#tabel untuk soal D (produksi = 0) pada tahun T
data_nol = data_tahun[(data_tahun["produksi"]==0)]
list_nol = list()
list_nol.extend(data_nol["kode_negara"])
cek4 = [i for i in file_si_json if i["alpha-3"] in list_nol]
list_negara3 = [i["name"]for i in cek4]
list_kode3 = [i["alpha-3"] for i in cek4]
list_region3 = [i["region"]for i in cek4]
list_subregion3 = [i["sub-region"] for i in cek4]
data_d_nol = {"Nama Negara" : list_negara3, "Kode Negara": list_kode3, "Region": list_region3, "Sub-region": list_subregion3}
data_frame_d_nol = pd.DataFrame(data_d_nol)
st.write("Data Negara dengan Jumlah Produksi Nol di Tahun", tahun)
st.table(data_frame_d_nol)
#tabel untuk soal D (produksi = 0) pada tahun T

#tabel untuk soal D (produksi = 0) pada keseluruhan tahun
data_total_reset = data_total_produksi.reset_index()
total_nol = data_total_reset[(data_total_reset["produksi"]==0)]
list_total_nol = list()
list_total_nol.extend(total_nol["kode_negara"])
cek5 = [i for i in file_si_json if i["alpha-3"] in list_total_nol]
list_negara4 = [i["name"]for i in cek5]
list_kode4 = [i["alpha-3"] for i in cek5]
list_region4 = [i["region"]for i in cek5]
list_subregion4 = [i["sub-region"] for i in cek5]
data_total_nol = {"Nama Negara" : list_negara4, "Kode Negara": list_kode4, "Region": list_region4, "Sub-region": list_subregion4}
data_frame_total_nol = pd.DataFrame(data_total_nol)
st.write("Data Negara dengan Jumlah Produksi Nol dari Tahun 1971-2015")
st.table(data_frame_total_nol)
#tabel untuk soal D (produksi = 0) pada keseluruhan tahun

#tabel untuk soal D (terkecil bukan 0) pada tahun T
data_lebih_nol = data_with_index[data_with_index['produksi'] >0]
data_terkecil = data_lebih_nol[(data_lebih_nol["tahun"]== int(tahun))]
b_kecil = data_terkecil.nsmallest(1, ["produksi"])
negara_terkecil_tahun = b_kecil.iloc[0]["kode_negara"]
besar_terkecil_tahun = b_kecil.iloc[0]["produksi"]
cek6 = [i for i in file_si_json if i["alpha-3"] in negara_terkecil_tahun]
list_negara5 = [i["name"]for i in cek6]
list_kode5 = [i["alpha-3"] for i in cek6]
list_region5 = [i["region"]for i in cek6]
list_subregion5 = [i["sub-region"] for i in cek6]
data_k = {"Nama Negara" : list_negara5, "Kode Negara": list_kode5, "Region": list_region5, "Sub-region": list_subregion5}
data_frame_k = pd.DataFrame(data_k)
st.write("Data Negara dengan Jumlah Produksi Terkecil (Bukan Nol) di Tahun", tahun, "dengan total produksi", besar_terkecil_tahun)
st.table(data_frame_k)
#tabel untuk soal D (terkecil bukan 0) pada tahun T

#tabel untuk soal D (terkecil bukan 0) pada keseluruhan tahun
data_total_kecil = data_lebih_nol.groupby("kode_negara")["produksi"].sum()
data_total_kecil.sort_values(ascending=True)
df_data_total_kecil= data_total_kecil.reset_index()
negara_terkecil_total = df_data_total_kecil.nsmallest(1, ["produksi"])
produksi_terkecil_total = negara_terkecil_total.iloc[0]["kode_negara"]
besar_terkecil_total = negara_terkecil_total.iloc[0]["produksi"]
cek7 = [i for i in file_si_json if i["alpha-3"] in produksi_terkecil_total]
list_negara6 = [i["name"]for i in cek7]
list_kode6 = [i["alpha-3"] for i in cek7]
list_region6 = [i["region"]for i in cek7]
list_subregion6 = [i["sub-region"] for i in cek7]
data_k_total = {"Nama Negara" : list_negara6, "Kode Negara": list_kode6, "Region": list_region6, "Sub-region": list_subregion6}
data_frame_k_total = pd.DataFrame(data_k_total)
st.write("Data Negara dengan Jumlah Produksi Terkecil (Bukan Nol) dari Tahun 1971-2015 dengan total produksi", besar_terkecil_total)
st.table(data_frame_k_total)
#tabel untuk soal D (terkecil bukan 0) pada keseluruhan tahun
