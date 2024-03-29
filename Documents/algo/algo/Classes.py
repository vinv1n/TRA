import os
import os.path
import datetime, time
from operator import attrgetter


class Customer(object):
    def __init__(self, id=0, name='', address='', phone=''):
        self.id = id
        self.name = name.replace('\t', '')
        self.address = address.replace('\t', '')
        self.phone = phone.replace('\t', '')
        self.next = None


class Driver(object):
    def __init__(self, id=0, officeid=0, name='', hireDate='', carModel=''):
        self.id = id
        self.name = name.replace('\t', '')
        self.hireDate = hireDate.replace('\t', '')
        self.carModel = carModel.replace('\t', '')
        self.officeid = officeid
        self.next = None

class apu:

    def __init__(self):
        self.answer = None


class Travel(object):
    def __init__(self, id=0, driverId=0, date='', time='', customerId=0, source='', destination='', amount=0.0):
        self.id = id
        self.driverId = driverId
        self.date = date.replace('\t', '')
        self.time = time.replace('\t', '')  # in hour:min format
        self.customerId = customerId
        self.source = source.replace('\t', '')
        self.destination = destination.replace('\t', '')
        self.amount = amount
        self.next = None


class Agency(object):
    def __init__(self, id=0, name='', regDate='', staffCount=0, managerName=''):
        self.id = id
        self.name = name.replace('\t', '')
        self.regDate = regDate.replace('\t', '')
        self.staffCount = staffCount
        self.managerName = managerName.replace('\t', '')
        self.next = None

class Node(object):

    def __init__(self, id, data):
        self.parent = None
        self.left = None    #noden vasen solmu
        self.right = None   #noden oikea solmu
        self.id = id        #noden key joka tässä id
        self.data = data    #idtä vastaava objecti

    def insert(self, id, data):     #funktio joka etsii nodelle oikean paikan puussa
        if self.id > id:
            if self.left:
                self.left.insert(id, data)
            else:
                self.left = Node(id, data)
        else:
            if self.right:
                self.right.insert(id, data)
            else:
                self.right = Node(id, data)

    def find(self, nimi):           #rekursiivinen haku ilman key:tä
        if self.data.name == nimi:
            apu.answer = self.data
            print('hep')
        else:
            if self.left and self.right is not None:
                self.right.find(nimi), self.left.find(nimi)
            elif self.right is not None:
                self.right.find(nimi)
            elif self.left is not None:
                self.left.find(nimi)

class Tree:

    def __init__(self):     #luo uuden puun ja sille rootin
        self.root = None

    def insert(self, id, data):     #lisää uuden noden puuhun
        if self.root:
            self.root.insert(id, data)
        else:
            self.root = Node(id, data)

    def find(self, nimi):
        if self.root:
            return self.root.find(nimi)
        else:
            return False

# Agencies Linked List.
# Modify or implement accordingly
class Agencies(object):
    def __init__(self):
        self.head = None
        if not os.path.exists('agencies.txt'):
            f = open('agencies.txt', 'w')
            f.close()

    def Load(self):

        f = open('agencies.txt', 'r')
        c = None
        for line in f.readlines():
            lineparts = line.replace('\n', '').split('\t')
            if len(lineparts) > 1:
                if self.head == None:
                    self.head = Agency(id=int(lineparts[0]), name=lineparts[1], regDate=lineparts[2],
                                       staffCount=int(lineparts[3]), managerName=lineparts[4])
                    c = self.head
                else:
                    c.next = Agency(id=int(lineparts[0]), name=lineparts[1], regDate=lineparts[2],
                                    staffCount=int(lineparts[3]), managerName=lineparts[4])
                    c = c.next
        f.close()

    def print(self):
        c = self.head
        print('%5s\t %10s\t %10s\t %6s\t %10s\n' % ('ID', 'Name', 'RegDate', '#Staff', 'Manager'))
        while c != None:
            print('%5d\t %10s\t %10s\t %6d\t %10s\n' % (c.id, c.name, c.regDate, c.staffCount, c.managerName))
            c = c.next

    # Implement
    def findById(self, id):
        c = self.head
        while c is not None:
            if c.id is id:
                return c
            else:
                c = c.next
        if c is None:
            return False

    def findByName(self, name):
        c = self.head
        while c is not None:
            if c.name == name:
                return c
            else:
                c = c.next

    # extra methods that you might need
    def methodName(self, pars):
        pass


