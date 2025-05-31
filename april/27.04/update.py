worker = {
    "name": "Иван",
    "age": 25
}

worker1 = {
    "name": "Антон",
    "fname": "Иванов"
}

# worker.update(worker1)
worker |= worker1
print(worker)