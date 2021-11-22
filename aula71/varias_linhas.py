""" Descrição rápida e simples.

O que é um Docstring?
Uma docstring é uma string literal que ocorre como a primeira instrução em uma definição de módulo, função, classe ou
método. Tal docstring torna-se o atributo especial __doc__ desse objeto.

Todos os módulos normalmente devem ter docstrings, e todas as funções e classes exportadas por um módulo também devem
ter docstrings. Os métodos públicos (incluindo o construtor __init__ ) também devem ter docstrings. Um pacote pode ser
documentado no docstring do módulo do arquivo __init__.py no diretório do pacote.

Literais de string que ocorrem em outro lugar no código Python também podem atuar como documentação.
Eles não são reconhecidos pelo compilador de bytecode Python e não são acessíveis como atributos de objeto de tempo de
execução (ou seja, não atribuídos a __doc__ ), mas dois tipos de docstrings extras podem ser extraídos por ferramentas
de software:

Literais de string que ocorrem imediatamente após uma atribuição simples no nível superior de um módulo, classe ou
método __init__ são chamados de "docstrings de atributo".
Literais de string que ocorrem imediatamente após outra docstring são chamados de "docstrings adicionais".
Consulte PEP 258 , "Docutils Design Specification" [2] , para uma descrição detalhada do atributo e docstrings
adicionais.

Para consistência, sempre use "" " aspas duplas triplas " "" ao redor de docstrings. Use r "" " aspas duplas triplas "
"" se você usar barras invertidas em suas docstrings. Para docstrings Unicode, use u "" " strings Unicode entre aspas
triplas " "" .

Existem duas formas de docstrings: docstrings de uma linha e de várias linhas.

"""

variavel = 'valor'


def funcao():
    return 1

