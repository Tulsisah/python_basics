# A program that sorts a list of numbers in ascending or 
def sort_list(numbers, order):
    if order == "A":
        sorted_list = sorted(numbers)
    elif order == "D":
        sorted_list = sorted(numbers, reverse=True)
    else:
        print("Invalid order! Please enter 'A' for ascending or 'D' for descending.")
        return
    print("Sorted List:", sorted_list)

list1 = input("Enter the list elements separated by spaces:\n").split()
list1 = [int(n) for n in list1]

order = input("Enter 'A' for ascending or 'D' for descending:\n").strip().upper()

sort_list(list1, order)
