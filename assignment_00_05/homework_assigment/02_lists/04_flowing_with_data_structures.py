# three copis

def add_three_copies(my_list, topic):
    for i in range(3):
        my_list.append(topic)


def copies():
    message = input("Enter a message to copy: ")
    my_list = []
    print("List before:", my_list)
    add_three_copies(my_list, message)
    print("List after:", my_list)



if __name__ == "__main__":
    copies()
    
    
    
 