import matplotlib.pyplot as plt
import time
import math

if __name__ == "__main__":

    susceptible = 7000000000
    infected = 500000
    death = 0

    Humans, Zombies, Death = list(), list(), list()
    month = 0

    while (susceptible != 0 and infected != 0) and (month < 50*12 and (susceptible > 100 or infected > 100)):

        SI = susceptible * infected
        Alpha = 0.06234375                  # Infection rate
        Mu = 0.016875                       # Cure Rate
        Epsilon = 0.0084375                 # Killed Zombies

        birthRate = round(susceptible * 0.018/12)
        naturalDeath = round(susceptible * 0.0077/12)

        curedZombies = round(Mu * SI / (susceptible + infected))
        peopleBitten = round(Alpha * SI / (susceptible + infected))

        killedZombies = round(Epsilon * SI / (susceptible + infected))

        susceptible += birthRate + curedZombies - peopleBitten - naturalDeath
        infected += peopleBitten - curedZombies - killedZombies
        death += killedZombies + naturalDeath

        print(f"Birthrate = {birthRate}\tNaturalDeath = {naturalDeath}\tCuredZombies = {curedZombies}\tPeoplebitten = {peopleBitten}\tkilledzomb = {killedZombies}\nSusceptible = {susceptible}\nInfected = {infected}\nDeath = {death}\nMonth = {month}\nYear {int(month/12)} Month {month%12}")
        #time.sleep(0.05)
        Humans.append(susceptible)
        Zombies.append(infected)
        Death.append(death)

        month += 1

    
    plt.plot(Humans, label = "Humans")
    plt.plot(Zombies, label = "Zombies")
    plt.plot(Death, label = "Death")
    plt.ylim(0)
    plt.xlim(0)
    plt.ylabel("Population (In Billions)")
    plt.xlabel("Months")

    plt.legend()
    plt.show()


