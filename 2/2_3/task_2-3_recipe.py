medium_name = input("Введите название питательной среды: ")
agar_conceptration = input("Введите концентрацию агара (%): ")
sterilization_temp = input("Введите температуру стерилизации (°С): ")
with open("recipe.txt", "w", encoding = "utf-8") as report:
    report.write(f"Введите название питательной среды : {medium_name}\n")
    report.write(f"Введите концентрацию агара (%): {agar_conceptration}\n")
    report.write(f"Введите температуру стерилизации (°С): {sterilization_temp}\n")
    print("Файл 'recipe.txt' успешно сформирован!")