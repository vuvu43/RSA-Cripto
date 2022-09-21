from random import randint
from math import gcd as mdc

códigos_para_símbolos = {111: '0', 112: '1', 113: '2', 114: '3', 115: '4',
                         116: '5', 117: '6', 118: '7', 119: '8', 121: '9', 122: '=', 123: '+',
                         124: '-', 125: '/', 126: '*', 127: 'a', 128: 'b', 129: 'c', 131: 'd',
                         132: 'e', 133: 'f', 134: 'g', 135: 'h', 136: 'i', 137: 'j', 138: 'k',
                         139: 'l', 141: 'm', 142: 'n', 143: 'o', 144: 'p', 145: 'q', 146: 'r',
                         147: 's', 148: 't', 149: 'u', 151: 'v', 152: 'w', 153: 'x', 154: 'y',
                         155: 'z', 156: 'á', 157: 'à', 158: 'â', 159: 'ã', 161: 'é', 162: 'ê',
                         163: 'í', 164: 'ó', 165: 'ô', 166: 'õ', 167: 'ú', 168: 'ç', 169: 'A',
                         171: 'B', 172: 'C', 173: 'D', 174: 'E', 175: 'F', 176: 'G', 177: 'H',
                         178: 'I', 179: 'J', 181: 'K', 182: 'L', 183: 'M', 184: 'N', 185: 'O',
                         186: 'P', 187: 'Q', 188: 'R', 189: 'S', 191: 'T', 192: 'U', 193: 'V',
                         194: 'W', 195: 'X', 196: 'Y', 197: 'Z', 198: 'Á', 199: 'À', 211: 'Â',
                         212: 'Ã', 213: 'É', 214: 'Ê', 215: 'Í', 216: 'Ó', 217: 'Ô', 218: 'Õ',
                         219: 'Ú', 221: 'Ç', 222: ',', 223: '.', 224: '!', 225: '?', 226: ';',
                         227: ':', 228: '_', 229: '(', 231: ')', 232: '"', 233: '#', 234: '$',
                         235: '%', 236: '@', 237: ' ', 238: '\n'}

símbolos_para_códigos = {'0': 111, '1': 112, '2': 113, '3': 114, '4': 115,
                         '5': 116, '6': 117, '7': 118, '8': 119, '9': 121, '=': 122, '+': 123,
                         '-': 124, '/': 125, '*': 126, 'a': 127, 'b': 128, 'c': 129, 'd': 131,
                         'e': 132, 'f': 133, 'g': 134, 'h': 135, 'i': 136, 'j': 137, 'k': 138,
                         'l': 139, 'm': 141, 'n': 142, 'o': 143, 'p': 144, 'q': 145, 'r': 146,
                         's': 147, 't': 148, 'u': 149, 'v': 151, 'w': 152, 'x': 153, 'y': 154,
                         'z': 155, 'á': 156, 'à': 157, 'â': 158, 'ã': 159, 'é': 161, 'ê': 162,
                         'í': 163, 'ó': 164, 'ô': 165, 'õ': 166, 'ú': 167, 'ç': 168, 'A': 169,
                         'B': 171, 'C': 172, 'D': 173, 'E': 174, 'F': 175, 'G': 176, 'H': 177,
                         'I': 178, 'J': 179, 'K': 181, 'L': 182, 'M': 183, 'N': 184, 'O': 185,
                         'P': 186, 'Q': 187, 'R': 188, 'S': 189, 'T': 191, 'U': 192, 'V': 193,
                         'W': 194, 'X': 195, 'Y': 196, 'Z': 197, 'Á': 198, 'À': 199, 'Â': 211,
                         'Ã': 212, 'É': 213, 'Ê': 214, 'Í': 215, 'Ó': 216, 'Ô': 217, 'Õ': 218,
                         'Ú': 219, 'Ç': 221, ',': 222, '.': 223, '!': 224, '?': 225, ';': 226,
                         ':': 227, '_': 228, '(': 229, ')': 231, '"': 232, '#': 233, '$': 234,
                         '%': 235, '@': 236, ' ': 237, '\n': 238}


