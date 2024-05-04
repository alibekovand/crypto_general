from sympy import *



def ascii_to_binary(st):
    return ''.join(format(ord(x), 'b') for x in st)

def binary_to_int(binary):
    return int(binary, 2)



def main():
    with open('rsa_pub_key.txt', 'r') as file:
        text = file.read()

    # Convert each character to binary and then to integer
    #integers = [binary_to_int(char_to_binary(char)) for char in text]
    bin_str = ascii_to_binary(text)
    pbk = binary_to_int(bin_str)
    print(pbk)

    # Public key
    n = binary_to_int(bin_str)
    e = 3 

    # Factor n
    p, q = factorint(n, multiple=False)

    # Compute the private key
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)

    print(d)


if __name__ == "__main__":
    main()