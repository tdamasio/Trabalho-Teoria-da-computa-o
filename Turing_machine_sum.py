import csv
from gettext import find

#Função para converter binário em unário
def binToUnary(bins):
    unys = []
    for i in bins:
        x = int(i,2)
        un = '1'
        while(x > 0):
            un += '1'
            x = x-1
        unys.append(un)
    return unys

def main():
    #Lendo os números do arquivo
    arquivo = open('exemplo2.CSV')
    exemplo = csv.reader(arquivo)
    binarios = []
    for aux in exemplo:
        entrada = aux
    binarios = entrada[0].split(";")
    #print(binarios)
    #Convertendo em Unário
    #binarios = ["1111","1000010"]
    unarios = binToUnary(binarios)
    
    #representação de R(m) com w - Fita 1
    Rm = '0001011101101110110011011101110110110011011011011011001110111011110111010011101101110110110011110110111110111010011111011011111101110100111111011011111101101000'
    #print(unarios)
    Rm += unarios[0] + "01110" + unarios[1]
    
    #Dividindo as transições da entrada
    aux = Rm.split("000")
    #print(aux)
    #transições
    transitions = aux[1].split("00")
    #print(transitions)
    #Fita 2 - estado atual
    estado_atual = '1'

    #fita de entrada
    fita_entrada = []
    cont = 0
    for i in unarios:
        fita_entrada.append("111")
        for j in i:
            aux = j + j
            fita_entrada.append(aux)
        cont = cont +1
    fita_entrada.append("111")
    #print(fita_entrada)
    cabeça_leitura = ""
    #Funcionamento da máquina
    cont = 1
    while(cont > 0):
        en = fita_entrada[cont - 1]
        t = estado_atual + "0" + en  + "0"
        for i in transitions:
           if(i.find(t) == 0):
               x = i.split("0")
               estado_atual = x[2]
               fita_entrada[cont - 1] = x[3]
               cabeça_leitura = x[4]
               if(cabeça_leitura =="11"):
                   cont = cont +1
               else:
                cont = cont - 1
               
               if(estado_atual == "111111"):
                   cont = 0
    #print(fita_entrada)
    total = ""
    for s in fita_entrada:
        if s =="11":
            total = total + "1"
    tamanho = len(total)
    saida = total[:tamanho - 1]
    num_dec = len(saida)
    num_bin = format(num_dec,"b")
    print(num_bin)
        
if __name__ == "__main__":
      main()
