from pyswip import Prolog

def consulta_prolog(pergunta):
    prolog = Prolog()
    prolog.consult("familia.pl")
    resultados = list(prolog.query(pergunta))
    
    if resultados:
        return resultados
    else:
        return "Nenhuma resposta encontrada."

if __name__ == "__main__":
    pergunta = input("Faça sua pergunta em Prolog: ")
    resposta = consulta_prolog(pergunta)
    print("Resposta:", resposta)
