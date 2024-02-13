import matplotlib.pyplot as plt
import time
import math

if __name__ == "__main__":

    susceptible = 7000000000
    infected = 100
    death = 0

    Humans, Zombies, Death = list(), list(), list()
    month = 0

    while susceptible > 0 and infected > 0:

        SI = susceptible * infected
        Alpha = 0.06234375
        Mu = 0.016875
        Epsilon = 0.0084375

        birthRate = math.ceil(susceptible * 0.018/12)
        naturalDeath = math.ceil(susceptible * 0.0077/12)

        curedZombies = math.ceil(infected * math.log(susceptible, 100) * Mu)
        peopleBitten = math.ceil(infected * Alpha * math.log(susceptible, 10))

        killedZombies = math.ceil(math.log(susceptible, 100) * infected * Epsilon)

        susceptible += birthRate + curedZombies - peopleBitten - naturalDeath
        infected += peopleBitten - curedZombies - killedZombies
        death += killedZombies + naturalDeath

        print(f"Birthrate = {birthRate}\tNaturalDeath = {naturalDeath}\tCuredZombies = {curedZombies}\tPeoplebitten = {peopleBitten}\tkilledzomb = {killedZombies}\nSusceptible = {susceptible}\nInfected = {infected}\nDeath = {death}\nMonth = {month}\nYear {int(month/12)} Month {month%12}")
        time.sleep(0.05)
        Humans.append(susceptible)
        Zombies.append(infected)
        Death.append(death)

        month += 1

    
    plt.plot(Humans, label = "Humans")
    plt.plot(Zombies, label = "Zombies")
    plt.plot(Death, label = "Death")
    plt.ylim(0)
    plt.xlim(0)
    plt.ylabel("Population")
    plt.xlabel("Months")
    plt.title("Human vs Zombies")

    plt.legend()
    plt.show()


