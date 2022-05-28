
import colorama
class BuildingError(Exception):
    def __str__(self):
        return f"with so such watecial the house can not built"
def check_material(amout_of_material, lint_valus):
    if amout_of_material > lint_valus:
        return  "enough materiel"
    else:
        raise BuildingError(amout_of_material)
check_material(int(input()), 300)
a = input()
try:
    print(10/0)
    print("sucssesful")
except ZeroDivisionError:
    print(colorama.Fore.RED + "It is not possible to divide by 0")
except  TypeError:
    print(colorama.Fore.RED + "It is not possible to divide by 0")
except NameError:
    print(colorama.Fore.YELLOW + "You are accessing an object that does not exist")
else:
    print(colorama.Fore.GREEN + "Mothing went wrong")
finally:
    print(colorama.Fore.GREEN + "The 'try except' is finished"
input()