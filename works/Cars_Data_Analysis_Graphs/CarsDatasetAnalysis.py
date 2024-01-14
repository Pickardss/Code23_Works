import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("cars.csv")

# Markaları ayırmak için bir liste oluşturulur
markalar = []
for i in df["name"].values:
    markalar.append(i.split(" ")[0])

# Markaları ve satış sayılarını içeren bir dataframe oluşturulur
markaSatis= pd.DataFrame({'Marka': markalar})
markaSatis['Satış Sayısı'] = 1
markaSatis = markaSatis.groupby('Marka').count().reset_index()

# Yan bar grafiği oluşturma
plt.figure(figsize=(10, 12))
sns.barplot(x='Satış Sayısı', y='Marka', data=markaSatis, palette='tab20')
plt.xlabel('Satış Sayısı')
plt.ylabel('Marka')
plt.title('Marka ve Satış Sayıları Arasındaki İlişki')
plt.tight_layout()
plt.show()

################################################################

# Yıllara göre satış miktarlarını içeren bir liste oluşturulur
yillikSatis = df['year'].value_counts().reset_index()
yillikSatis.columns = ['Yıl', 'Satış Miktarı']

# Dik bar grafiği oluşturma
plt.figure(figsize=(12, 6))
sns.barplot(x='Yıl', y='Satış Miktarı', data=yillikSatis, color='green')
plt.xlabel('Yıl')
plt.ylabel('Satış Miktarı')
plt.title('Yıllara Göre Araba Satış Miktarları')
plt.tight_layout()
plt.show()

################################################################

# Yıllara göre arabaların ortalama satış fiyatları
yillikOrtSatis = df.groupby('year')['selling_price'].mean().reset_index()

# Çizgi grafiği oluşturma
plt.figure(figsize=(12, 6))
sns.lineplot(x='year', y='selling_price', data=yillikOrtSatis, marker='o')
plt.xlabel('Yıl')
plt.ylabel('Ortalama Satış Fiyatı')
plt.title('Yıllara Göre Arabaların Ortalama Satış Fiyatları')
plt.grid(True)
plt.tight_layout()
plt.show()

################################################################

# Yıllara göre ortalama kilometreleri 
yillikKM = df.groupby('year')['km_driven'].mean().reset_index()
yillikKM.columns = ['Yıl', 'Ortalama Kilometre']

# Çizgi grafiği oluşturma
plt.figure(figsize=(12, 6))
sns.lineplot(x='Yıl', y='Ortalama Kilometre', data=yillikKM, color='red', marker='o')
plt.xlabel('Yıl')
plt.ylabel('Ortalama Kilometre')
plt.title('Yıllara Göre Araba Ortalama Kilometreleri')
plt.grid(True)
plt.tight_layout()
plt.show()

################################################################

# Yıla ve yakıt türüne göre satış miktarlarını hesapla
yillikyakit = df.groupby(['year', 'fuel'])['selling_price'].count().reset_index()

# Dik çubuk grafiği oluşturma
plt.figure(figsize=(12, 8))
sns.barplot(x='year', y='selling_price', hue='fuel', data=yillikyakit, palette='Set2')
plt.xlabel('Yıl')
plt.ylabel('Satış Miktarı')
plt.title('Yıllara Göre Yakıt Tipi ve Satış Miktarı')
plt.legend(title='Yakıt Türü')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

################################################################

# Satış fiyatını daha geniş aralıklara bölen yeni bir sütun oluşturma
df['price_range'] = pd.cut(df['selling_price'], bins=[0, 500000, 1000000, 1500000, 2000000, float('inf')],
                           labels=['0-500K', '500K-1M', '1M-1.5M', '1.5M-2M', '2M+'])

# Satıcı türleri ve satış sayıları arasındaki ilişkiyi içeren veri çerçevesini oluşturun
satici = df.groupby(['seller_type', 'price_range']).size().reset_index(name='satış_sayısı')

# Scatter plot oluşturma
plt.figure(figsize=(12, 6))
sns.scatterplot(x='price_range', y='satış_sayısı', hue='seller_type', data=satici, s=100, alpha=0.7, palette='Dark2')
plt.xlabel('Satış Fiyatı Aralığı')
plt.ylabel('Satış Sayısı')
plt.title('Satıcı Türleri ve Satış Fiyatlarına Göre Araba Satış Sayısı')
plt.legend(title='Satıcı Türü', loc='upper right')
plt.grid(False)  
plt.tight_layout()
plt.show()

################################################################

# Yıllara ve vites türlerine göre ortalama satış fiyatları
vites = df.groupby(['year', 'transmission'])['selling_price'].mean().reset_index()

# Çizgi grafiği oluşturma
plt.figure(figsize=(12, 6))
sns.lineplot(x='year', y='selling_price', hue='transmission',marker="o", data=vites, palette='Set1')
plt.xlabel('Yıl')
plt.ylabel('Ortalama Satış Fiyatı')
plt.title('Yıllara ve Vites Türlerine Göre Araba Ortalama Satış Fiyatları')
plt.legend(title='Vites Türü', loc='upper right', bbox_to_anchor=(1.2, 1))
plt.grid(True)
plt.tight_layout()
plt.show()