import sqlite3
import sys


# 1. FUNÇÃO PARA CRIAR O BANCO DE DADOS E A TABELA (ADAPTADA PARA 3 MATÉRIAS)

def inicializar_banco():
    conexao = sqlite3.connect("edugrade.db")
    cursor = conexao.cursor()
    
    # Criamos uma tabela que salva o aluno, a matéria e os resultados daquela matéria
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notas_materias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_aluno TEXT NOT NULL,
        materia TEXT NOT NULL,
        faltas INTEGER NOT NULL,
        nota1 REAL NOT NULL,
        nota2 REAL NOT NULL,
        nota3 REAL NOT NULL,
        media REAL NOT NULL,
        status TEXT NOT NULL
    )
    """)
    conexao.commit()
    conexao.close()


# 2. FUNÇÃO PARA SALVAR OS DADOS DE UMA MATÉRIA NO BANCO

def salvar_materia_no_banco(nome, materia, faltas, notas, media, status):
    conexao = sqlite3.connect("edugrade.db")
    cursor = conexao.cursor()
    
    cursor.execute("""
    INSERT INTO notas_materias (nome_aluno, materia, faltas, nota1, nota2, nota3, media, status)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (nome, materia, faltas, notas[0], notas[1], notas[2], media, status))
    
    conexao.commit()
    conexao.close()


# 3. SISTEMA PRINCIPAL

# Login do Professor
login_professor = (input("Digite seu nome de login: ")).strip().lower()
if login_professor == "professor carlos":
    print("Bem vindo ao sistema Edugrade, professor carlos!\n")
else:
    print("Acesso negado. Usuário não reconhecido.")
    sys.exit() # Encerra o programa de forma limpa


def calcular_media_escolar():
    print("=" * 50)
    print("   SISTEMA EDUGRADE - ESCOLA INTEGRADA PRISMA      ")
    print("=" * 50)
    
    TOTAL_AULAS_POR_MATERIA = 100
    # Lista com as 3 matérias do sistema
    MATERIAS = ["Matemática", "Português", "História"]
    
    nome_aluno = input("Digite o nome do aluno: ").strip()
    print("-" * 50)
    
    # Loop que vai rodar 3 vezes (uma para cada matéria)
    for materia in MATERIAS:
        print(f"\n>>> Lançando dados de: {materia.upper()} <<<")
        
        # Número de Faltas na matéria
        while True:
            try:
                faltas = int(input(f"Digite as faltas em {materia} (0 a {TOTAL_AULAS_POR_MATERIA}): "))
                if 0 <= faltas <= TOTAL_AULAS_POR_MATERIA:
                    break
                else:
                    print(f"Por favor, digite um número entre 0 e {TOTAL_AULAS_POR_MATERIA}.")
            except ValueError:
                print("Entrada inválida! Digite apenas números inteiros.")
        
        # 3 Notas da matéria
        notas = []
        i = 1
        while i <= 3:
            try:
                nota = float(input(f"Digite a {i}ª nota de {materia} (0 a 10): "))
                if 0.0 <= nota <= 10.0:
                    notas.append(nota)
                    i += 1
                else:
                    print("Nota inválida! A nota deve estar entre 0.0 e 10.0.")
            except ValueError:
                print("Entrada inválida! Digite apenas números (Ex: 7.5).")

        # Cálculos da matéria atual
        media = sum(notas) / 3
        frequencia_porcentagem = ((TOTAL_AULAS_POR_MATERIA - faltas) / TOTAL_AULAS_POR_MATERIA) * 100
        
        # Lógica de Status da matéria atual
        if faltas >= 25:
            status_final = "REPROVADO POR FALTA"
        elif media >= 7.0:
            status_final = "APROVADO"
        elif 5.0 <= media <= 6.9:
            status_final = "RECUPERAÇÃO"
        else:
            status_final = "REPROVADO POR NOTA"
            
        # Mostra o resumo na tela
        print(f"\nResumo de {materia}:")
        print(f"  Média: {media:.2f} | Frequência: {frequencia_porcentagem:.1f}% ({faltas} faltas)")
        print(f"  STATUS EM {materia.upper()}: {status_final}")
        print("-" * 50)
        
        # Salva os dados desta matéria específica no banco
        salvar_materia_no_banco(nome_aluno, materia, faltas, notas, media, status_final)
        
    print("\n" + "=" * 50)
    print("✨ Processo concluído! Todas as matérias foram salvas.")
    print("=" * 50)


if __name__ == "__main__":
    inicializar_banco()
    calcular_media_escolar()