import math

import numpy as np

import matplotlib.pyplot as plt


def calculate_half_life(k):
    """
    Calculate half-life from elimination rate constant.
    """
    if k <= 0:
        raise ValueError("Elimination rate constant must be greater than zero")

    return math.log(2) / k


def calculate_elimination_rate_constant(half_life):
    """
    Calculate the elimination rate constant from half-life.
    """
    if half_life <= 0:
        raise ValueError("Half-life must be greater than zero")

    return math.log(2) / half_life


def calculate_concentration(initial_concentration, k, time):
    """
    Calculate drug concentration at a specific time
    using first-order elimination.
    """
    if initial_concentration <= 0:
        raise ValueError("Initial concentration must be greater than zero.")

    if k <= 0:
        raise ValueError("Elimination rate constant must be greater than zero.")

    if time < 0:
        raise ValueError("Time cannot be negative. ")

    return initial_concentration * math.exp(-k * time)


def calculate_concentration_over_time(initial_concentration, k, times):
    """
    Calculate drug concentration at multiple time points.
    """
    concentrations = []

    for time in times:
        concentration = calculate_concentration(initial_concentration, k, time)
        concentrations.append(concentration)

    return concentrations
    
def main():
    while True:
        print("-" * 40)
        print("Pharmacokinetics Calculator")
        print("-" * 40)
        print("1 - Calculate Half-life")
        print("2 - Calculate Elimination Rate Constant")
        print("3 - Calculate Drug Concentration")
        print("4 - Plot Concentration-Time Profile")
        print("5 - Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            try:
                k = float(input("Enter the Elimination Rate Constant (k): "))
                half_life = calculate_half_life(k)
                print(f"Half-life: {half_life:.2f} hours")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            try:
                half_life = float(input("Enter half-life (hours): "))
                k = calculate_elimination_rate_constant(half_life)
                print(f"Elimination rate constant (k): {k:.4f} hour^-1 ")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "3":
            try:
                initial_concentration = float(input("Enter initial concentration: "))
                k = float(input("Enter elimination rate constant (k): "))
                time = float(input("Enter time (hours): "))
                concentration = calculate_concentration(initial_concentration, k, time)
                print(f"Drug concentration at {time} hours: "
                    f"{concentration:.2f}")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "4":
            try:
                initial_concentration = float(input("Enter initial concentration: "))
                k = float(input("Enter elimination rate constant (k): "))
                total_time = float(input("Enter total time (hours): "))
                if total_time < 0:
                    raise ValueError("Total time cannot be negative.")
                times = np.arange(0, total_time + 1, 1)
                concentrations = calculate_concentration_over_time(initial_concentration, k, times)
                plt.plot(times, concentrations)
                plt.xlabel("Time (hours)")
                plt.ylabel("Drug concentration")
                plt.title("Concentration-Time Profile")
                plt.grid(True)
                plt.show()
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "5":
            print("Exit Pharmacokinetics Calculator ...")
            break
        else:
            print("Invalid option. Please choose between 1 and 5.")
if __name__ == "__main__":
    main()


        




