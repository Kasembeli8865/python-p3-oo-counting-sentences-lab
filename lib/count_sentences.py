class MyString:
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        sentences = self.value.split(r'[.!?]')
        num_sentences = len([sentence for sentence in sentences if sentence.strip()])
        return num_sentences

