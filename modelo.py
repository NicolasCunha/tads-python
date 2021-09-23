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

# test Pessoa class
if __name__ == '__main__':
    # delete dbfile if exists
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
    
    # create db tables
    db.create_all()

    # create Pessoa instances
    p1 = Pessoa(nome = 'João da Silva', email = 'emaildojoao@gmail.com', telefone = '47 3355-6677')
    p2 = Pessoa(nome = 'Maria da Silva', email = 'emaildamaria@gmail.com', telefone = '47 2244-8899')

    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()
    
    # Print values
    print(p1)
    print(p2)