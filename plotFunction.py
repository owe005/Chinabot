from library import *

replacements = {
    'sin' : 'np.sin',
    'cos' : 'np.cos',
    'exp': 'np.exp',
    'sqrt': 'np.sqrt',
    '^': '**',
    'log': 'np.log10',
    'tan': 'np.tan',
    'ln': 'np.log',
    'e': 'np.e',
    'pi': 'np.pi',
}

allowed_words = [
    'x',
    'sin',
    'cos',
    'sqrt',
    'exp',
    'log',
    'tan',
    'ln',
    'e',
    'pi'
]

def string2func(string):
    ''' evaluates the string and returns a function of x '''
    # find all words and check if all are allowed:
    for word in re.findall('[a-zA-Z_]+', string):
        if word not in allowed_words:
            raise ValueError(
                '"{}" is forbidden to use in math expression'.format(word)
            )

    for old, new in replacements.items():
        string = string.replace(old, new)

    def func(x):
        return eval(string)

    return func