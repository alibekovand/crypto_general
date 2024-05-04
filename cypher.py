import des
import rsa
import md5


def encrypt():
    #DES
    cypher_text_file = open("plaintext.txt","r")
    enc_text_file = open("enc_text.txt", "w", encoding="utf-8")
    dec_text_file = open("dec_text.txt", "w", encoding="utf-8")
    input = cypher_text_file.readlines()
    des_enc = des.encryption(''.join(input))
    print('Plain text: ', input, '\n')
    print("DES encryption: ", des_enc, '\n')

    #RSA
    # Генерация ключей
    public_key, private_key = rsa.generate_keypair(128)

    # Вывод ключей
    print("public key:", public_key)
    print("private key:", private_key)

    # Шифрование
    plaintext = "Hello, World!"
    cypher = rsa.encrypt(public_key, des_enc)
    print("RSA Encryption:", cypher, '\n')

    # MD5
    hash = md5.md5(str(cypher))
    print('MD5 hash: ', hash)



encrypt()