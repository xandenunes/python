segundos=input("Por favor, entre com o número de segundos que deseja converter: ")
segundosInt=int(segundos)
dia=segundosInt//86400
restoDia=segundosInt%86400
horas=restoDia//3600
restoHora=restoDia%3600
minutos=restoHora//60
restoMinutos=restoHora%60
print(dia,"dias,",horas,"horas,",minutos,"minutos e",restoMinutos,"segundos.")