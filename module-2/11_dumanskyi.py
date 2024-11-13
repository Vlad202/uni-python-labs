from colorama import Fore, Style


array = [2, 1, -7, -8, 1, 0, -2, 1, -2, -6, -7, -9, 0, 6, 1, 8, 4, 4, -1, 1, 12]

sorted_indices = sorted(range(len(array)), key=lambda i: array[i])
first_min_index = sorted_indices[0]
second_min_index = sorted_indices[1]

print(Fore.WHITE + f"Масив {Fore.BLUE}22 {Fore.WHITE}елементів:\n" + Style.RESET_ALL, end="")
for index, value in enumerate(array):
    if index == first_min_index:
        print(Fore.WHITE + f"{value}" + "*" + Style.RESET_ALL, end=" ")
    elif index == second_min_index:
        print(Fore.WHITE + f"{value}" + "*" + Style.RESET_ALL, end=" ")
    else:
        print(Fore.RED + f"{value}" + Style.RESET_ALL, end=" ")
print("\n")

elements_before_first_min = first_min_index
elements_between_mins = abs(second_min_index - first_min_index) - 1
elements_after_second_min = len(array) - max(first_min_index, second_min_index) - 1

print(Fore.WHITE + "Кількість елементів до першого мінімального: " + Fore.BLUE + f"{elements_before_first_min}" + Style.RESET_ALL)
print(Fore.WHITE + "Кількість елементів між двома мінімальними: " + Fore.BLUE + f"{elements_between_mins}" + Style.RESET_ALL)
print(Fore.WHITE + "Кількість елементів після другого мінімального: " + Fore.BLUE + f"{elements_after_second_min}" + Style.RESET_ALL)
print("\n" + Fore.BLUE + f"{elements_before_first_min}" + Fore.WHITE + " < " + Fore.BLUE + f"{elements_between_mins}" + Fore.WHITE + " = " + Fore.BLUE + f"{elements_after_second_min}" + Style.RESET_ALL)