# implement classes
class Customers(object):
    def __init__(self):
        self.head = None
        if not os.path.exists('customers.txt'):
            f = open('customers.txt', 'w')
            f.close()

    def Load(self):

        f = open('customers.txt', 'r')
        c = None
        for line in f.readlines():
            lineparts = line.replace('\n', '').split('\t')
            if len(lineparts) > 1:
                if self.head == None:
                    self.head = Customer(id=int(lineparts[0]), name=lineparts[1], address=lineparts[2],
                                         phone=str(lineparts[3]))
                    c = self.head
                    tree = Tree()
                    tree.insert(c.id, c)
                else:
                    c.next = Customer(id=int(lineparts[0]), name=lineparts[1], address=lineparts[2],
                                      phone=str(lineparts[3]))
                    c = c.next
                    tree.insert(c.id, c)
        f.close()
        return tree

    def print(self):
        c = self.head
        print('%5s\t %10s\t %10s\t %10s\n' % ('ID', 'Name', 'Address', 'Phone'))
        while c != None:
            print("%5d\t %10s\t %10s\t %10s\n" % (c.id, c.name, c.address, c.phone))
            c = c.next

    # Implement

    def findById(self, id2, tree):
        c = tree.root
        while c is not None:
            if id2 < c.id:
                c = c.left
            elif id2 == c.id:
                return c.data
            else:
                c = c.right




    def findByName(self, nimi, c):  #haetaan asiakasta nimen perusteella
        apu.answer = None           #asetetaan apu classin arvo noneksi, jotta voidaan hakea useamman kerran + eikä virheellinen syöte sekoita
        c.find(nimi)
        if apu.answer:
            return apu.answer
        else:
            return None



class Drivers(object):
    def __init__(self):
        self.head = None
        if not os.path.exists('drivers.txt'):
            f = open('drivers.txt', 'w')
            f.close()

    def Load(self):

        f = open('drivers.txt', 'r')
        c = None
        for line in f.readlines():
            lineparts = line.replace('\n', '').split('\t')
            if len(lineparts) > 1:
                if self.head == None:
                    self.head = Driver(id=int(lineparts[0]), officeid=int(lineparts[1]), name=lineparts[2],
                                       hireDate=lineparts[3], carModel=str(lineparts[4]))
                    c = self.head
                    data = c
                    tree1 = Tree()
                    tree1.insert(c.id, data)
                else:
                    c.next = Driver(id=int(lineparts[0]), officeid=int(lineparts[1]), name=lineparts[2],
                                    hireDate=lineparts[3], carModel=str(lineparts[4]))
                    c = c.next
                    data = c
                    tree1.insert(c.id, data)
        f.close()
        return tree1

    def print(self):
        c = self.head
        print('%5s\t %10s\t %10s\t %10s\t %10s\n' % ('ID', 'OfficeId', 'Name', 'Hiredate', 'Car Model'))
        while c != None:
            print("%5d\t %10d\t %10s\t %10s\t %10s\n" % (c.id, c.officeid, c.name, c.hireDate, c.carModel))
            c = c.next

    # Implement
    def findById(self, id, tree1):
        c = tree1.root
        while c is not None:
            if id < c.id:
                c = c.left
            elif id is c.id:
                return c.data
            else:
                c = c.right
        if c is None:
            return False

    def findByName(self, c, nimi):
        apu.answer = None  # sama kuin aikaisemmin
        c.find(nimi)
        if apu.answer:
            return apu.answer
        else:
            return None


