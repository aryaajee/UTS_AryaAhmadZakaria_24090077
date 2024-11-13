
def hitung_bmi(bb, tb):
    bmi = bb / (tb ** 2)
    return bmi
def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Kurus (Underweight)"
    elif 18.5 <= bmi < 24.9:
        return "Normal (Healthy weight)"
    elif 25 <= bmi < 29.9:
        return "Gemuk (Overweight)"
    else:
        return "Obesitas (Obese)"
bb = float(input("Masukkan berat badan Anda (kg): "))
tb = float(input("Masukkan tinggi badan Anda (m): "))
bmi = hitung_bmi(bb, tb)
kategori = kategori_bmi(bmi)
print(f"BMI Anda adalah: {bmi:.2f}")
print(f"Kategori BMI Anda adalah: {kategori}")
