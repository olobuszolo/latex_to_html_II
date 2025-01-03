from parser import parser

# def latex_to_html(latex_expr):
#     try:
#         html = parser.parse(latex_expr)
#         return html
#     except Exception as e:
#         print(f"Error during parsing: {e}")
#         return None


def latex_to_html(latex_expr):
    try:
        html = parser.parse(latex_expr)
        if html:
            html = html.replace(r"\\", "<br>")
        return html
    except Exception as e:
        print(f"Error during parsing: {e}")
        return None