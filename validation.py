class validate:


    def mail(mail=''):
        e = mail
        lista = []
        for i in e:
            lista.append(i)
        # print(lista)

        try:
            lista.index("@")
            return True
        except:
            return False


    def tel(tel=''):
        t = tel
        print(len(t))
        if t.isdigit() and len(t) == 10:
            return True
        else:
            return False





