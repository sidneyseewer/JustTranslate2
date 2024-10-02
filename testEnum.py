

from enum import Enum

class Languages(Enum):
    de = 'Deutsch'
    fr = 'Français'
    es = 'Espanol'
    ru = 'Russki'

print(f"Value: {Languages.de.name}")