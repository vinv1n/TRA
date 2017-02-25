import time
from Classes import Agency, Agencies, Customer, Customers, Drivers, Driver, Travels, Travel


def menu():
    k = True
    while k is True:
        print('Valinnta:\n'
              '\t1: Etsi Matkatoimisto\n'
              '\t2: Etsi Kuljettaja\n'
              '\t3: Etsi matka\n'
              '\t4: Lisää\poista matka\n'
              '\t5: Lopeta\n')
        try:
            action = int(input('Minä toiminnon valitset?(Anna valinta numerona): '))
        except ValueError:
            print('Anna valinta numerona!')
        else:
            if action is 1:
                ag = Agencies()
                ag.Load()
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
                        if a is False:
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
            elif action is 2:
                dr = Drivers()
                tree1 = dr.Load()
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
                        dr = dr.findByName(name)
                        if a is False:
                            print('Nimellä ei löytynyt kuljettajaa')
                        else:
                            print(a.name, a.id, a.staffCount, a.regDate, a.managerName)
                    elif action2 is 2:
                        try:
                            id = int(input('Syötä Id lukuna: '))
                        except ValueError:
                            print('Id:n täytyy olla luku!')
                        else:
                            d = dr.findById(id, tree1)
                            if d is False:
                                print('Idllä ei löytynyt kuljettajaa!')
                            else:
                                print(d.id, d.name, d.hireDate, d.officeid, d.carModel)
            elif action == 3:
                tr = Travels()
                tr.Load()
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
                            for j in range(0, 5):  # for looppi jotta ei tarvitse tehdä erillistä postumista
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
                            print('Syötit liian monesti väärin palataan alkuun')
                    elif action3 == 3:
                        try:
                            t = int(input('Syötä asiakkaan tunnus:').strip())
                        except ValueError:
                            print('Syötä luku')
                        else:
                            dr = Drivers()
                            tre = dr.Load()
                            f = tr.findDriver(t, tre)
                            if len(f) == 0:
                                print('ei löytynyt')
                            else:
                                for l in range(0, len(f)):
                                    print('\t', f[l].id, f[l].officeid, f[l].name, f[l].hireDate, f[l].carModel, '\n')
            elif action == 4:  # tr.add lisä ominaisuus kirjoittaa syötetyt tiedot travels.txt:n loppuun, muuten lukee listatsta
                print('Valitse toiminto:'
                      '1: Poista'
                      '2: Lisää')
                print('Valitse lista: ')
                print('1: Ajan mukaan listatusta\n'
                      '2: Asiakkaan mukaan listatuista\n'
                      '3: Kuljettajan mukaan listatuista\n')
                try:
                    action4 = int(input('Poistetaanko(1) vai lisätäänkö(2) listata?'))
                    act = int(input('Mihin listaan toiminto suoritetaan?'))
                except ValueError:
                    print('Valintaa tehdään numeroilla!')
                    time.sleep(2)
                else:
                    tr

            elif action == 5:
                print('Lopeta peli kirjoittamalla q/quit tai jatka kirjoittamalla n/no\n')
                a = str(input('Do you really want to quit:').lower())
                if a == 'q' or a == 'quit':
                    k = False
                elif a == 'n' or a == 'no':
                    print('Ohjelma looppaa')
                    for f in range(0, 4):
                        print('#' * (f + 1), '.' * (3 - f))
                        time.sleep(1 / 2)
            else:
                print('rip, yritä uudestaan')
                time.sleep(2)
                print('\n' * 3)
    return 0
