import ply.lex as lex

tokens = (
    "ID",
    "NUM",
    "IF",
    "WHILE",
    "RELOP",  # >=, <=, ==, >, <
    "ADDOP",  # +, -
    "MULOP",  # *, /
    "EQ",
    "SEMI",
    "LPAREN",
    "RPAREN",
    "LBRACE",
    "RBRACE",
)

reserved = {"if": "IF", "while": "WHILE"}

t_EQ = r"="
t_SEMI = r";"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACE = r"\{"
t_RBRACE = r"\}"

t_RELOP = r">=|<=|==|>|<"
t_MULOP = r"[*/]"
t_ADDOP = r"[+\-]"

t_ignore = " \t\n"


def t_ID(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, "ID")
    return t


# Function rules run before string rules, so +/- followed by a digit
# is captured as part of the number, not as a separate operator.
def t_NUM(t):
    r"[+-]?\d+(\.\d+)?"
    t.value = float(t.value)
    return t


def t_error(t):
    print("Illegal character:", t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
