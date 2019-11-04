# BACKLOG sp03bl01 - Cálculo do digito verificador do CPF
## História do usuário
> Eu como usuário preciso do cálculo do dígito verificador para um CPF informado.
> Vou informar os 9 primeiros dígitos e quero receber como resposta o CPF completo
> incluindo o dígito calculado.

## Arquitetura
* 1o passo: 
  * cada dígito do CPF informado deve ser multiplicado por um fator;
  * a lista de fatores é : 10,9,8,7,6,5,4,3,2 sendo que o 1o fator será o multiplicador
  do 1o número do CPF e assim por diante;
  * o resultado de cada multiplicação deve ser somado e armazenado em um total;
* 2o passo:
  * o total deve ser multiplicado por 10 e o resto da divisão por 11 será o 1o número 
  do dígito verificador;
  * adicionar o 1o número do dígito verificador ao final do CPF informado.
* 3o passo:
  * efetuar a mesma multiplicação por fatores anterior, agora começando pelo 2o número do 
   CPF informado;
  * o resultado de cada multiplicação deve ser somado e armazenado em um total;
* 4o passo:
  * o total deve ser multiplicado por 10 e o resto da divisão por 11 é o 2o número 
  do dígito verificador;
  * adicionar o 1o número do dígito verificador ao final do CPF informado.
  
## Convenção de nomes
0. Arquivo **cpf_dv.py**.
0. Função  **cpf_dv**.

## Critério de Aceite do _backlog_
0. A partir da informação de um conjunto de 9 dígitos calcular seu dígito verificador
com base nas regras do cálculo do CPF. 
0. Para o CPF **464668920** são esperados os seguintes valores:
````
1o passo Total : 286
        Primeiro digito : 0
2o passo CPF: 4646689200
3o passo Total : 287
        Segundo digito : 0
4o passo CPF : 46466892000
````
0. O algoritmo deve passar pelo teste **cpf_dv_teste.py** .