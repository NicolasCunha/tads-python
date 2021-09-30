from config import *

class Pessoa(db.Model):
    # atributtes
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))

    # str override
    def __str__(self):
        return str(self.id) + ", " + self.nome + ", " + self.email + ", " + self.telefone

    # json serialize
    def to_json(self):
        return {
            'nome' : self.nome,
            'email' : self.email,
            'telefone' : self.telefone
            }
