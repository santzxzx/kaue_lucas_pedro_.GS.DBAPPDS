Explicação do Funcionamento do Programa
Este programa tem como objetivo monitorar e analisar o consumo de energia limpa de uma comunidade ao longo de n dias, informando se as metas de consumo sustentável foram atingidas e fornecendo estatísticas adicionais sobre os dados coletados.

Passo a Passo do Funcionamento:
Solicitação de Entrada de Dados:

O programa solicita ao usuário que insira um número inteiro n, representando a quantidade de dias para os quais os dados de consumo de energia serão fornecidos.
Em seguida, o programa solicita a entrada de um valor inteiro para cada dia, representando o consumo de energia (em kWh).
Variáveis de Controle:

total_consumo: Soma dos consumos inseridos ao longo dos n dias.
dias_cumpriram_meta: Conta o número de dias em que o consumo foi igual ou superior à meta de 150 kWh.
dias_nao_cumpriram_meta: Conta o número de dias em que o consumo foi inferior à meta.
maior_consumo e menor_consumo: Guardam os valores do maior e do menor consumo registrado durante os n dias.
Processamento dos Dados:

Para cada dia, o consumo é somado ao total_consumo.
É realizada a verificação se o consumo do dia atingiu ou superou a meta de 150 kWh para contabilização nos contadores dias_cumpriram_meta e dias_nao_cumpriram_meta.
Simultaneamente, é determinado o maior e o menor consumo entre os valores fornecidos.
Cálculo e Relatório de Resultados:

A média de consumo ao longo dos n dias é calculada.
Dependendo dos valores dos contadores, o programa imprime um relatório indicando:
Se todos os dias cumpriram a meta.
Se nenhum dia cumpriu a meta.
O número de dias que cumpriram e não cumpriram a meta.
Além disso, são exibidos os valores da média, o maior consumo e o menor consumo.
Etapas para Executar o Código:
Abra um terminal ou console (por exemplo, em um editor de código como VS Code ou PyCharm).
Execute o código digitando o comando: python nome_do_arquivo.py (substitua nome_do_arquivo.py pelo nome do arquivo onde você salvou o código).
Insira a quantidade de dias quando solicitado.
Insira os valores de consumo para cada dia conforme solicitado pelo programa.
Observe a saída fornecida pelo programa, que incluirá informações sobre o cumprimento das metas, a média de consumo e os valores de maior e menor consumo.
Esse programa é um exemplo de como monitorar e analisar dados de consumo de forma eficiente usando estruturas básicas de controle e laços em Python, sem o uso de coleções como listas ou dicionários.
