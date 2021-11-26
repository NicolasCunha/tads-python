def str_empty(arg):
    try:
        if arg and arg.strip():
            #is not None AND myString is not empty or blank
            return False
        return True
    except Exception as e:
        return True