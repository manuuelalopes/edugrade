# Especificação de Requisitos de Software (SRS)
## Sistema de Gerenciamento de Notas e Frequência (SGNF)

Conforme a norma **ISO/IEC/IEEE 29148:2018**, este documento especifica os requisitos para o sistema de gerenciamento de notas de alunos, estabelecendo as diretrizes de escopo, funções, características de qualidade e restrições do projeto.

---

### 1. Introdução

#### 1.1 Escopo do Sistema
O Sistema de Gerenciamento de Notas e Frequência (SGNF) é uma aplicação em linha de comando (CLI) projetada para automatizar o processamento da situação acadêmica de alunos em uma determinada disciplina. O sistema valida as entradas de dados, calcula médias aritméticas, cruza dados de aproveitamento com registros de assiduidade e emite um boletim detalhado.

#### 1.2 Visão Geral do Produto
O produto opera de forma autônoma via terminal, servindo como uma ferramenta direta e ágil para o corpo docente consolidar o fechamento de turmas sem a necessidade de interfaces gráficas complexas ou infraestruturas de rede pesadas.

---

### 2. Contexto e Descrição Geral

#### 2.1 Perspectiva do Produto
O SGNF é uma ferramenta standalone. A lógica de negócios é estritamente local, focada na entrada de dados por sessão de execução e na exibição imediata do relatório final (Boletim).

#### 2.2 Características dos Usuários
* **Professor / Operador do Sistema:** Usuário com competência para avaliar os discentes e operar interfaces textuais básicas de computadores.

#### 2.3 Restrições de Design e Implementação
* **Interface:** Exclusivamente via Interface de Linha de Comando (CLI).
* **Persistência:** Não aplicável para esta versão inicial (processamento em memória por ciclo de execução).

---

### 3. Requisitos Funcionais (RF)

Esta seção detalha os requisitos funcionais mapeados a partir das necessidades de negócio do projeto.

| ID | Nome do Requisito | Descrição |
| :--- | :--- | :--- |
| **RF01** | Entrada do Nome do Aluno | O sistema deve permitir que o usuário insira o nome completo do aluno no formato textual. |
| **RF02** | Entrada de Notas | O sistema deve permitir a entrada de exatamente 3 (três) notas para a disciplina avaliada. |
| **RF03** | Entrada de Frequência | O sistema deve permitir a inserção da porcentagem de presença total do aluno na disciplina. |
| **RF04** | Emissão de Boletim Final | O sistema deve processar os dados e exibir em tela um relatório detalhado contendo: Nome do Aluno, as 3 Notas Individuais, Média Aritmética Calculada, Porcentagem de Frequência e o Status Final do Aluno. |
| **RF05** | Controle de Fluxo e Encerramento | O sistema deve permitir que, após a exibição do boletim final, o usuário escolha entre iniciar o cadastro e avaliação de um novo aluno (reiniciando o fluxo a partir do RF01) ou encerrar a execução da aplicação de forma segura através de um comando específico (ex: digitar 'S'). |


---

### 4. Regras de Negócio (RN)

As regras de negócio determinam o comportamento dos algoritmos de cálculo e a lógica de tomada de decisão do sistema.

#### RN01 – Cálculo da Média Aritmética
O sistema deve calcular a média aritmética simples baseada nas três notas fornecidas, utilizando a fórmula:
$$	ext{Média} = rac{	ext{Nota 1} + 	ext{Nota 2} + 	ext{Nota 3}}{3}$$

#### RN02 – Verificação de Frequência Mínima Obrigatória
A frequência é o primeiro critério eliminatório de aprovação. 
* Se a frequência inserida for **menor que 75%**, o aluno estará **Reprovado por Falta**, independentemente de sua média de notas.

#### RN03 – Lógica de Determinação do Status Acadêmico
Caso o aluno cumpra o requisito de frequência mínima ($\ge 75\%$), o seu status será definido pela média conforme os critérios abaixo:

| Faixa de Média | Condição de Frequência | Status Final |
| :--- | :--- | :--- |
| Qualquer valor | < 75% | **Reprovado por Falta** |
| $\ge$ 7.0 | $\ge$ 75% | **Aprovado** |
| Entre 5.0 e 6.9 | $\ge$ 75% | **Recuperação** |
| < 5.0 | $\ge$ 75% | **Reprovado por Nota** |

---

### 5. Requisitos Não Funcionais (RNF) e Tratamento de Exceções

#### RNF01 – Interface Baseada em Linha de Comando (CLI)
O sistema deve ser executado nativamente em terminais/consoles de comando (como Bash, PowerShell ou Prompt de Comando), utilizando entradas (`stdin`) e saídas (`stdout`) textuais padrão.

#### RNF02 – Robustez e Tolerância a Falhas (Validação de Dados)
O sistema não deve interromper sua execução de forma abrupta (crash/crash por exceção de tipo) diante de entradas inválidas. Ele deve realizar os seguintes tratamentos:

1. **Validação de Tipo de Dado (Notas e Frequência):** Caso o usuário digite caracteres alfabéticos, símbolos ou strings vazias onde se esperam valores numéricos (pontos flutuantes ou inteiros), o sistema deve capturar o erro, exibir uma mensagem de orientação amigável e solicitar o dado novamente.
2. **Validação de Intervalo de Notas:** O sistema só deve aceitar notas que estejam estritamente contidas no intervalo fechado de `0.0` a `10.0`. Valores fora desse intervalo devem ser rejeitados com um alerta ao usuário.
3. **Validação de Intervalo de Frequência:** A porcentagem de presença deve estar estritamente contida no intervalo numérico de `0` a `100`. Valores negativos ou superiores a 100 devem disparar uma mensagem de erro e repetição de input.

