edad = int(input("Digite su edad: "))
etapa = None
if 0 <= edad < 10:
    etapa = "La infancia es increible la vida es bella"
elif 10 <= edad < 20:
    etapa = "Empiezan las responsabilidades"
elif 20 <= edad < 30:
    etapa = "Trabajo y amor"
elif 30 <= edad < 40:
    etapa = "Hijos"
elif 50 <= edad < 60:
    etapa = "Empezas a ver los frutos de tu trabajo"
elif 70 <= edad < 100:
    etapa = "Disfrutas de viajes y tus hijos"
    
print(f" Tu edad es de {edad} y estas atravesando la epoca de tu vida donde {etapa} ")
