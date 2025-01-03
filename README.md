# Konwerter LaTeX na HTML

Projekt służy do konwersji matematycznych wyrażeń zapisanych w LaTeX na format HTML. Wykorzystuje biblioteki `Ply` (lexer i parser) do analizy leksykalnej i składniowej.

---

## Funkcje

- **Lexer (analizator leksykalny)**  
  Rozpoznaje elementy LaTeX, takie jak liczby, operatory, funkcje trygonometryczne i symbole.  
  Tokeny są definiowane w pliku `lexer.py`.

- **Parser (analizator składniowy)**  
  Opisuje gramatykę LaTeX, definiując strukturę poprawnych wyrażeń.  
  Gramatyka jest zaimplementowana w pliku `parser.py` z wykorzystaniem narzędzia `yacc`.

- **Translator (konwerter)**  
  Konwertuje poprawne wyrażenia LaTeX na odpowiadające im wyrażenia HTML.  
  Logika znajduje się w pliku `translator.py`.

- **Aplikacja główna**  
  Interfejs użytkownika umożliwiający przetestowanie działania programu i zapis wyników w pliku HTML.  
  Znajduje się w pliku `main.py`.

---

## Struktura plików

1. **`lexer.py`**  
   Zawiera definicje tokenów i reguły leksykalne, takie jak:
   - `NUMBER` (liczby),
   - `PLUS` (dodawanie),
   - `SIN` (sinus),
   - `SQRT` (pierwiastek).  

   Tokeny pozwalają na rozpoznawanie składników wejściowego wyrażenia.

2. **`parser.py`**  
   Definiuje gramatykę wyrażeń LaTeX przy użyciu narzędzia `yacc`.  
   Przykładowe reguły gramatyczne:
   - `expression -> expression PLUS term`  
   - `term -> term TIMES factor`  
   - `factor -> SQRT LBRACE expression RBRACE`  
   
   Reguły odpowiadają za składnię LaTeX, przekształcając wyrażenia na elementy logiczne.

3. **`translator.py`**  
   Wykorzystuje parser do analizy składniowej i zamienia wyrażenia LaTeX na HTML.  
   Przykład konwersji:  
   - LaTeX: `\alpha + \beta`  
   - HTML: `&alpha; + &beta;`.

4. **`main.py`**  
   Główna aplikacja, w której można:
   - wprowadzić wyrażenie LaTeX,  
   - przetworzyć je na HTML,  
   - zapisać wynik do pliku `output.html`.

5. **`productions.txt`**  
   Zawiera listę wszystkich reguł gramatycznych użytych w parserze.

---

## Jak korzystać z programu
   W pliku **main.py** należy umieścić ciąg sekwencji, które chcemy przetłmaczyć z formy latex do html.
   Należy pamiętać, że umieszczany tekst musi być w formie: **r"tekst..."**
   Jeśli chcemy, aby w pliku html tekst pojawił się w nowej lini, to w miejscu outputu umieszczamy symbol "\\"

### Przykład:
```python
latex_input = (
    r"\alpha + \beta \cdot \gamma  \\ \delta + \sin(\gamma + 4) + \cos(\beta) \cdot \frac{1}{2} + \tan(1) + \log(10) + \sqrt{9} + "
    r"\pi + "
    r"\int \sin(x) + \int \frac{\beta}{\beta} + \int \cos(x) + \frac{1}{2} + \frac{1}{3} + \frac{\alpha}{4} - "
    r"\alpha + 2 \cdot \pi \\"
    r"x + 3 + 4^\alpha"
)

W celu zwiększenia czytelności w latex_input możemy umieszczać pare lini tekstu, jednak dla translatora kluczowe w uzyskaniu nowej lini jako rezulat jest symbol "\\". Bez niego nie uzyskamy nowej lini jako rezultat.
W powyższym przykładzie mamy wynik jako 3 linijki.

Po wykonaniu programu generuje nam się plik **output.html**. Następnie należy go przeciągnąć w okienko ulubionej przeglądarki internetowej i cieszyć się wynikiem działania programu.  
