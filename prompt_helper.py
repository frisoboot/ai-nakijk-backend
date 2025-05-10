def build_prompt(vraag, modelantwoord, studentantwoord):
    return f"""
Beoordeel onderstaand antwoord op de gegeven open vraag.

Vraag:
{vraag}

Modelantwoord:
{modelantwoord}

Antwoord student:
{studentantwoord}

Beoordeel dit antwoord met een score van 0 t/m 1 (bijv. 0.7). Geef ook 1 korte feedbackregel.
Antwoord in het volgende format:
Score: [score]
Feedback: [feedback]
"""