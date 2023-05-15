
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.next_token()

    def next_token(self):
        if len(self.tokens) > 0:
            self.current_token = self.tokens.pop(0)
        else:
            self.current_token = None

    def error(self):
        raise Exception('Invalid syntax')

    def parse(self):
        self.program()

    def program(self):
        if self.current_token == None:
            return
        else:
            self.top_level_form()
            self.program()

    def top_level_form(self):
        if self.current_token == 'LEFTPAR':
            self.next_token()
            self.second_level_form()
            if self.current_token == 'RIGHTPAR':
                self.next_token()
            else:
                self.error()
        else:
            self.error()

    def second_level_form(self):
        if self.current_token == 'LEFTPAR':
            self.next_token()
            self.fun_call()
            if self.current_token == 'RIGHTPAR':
                self.next_token()
            else:
                self.error()
        else:
            self.definition()