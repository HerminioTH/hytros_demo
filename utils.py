
def fid(type, name):
    id = {"tab": type, "name": name}
    return id

def gid(type, name, i):
    id = {"tab": type, "name": name, "i": i}
    return id

def bid(tab, barrier):
    id = {"tab": tab, "barrier": barrier}
    return id

def rid(tab, retrievable):
    id = {"tab": tab, "retrievable": retrievable}
    return id

def qid(tab, question):
    id = {"tab": tab, "question": question}
    return id