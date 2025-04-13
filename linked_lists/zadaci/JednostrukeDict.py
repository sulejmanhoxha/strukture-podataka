class PjesmeNode():
    def __init__(self, ime, zanr, godina, rejting):
        self.pjesma = {'ime':ime, 'zanr':zanr, 'godina':godina, 'rejting':rejting}
        
class LinkedListPjesme:
    def __init__(self, head=None):
        self.head = head
        
    def print(self):
        current = self.head
        while current:
            print(current.pjesma)
            current = current.next
        
    def append(self,new_element):
        current = self.head
        if not current:
            self.head = new_element
            new_element.next = None
        else:
            while current.next:
                
                current = current.next
            current.next = new_element
            new_element.next = None
            
    def prosjek_godina(self,godina):
        current = self.head
        count = 0
        sum_rate = 0
        while current:
            if current.pjesma['godina'] == godina:
                count = count + 1
                sum_rate =  sum_rate + current.pjesma['rejting']

            current = current.next
        if count!= 0: return sum_rate/count
        else: return None
            
    def pjesme_manje(self,max_godina):
        current = self.head
        while current:
            if current.pjesma['godina']< max_godina:
                print(current.pjesma)
            current = current.next
            
    def prosjek(self):
        current = self.head
        count = 0
        sum_rate = 0
        while current:
          count = count + 1
          sum_rate =  sum_rate + current.pjesma['rejting']

          current = current.next
        if count!= 0: return sum_rate/count
        else: return None
    def prosjek_veci(self,prosjek):
        current = self.head
        while current:
            if current.pjesma['rejting']> prosjek:
                print(current.pjesma)
            current = current.next


n1 = PjesmeNode('In corpore sano', 'pop', 2022, 9.2)
n2 = PjesmeNode('Slow Mo', 'rege', 2021, 8.4)
n3 = PjesmeNode('Secret', 'national', 2021, 7.1)
n4 = PjesmeNode('Gde je sad', 'jazz', 2002, 9.3)
n5 = PjesmeNode("Cveta", 'national', 1987, 9.2)
n6 = PjesmeNode('Krsto Zrnov', 'crnogorska', 1918, 8.5)

pjesme_list = LinkedListPjesme()
pjesme_list.append(n1)
pjesme_list.append(n2)
pjesme_list.append(n3)
pjesme_list.append(n4)
pjesme_list.append(n5)
pjesme_list.append(n6)
pjesme_list.print()
print(pjesme_list.prosjek_godina(2021))
print(pjesme_list.pjesme_manje(2005))
print(pjesme_list.prosjek())
print(pjesme_list.prosjek_veci(pjesme_list.prosjek()))