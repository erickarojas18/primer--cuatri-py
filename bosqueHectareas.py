#Determinar cuanto se debe sembrar en las hectareas

#Reforestar el bosque
r = 1
pinos = 8
eucalipto = 15
cedro = 10

NH  = float(input("Digite el numero de hectareas a reforestar:"))
while True:
    if NH > 100:
      p = NH*0.7
      e = NH*0.20
      c = NH*0.10
      print("la densidad de pinos seria de:",p,"\n la densidad de eucaliptos seria de:",e,"\nla densidad de cedros seria de:",c)


    else:
      p1 = NH*0.45
      e1 = NH*0.30
      c1 = NH*0.25
      print( "la densidad de pinos seria de:", p1, "\n la densidad de eucaliptos seria de:", e1,
            "\nla densidad de cedros seria de:", c1 )


    TP = NH/10*pinos
    TE =NH/15*eucalipto
    TC = NH/18*cedro
    print("La cantidad de pinos seria de:",TP,"\n la cantidad de eucaliptos seria de;",TE,"\nla cantidad de cedros eeria de:",TC)

    break