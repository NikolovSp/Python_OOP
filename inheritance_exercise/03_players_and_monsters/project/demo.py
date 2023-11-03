from project.elf import Elf
from project.hero import Hero
from project.blade_knight import BladeKnight
from project.soul_master import SoulMaster

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)

master_knight = BladeKnight("Master", 12)
print(str(master_knight))
print(master_knight.level)
print(master_knight.username)

soul = SoulMaster("Soul", 1)
print(str(soul))
print(soul.level)
print(soul.username)
