import names
import random

from data.pessoa import Pessoa
from config import *

while True:
    for i in range(1, 10000):
        gen_name = names.get_full_name()
        gen_email = gen_name.strip() + '@.gmail.com'
        gen_phone = '9'
        for i in range(1,7):
            gen_phone += str(random.randint(1,9))
        db.session.add(Pessoa(nome = gen_name, email = gen_email, telefone = gen_phone))
    print('Commiting 10000 records')
    db.session.commit()
    print('Finished commiting 10000 records')