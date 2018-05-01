class Item(object): 
    def __init__(self, unq_id, name, price, qty):
            self.unq_id = unq_id
            self.product_name = name
            self.price = price
            self.qty = qty
class Cart(object):
    def __init__(self):
        self.content = dict()

    def update(self, item):
        if item.unq_id not in self.content:
            self.content.update({item.unq_id: item})             
            return
        for k, v in self.content.get(item.unq_id).iteritems():
            if k == 'unq_id':
              continue
            elif k == 'qty':
                total_qty = v.qty + item.qty
                if total.qty:
                    v.qty =total_qty
                    continue
                self.remove_item(k)
            else:
                v[k]=item[k]
item1=Item(1, "Ba", 1., 1)
cart=Cart()
cart.update(item1)
print("You have")
