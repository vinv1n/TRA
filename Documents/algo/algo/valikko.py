import time
from Classes import Agency, Agencies, Customer, Customers, Drivers, Driver, Travels, Travel, Node

def alustus(): #saadaan siististi globaaleja muuttujia
    tr = Travels()
    tr.Load()
    list1 = tr.create()
    ag = Agencies()
    ag.Load()
    cu = Customers()
    tree = cu.Load()
    dr = Drivers()
    tree1 = dr.Load()
    return list1, tree1, ag, tr, dr, tree, cu


def menu():
    list1, tree1, ag, tr, dr, tree, cu = alustus()
    k = True
    while k is True:
        print('Valinta:\n'
              '\t1: Etsi Matkatoimisto\n'
              '\t2: Etsi Kuljettaja\n'
              '\t3: Etsi matka\n'
              '\t4: Etsi Asiakas\n'
              '\t5: Lisää\poista matka\n'
              '\t6: Lopeta\n')
        try:
            action = int(input('Minä toiminnon valitset?(Anna valinta numerona): '))
        except ValueError:
            print('Anna valinta numerona!')
        else:
            if action is 1:
                print('Etsitäänkö matkatoimisto:\n'
                      '\t1: Nimellä\n'
                      '\t2: Idllä\n')
                try:
                    action1 = int(input('Anna valinta numerona: '))
                except ValueError:
                    print('Anna valinta numerona!')
                else:
                    if action1 is 1:
                        name = input('Syötä nimi: ').strip().title()
                        a = ag.findByName(name)
                        if a is None:
                            print('Nimellä ei löytynyt toimistoa')
                        else:
                            print(a.name, a.id, a.staffCount, a.regDate, a.managerName)
                    elif action1 is 2:
                        try:
                            id = int(input('Syötä Id lukuna: '))
                        except ValueError:
                            print('Id:n täytyy olla luku!')
                        else:
                            d = ag.findById(id)
                            if d is False:
                                print('Idllä ei löytynyt toimistoa!')
                            else:
                                print(d.name, d.id, d.staffCount,
                                      d.regDate, d.managerName)
            elif action == 2:
                print('Etsitäänkö kuljettaja:\n'
                      '\t1: Nimellä\n'
                      '\t2: Id:llä\n')
                try:
                    action2 = int(input('Syötä valinta numerona: '))
                except ValueError:
                    print('Syötä valinta numerona')
                else:
                    if action2 is 1:
                        name = input('Syötä nimi: ').strip().title()
                        a = dr.findByName(tree1, name)
                        if a is None:
                            print('Nimellä ei löytynyt kuljettajaa')
                        else:
                            print(a.id, a.officeid,  a.name, a.hireDate, a.carModel)
                    elif action2 is 2:
                        try:
                            id7 = int(input('Syötä Id lukuna: '))
                        except ValueError:
                            print('Id:n täytyy olla luku!')
                        else:
                            d = dr.findById(id7, tree1)
                            if d is None:
                                print('Idllä ei löytynyt kuljettajaa!')
                            else:
                                print(d.id, d.name, d.hireDate, d.officeid, d.carModel)
            elif action == 3:
                print('Etsitäänkö matkoja:\n'
                      '\t1: Asiakkaan mukaan tietyllä aikavälillä\n'
                      '\t2: Tietyn asiakkaan saamat palvelut aikavälillä\n'
                      '\t3: Kuljettajan mukaan, jotka ovat palvelleet annettua asiakasta\n')
                try:
                    action3 = int(input('Syötä valinta numerona: '))
                except ValueError:
                    print('Syötä valinta numerona')
                else:
                    if action3 == 1:
                        id1 = int(input('Syötä asiakkaan Id: '))
                        d = tr.findById(id1)
                        if len(d) is 0:
                            print('Idllä ei löytynyt asiakasta')
                        else:
                            for i in range(0, len(d)):
                                print('\t', d[i].id, d[i].driverId, d[i].date,
                                      d[i].time, d[i].customerId, d[i].source,
                                      d[i].destination, d[i].amount, '\n')
                    elif action3 == 2:  # etsitään asiakkaan saamia palveluita aikavälillä
                        try:
                            id2 = int(input('Syötä asiakkaan Id lukuna: '))
                        except ValueError:
                            print('Id:n täytyy olla luku!')
                        else:
                            for j in range(0, 5):  # for looppi jotta ei tarvitse tehdä erillistä postumista == väkerrys josta ei käytännön hyötyä
                                date1 = input('Syötä aloitus päivämäärä . erotettuna muodossa vv.kk.pp: ').split('.')
                                date2 = input('Syötä aloitus lopetus päivämäärä . erotettu vv.kk.pp: ').split('.')
                                if len(date1) and len(date2) is not 3:
                                    print('Syötit päivämäärän väärin!')
                                else:
                                    d = tr.findCustomer(id2, date1, date2)  # pitää tehdä loppuun
                                    if len(d) is 0:
                                        print('Idllä ei löytynyt kuljettajaa!')
                                    else:
                                        for i in range(0, len(d)):
                                            print('\t', d[i].id, d[i].driverId, d[i].date,
                                                  d[i].time, d[i].customerId, d[i].source,
                                                  d[i].destination, d[i].amount, '\n')
                                        break
                    elif action3 == 3:
                        try:
                            t = int(input('Syötä asiakkaan tunnus:').strip())
                        except ValueError:
                            print('Syötä luku')
                        else:
                            f = tr.findDriver(t, tree1)
                            if len(f) == 0:
                                print('ei löytynyt')
                            else:
                                for l in range(0, len(f)):
                                    print('\t', f[l].id, f[l].officeid, f[l].name, f[l].hireDate, f[l].carModel, '\n')
            elif action == 4:
                print('Etsitäänkö Asiakasta:\n'
                      '\t1: Nimen perusteella\n'
                      '\t2: Idn peristeella\n')
                try:
                    action6 = int(input('Valinta:').strip())
                except ValueError:
                    print('Valinta kokonaislukuna!')
                else:
                    if action6 == 1:
                        nimi6 = input('Syötä asiakkaan nimi:').strip().title()      #saataa olla lisää samoja virheitä, koska Customer#1 != customer#1
                        data66 = cu.findByName(nimi6, tree)
                        if data66 is None:
                            print('Nimellä ei löytynyt asiakasta')
                        else:
                            print(data66.id, data66.name, data66.address, data66.phone)
                    elif action6 == 2:
                        try:
                            id2 = int(input('Syötä asiakkaan id:').strip())
                        except ValueError:
                            print('Anna id lukuna!')
                        else:
                            h = cu.findById(id2, tree)
                            if h is None:
                                print('Idllä ei löytynyt asiakasta')
                            else:
                                print(h.id, h.name, h.address, h.phone)
                    else:
                        print('Syötä luku, joka on pienempi tai yhtäsuuri kuin 2')
                        time.sleep(2)
            elif action == 5:  # tr.add1 lisä ominaisuus kirjoittaa syötetyt tiedot travels.txt:n loppuun, muuten lukee listatsta
                print('Valitse toiminto:\n'
                      '1: Poista\n'
                      '2: Lisää\n'
                      '3: Etsi')
                try:
                    action4 = int(input(': ').strip())
                    tri = int(input('Syötä matkan tunnus:').strip()) #etsiminen rajoitettu tunnukseen voisi periaatteessa olla mikä tahansa mutta olisi epätarkka
                except ValueError:
                    print('Valintaa tehdään numeroilla!')
                    time.sleep(2)
                else:
                    if action4 == 1:
                       ty = tr.add(list1, action4, tri, kohde=None)
                       if ty is False:
                           print('Matkaa ei löytynyt!')
                           time.sleep(2)
                       else:
                           print('Matka poistettiin')
                    elif action4 == 2:
                        print('Anna loput tiedot:')
                        print('Insert driverId, date, time, customerId, source, destination, amount, in specific order and separeted by pilkku')
                        rt = input(': ').strip()
                        rt = rt.split(',')
                        print(len(rt))
                        if len(rt) != 7:
                            print('Tapahtui virhe!')
                        else:
                            kohde = Travel(tri, int(rt[0]), rt[1], rt[2], int(rt[3]), rt[4], rt[5], float(rt[6]))
                            tr.add(list1, action4, tri, kohde)
                            print(len(list1))
                    elif action4 == 3:
                        tr.add(action4, list1, tri, kohde=None)
                    else:
                        print('Virheellinen syöte')
            elif action == 6:
                print('Lopeta peli kirjoittamalla q/quit tai jatka kirjoittamalla n/no\n')
                a = str(input('Do you really want to quit:').lower())
                if a == 'q' or a == 'quit':
                    k = False
                elif a == 'n' or a == 'no':
                    print('Ohjelma looppaa')
                    for f in range(0, 10):
                        if f == 4:
                            print('#'* f, '-_-', '.' * (10 - f))
                        elif f == 7:
                            print('#' * 4, '-_-', '#' * (f - 3), '.' * (10 - f))
                            print('ei enää pliis')
                        elif f > 4:
                            print('#'*4, '-_-', '#'*(f-4), '.'*(10-f))
                        else:
                            print('#' * (f + 1), '.' * (10 - f))
                        time.sleep(1)
            else:
                print('rip, yritä uudestaan')
                time.sleep(2)
                print('\n' * 3)
    return 0
