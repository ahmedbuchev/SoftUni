num = int(input())
heroes_dict = {}

for _ in range(num):
    hero_name, hit_points, mana_points = input().split()
    hit_points, mana_points = int(hit_points), int(mana_points)
    # max HP = 100 and max MP = 200

    heroes_dict[hero_name] = {'hp': hit_points, 'mp': mana_points}

command = input()
while not command == "End":
    command_split = command.split(" - ")
    cmd = command_split[0]

    if cmd == "CastSpell":
        hero_name, mp_needed, spell_name = command_split[1:]
        mp_needed = int(mp_needed)

        if heroes_dict[hero_name]['mp'] >= mp_needed:
            heroes_dict[hero_name]['mp'] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name]['mp']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif cmd == "TakeDamage":
        hero_name, damage, attacker = command_split[1:]
        damage = int(damage)

        heroes_dict[hero_name]['hp'] -= damage

        if heroes_dict[hero_name]['hp'] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has "
                  f"{heroes_dict[hero_name]['hp']} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes_dict[hero_name]

    elif cmd == "Recharge":
        hero_name, amount = command_split[1:]
        amount = int(amount)

        if heroes_dict[hero_name]['mp'] + amount > 200:
            amount = 200 - heroes_dict[hero_name]['mp']
            heroes_dict[hero_name]['mp'] = 200
        else:
            heroes_dict[hero_name]['mp'] += amount

        print(f"{hero_name} recharged for {amount} MP!")

    elif cmd == "Heal":
        hero_name, amount = command_split[1:]
        amount = int(amount)

        if heroes_dict[hero_name]['hp'] + amount > 100:
            amount = 100 - heroes_dict[hero_name]['hp']
            heroes_dict[hero_name]['hp'] = 100
        else:
            heroes_dict[hero_name]['hp'] += amount

        print(f"{hero_name} healed for {amount} HP!")

    command = input()

for hero_name, value in heroes_dict.items():
    print(hero_name)
    print(f"  HP: {value['hp']}")
    print(f"  MP: {value['mp']}")
