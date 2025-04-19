class Character:
    def __init__(self, *, level: int) -> None:
        self.level = level
        self.health_points = self.base_health_points * level
        self.attack_power = self.base_attack_power * level

    def attack(self, *, target: "Character") -> None:
        target.get_damage(damage=self.attack_power)
        # print(f"{self.character_name} attacks {target.character_name} with {self.attack_power} power")
        # target.health_points -= self.attack_power
        # print(f"After attack {target.character_name} hp has {target.health_points}")

    def get_damage(self, *, damage: int) -> None:
        damage = damage * (100 - self.defence) / 100
        damage = round(damage)
        self.health_points -= damage

    def is_alive(self) -> bool:
        return self.health_points > 0
    
    @property
    def defence(self) -> int:
        defence = self.base_defence * self.level
        return defence
    
    @property
    def max_health_points(self) -> int:
        return self.level * self.base_health_points

    def health_points_percentage(self):
        return (self.health_points / self.max_health_points) * 100

    def __str__(self):
        return(f"{self.character_name} (level: {self.level}), hp: {self.health_points}")
    

class Warrior(Character):
    base_health_points = 100
    base_attack_power = 10
    character_name = "Warrior"
    base_defence = 15

    @property
    def defence(self) -> int:
        defence = super().defence
        if self.health_points < 50:
            defence *= 3
        return defence


class Elf(Character):
    base_health_points = 50
    base_attack_power = 15
    character_name = "Elf"
    base_defence = 10

    def attack(self, *, target: "Character") -> None:
        attack_power = self.attack_power
        if target.health_points_percentage() < 30:
            attack_power *= 3
        target.get_damage(damage=attack_power)


def fight(*, char_1: Character, char_2: Character) -> None:
    while char_1.is_alive() and char_2.is_alive():
        char_1.attack(target=char_2)
        if char_2.is_alive():
            char_2.attack(target=char_1)

    print(f"Character 1 : {char_1}, Char 1 is alive : {char_1.is_alive()}")
    print(f"Character 2 : {char_2}, Char 2 is alive : {char_2.is_alive()}")


# warrior = Warrior(level=1)
# warrior.health_points = 29
# print(warrior.health_points_percentage())

warrior = Warrior(level=1)
elf = Elf(level=1)
# elf.attack(target=warrior)

# print(warrior.defence)

fight(char_1=warrior, char_2=elf)



# class Warrior:
#     def __init__(self, *, level: int) -> None:
#         self.level = level
#         self.health_points = 100 * level
#         self.attack_power = 10 * level

#     def attack(self):
#         print(f"Warrior attacks with {self.attack_power} power")

#     def __str__(self):
#         return(f"Warrior (level: {self.level}), hp: {self.health_points}")



# class Elf:
#     def __init__(self, *, level: int) -> None:
#         self.level = level
#         self.health_points = 50 * level
#         self.attack_power = 15 * level

#     def attack(self):
#         print(f"Eld attacks with {self.attack_power} power")

#     def __str__(self):
#         return(f"Elf (level: {self.level}), hp: {self.health_points}")
