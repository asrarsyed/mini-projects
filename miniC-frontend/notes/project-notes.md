# My Project Notes (Lexer + Parser)

Project goals:
1. Define valid tokenization rules (`MiniCLexer.py` -> converts input text into tokens)
2. Define grammar rules in PLY (`MiniCParser.py` -> builds a parse tree from tokens)
3. Match the given CFG structure
4. Produce correct nested list parse trees
5. Support full nesting (if/while/blocks/expressions)

Given requirements: 
- Must use PLY (Python Lex-Yacc style)
- Must work with MiniC.py (the given driver program)

## Resources 

Read [PLY Documentation](https://ply.readthedocs.io/en/latest/index.html) here.

![Example Grammar](assets/example.png)

> Simplified excerpt of the formal grammar for the C programming language (left), and a derivation of a piece of C code (right) from the nonterminal symbol ⟨Stmt⟩. Nonterminal and terminal symbols are shown in blue and red, respectively.

## Grammar to Support

```
# Statements
<stmt> -> <id> = <expr> ;            # Assignment
<stmt> -> { <stmtlist> }             # Block
<stmt> -> if ( <expr> ) <stmt>       # Conditional
<stmt> -> while ( <expr> ) <stmt>    # Loop

# Statements List - A sequence of statements inside {}
<stmtlist> -> <stmt>
<stmtlist> -> <stmtlist> <stmt>

# Expressions
<expr> -> <id>                       # Identifier
<expr> -> <num>                      # Number
<expr> -> <expr> <optr> <expr>       # Binary expression
```

## Tokens

1. Keywords => `if`, `while`
2. Symbols => `;`, `{`, `}`, `(`, `)`, `=`
3. Operators (optr) =>  { >=, <=, ==, >, <, +, -, *, / }
4. Identifiers (id) =>  any legal identifier in most programming languages, such as x, y, Xy, y_1, z2, etc.
5. Numbers (num) =>  any real number, such as 8, -8, +9, 9., -9., +10.5, 3.14159, etc.

## Important properties of the language

1. Arbitrary nesting
   - if inside while
   - while inside if
   - blocks inside blocks

2. Statement lists should become a flat list
   - { a=1; b=2; c=3; }
   - stored as a single python list -> [ stmt1, stmt2 ]

3. Expressions are recursive and right-associative and should build right-nested trees
   - a + b + c + d
   - They should build right-nested trees -> a + (b + (c + d))

4. Operator precedence must be enforced
   - `*` and `/` have higher precedence than `+` and `-`
   - Comparison operators (>, <, ==, etc.) are lower precedence

5. Numbers include optional leading + or -
   handled in lexer

6. Everything is recursive
   - stmt contains stmt
   - expr contains expr

7. Output is ONLY a parse tree
   - no execution
   - no evaluation
   - no symbol table
