populations_wealth = [int(el) for el in input().split(", ")]
minimum_wealth = int(input())
is_distribution_possible = True
for index in range(len(populations_wealth)):
    if populations_wealth[index] < minimum_wealth:
        wealthiest_person = max(populations_wealth)
        index_of_wealthiest = populations_wealth.index(wealthiest_person)
        diff = minimum_wealth - populations_wealth[index]
        if wealthiest_person - diff >= minimum_wealth:
            populations_wealth[index] += diff
            populations_wealth[index_of_wealthiest] -= diff
        else:
            is_distribution_possible = False
            break

if is_distribution_possible:
    print(populations_wealth)
else:
    print("No equal distribution possible")



