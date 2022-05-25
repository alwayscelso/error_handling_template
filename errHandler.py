import sys

#dicionario que relaciona os codigos de erro suas respectivas mensagens de erro
errCoding={
    #100: Classe de erros de credenciais
    #200: Classe de erros de rede
    #300: Classe de erros de arquivo
}

#Funcao de tratamento de erros, exibe uma mensagem util de erro e tambem fecha buffers
def reportError(errCode, buffer=-1):
    if(errCode >= 100 and errCode < 200):
        credError(errCode, buffer)
    elif(errCode >= 200 and errCode < 300):
        netError(errCode, buffer)
    elif(errCode >= 300 and errCode < 400):
        fileError(errCode, buffer)

def credError(errCode, buffer=-1):
    #TODO

def netError(errCode, buffer=-1):
    #TODO

def fileError(errCode, buffer=-1):
    #TODO
