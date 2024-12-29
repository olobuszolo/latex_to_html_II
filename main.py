from translator import latex_to_html


def save_to_html_file(html_content, filename="output.html"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("<!DOCTYPE html>\n")
            f.write("<html lang=\"en\">\n")
            f.write("<head><meta charset=\"UTF-8\"><title>Math Expression</title></head>\n")
            f.write("<body><p>")
            f.write(html_content)
            f.write("</p></body>\n")
            f.write("</html>")
        print(f"HTML file saved as {filename}")
    except Exception as e:
        print(f"Error saving HTML file: {e}")

if __name__ == "__main__":
    latex_input = (
        r"\alpha + \beta \cdot \gamma + \delta + \sin(\gamma + 4) + \cos(\beta) \cdot \frac{1}{2} + \tan(1) + \log(10) + \sqrt{9} + "
        r"\pi + "
        r"\int_{0}^{1} \sin(x) + \iint_{0}^{1} \frac{\beta}{\beta} + \iiint_{0}^{1} \cos(x) + \frac{1}{2} + \frac{1}{3} + \frac{\alpha}{4}"
    )
    html_output = latex_to_html(latex_input)
    if html_output:
        save_to_html_file(html_output)
