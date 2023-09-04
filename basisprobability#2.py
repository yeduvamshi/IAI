def main():
    favorableOutcomes = 0  # Count of favorable outcomes

    # Loop through all possible outcomes of two dice
    for dice1 in range(1, 7):
        for dice2 in range(1, 7):
            # Check if the values are different and their sum is 6
            if dice1 != dice2 and dice1 + dice2 == 6:
                favorableOutcomes += 1

    totalPossibleOutcomes = 6 * 6  # Total possible outcomes for two dice

    # Calculate the probability as a fraction
    gcd = 1  # Greatest common divisor
    for i in range(1, favorableOutcomes + 1):
        if favorableOutcomes % i == 0 and totalPossibleOutcomes % i == 0:
            gcd = i

    numerator = favorableOutcomes // gcd
    denominator = totalPossibleOutcomes // gcd

    # Output the probability as an irreducible fraction
    print(f"{numerator}/{denominator}")

if __name__ == "__main__":
    main()
