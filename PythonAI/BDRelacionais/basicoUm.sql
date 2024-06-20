    # MER
        Modelo Entidade Relacionamento
    # DER
        Diagramas Entidade Relacionamento
    # ENTIDADES (Tabelas)
        As entidades são nomeadas com substantivos concretos ou abstratos que representem de forma clara sua função dentro do domínio
            ## TABELAS
                Usada para armazenar dados de forma organizada.
                Cada tabela em um banco de dados relacional tem um nome único e é dividida em colunas e linhas.
                # COLUNA
                    Representa um atributo específico dos dados armazenados. Possui nome único e tipo de dado associado que difine o tipo de informação que pode ser armazenado nela, como números, texxtos, datas, etc.
                # REGISTRO
                    Conhecido como linha ou tupla, é uma instância individual de dados em uma tabela.
    # Atributos (Campos ou tuplas da tabela)
        Os atributos são as características ou propriedades das entidades. Eles descrevem informações específicas sobre uma entidade.
    # Relacionamentos
        Os relacionamentos representam as associções entre entidades.

    ## COMANDOS SQL
        ## CREATE
            ## TABELA DE USUÁRIOS
        CREATE TABLE USUARIOS COMMENT 'usuários é o nome da tabela'(
            ID INT,
            NOME VARCHAR(255) NOT NULL COMMENT 'aqui entra o nome do usuário',
            EMAIL VARCHAR(100) NOT NULL UNIQUE COMMENT 'E-MAIL DO USUÁRIO',
            ENDERECO VARCHAR(255) NOT NULL COMMENT 'ENDEREÇO DO USUÁRIO',
            DATA_NASCIMENTO DATE NOT NULL COMMENT 'DATA DE NASCIMENTO DO USUÁRIO'
        );
            ## TABELA DE DESTINOS
        CREATE TABLE DESTINOS COMMENT 'o nome dessa nova tabela é destinos'(
            ID INT,
            NOME VARCHAR(255) NOT NULL UNIQUE COMMENT 'NOME DO DESTINO',
            DESCRICAO VARCHAR(255) NOT NULL COMMENT 'DESCRICAO DO DESTINO'
        );
            ## TABELA DE RESERVAS
        CREATE TABLE RESERVAS COMMENT 'O nome dessa tabela é reservas'(
            id INT COMMENT 'IDENTIFICADOR UNICO DA RESERVA',
            ID_USUARIO INT COMMENT 'REFERENCIA AO ID DO USUÁRIOS QUE FEZ A RESERVA',
            ID_DESTINOS INT COMMENT 'REFERENCIA AO ID DO DESTINO DA RESERVA',
            DATA DATE COMMENT 'DATA DA RESERVA',
            STATUS VARCHAR(255) DEFAULT 'PEDENTE' COMMENT 'STATUS DA RESERVA (CONFIRMADO, PENDENTE, CANCELADA, ETC)'
        );
        ## DELETE
        DELETE FROM DESTINOS
        WHERE NOME = "BLABLA"
        ## DROP
            O comando DROP TABLE é usado no SQL para remover uma tabela existente de um banco de dados relacional.
            Ele exclui permanentemente a tabela.
        DROP TABLE DESTINOS

## CHAVES PRIMÁRIAS
    IDENTIFICA EXCLUSIVISAMENTE
    NÃO PODE CONTER VALORES NULOS (NULL)
    UMA TABELA PODE TER APENAS UMA CHAVE PRIMÁRIA
## CHAVES ESTRANGEIRAS
    Ela é usada para estabelecer e manter a integridade dos dados entre tabelas relacionadas.
    Po ser nula (not NULL)
    É possível ter mais de uma (ou nenhuma) em uma tabela.
        (
        chave_estrangeira tipoNumerico,
        Foreign Key (chave_estrangeira) REFERENCES (Nome da Tabela Original da chave estrangeira (id))
        )
        ## CHAVES ESTRANGEIRAS - RESTRIÇÕES
            ON DELETE, ON UPDATE, CASCADE, SET NULL, SET DEFAULT, RESTRICT

## NORMALIZAÇÃO DE DADOS
    A normalização de dados é um processo no qual se organiza e estrutura um banco de dados relacional de forma a eliminar redundâncias e anomalias, garantindo a consistência e integridade dos dados.

## CONSULTAS AVANÇADAS - JUNÇÕES E SUBCONSULTAS
    INNER JOIN = > EFETUA A RETORNO DAS LINHAS ONDE A CLÁUSULA DE COMPARAÇÃO ESTÁ PRESENTE. NAS TABELAS ONDE EXISTE ESSA CLÁUSULA, TERÁ OS RETORNOS DA BUSCA.
    LEFT JOIN = > RETORNA TODAS AS LINHAS DA TABELA À ESQUERDA E AS LINHAS CORRESPONDENTES DA TABELA À DIREITA, SE NÃO HOUVER CORRESPONDÊNCIA, OS VALORS  DA TAVELA À DIREIRA SERÃO NULL.
    RIGHT JOIN = > RETORNA TODAS AS LINHAS DA TABELA À DIREITA E AS LINHAS CORRESPONDENTES DA TABELA À ESQUERDA, SE NÃO HOUVER CORRESPONDÊNCIA, OS VALORS  DA TAVELA À ESQUERDA SERÃO NULL.
## SUB CONSULTAS
    ELAS PERMITEM REALIZAR CONSULTAS MAIS COMPLEXAS PERMITINDO QUE VOCÊ USE O RESULTADO DE UMA CONSULTA COMO ENTRADA PARA OUTRA CONSULTA.
    O RESULTADO DE UMA CONSULTA ANINHADA, ELA SERVE COMO PARÂMETRO PARA A CONSULTA EXTERNA.
        EXEMPLOS:
            SELECT * FROM DESTINOS
                WHERE ID NOT IN (
                    SELECT ID_DESTINOS FROM RESERVAS
                )
            SELECT * FROM USUARIOS
                WHERE ID NOT IN (
                    SELECT ID_USUARIOS FROM RESERVAS
                )
            SELECT NOME, (
                SELECT COUNT(*) FROM RESERVAS 
                    WHERE ID_USUARIOS = USUARIOS.ID
            ) AS TOTAL_RESERVAS FROM USUARIOS
## CONSULTAS AVANÇADAS - FUNÇÕES AGREGADAS E AGRUPAMENTOS DE RSULTADOS
    COUNT, SUM, AVG, MIN, MAX. 
        SELECT MAX(
            TIMESTAMPDIFF(
                YEAR, DATA_NASCIMENTO, CURRENT_DATE()
            )
        ) AS MAIOR_IDADE 
            FROM USUARIOS
    GROUP BY, HAVING