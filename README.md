
# Desafio Codeforces — Mentoria Codificadas | Além do Código
 
## Sobre este repositório
 
Este repositório contém minha resolução para o desafio de programação proposto na mentoria, utilizando problemas da plataforma [Codeforces](https://codeforces.com/) com auxílio de Inteligência Artificial.
 
---
 
## Problemas escolhidos
 
| # | Nome do problema | Link | Dificuldade |
|---|-----------------|------|-------------|
| 1 | 71A - Way Too Long Words | [Ver no Codeforces](https://codeforces.com/problemset/problem/71/A) | 800 |
| 2 | 118A - String Task | [Ver no Codeforces](https://codeforces.com/problemset/problem/118/A) | 1000 |

 
<!-- Remova as linhas dos problemas que não foram resolvidos caso tenha escolhido menos de 3.-->
 
---
 
## Problema 1 — 71A - Way Too Long Words
 
### O que o problema pede?
O problema pede para abreviar palavras que possuem mais de 10 caracteres. A abreviação deve conter a primeira letra da palavra, a quantidade de letras removidas do meio e a última letra.
 
 
### Como eu resolvi?
Utilizei uma estrutura de repetição para percorrer todas as palavras informadas. Em seguida, verifiquei o tamanho de cada palavra. Quando a palavra possuía mais de 10 caracteres, realizei a abreviação utilizando a primeira letra, o número de letras removidas e a última letra. Caso contrário, a palavra era exibida normalmente.
 
 
### Código
```python
n = int(input())
for _ in range(n):
    word = input()
    if len(word) > 10:
        print(word[0] + str(len(word) - 2) + word[-1])
    else:
        print(word)
```
 
---
 
## Problema 2 — 118A - String Task
 
### O que o problema pede?
O problema apresenta uma palavra e solicita a remoção de todas as vogais. Após isso, cada consoante deve ser precedida por um ponto "." e todas as letras devem ficar em minúsculo.
 
### Como eu resolvi?
Primeiro converti toda a palavra para letras minúsculas. Depois percorri cada caractere da string e verifiquei se ele não era uma vogal. Quando o caractere era uma consoante, adicionei um ponto seguido da letra ao resultado final.
 
 
### Código
```python
word = input().lower()
result = ""
for char in word:
    if char not in "aoyeui":
        result += "." + char
print(result)
```

---

## IA utilizada
 
### Qual IA você usou?
ChatGPT.
 
### Como a IA te ajudou?
Utilizei o ChatGPT para compreender melhor os enunciados, entender a lógica necessária para resolver os problemas, revisar as estratégias utilizadas e auxiliar na elaboração da documentação do projeto. A IA foi utilizada como ferramenta de apoio ao aprendizado durante todo o processo.
 
---
 
## Reflexão
 
### Dificuldades encontradas
A principal dificuldade foi interpretar corretamente os enunciados em inglês e compreender os formatos de entrada e saída exigidos pela plataforma Codeforces. Também foi necessário entender melhor a manipulação de strings em Python.
 
 
### O que aprendi
Aprendi a trabalhar com estruturas condicionais, laços de repetição e manipulação de strings. Também compreendi melhor como utilizar a Inteligência Artificial como ferramenta de apoio ao aprendizado e à resolução de problemas.
 
 
### Como foi a experiência?
A experiência foi muito positiva, pois permitiu praticar lógica de programação e conhecer uma plataforma amplamente utilizada para programação competitiva. Gostei especialmente de aprender novas formas de resolver problemas e de utilizar a IA para esclarecer dúvidas e aprofundar meu entendimento dos conceitos.
