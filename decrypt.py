import os 
import pyaes

nome_arq = "texto.txt.ransomwaretroll"
arq = open(nome_arq, "rb")
dados_arq = arq.read()
arq.close()

chave = b"testeransomware"
aes = pyaes.AESModeOfOperationCTR(chave)
decrypt_data = aes.decrypt(dados_arq)

os.remove(nome_arq)

novo_arq = "teste.txt"
novo_arq = open(f'{novo_arq}', "wb")
novo_arq.write(decrypt_data)
novo_arq.close()