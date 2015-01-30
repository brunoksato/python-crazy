x = int(raw_input("Favor digitar um inteiro: "))

 if x < 0:
      x = 0
   print 'Negativo alterado para zero'
elif x == 0:
     print 'Zero'
elif x == 1:
      print 'Unidade'
 else:
      print 'Mais'

a = ['gato', 'janela', 'defenestrar']
for x in a:
    print x, len(x)


for x in a[:]: # fazer uma cópia da lista inteira
    if len(x) > 6: a.insert(0, x)

range(10)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print i, a[i]

while True:
    pass

class MinhaClasseVazia:
    pass

def initlog(*args):
    pass

def fib(n):    # escrever série de Fibonacci até n
   """Exibe série de Fibonacci até n"""
   a, b = 0, 1
  while a < n:
        print a,
        a, b = b, a+b

def confirmar(pergunta, tentativas=4, reclamacao='Sim ou não, por favor!'):
    while True:
        ok = raw_input(pergunta).lower()
        if ok in ('s', 'si', 'sim'):
            return True
        if ok in ('n', 'no', 'não', 'nananinanão'):
            return False
        tentativas = tentativas - 1
        if tentativas == 0:
            raise IOError('usuario nao quer cooperar')
        print reclamacao

i = 5

def f(arg=i):
    print arg

i = 6
f()

def f(a, L=[]):
    L.append(a)
    return L

print f(1)
print f(2)
print f(3)

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"

def cheeseshop(kind, *arguments, **keywords):
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments:
        print arg
    print "-" * 40
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]

def escrever_multiplos_items(arquivo, separador, *args):
    arquivo.write(separador.join(args))