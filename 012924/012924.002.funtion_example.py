''''
def suma_dos(numero_uno, numero_dos):
    resultado = int(numero_uno) + int(numero_dos)
    return resultado

print(suma_dos(5, 1))
'''

def team(team_name):
    return f"El nombre del equipo es {team_name}"

#print(team('Oracle Red Bull Racing'))

def drivers(team, driver_one, driver_two):
    return f"{team}. Los pilotos son {driver_one} y {driver_two}"
    
#print(drivers(team("Oracle Red Bull Racing"), "Max Verstappen", "Sergio Perez"))
#team = team("Oracle Red Bull Racing")
#print(drivers(team, "Max Verstappen", "Sergio Perez"))

user_team = input("team name: ")
#print(type(user_team))
input_team = team(user_team)
#print(input_team)
team_pilot_one = input("Piloto uno: ")
team_pilot_two = input("Piloto dos: ")

print(drivers(input_team, team_pilot_one, team_pilot_two))