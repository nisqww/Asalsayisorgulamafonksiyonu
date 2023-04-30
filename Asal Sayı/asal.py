def isPrime(t):
    while True:
        if t<0:
            print("Negatif sayılarda asallık söz konusu değildir. Ama girdiğiniz sayının pozitif hali için konuşucak olursak: ")
            t=-t
        if t>2:
            a = int(t**(1/2))+1
            r = list(range(2,a+1))
            p = []
            for x in r:
                c = 1
                sp = []
                for a in p:
                    if a <= int(x**(1/2))+1 :
                        sp.append(a)
                    else:
                        break
                for a in sp:
                    if x % a == 0:
                        c = 0
                        break
                if c == 1:
                    p.append(x)
            for e in p:
                if t % e == 0:
                    return (print("Sayı Asal Değildir. Sayının Böleni: ",e))
            return (print("Sayımız Asaldır. Baktığımız asal sayılar: ",p))
        
        elif t==2:
            return(print("2 Asal sayıdır."))
            break
        

    
        
       
        

