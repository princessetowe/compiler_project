class RetentionTable:
    def __init__(self):
        self.tokens = []

    def add_token(self, token):
        self.tokens.append(token)

    def display(self):
        print("Retention Table:")
        for token in self.tokens:
            print(token)
