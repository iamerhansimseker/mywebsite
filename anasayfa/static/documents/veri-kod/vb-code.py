import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

data = pd.read_csv('C:\\Users\\erhan\\Desktop\\heart.csv')

print("Temel Bilgiler:")
print(data.info())
print("\nÖzet İstatistikler:")
print(data.describe())

sns.countplot(data['target'])
plt.title('Hedef Değişkenin Dağılımı')
plt.xlabel('Kalp Hastalığı (1 = Var, 0 = Yok)')
plt.ylabel('Adet')
plt.show()

plt.figure(figsize=(12, 8))
sns.heatmap(data.corr(), annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Korelasyon Isı Haritası')
plt.show()

missing_values = data.isnull().sum()
print("\nEksik Değerler:")
print(missing_values)

scaler = StandardScaler()
numerical_features = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
data[numerical_features] = scaler.fit_transform(data[numerical_features])

X = data.drop('target', axis=1)
y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("\nKarışıklık Matrisi:")
print(confusion_matrix(y_test, predictions))

print("\nSınıflandırma Raporu:")
print(classification_report(y_test, predictions))

print("\nDoğruluk Skoru:")
accuracy = accuracy_score(y_test, predictions)
print(accuracy)

print("\n--- Sonuçların Yorumlanması ---")
print(f"Model, {accuracy:.2%} doğruluk oranına ulaşmıştır, bu da modelin tahminlerinin yaklaşık {accuracy:.2%} oranında doğru olduğunu göstermektedir.")
print("\nKarışıklık Matrisi Açıklaması:")
cm = confusion_matrix(y_test, predictions)
true_negatives, false_positives, false_negatives, true_positives = cm.ravel()
print(f"Doğru Negatifler (Hastalık yokken doğru tahmin edilenler): {true_negatives}")
print(f"Yanlış Pozitifler (Hastalık yokken yanlışlıkla 'Hastalık var' denilenler): {false_positives}")
print(f"Yanlış Negatifler (Hastalık varken kaçırılanlar): {false_negatives}")
print(f"Doğru Pozitifler (Hastalık varken doğru tahmin edilenler): {true_positives}")

print("\nAnahtar Metrikler:")
report = classification_report(y_test, predictions, output_dict=True)
precision = report['1']['precision']
recall = report['1']['recall']
f1_score = report['1']['f1-score']
print(f"Kalp hastalığını tespit etme hassasiyeti (Precision): {precision:.2%}. Bu, modelin 'Hastalık var' dediğinde ne kadar doğru olduğunu gösterir.")
print(f"Kalp hastalığını tespit etme duyarlılığı (Recall): {recall:.2%}. Bu, modelin gerçek 'Hastalık' vakalarının ne kadarını doğru tespit ettiğini gösterir.")
print(f"F1 Skoru: {f1_score:.2%}. Bu metrik, hassasiyet ve duyarlılık arasındaki dengeyi ifade eder.")

print("\nBu sonuçlar, modelin kalp hastalığını tespit etmede etkili olduğunu göstermektedir ancak yanlış pozitif ve yanlış negatif sonuçları azaltmak için iyileştirmeler yapılabilir.")

plt.figure(figsize=(10, 6))
feature_importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
feature_importances.plot(kind='bar', color='skyblue')
plt.title('Özellik Önem Düzeyleri')
plt.ylabel('Önem')
plt.xlabel('Özellikler')
plt.show()

output_summary = {
    "accuracy": accuracy,
    "classification_report": classification_report(y_test, predictions, output_dict=True)
}

import json
with open('C:\\Users\\erhan\\Desktop\\heart_disease_results.json', 'w') as f:
    json.dump(output_summary, f)

print("\nAnaliz tamamlandı. Sonuçlar kaydedildi.")