class Travels(object):
    def __init__(self):
        self.head = None
        if not os.path.exists('travels.txt'):
            f = open('travels.txt', 'w')
            f.close()

    def Load(self):

        f = open('travels.txt', 'r')
        c = None
        for line in f.readlines():
            lineparts = line.replace('\n', '').split('\t')
            if len(lineparts) > 1:
                if len(lineparts) is not 8:         #tapaus, jossa aijan ja päivämäärän välillä ei tabiä
                    s = (lineparts[2]).split(' ')   # muokataan listasta luettava poistamalla väli, koska ajan ja päivän välissä space eikä tabi
                    lineparts.pop(2)
                    part1 = s[0]
                    part2 = s[1]
                    lineparts.insert(2, part1)
                    lineparts.insert(3, part2)
                    if self.head is None:
                        self.head = Travel(id=int(lineparts[0]), driverId=int(lineparts[1]), date=lineparts[2],
                                           time=lineparts[3],
                                           customerId=int(lineparts[4]), source=lineparts[5], destination=lineparts[6],
                                           amount=float(lineparts[7]))
                        c = self.head
                    else:
                        c.next = Travel(id=int(lineparts[0]), driverId=int(lineparts[1]), date=lineparts[2],
                                        time=lineparts[3],
                                        customerId=int(lineparts[4]), source=lineparts[5], destination=lineparts[6],
                                        amount=float(lineparts[7]))
                        c = c.next
                elif self.head == None: #tapaus, jossa päivämäärä ja aika erotettu tabillä
                    self.head = Travel(id=int(lineparts[0]), driverId=int(lineparts[1]), date=lineparts[2],
                                       time=lineparts[3],
                                       customerId=int(lineparts[4]), source=lineparts[5], destination=lineparts[6],
                                       amount=int(lineparts[7]))
                    c = self.head
                else:
                    c.next = Travel(id=int(lineparts[0]), driverId=int(lineparts[1]), date=lineparts[2],
                                    time=lineparts[3],
                                    customerId=int(lineparts[4]), source=lineparts[5], destination=lineparts[6],
                                    amount=int(lineparts[7]))  #käytännössä turhaa, koska ei ole missään käytetty tabia sama elifille
                    c = c.next
        f.close()

    def print(self):
        c = self.head
        print('%5s\t %10s\t %10s\t %10s\t %10s %10s\t %10s\t %10s\n' % (
        'ID', 'DriverId', 'Date', 'Time', 'Customer', 'Source', 'Destination', 'Amount'))
        while c != None:
            print("%5d\t %10s\t %10s\t %10s\t %10s %10s\t %10s\t %10s\n" % (
            c.id, c.driverId, c.date, c.time, c.customerId, c.source, c.destination, c.amount))
            c = c.next

    def findById(self, customerId): #tietyn asiakkaan saamat palveluista aikajärjestyksessä ensimmäinen valinta
        c = self.head
        ListByCustomer = []
        while c is not None:
            if c.customerId is customerId:
                ListByCustomer.append(c)
                c = c.next
            else:
                c = c.next
        return ListByCustomer


    def findCustomer(self, customerId, date1, date2): #asiakkaat, jotka ovat hankkineet palveluita tietyllä aikavälillä 2 valinta
        c = self.head                                 #pitää vielä järjestää aikajärjestykseen
        ListByTime = []
        while c is not None:
            date = c.date.split('.')
            if customerId == c.customerId:
                if datetime.date(int(date[0]), int(date[1]), int(date[2])) >= datetime.date(int(date1[0]), int(date1[1]), int(date1[2])) and datetime.date(int(date[0]), int(date[1]), int(date[2])) <= datetime.date(int(date2[0]), int(date2[1]), int(date2[2])):
                    ListByTime.append(c)
                    c = c.next
                else:
                    c = c.next
            else:
                c = c.next
        ListByTime.sort(key=attrgetter('date', 'time'))
        return ListByTime


    def findDriver(self, t, tree): #Kuljettajat, jotka ovat palvelleet tiettyä asiakasta
        c = self.head
        d = tree.root
        ListByDriver = []
        while c is not None:
            if c.customerId == t:
                while d is not None:
                    if d.data.id == c.driverId:
                        ListByDriver.append(d.data)
                        c = c.next
                        d = tree.root
                        break
                    elif c.driverId < d.data.id:
                        d = d.left
                    else:
                        d = d.right
            else:
                c = c.next
        ListByDriver.sort(key=attrgetter('name'))
        return ListByDriver



    def add1(self, id, driverId, date, time, customerId, source, destination, amount): #lisää matkoja ei tarvitse mutta kiva ominaisuus
        f = open('test', 'a+')
        l = [id, driverId, date, time, customerId, source, destination, amount]
        for i in range(8):
            if i is 7:
                f.write(str(l[i]))
                f.write('\n')
            else:
                f.write(str(l[i]))
                f.write('\t')
        f.close()


    def add(self, list1, action4, tri, kohde): #pidetään muuttujat samana, koska helpompi muistaa
        if action4 == 1:
            for p in range(len(list1)):
                if list1[p].id == tri:
                    list1.pop(p)
                    list1.sort(key=attrgetter('date'))
                    return list1
            if p > len(list1):
                print('Muutoksia ei tehty')
                return list1
        elif action4 == 2:
            if kohde is not None:
                list1.append(kohde)
                list1.sort(key=attrgetter('date'))
                return list1
        elif action4 == 3:
            for f in range(len(list1)):
                if tri == list1[f].id:
                    return list1[f]
            if f > len(list1):
                return False
        else:
            print('Annoit väärän arvon!')
            time.sleep(2)

    def create(self):
        c = self.head
        list1 = []
        while c is not None:
            list1.append(c)
            c = c.next
        return list1
