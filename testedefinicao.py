def bem_vindo():
   print('Bem vindo! Vamos calcular a média')
   return
def retorna_media(num1,num2,num3):
    media=(num1+num2+num3)/3
    return media
bem_vindo()
print("Digite o primeiro valor")
n1 = int(input())
print('Digite o segundo valor')
n2 = int(input())
print('Digite o terceiro valor')
n3 = int(input())
reposta=retorna_media(n1,n2,n3)
print('A média é: ', reposta)