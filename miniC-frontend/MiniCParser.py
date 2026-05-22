import ply.yacc as yacc

from MiniCLexer import tokens as tokens

# Right-associative so a + b + c builds a + (b + c), not (a + b) + c.
# Last entry in the tuple has highest precedence.
precedence = (
    ("right", "RELOP"),
    ("right", "ADDOP"),
    ("right", "MULOP"),
)


def p_program(p):
    "program : stmtlist"
    p[0] = p[1]


def p_stmt_assign(p):
    "stmt : ID EQ expr SEMI"
    p[0] = [["id", p[1]], "=", p[3]]


def p_stmt_if(p):
    "stmt : IF LPAREN expr RPAREN stmt"
    p[0] = ["if", p[3], p[5]]


def p_stmt_while(p):
    "stmt : WHILE LPAREN expr RPAREN stmt"
    p[0] = ["while", p[3], p[5]]


def p_stmt_block(p):
    "stmt : LBRACE stmtlist RBRACE"
    p[0] = p[2]


def p_stmtlist_single(p):
    "stmtlist : stmt"
    p[0] = p[1]


def p_stmtlist_multi(p):
    "stmtlist : stmtlist stmt"
    # Concatenate so multiple statements stay in one flat list
    p[0] = p[1] + p[2]


def p_expr_id(p):
    "expr : ID"
    p[0] = ["id", p[1]]


def p_expr_num(p):
    "expr : NUM"
    p[0] = ["num", p[1]]


def p_expr_binop(p):
    """expr : expr RELOP expr
    | expr ADDOP expr
    | expr MULOP expr"""
    p[0] = [p[1], ["optr", p[2]], p[3]]


def p_error(p):
    if p:
        raise SyntaxError(f"Syntax error at '{p.value}'")
    else:
        raise SyntaxError("Syntax error at EOF")


parser = yacc.yacc()
