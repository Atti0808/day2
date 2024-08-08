#swap head and tail with ChatGpt

def swap_head_tail(lst):
    if len(lst) <= 1:
        return lst  # No need to swap if the list has 0 or 1 element
    
    mid = len(lst) // 2

    if len(lst) % 2 == 0:
        # If the list has an even number of elements
        head = lst[:mid]
        tail = lst[mid:]
        return tail + head
    else:
        # If the list has an odd number of elements
        head = lst[:mid]
        middle = lst[mid]
        tail = lst[mid+1:]
        return tail + [middle] + head

# Example usage:
my_list = ["chips", "tomatoes", 3, "brocolli", "cherries"]
print("Original list:", my_list)
swapped_list = swap_head_tail(my_list)
print("Swapped list:", swapped_list)
