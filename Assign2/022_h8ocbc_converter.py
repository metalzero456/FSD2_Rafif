# Definisi fungsi konversi ke kelvin dengan parameter nilai temperatur dan dari unit mana.
def convertKelvin(temp, fromWhat=''):
    # Kondisi apabila konversi unit dari celsius
    if(fromWhat == 'c'):
        k = temp + 273.15
        return roundDecimal(k)
    # Kondisi apabila konversi unit dari fahrenheit
    elif(fromWhat == 'f'):
        k = ((temp - 32) * 5)/9 + 273.15
        return roundDecimal(k)
    # Kondisi default tidak melakukan konversi
    else:
        return temp

# Definisi fungsi konversi ke fahrenheit dengan parameter nilai temperatur dan dari unit mana.
def convertFahrenheit(temp, fromWhat=''):
    # Kondisi apabila konversi unit dari celsius
    if(fromWhat == 'c'):
        f = (temp * 9) / 5 + 32
        return roundDecimal(f)
    # Kondisi apabila konversi unit dari kelvin
    elif(fromWhat == 'k'):
        f = (temp - 273.15) * (9/5) + 32
        return roundDecimal(f)
    # Kondisi default tidak melakukan konversi
    else:
        return temp

# Definisi fungsi konversi ke celsius dengan parameter nilai temperatur dan dari unit mana.
def convertCelsius(temp, fromWhat=''):
    # Kondisi apabila konversi unit dari kelvin
    if(fromWhat == 'k'):
        c = temp - 273.15
        return roundDecimal(c)
    # Kondisi apabila konversi unit dari fahrenheit
    elif(fromWhat == 'f'):
        c = (temp - 32) * (5/9)
        return roundDecimal(c)
    # Kondisi default tidak melakukan konversi
    else:
        return temp

# Definisi fungsi untuk membulatkan floating point number ke 2 angka dibelakang koma.
def roundDecimal(num):
    return "{:.2f}".format(num)


inp = ''

print("============= Convert your TEMPS =============")
print("by Rafif Taqiuddin\nFSDO001ONL022")
print("----------------------------------------------")
# Looping while yang akan berjalan selama kondisi input user tidak sama dengan 0.
while(inp != '0'):
    print("Which unit you want to convert to?\n1.Celsius\n2.Kelvin\n3.Fahrenheit\n0.Exit Program\nSelect:")
    # Menyimpan pilihan input user ke variabel inp
    inp = input()
    # Memeriksa apakah nilai input sama dengan 0, apabila iya looping berakhir sehingga program selesai
    if (inp == '0'):
        print("Exiting Program...")
        break
    print("Please enter your desired Temperature with its unit:\n(K : Kelvin, C: Celsius, F: Fahrenheit, ex : 90 C, 45 F, 75 K)")
    # Menyimpan input nilai temperatur dari user lalu di split menjadi list temp
    temp = input().split()
    # Mencoba menyimpan nilai list temp index ke-1 yang berisi kode unit temperatur ke dalam variabel fromWhat
    try:
        fromWhat = temp[1]
    # Apabila muncul exception maka nilai variabel fromWhat diisi string kosong
    except:
        fromWhat = ''
    print("Result:")
    # Apabila nilai inp == 1 maka jalankan fungsi convertCelsius
    if(inp == '1'):
        print(convertCelsius(float(temp[0]), fromWhat.lower()), "C")
    # Apabila nilai inp == 2 maka jalankan fungsi convertKelvin
    elif(inp == '2'):
        print(convertKelvin(float(temp[0]), fromWhat.lower()), "K")
    # Apabila nilai inp == 3 maka jalankan fungsi convertFahrenheit
    elif(inp == '3'):
        print(convertFahrenheit(float(temp[0]), fromWhat.lower()), "F")
    # Default condition apabila nilai inp tidak masuk ke tiga kondisi diatas
    else:
        print("Input Mismatch!")
    print("----------------------------------------------")