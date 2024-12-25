import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Data performa attachment (contoh, data perlu disesuaikan berdasarkan kebutuhan)
attachments = {
    "Muzzle": ["Flash Hider", "Compensator", "Suppressor"],
    "Grip": ["Vertical Grip", "Angled Grip"],
    "Sight": ["Holographic", "Reflex", "ACOG"]
}

# Simulasi performa berdasarkan skor (contoh, bisa diganti dengan data nyata)
def calculate_performance(muzzle, grip, sight):
    performance_data = {
        ("Flash Hider", "Vertical Grip", "Holographic"): 85,
        ("Flash Hider", "Vertical Grip", "Reflex"): 80,
        ("Flash Hider", "Vertical Grip", "ACOG"): 88,
        ("Flash Hider", "Angled Grip", "Holographic"): 78,
        # Tambahkan kombinasi lainnya...
    }
    return performance_data.get((muzzle, grip, sight), 70)  # Default performance jika kombinasi tidak ada

# Grafik untuk menyimpan data
combinations = []
performances = []

# Fungsi untuk memperbarui grafik
def update_graph():
    plt.figure(figsize=(8, 6))
    plt.plot(combinations, performances, marker='o', linestyle='-', color='skyblue')
    plt.title('Performance of Weapon Attachments')
    plt.xlabel('Attachment Combination')
    plt.ylabel('Performance Score')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(True)
    plt.show()

# Fungsi untuk mencetak tabel hasil
def print_performance_table():
    table = PrettyTable()
    table.field_names = ["Combination", "Performance Score"]
    for i in range(len(combinations)):
        table.add_row([combinations[i], performances[i]])
    print(table)

# Program utama
while True:
    try:
        print("\nAvailable Attachments:")
        print(f"Muzzles: {attachments['Muzzle']}")
        print(f"Grips: {attachments['Grip']}")
        print(f"Sights: {attachments['Sight']}")
        print(f"KETIK EXIT UNTUK KELUAR")

        muzzle = input("Choose a muzzle: ").strip()
        grip = input("Choose a grip: ").strip()
        sight = input("Choose a sight: ").strip()

        if muzzle == "exit" or grip == "exit" or sight == "exit":
            print("Program selesai. Terima kasih!")
            break

        if muzzle not in attachments['Muzzle'] or grip not in attachments['Grip'] or sight not in attachments['Sight']:
            print("Invalid attachment combination. Please choose from the available options.")
            continue

        combination = f"{muzzle} + {grip} + {sight}"
        performance = calculate_performance(muzzle, grip, sight)

        combinations.append(combination)
        performances.append(performance)

        # Cetak tabel hasil
        print_performance_table()

        # Perbarui grafik
        update_graph()

    except Exception as e:
        print(f"An error occurred: {e}")
