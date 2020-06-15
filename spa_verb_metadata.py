
TENSES = {
    'infinitive' : ('Infinitivo', 'Infinitivo Infinitivo'),
    'present perfect' : ('Participo', 'Participo Participo'),
    'gerund' : ('Gerundio', 'Gerundio Gerondio'),
    'present' : ('Indicativo', 'Indicativo presente'),
    'preterite' : ('Indicativo', 'Indicativo pretérito perfecto simple'),
    'imperfect' : ('Indicativo', 'Indicativo pretérito imperfecto'),
    'future' : ('Indicativo', 'Indicativo futuro'),
    'conditional' : ('Condicional', 'Condicional Condicional'),
    'present subjunctive' : ('Subjuntivo', 'Subjuntivo presente'),
    'imperfect subjunctive' : ('Subjuntivo', 'Subjuntivo pretérito imperfecto 1'),
    'imperative' : ('Imperativo', 'Imperativo Afirmativo')
}

SUBJECTS = {
    '1s' : ['yo'],
    '2s' : ['tú'],
    '3s' : ['él', 'ella', 'usted', 'María', 'Juan', 'Santiago', 'Sofía', 'José', 'Isabella'],
    '1p' : ['nosotros', 'Lucia y yo', 'Juan y yo', 'Maria y yo', 'José y yo'],
    '2p' : ['vosotros'],
    '3p' : ['ellos', 'ellas', 'ustedes', 'Isabella y Diego', 'Juan y Maria', 'Santiago y Sofía']
}

IMPERATIVE_SUBJECTS = {
    '2s' : 'tú',
    '3s' : 'usted',
    '1p' : 'nosotros',
    '2p' : 'vosotros',
    '3p' : 'ustedes'
}

PERSPECTIVES = {
    '1s' : 'yo',
    '2s' : 'tú',
    '3s' : 'él/ella/usted',
    '1p' : 'nosotros',
    '2p' : 'vosotros',
    '3p' : 'ellos/ellas/ustedes'
}

SYMBOLS = {
    'present perfect' : '<-',
    'gerund' : '...',
    'present' : '-',
    'preterite' : '↓',
    'imperfect' : '←',
    'future' : '→',
    'conditional' : '?',
    'present subjunctive' : '~',
    'imperfect subjunctive' : '↜',
    'imperative' : '!'
}

SENTENCES = {
    'present perfect' : 'Recientemente',
    'gerund' : 'Ahora mismo',
    'present' : 'En general',
    'preterite' : 'En ese momento',
    'imperfect' : 'Era bueno,',
    'future' : 'En el futuro',
    'conditional' : 'En ese caso',
    'present subjunctive' : 'Es bueno que',
    'imperfect subjunctive' : 'Era bueno que',
    'imperative' : None
}

INCORRECTLY_CONJUGATED = [
    'parecer',
    'esparcir',
    'extinguir'
]

