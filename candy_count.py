name = "Jayden"
chocolate = 10
gummies = 5
lollipops = 7
given_away = 3
sour_worms = 8

total = chocolate + gummies + lollipops + sour_worms - given_away
left = total - given_away

print("Candy report for", name)
print("Total pieces:", total)
print("Pieces left after sharing:", left)