import time
import random


class Node:
    def __init__(self, data):
        # vorheriger Pointer
        self.prev = None
        # Daten vom Eintrag
        self.data = data
        # pointer zum Nachfolgenden Eintrag
        self.next = None


def swapData(first, second):
    value = first.data
    first.data = second.data
    second.data = value


class LinkedList:

    def __init__(self):
        # initializing the head with None
        self.head = None
        self.tail = None

    def insert(self, new_node):
        # Überprüfen ob Kopf leer ist
        if self.head:
            # letzt node getten
            last_node = self.head
            while last_node.next != None:
                last_node = last_node.next
            # letzte node als previous Zeiger hinzufühen
            new_node.prev = last_node
            # neue node als next Zeiger hinzufügen
            last_node.next = new_node
        else:
            self.head = new_node

    def display(self):
        if self.head:
            print(self.head.data)
            tempvar = self.head
            while tempvar.next != None:
                tempvar = tempvar.next
                print(tempvar.data)

    def insert_after(self, value, after):
        found = False
        node = self.head
        while node:
            if after == node.data:
                found = True
                temp_prev = node
                temp_next = node.next
                node.next = value
                node = node.next
                node.prev = temp_prev
                node.next = temp_next
                node = node.next
                node.prev = value
                break
            node = node.next
        if not found:
            print(str(after) + " ist nicht in der Liste")

    def insert_before(self, value, before):
        found = False
        node = self.head
        while node:
            if before == node.data:
                found = True
                temp_next = node
                temp_prev = node.prev
                node.prev = value
                node = node.prev
                node.next = temp_next
                node.prev = temp_prev
                node = node.prev
                node.next = value
                break
            node = node.next
        if not found:
            print(str(before) + " ist nicht in der Liste")

    def delete_after(self, after):
        found = False
        node = self.head
        while node:
            if after == node.data:
                found = True
                if node.next is None:
                    print(str(after) + " ist schon das letzte Element")
                    break
                if node.next.next is not None:
                    node.next = node.next.next
                    node.next.next.prev = node
                    break
                node.next = None
            node = node.next
        if not found:
            print(str(after) + " ist nicht in der Liste")

    def delete_before(self, before):
        found = False
        node = self.head
        while node:
            if before == node.data:
                found = True
                if node.prev is None:
                    print(str(before) + " ist schon das erste Element")
                    break
                if node.prev.prev is not None:
                    node.prev = node.prev.prev
                    node.prev.next = node
                    break
                node.prev = None
            node = node.next
        if not found:
            print(str(before) + " ist nicht in der Liste")

    def length(self):
        temp_node = self.head
        k = 0
        while temp_node:
            k += 1
            temp_node = temp_node.next
        return k

    def sortASC(self):
        start = time.time()
        front = self.head
        back = None
        while front is not None:
            back = front.next
            while back is not None and back.prev is not None and back.data < back.prev.data:
                swapData(back, back.prev)
                back = back.prev
            front = front.next

        end = time.time()
        print("Zeit zum Sortieren der Linkedlist aufsteigend:")
        print('{:5.3f}s'.format(end-start))
        return end-start

    def sortDESC(self):
        start = time.time()
        front = self.head
        back = None
        while front is not None:
            back = front.next
            while back is not None and back.prev is not None and back.data > back.prev.data:
                swapData(back, back.prev)
                back = back.prev
            front = front.next
        end = time.time()
        print("Zeit zum Sortieren der Linkedlist absteigend:")
        print('{:5.3f}s'.format(end-start))
        return end-start

    def clear_list(self):
        curr = self.head
        while curr:
            temp = curr.next
            del curr.data
            curr = temp
        print("LinkedList deleted")


class Arraylist:
    def __init__(self):
        self.list = []

    def insert(self, val):
        self.list.append(val)

    def delete_after(self, index):
        if index >= 0 and index < len(self.list) and len(self.list) > index+1:
            self.list.pop(index+1)

    def delete_before(self, index):
        if 0 < index < len(self.list) and index - 1 > -1:
            self.list.pop(index - 1)

    def delete_index(self, index):
        self.list.pop(index)

    def insert_after(self, index, val):
        if 0 <= index < len(self.list):
            self.list.insert(index + 1, val)

    def insert_before(self, index, val):
        if 0 <= index < len(self.list) and index - 1 >= 0:
            self.list.insert(index - 1, val)

    def insert_index_after(self, index, val):
        self.list.insert(index, val)

    def ausgabe_list(self):
        for index in self.list:
            print(index)

    def laenge_list(self):
        return len(self.list)

    def find(self, val):
        for index in self.list:
            if index == val:
                print(index, "Value wurde hier gefunden")
            else:
                print("Wert existiert nicht")

    def sortASC(self):
        start = time.time()
        for i in range(1, len(self.list)):
            key = self.list[i]
            j = i-1
            while j >= 0 and key < self.list[j]:
                self.list[j+1] = self.list[j]
                j -= 1
            self.list[j+1] = key
            end = time.time()
        print("Zeit zum Sortieren der List aufsteigend:")
        print('{:5.3f}s'.format(end-start))
        return end-start

    def sortDESC(self):
        start = time.time()
        for i in range(1, len(self.list)):
            key = self.list[i]
            j = i-1
            while j >= 0 and key > self.list[j]:
                self.list[j+1] = self.list[j]
                j -= 1
            self.list[j+1] = key
            end = time.time()
        print("Zeit zum Sortieren der List absteigend:")
        print('{:5.3f}s'.format(end-start))
        return end-start


def werte_erstellen(zahl):
    x = []
    for i in range(zahl):
        x.append(random.randint(0, 700000))

    return x


def befuellen_linked(x, linkedl):
    start = time.time()
    for i in range(len(x)):
        linkedl.insert(Node(x[i]))
    end = time.time()
    print("Zeit zum Befüllen der Linkedlist:")
    print('{:5.3f}s'.format(end-start))
    return end-start


def befuellen_array(x, arrayl):
    start = time.time()
    for i in range(len(x)):
        arrayl.insert(x[i])
    end = time.time()
    print("Zeit zum Befüllen der Arraylistt:")
    print('{:5.3f}s'.format(end-start))
    return end-start


def ausgabe():
    print("Hier ist die Verlinkung zu einer anderren Datei")


if __name__ == '__main__':
    print("Programm Startet")
    ll = LinkedList()
    ar = Arraylist()
    x = werte_erstellen(10000)

    befuellen_linked(x, ll)
    befuellen_array(x, ar)

    print("LinkedList")
    print("----------------------------------------------------------------")
    ll.sortASC()
    print("----------------------------------------------------------------")
    ll.sortDESC()
    print("----------------------------------------------------------------")
    print("List")
    print("----------------------------------------------------------------")
    ar.sortASC()
    print("----------------------------------------------------------------")
    ar.sortDESC()
    print("----------------------------------------------------------------")
