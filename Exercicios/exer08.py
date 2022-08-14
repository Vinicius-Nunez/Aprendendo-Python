metros = float(input('Metros: '))
centimetro = metros * 100
milimetro = centimetro * 10
km = metros / 1000
milha= km/1.609
hm = metros / 100
dam = metros / 10
dm = metros * 10
print(f'{km:.3f}km\n{hm:.2f}hm\n{dam:.1f}dam\n{dm:.0f}dm\n{metros:.1f}m\n{centimetro:.0f}cm\n{milimetro:.0f}mm\n{milha:.2f} milhas')