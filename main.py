import linked_list as LinkedList

def swap_nodes(input_list, val1, val2):
        
    node1 = input_list.head_node
    node2 = input_list.head_node
    node1_prev = None
    node2_prev = None

    if val1 == val2:
        print('Element are the same - no swap needed')
        return   
        
    print(f'Swap {val1} with {val2}')

    while node1 is not None:
        if node1.get_value() == val1:
            break
        node1_prev = node1
        node1 = node1.get_next_node()

    while node2 is not None:
        if node2.get_value() == val2:
            break
        node2_prev = node2
        node2 = node2.get_next_node()
        
    if (node1 is None or node2 is None):
        print('Swap not possible - onde or mor element is not in the list')
        return

    #this if statement check if the node1 is the head_node, if it is then input_list.head_node assign node2
    #if it's not, node1_prev assing nodo2
    if node1_prev is None:
        input_list.head_node = node2
    else:
        node1_prev.set_next_node(node2)

    #this if statement check if the node2 is the head_node, if it is, then input_list.head_node assign node1
        
    if node2_prev is None:
        input_list.head_node = node1
    else:
        node2_prev.set_next_node(node1)

    #setting the new next node of node1 and node 2
    node2.get_next_node()
    temp = node1.get_next_node()

    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)


ll = LinkedList.LinkedList()
for i in range(10):
  ll.insert_beginning(i)

print(ll.stringify_list())
swap_nodes(ll, 9, 5)
print(ll.stringify_list())