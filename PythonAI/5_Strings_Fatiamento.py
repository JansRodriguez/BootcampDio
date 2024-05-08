## MÉTODOS PARA MANIPULAR OBJETOS DO TIPO STRING, COMO INTERPOLAR VALORES DE VARIÁVEIS E ENTENDER O FUNCIONAMENTO DO FATIAMENTO.

        ## MÉTODO ÚTEIS DA CLASSE STRING
""" curso = "pYtHoN bEgInNeRs"

print(curso.upper())
print(curso.lower())
print(curso.title()) 

cursoComEspaços = "         pYtHoN  bEgInNeRs  "
print(cursoComEspaços)
print(cursoComEspaços.strip())
print(cursoComEspaços.lstrip())
print(cursoComEspaços.rstrip())

cursoAdicionandoCaracteres = "pYtHoN"
print(cursoAdicionandoCaracteres)
print(cursoAdicionandoCaracteres.upper())
print(cursoAdicionandoCaracteres.upper().center(10,"_"))

cursoParaJuntar = "Python" ## O JOIN ACRESCENTA ITEM A ITEM O VALOR A JUNTAR
print(cursoParaJuntar)
print(".".join(cursoParaJuntar)) ## PRIMEIRO SE COLOCAR O VALOR A JUNTAR, APOS QUE SE IDENTIFICA O OBJETO
"""
            ## INTERPOLAÇÃO DE VARIÁVEIS
"""
##Em Python 3, utiliza-se o método FORMAT e f strings para interpolar variáveis.
    ## FORMAT
nome = "Guilherme"
idade = 28
profissão = "Programador"
linguagem = "Python"
        ## EXEMPLO - FORMAT   
print(
    "Olá, me chamo {}, tenho {} anos de idade e atualmente trabalho como {}, e estou matriculado no curso de {}."
    .format(nome, idade, profissão, linguagem)
)
        ## EXEMPLO - f STRINGS
print(
    f"Olá, me chamo {nome}, tenho {idade} anos de idade e atualmente trabalho como {profissão}, e estou matriculado no curso de {linguagem}."
)  

PI = 3.14159265358979323846

print(f"Valor de PI: {PI}")
print(f'Valor de PI: {PI:.3f}')
print(f'Valor de PI: {PI:10.3f}')
"""
## FATIAMENTO DE STRING
"""
    ## É uma técnica utilizada para retornar sobstrings (partes da string original), informando inicio (start) fim (stop) e passo (step) : [start, stop[, step]]
        # Para acessar a string utilizamos os índices, a partir do 0 e os :
string = 'Hascbaf aorur vsofuvarvuaa afbbsrljfsrau jcravcsb'
print(string)
print(len(string))
print(string[:20]) # desde o início até o índice 20
print(string[20:]) # do índice 20 até o final
print(string[15:46:5]) # do índice 15 ao 46 (-1) pulando de 5 em 5
print(string[:]) # Retorna a string inteira
print(string[:-2]) ## Retorna a string subtraindo a quantidade de elementos informado após o -
print(string[::-1]) ## Retorna a string de tras para frente
"""
## STRING MÚLTIPLAS DE LINHAS
"""  
## Tem o uso das aspas triplas. Ele são utilizados quando se quer trazer um MENU ou comentários maiores no código
print(
    ==================MENU==================

    1 - Depositar
    2 - Sacar
    3 - Extrato
    0 - Sair    

    ==================MENU==================

)
"""
