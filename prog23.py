erros = int(input("digite o código de erros? "))
match erros:

    case 200:
        print("200 - Sucesso! Tudo certo com sua requisição.")

    case 400:
        print("400 - Erro do cliente: Requisição malformada.")

    case 401 | 403:
        print("401/403 - Erros de permissão: você não tem acesso a esta página.")

    case 404:
        print("404 - Erro: Página não encontrada.")

    case 500 | 503:
        print("500/503 - Erros no servidor: nosso sistema está instável no momento.")

    case _:
        print(f"Código HTTP {erros} status desconhecido.")