import re 

#definición de patrones para cada tipo de token
token_specification = [
    ('if', r'\bif\b', 19),
    ('while', r'\bwhile\b', 20),
    ('return', r'\breturn\b', 21),
    ('else', r'\belse\b', 22),
    ('tipo', r'\b(int|float|void)\b', 4),
    ('real', r'\d+\.\d+', 2),
    ('entero', r'\d+', 1),
    ('identificador', r'[a-zA-Z_][a-zA-Z0-9_]*', 0),
    ('opIgualdad', r'(==|!=)', 11),
    ('opRelac', r'(<=|>=|<|>)', 7),
    ('opAnd', r'&&', 9),
    ('opOr', r'\|\|', 8),
    ('opNot', r'!', 10),
    ('opSuma', r'[+-]', 5),
    ('opMul', r'[*/]', 6),
    ('asignacion', r'=', 18),
    ('punto_coma', r';', 12),
    ('coma', r',', 13),
    ('paren_izq', r'\(', 14),
    ('paren_der', r'\)', 15),
    ('llave_izq', r'\{', 16),
    ('llave_der', r'\}', 17),
    ('espacio', r'[ \t\n]+', None), #Ignorar espacios en blanco
    ('desconocido', r'.', None)
]

#Compilar patrones de regex
regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern, _ in token_specification)

#funcion para el analisis lexico
def analizador_lexico(codigo):
    tokens = []
    for match in re.finditer(regex,codigo):
        tipo_token = match.lastgroup
        valor = match.group()
        tipo = next((t for n, p, t in token_specification if n == tipo_token), None)

        if tipo_token == 'espacio':
            continue #ignorar espacios en blanco
        elif tipo is not None:
            tokens.append((valor,tipo))
        else:
            print(f"Error lexico: simbolo desconocido '{valor}'" )
    tokens.append(('$', 23)) #Agregar el simbolo de fin de entrada
    return tokens

#Ejemplo de uso
codigo_prueba = """
int a = 5;
float b= 3.14;
if(a > b){
    return a + b;
} else {
    while (a != 0){
        a = a - 1;
    }
}
"""

resultado = analizador_lexico(codigo_prueba)
for token in resultado:
    print(token)