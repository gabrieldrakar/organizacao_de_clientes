
import os

if os.path.isdir ('arquivos') == False:
  os.mkdir('arquivos')
os.chdir('arquivos')
cwd = os.getcwd()
print (cwd)
arquivo1 =input('nome do arquivo: ') +'.txt'

if os.path.exists(arquivo1) == False:
  arquivo= open(arquivo1, 'w+')

elif os.path.exists(arquivo1) == True:
  arquivo=open ( arquivo1,'a')

class client:
  def __init__(self):
    self.Nome=input('qual o nome do seu cliente? ')
    self.Cidade=input('qual a cidade do seu cliente? ')
    self.Estado=input('qual o estado do seu cliente? ')
    self.Pedido=input('qual o pedido do seu cliente? ')
    self.massa=int(input('qual o peso do pedido do seu cliente? '))
    self.Quantidade=int(input('qual a quantidade do pedido do seu cliente? '))
    self.soma=self.massa+self.Quantidade
    return

def note(client):
  arquivo.write(f'\n \nnome do cliente \n{client.Nome}\n')
  arquivo.write(f'cidade do cliente \n{client.Cidade}\n')
  arquivo.write(f'estado do cliente \n{client.Estado}\n')
  arquivo.write(f'pedido do cliente \n{client.Pedido}\n')
  arquivo.write(f'peso+quantidade do ciente \n{client.soma}\n')

a=client()
b=note(a)

arquivo.close()


