# -*- coding: utf-8 -*-
"""clustering_amazon_product.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aGqbQFxYC1DadNOnNMWWsA4-tWT9aVxV
"""

import pandas as pd
import matplotlib.pyplot as plt
import zipfile
import os

# Membaca dataset
file_path = 'aftercleansingamazon.xlsx'
df = pd.read_excel(file_path)

# Menghitung jumlah produk dalam setiap kategori
category_counts = df['category'].value_counts()

# Mengurutkan kategori berdasarkan jumlah produk
sorted_categories = category_counts.sort_values(ascending=False)

# Menampilkan hasil pengurutan
sorted_df = pd.DataFrame({'Category': sorted_categories.index, 'Jumlah Produk': sorted_categories.values})
print("Hasil Pengurutan Kategori:")
print(sorted_df)

# Mengambil kategori dengan jumlah produk paling banyak
most_popular_category = sorted_categories.idxmax()
most_popular_group = df[df['category'] == most_popular_category]
print("Kategori yang paling banyak produk:")
print(most_popular_category)

# Menampilkan produk dalam setiap kategori dalam file Excel dalam satu file zip
output_zip_path = 'produk_per_kategori.zip'
with zipfile.ZipFile(output_zip_path, 'w') as zip_file:
    for category in sorted_categories.index:
        # Membuat grup berdasarkan kategori
        group = df[df['category'] == category]

        # Menyimpan setiap grup ke dalam file Excel temporary
        temp_excel_path = f'temp_{category}.xlsx'
        group[['product_id', 'product_name', 'discounted_price', 'actual_price']].to_excel(temp_excel_path, index=False)

        # Menambahkan file temporary ke dalam zip
        zip_file.write(temp_excel_path, arcname=f'{category}.xlsx')

        # Menghapus file temporary setelah ditambahkan ke dalam zip
        os.remove(temp_excel_path)

# Menampilkan konfirmasi
print(f"Data produk per kategori telah disimpan dalam file zip: {output_zip_path}")

# Membuat diagram batang
plt.figure(figsize=(10, 6))
sorted_categories.plot(kind='bar', color='skyblue')
plt.title('Jumlah Produk dalam Setiap Kategori (Diurutkan)')
plt.xlabel('Kategori')
plt.ylabel('Jumlah Produk')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Menampilkan diagram batang
plt.show()