---

### 6. Rastreabilidade de Requisitos

Para garantir que cada necessidade do usuário seja atendida, a matriz abaixo correlaciona as histórias/necessidades com os requisitos e regras de negócio:

* **Necessidade:** *Cadastro e Avaliação (Inserir nome, notas e frequência)*
  * Alinhada com: **RF01**, **RF02**, **RF03**, **RN01**, **RN02**, **RNF02**.
* **Necessidade:** *Emissão de Boletim (Visualizar relatório detalhado)*
  * Alinhada com: **RF04**, **RN03**, **RNF01**.
especificacao_requisitos_iso29148.md
Exibindo especificacao_requisitos_iso29148.md.


# Backlog do Projeto: 

Este backlog contém as tarefas necessárias para o desenvolvimento do sistema de gestão de notas, estruturado para ser distribuído em um quadro Kanban.

---

##  Sprint 1 : Configuração da Base e Estrutura de Dados
*Objetivo: Criar o alicerce do sistema para permitir o armazenamento e manipulação das informações.*

### Tarefa 01 -  Modelagem e Criação do Banco de Dados
*   **Descrição:** Criar as tabelas e relacionamentos no banco de dados para suportar o ecossistema da Escola Integrada Prisma.
*   **Requisitos Atendidos:** Estrutura base para RFs e RNs.
*   **Critérios de Aceite:**
    *    Criar tabela de `Alunos` (ID, Nome, Matrícula).
    *    Criar tabela de `Disciplinas` (ID, Nome).
    *    Criar tabela de `Boletim` que relacione Aluno e Disciplina, contendo campos para: Nota 1, Nota 2, Nota 3, Média Final, Frequência (em %) e Status.
    *   Garantir que o campo de frequência armazene valores de 0 a 100.

### Tarefa 02 - Interface Base para Carga de Dados (Alunos e Disciplinas)
*   **Descrição:** Desenvolver uma interface simples ou script de migração para cadastrar os primeiros alunos e disciplinas, permitindo que o sistema tenha dados para os testes de lógica.
*   **Critérios de Aceite:**
    *    Permitir a inserção de novos alunos no sistema.
    *    Permitir a vinculação de alunos às disciplinas criadas.

---

##  Sprint 2: Módulo de Lançamento e Regras de Negócio
*Objetivo: Implementar o motor de cálculo e as travas de segurança pedagógicas da escola.*

### Tarefa 03 Tela de Lançamento de Notas e Frequência (RF)
*   **Descrição:** Desenvolver a interface visual onde o professor ou a secretaria poderá selecionar o aluno, a disciplina e preencher as informações de desempenho.
*   **Critérios de Aceite:**
    *    Exibir um dropdown ou campo de busca para selecionar o Aluno e a Disciplina.
    *    Disponibilizar 3 campos numéricos para digitação das notas (N1, N2, N3).
    *    Disponibilizar 1 campo numérico para inserção da frequência acumulada (%).

### Tarefa 04 Motor de Cálculo: Média Aritmética (RN)
*   **Descrição:** Desenvolver o código backend que captura as 3 notas inseridas na Task 03 e calcula a média do aluno.
*   **Critérios de Aceite:**
    *    Aplicar a fórmula: $M\acute{e}dia = \frac{N1 + N2 + N3}{3}$
    *    O cálculo deve ser acionado automaticamente após o preenchimento da terceira nota.
    *    O resultado deve ser arredondado ou limitado a apenas 1 casa decimal (ex: 6.8).

### Tarefa 05 Motor de Lógica: Status por Nota (RN)
*   **Descrição:** Implementar os condicionais que definem a situação do aluno com base estritamente na média calculada.
*   **Critérios de Aceite:**
    *    Se a Média for menor que 5.0 $\rightarrow$ Definir temporariamente como **Reprovado**.
    *    Se a Média for entre 5.0 e 6.9 $\rightarrow$ Definir temporariamente como **Recuperação**.
    *    Se a Média for maior ou igual a 7.0 $\rightarrow$ Definir temporariamente como **Aprovado**.

### Tarefa 06 Validação da Frequência Mínima Obrigatória (RN - Trava Soberana)
*   **Descrição:** Implementar a regra de negócio que sobrepõe qualquer nota caso o aluno não atinja a presença mínima exigida pela Escola Integrada Prisma.
*   **Critérios de Aceite:**
    *    O sistema deve verificar o campo de frequência (%).
    *    Se a Frequência for menor que 75%, o status do aluno deve mudar obrigatoriamente para **Reprovado por Falta**.
    *    Esta regra deve ignorar as notas. (Exemplo: Aluno com média 9.5 e frequência 72% deve ser classificado como "Reprovado por Falta").

---

##  Sprint 3: Visualização e Emissão de Resultados
*Objetivo: Entregar o produto final para a coordenação e para os responsáveis pelos alunos.*

### Tarefa 07 Tela de Consulta do Boletim Final (RF)
*   **Descrição:** Criar a interface de visualização do boletim, onde constará a identidade visual da escola e o resumo do ano letivo do aluno.
*   **Critérios de Aceite:**
    *    Exibir no topo o nome: **Escola Integrada Prisma**.
    *    Exibir os dados do aluno (Nome e Matrícula).
    *    Exibir uma tabela contendo: Disciplina, Nota 1, Nota 2, Nota 3, Média Final, Frequência (%) e o Status Final.
    *    Aplicar cores diferenciais para o Status Final (ex: Verde para Aprovado, Amarelo para Recuperação, Vermelho para Reprovados).






