def menu():
     menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))