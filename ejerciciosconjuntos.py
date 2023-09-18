grupos_musicales = {'duelo','bronco','primavera','intocable','pesado','calibre50'}
print('Estos son los grupos musicales:', grupos_musicales )
len(grupos_musicales)
print('La longitud de la lista de los grupos:',len(grupos_musicales))
print('Existe bronco en la lista?:', 'bronco' in grupos_musicales)
grupos_musicales.add('los temerarios')
print('la lista con otro gruo agregado:', grupos_musicales)
eliminado = grupos_musicales.pop()
print('grupo eliminado:', eliminado)