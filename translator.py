from parser import parser

def latex_to_html(latex_expr):
    latex_expr = latex_expr.replace("\\", "\\\\")
    try:
        html = parser.parse(latex_expr)
        return html
    except Exception as e:
        print(f"Error during parsing: {e}")
        return None
