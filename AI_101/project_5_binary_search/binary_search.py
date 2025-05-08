def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

def main():
    print("Welcome to Binary Search!")
    arr = input("Enter a sorted list of numbers (comma separated): ")
    arr = list(map(int, arr.split(',')))
    arr.sort()  # Ensure the list is sorted

    target = int(input("Enter the number to search for: "))

    result_iter = binary_search_iterative(arr, target)
    result_rec = binary_search_recursive(arr, target, 0, len(arr) - 1)

    print("\n--- Results ---")
    if result_iter != -1:
        print(f"Iterative: Found {target} at index {result_iter}")
    else:
        print("Iterative: Target not found.")

    if result_rec != -1:
        print(f"Recursive: Found {target} at index {result_rec}")
    else:
        print("Recursive: Target not found.")

if __name__ == "__main__":
    main()
