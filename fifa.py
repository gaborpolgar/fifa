from placed import Placed
     
placeds = []

def main():
    createList()
    kiir_03()
    feladat_04()
    feladat_05()
    feladat_06()
    feladat_07()
    feladat_08()
    kiir_08()

def kiir_03():
        table_data = []
        for item in placeds:
            data = [item.country, "|", item.place, "|", item.changed, "|", item.points]
            table_data.append(data)
        for row in table_data:
            print("{: <13} {: >5} {: >5}{: >2}{: >5}{: >2}{: >5}".format(*row))
     
def feladat_04():
    print(f"A világranglistán {len(placeds)} csapat szerepel.")

def feladat_05(): 
    sum = 0
    for team in placeds:
        sum += team.points
    print("A csapatok átlagos pontszáma: {:.2f}".format(sum/len(placeds)))

def feladat_08():
    file = open("statisztika.txt","w")
    file.write("Statisztika azon helyezésváltozásokról, melyek esetében a csapatok száma több mint egy volt: ")
    maxChanged = 0
    minChanged = 0
    for item in placeds:
        if item.changed > maxChanged:
            maxChanged = item.changed
        if item.changed < minChanged:
            minChanged = item.changed
    teamsCount= []
    changeds = []
    for i in range(minChanged, maxChanged):
        teams=set()
        for item in placeds:
            if item.changed == i:
                teams.add(item)
        if len(teams)>1:
            print(f"{i} helyet változtatott: {len(teams)} csapat.")
            teamsCount.append(len(teams))
            changeds.append(i)
    for i in range(len(changeds)):
        file.write(f"{changeds[i]} helyet változtatott: {teamsCount[i]} csapat.")
    file.close()
                     
def kiir_08():
    print("A statisztika.txt állomány a kívánt tartalommal és formával létrejött")

def feladat_07():
    for team in placeds:
        if team.country == "Magyarország":
            return print("A csapatok között van Magyarország.")
    return print("A csapatok között nincs Magyarország.")

def feladat_06():
    theMostChangedTeam = placeds[0]
    for team in placeds:
        if (team.changed > theMostChangedTeam.changed):
            theMostChangedTeam = team
    print(f"A legtöbbet javító csapat: \n Helyezés: {theMostChangedTeam.place} \n Név: {theMostChangedTeam.country}\n Pontszám: {theMostChangedTeam.points}")

def createList():
    file = open("fifa.txt")
    file.readline()
    lines = file.readlines()
    for line in lines:
        data = line.strip().split(';')
        placed = Placed(data[0], data[1], int(data[2]), int(data[3]))
        placeds.append(placed)
    file.close()
    print("A fájl beolvasása megtörtént.")

main()


