class Node():
    def __init__(self, process_id, size):
        self.process_id = process_id
        self.size = size
        self.next = None

class LinkedList():
    def __init__(self, total_size):
        self.head = None
        self.total_size = total_size

    def OS_Allowcate(self, size):
        OS = Node("OS", size)
        remain = Node("FREE", self.total_size - size)
        self.head = OS
        OS.next = remain

    def insert(self, process_id, size):
        current = self.head
        process_done = False

        while current.next != None and current.process_id != "FREE" or current.size < size:
            current = current.next

        if current.process_id == "FREE":
            if current.size == size:
                current.process_id = process_id
                process_done = True

            elif current.size > size:
                current.process_id = process_id
                remaining_space = current.size - size
                current.size = size
                new_node = Node("FREE", remaining_space)
                new_node.next = current.next
                current.next = new_node
                process_done = True

        if process_done == True:
            print("Memory for Process", process_id, "has been successfully allocated")
        else:
            print("Sorry! Not enough memory for the process", process_id)

    def current_total(self):
        if self.head != None:
            current = self.head
            total = 0
            while current.next != None:
                if current.process_id != "FREE":
                    total = total + current.size
                current = current.next
                if current.next == None and current.process_id != "FREE":
                    total = total + current.size
            return total
        else:
            return 0

    def remove(self, process_id):
        current = self.head
        prev = None
        super_prev = None
        removed = False

        while current.process_id != process_id:
            if current.next != None:
                super_prev = prev
                prev = current
                current = current.next
            else:
                break

        if current.process_id == process_id:
            if prev.process_id == "FREE" and current.next.process_id == "FREE":
                current.size = current.size + prev.size + current.next.size
                super_prev.next = current
                current.next = current.next.next

            elif prev.process_id == "FREE":
                current.size = current.size + prev.size
                super_prev.next = current

            elif current.next.process_id == "FREE":
                current.size = current.size + current.next.size
                current.next = current.next.next

            current.process_id = "FREE"
            removed = True

        if removed == True:
            print("Process", process_id, "has been successfully removed")
        else:
            print("Sorry! The process", process_id, "is not found")

    def print_Linked_List(self):
        if self.head != None:
            current = self.head
            while current != None:
                print("----------------")
                print("|", current.size, "k", "|", current.process_id)
                current = current.next
            print("----------------")
        else:
            print("List is empty")

def cmd_check(cmd, memory):
    if cmd == "check":
        memory.print_Linked_List()
    elif cmd == "a":
        process_id = input("Enter the process ID : ").upper()
        size = int(input("Enter the size Of the process : "))
        memory.insert(process_id, size)
    elif cmd == "t":
        process_id = input("Enter the process ID : ").upper()
        memory.remove(process_id)
    else:
        print("\n\nYour cmd is incorrect. Try again.\n")
        print("A : To Allocate")
        print("T : To Terminate")
        print("CHECK : To see the current snapshot of the memory")
        print("DONE : To end the program")

memory = LinkedList(int(input("Enter the 'TOTAL SIZE' Of The memory : ")))
memory.OS_Allowcate(int(input("Enter the default memory size for the 'OS' : ")))

print("A : To Allocate")
print("T : To Terminate")
print("CHECK : To see the current snapshot of the memory")
print("DONE : To end the program")

while True:
    cmd = input("\n\nEnter the cmd : ").lower()
    if cmd == "done":
        break
    else:
        cmd_check(cmd, memory)