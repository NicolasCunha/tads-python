import names
import random

from data.pessoa import Pessoa
from config import *

db.create_all()

for i in range(1, 101):
    gen_name = names.get_full_name()
    gen_email = gen_name.strip() + '@.gmail.com'
    gen_phone = '9'
    for i in range(1,7):
        gen_phone += str(random.randint(1,9))
    db.session.add(Pessoa(nome = gen_name, email = gen_email, telefone = gen_phone))

db.session.commit()
