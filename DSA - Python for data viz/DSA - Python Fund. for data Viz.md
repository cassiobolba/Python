



**BOLD**
*italic*

`codigo inlinne`

```py
```
#
##
###
####
  
<p align="center">     
 <img width="600" height="180" src="">
 </p> 

20:30  

## 1.INTRODUÇÃO  
Programação = Analisar uma tarefa, separar em etapas, e criar linhas de comandos que o computador executa.  
  
Python = Liguagem interpretada (há um interpretador), É orientada a objetos, portável (mc, win, linux).  

Why Python:  
* pq é capaz de ser usada em muitas da tarefas que da área de DS (scrpping, collecting, analizing, cleaning, publishing);  
* Grande comunidade de uso;  
* Tem bibliotecas de análise de dados craidas por usuários;   
* Open Source;  
* Jupyter Notebook, programação via browser;  
* Facilidade de aprender;  
* Escalabilidade (fácil de escalar o tamanho dos projetos) e portabilidade (win, linux, mac);  

**PyData Stack:**   
Pack de pacotes prontos para uso em projetos; 
Pandas, NumPy, SciKit Learn, MarPlotLib  

**Para Desenvolver em Python:**    
* Interpretador:  
* Editor de textos ou IDE: IDE (Ambiente integrado de Desenvolvimento).  Sublime text, VSCode, Jupyter Notebook.   
Sugestão de IDE = PyCharm , Rodeo, Spyder  

DSA não recomenda usar Jupyter Lab pelo Conda NAvigador, mas chamar pelo prompt de comando:  
abra cmd > cd .. > cd .. 

**Executar pelo cmd**  
nome_da_engine nome_arquivo.py    
python hello.py  

Para habilitar a execução do python via cmd, deve ter clicado na caixa "add python ao path". Se nã, siga esse tutorial: 

https://dicasdepython.com.br/resolvido-python-nao-e-reconhecido-como-um-comando-interno/  

Para usar direto o shell do python, digite apenas python. 
dentro do shell, você pode executar codigos de python

**Bibliografia Recomendada**  
python.org

**CONHECENDO SO**  
* Variáveis de ambiente = local onde meus softwares estão  
Este Computador > righ click Propriedades > Configurações Avançadas de Sistema > Váriáveis de ambiente  
Configurar caminhos para executar programas no cmd;  
https://dicasdepython.com.br/resolvido-python-nao-e-reconhecido-como-um-comando-interno/   

* Lista de serviços Executados   
services.msc no executar  
Ex: Depois de instalar Oracle, ele sempre inicia o serviço em segundo plano. Se não estiver executando, poder parar o serviço nesse menu;  

* Contas de Usuário = Sempre criar contas sem espaço no nome, dentro windows, pois plataformas baseadas em unix podem apresentar problemas (spark, R);  

* Java = JRE (Java Runtime Environment) e JDK (Java development kit). Se for usar spark, hadoop... melhor instalar o JDK pq ele tem todos packs.  
Como saber a versão do java:  
CMD > C:\Users\cassio.bolba>java -version > enter  
se nada aparecer, voce não tem java.   

* Oracle Virtual Box = Virtual Machine  


CONFIGURAR VARIÁVEL JUPYTER


## 2. Variáveis, Tipo e Estrutura de Dados  
* Python é linguagem interpretada, precisa do interretador escrito em bitecode, que é multiplataforma (mac, win).  

* 3 modos de executar programas em python:  
* Modo Shell (cmd)  
* Modo Script (arquivos ext py)  
* Modo interativo (Jupyter)  

* Indentação faz parte da sintaxe do Python para definir hierarquia. Use tab ou espaços (4 espaços)

* Comente os códigos # ou 3 aspas duplas;    

### 2.1 Números e operações matemáticas:   
Int - Num inteiros, pos ou neg  
Float - Núm fracionários = 7.1    

Type() - Saber tipo de número  

int() e float () para transformar em um dos tipos  

Conversão
```py 
float(9)
9.0
int(6.0)
6
int(6.5)
6
Hexadecimal e Binário
hex(394)
'0x18a'
hex(217)
bin(286)
'0b100011110'
bin(390)
Funções abs, round e pow
# Retorna o valor absoluto
abs(-8)
8
# Retorna o valor absoluto
abs(8)
8
# Retorna o valor com arredondamento
round(3.14151922,2)
3.14
# Potência
pow(4,2)
16
# Potência
pow(5,3)
125
```  

### 2.2 Variáveis e Operadores:  
**Variáveis**  
Usadas para armazenar valores que queremos usar mais tarde.   
```py
b = 10
```  
```py
print(b) = 10  
```  

* Nome de variável não pode começar com numero  
* Não pode haver espaço no nome  
* há alguns simbolos que não pode usar
* Não pode usar palavras reservadas  

**Operadores**    
* Aritiméticos: +, -
* Relacionais: <, >, ==, != 
* Atribuição: Z = 10 ou Z += 10 (é igual a Z + 10) (duas operações na mesma linha)  
* Lógicos: and, or, not  

**Declaração Múltipla**
```py
#Declaração Múltipla
pessoa1, pessoa2, pessoa3 = "Maria", "José", "Tobias"
pessoa1
'Maria'
pessoa2
'José'
pessoa3
'Tobias'
fruta1 = fruta2 = fruta3 = "Laranja"
fruta1
'Laranja'
fruta2
'Laranja'
# Fique atento!!! Python é case-sensitive. Criamos a variável fruta2, mas não a variável Fruta2.
# Letras maiúsculas e minúsculas tem diferença no nome da variável.
Fruta2
```

```py  
#Variáveis atribuídas a outras variáveis e ordem dos operadores
l
largura = 2
altura = 4
area = largura * altura
area
8
perimetro = 2 * largura + 2 * altura
perimetro
12
# A ordem dos operadores é a mesma seguida na Matemática
perimetro = 2 * (largura + 2)  * altura
perimetro
32

#Operações com variáveis
idade1 = 25
idade2 = 35
idade1 + idade2
60
idade2 - idade1
10
idade2 * idade1
875
idade2 / idade1
1.4
idade2 % idade1
10

#Concatenação de Variáveis
nome = "Steve"
sobrenome = "Jobs"
fullName = nome + " " + sobrenome
fullName
'Steve Jobs'
```
 