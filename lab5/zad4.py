from datetime import datetime


kolokwium = datetime(2024, 2, 6)
lab = datetime(2024, 1, 14)
obecna = datetime.now()

dni_od_lab = (obecna - lab).days
dni_od_kolokwium = (obecna - kolokwium).days


print("Od ostatnich laboratoriów minęło:", dni_od_lab, "dni")
print("Od kolokwium minęło:", dni_od_kolokwium, "dni")