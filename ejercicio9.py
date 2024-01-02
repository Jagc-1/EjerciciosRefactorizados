# Muestra una gráfica de asteriscos [ * ]

XN = 7


print("-----------------")
for f in range(9):
  serie = ""
  if (f >= 5):
    XN = XN + 2
  for c in range(XN - f):
      serie = serie + "*"
  print(serie)
