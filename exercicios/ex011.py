larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
# tinta = área / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².\n'
      'Para pintar essa parede , você precisará de {:.3f}l de tinta'.format(larg, alt, área, área/2))
