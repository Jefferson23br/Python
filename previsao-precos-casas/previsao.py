import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Carregar dados
df = pd.read_csv("casas.csv")
X = df[["Tamanho", "Quartos"]]
y = df["Preço"]

# Dividir dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Previsões
y_pred = modelo.predict(X_test)

# Visualizar resultado
plt.scatter(X_test["Tamanho"], y_test, color="blue", label="Preço real")
plt.scatter(X_test["Tamanho"], y_pred, color="red", label="Previsão")
plt.xlabel("Tamanho da Casa (m²)")
plt.ylabel("Preço (R$)")
plt.title("Previsão de Preços de Casas")
plt.legend()
plt.grid(True)
plt.show()