def fatora_dois(m):
    k = 0
    q = m
    while q % 2 == 0:
        q //= 2
        k += 1
    return k, q


def miller_rabin(n, b):
    # Passo 1
    k, q = fatora_dois(n - 1)

    # Passo 2
    chute = pow(b, q, n)
    if chute == 1 or chute == n - 1:
        return True

    # Passo 3
    for j in range(1, k + 1):
        chute = pow(chute, 2, n)
        if chute == 1:
            return False
        if chute == n - 1:
            return True

    # Passo 4
    return False


def gera_primos(n):
    teste = False
    while not teste:
        p = randint(10 ** n + 1, 10 ** (n + 2) + 1)
        for i in range(10):  # Rodando o teste de Miller-Rabin 10 vezes
            b = randint(2, p+1)
            if not miller_rabin(p, b):
                teste = False
                break  # Caso o teste falhe, ele imediatamene sai do laço para poder testar outro número
            if miller_rabin(p, b):
                teste = True
    return p


def aee(a, b):  # usando algoritmo de euclides extendido para achar o inverso multiplicativo de 'a' no módulo 'b'
    if a == 0:
        return b, 0, 1
    if b == 0:
        return a, 1, 0

    x_anterior = 1
    x_atual = 0
    y_anterior = 0
    y_atual = 1
    dividendo, divisor = a, b

    while True:
        quociente, resto = divmod(dividendo, divisor)
        x_anterior, x_atual = x_atual, (x_anterior - x_atual*quociente)
        y_anterior, y_atual = y_atual, (y_anterior - y_atual*quociente)
        if resto == 0:
            if x_anterior < 0:
                return x_anterior + b
            else:
                return x_anterior
        dividendo, divisor = divisor, resto


def gera_chaves(v=1):
    p = gera_primos(v)
    q = gera_primos(v)
    phi = (p-1)*(q-1)

    while True:
        e = randint(1, 100)
        if mdc(e, phi) == 1:
            break

    n = p * q
    d = aee(e, phi)

    return n, e, d, p, q


def encriptar(texto, n=3401574593, e=7):
    transforma = list(texto)  # transforma o texto em lista para facilitar a mudança de caracteres para número

    for i in range(len(transforma)):  # percorre a lista mudando os caracteres para números
        transforma[i] = str(símbolos_para_códigos[transforma[i]])
    transforma = ''.join(transforma)

    div_transforma = []
    k = 0
    for i in range(len(transforma) - 1):  # percorre o texto transformado dividindo-o em blocos menores que n
        if int(transforma[k:i + 1]) > n:
            div_transforma.append(int(transforma[k:i]))
            k = i
    div_transforma.append(int(transforma[k:]))

    texto_codificado = []
    for i in div_transforma:  # transforma o texto dividido nos blocos encriptados
        texto_codificado.append(pow(i, e, n))
    return texto_codificado


def descriptar(blocos, n=3401574593, d=971773783):
    blocos = list(map(lambda x: pow(x, d, n), blocos))  # descriptando os blocos
    blocos = list(map(str, blocos))  # transformando os blocos em strings
    blocos = ''.join(blocos)  # juntandos todos os blocos

    k = 0
    blocos_div_3 = []
    for i in range(1, len(blocos)):  # dividindo a mensagem descriptada em blocos de 3
        if i % 3 == 0:
            blocos_div_3.append(blocos[k:i])
            k = i
    blocos_div_3.append(blocos[k:])

    mensagem = []
    for i in range(len(blocos_div_3)):  # percorre a lista mudando os números para caracteres
        mensagem += códigos_para_símbolos[int(blocos_div_3[i])]

    return ''.join(mensagem)



