
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_paths = ["results/RY5.txt", "results/RA5.txt", "results/FN5.txt", "results/ESU25.txt"]

# Leemos los archivos .txt, eliminamos los corchetes y convertimos los valores a floats
def clean_data(file_path):
    data = pd.read_csv(file_path, header=None).values.flatten()  # Leemwdd
    return pd.to_numeric(data, errors='coerce')  # Convertir a valores floars

# Limpiamos y leemos los datos de cada archivo
RY5 = clean_data(file_paths[0])
RA5 = clean_data(file_paths[1])
FN5 = clean_data(file_paths[2])
ESU25 = clean_data(file_paths[3])
# Plotting the results as histograms with smoothed line curves (Kernel Density Estimation)
plt.figure(figsize=(10,6))

# Plot el Kernel Density Estimation (funcion de seaborn) por cada ansatz
sns.kdeplot(RY5, label='RY5', linewidth=2.5, alpha=0.5,  color='blue')
sns.kdeplot(RA5, label='RA5', linewidth=2.5, alpha=0.5,  color='green')
sns.kdeplot(FN5, label='FN5', linewidth=2.5, alpha=0.5, color='red')
sns.kdeplot(ESU25, label='ESU25', linewidth=2.5, alpha=0.5, color='purple')


plt.title('Comparison of <E> values from different algorithms (Smoothed KDE)')
plt.xlabel('<E> Values')
plt.ylabel('Density')
plt.legend()
plt.grid(True)


plt.show()
