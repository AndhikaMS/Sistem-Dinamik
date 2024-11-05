import numpy as np
import matplotlib.pyplot as plt

# Data waktu solve
waktu = [16.49, 15.87, 17.05, 17.53, 13.60]

# Menghapus waktu tercepat dan terlambat
waktu_filtered = sorted(waktu)[1:-1]  # Menghapus waktu tercepat dan terlambat

# Menghitung rata-rata WCA
average_WCA = np.mean(waktu_filtered)

# Menampilkan hasil
print("Waktu yang dihitung (tanpa tercepat dan terlambat):", waktu_filtered)
print("Rata-rata WCA:", average_WCA)

# Plot data waktu solve
percobaan = list(range(1, len(waktu) + 1))
plt.figure(figsize=(10, 6))
plt.plot(percobaan, waktu, marker='o', color='b', label="Waktu Solve")

# Menambahkan anotasi waktu di setiap titik data
for i, waktu_val in enumerate(waktu):
    plt.text(percobaan[i], waktu_val + 0.1, f"{waktu_val:.2f}", ha='center')

# Menambahkan garis rata-rata WCA
plt.axhline(average_WCA, color='r', linestyle='--', label=f"Rata-rata WCA = {average_WCA:.2f}")

# Mengatur tampilan grafik
plt.title("Waktu Penyelesaian Rubik 3x3 dengan Metode WCA")
plt.xlabel("Percobaan ke-")
plt.ylabel("Waktu (detik)")
plt.xticks(percobaan)  # Mengatur sumbu x hanya menampilkan bilangan bulat
plt.legend()
plt.grid()
plt.show()
