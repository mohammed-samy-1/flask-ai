
class ToxicResponse:

    def __init__(self, comment_text, toxic=False, severe_toxic=False, obscene=False,
                 threat=False, insult=False, identity_hate=False):
        self.comment_text = comment_text
        self.toxic = toxic
        self.severe_toxic = severe_toxic
        self.obscene = obscene
        self.threat = threat
        self.insult = insult
        self.identity_hate = identity_hate

    def __json__(self):
        return self.__dict__