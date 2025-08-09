class Subscriber:
    def __init__(self, name):
        self.name = name
    
    def update(self, data: dict):
        print(f"Подписчик {self.name} получил уведомление: {data["type"]} id {data["id"]}")


class Publisher:
    def __init__(self):
        self.subscribers = []
        
    def subscribe(self, obj: Subscriber):
        self.subscribers.append(obj)
        
    def unsubscribe(self, obj: Subscriber):
        self.subscribers.remove(obj)
        
    def notify(self, data: dict):
        for sub in self.subscribers:
            sub.update(data)
            
            
        
        
order = Publisher()


kitchen = Subscriber("Кухня")
count = Subscriber("Бухгалтерия")

order.subscribe(kitchen)
order.subscribe(count)

order.notify({"type": "заказ", "id": "001", "phone": "8-800-555-35-35"})
order.notify({"type": "заказ", "id": "002", "phone": "8-899-445-35-35"})