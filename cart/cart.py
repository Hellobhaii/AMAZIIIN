from item.models import Item

class Cart():
    def __init__(self, request):
        self.session = request.session
        
        cart = self.session.get('session_key')
        
        if 'session_key' not in request.session:
            cart = self.session['session_key']= {}
            
        self.cart = cart
        
        
        
    def add(self, item, quantity):
        item_id = str(item.id)
        item_qty = str(quantity)
        # logic
        if item_id in self.cart:
            pass
        else:
            self.cart[item_id] = int(item_qty)
            
        self.session.modified = True 
        
    def cart_total(self):
        item_ids = self.cart.keys()
        items = Item.objects.filter(id__in = item_ids)
        quantities = self.cart
        total = 0
        for key, value in quantities.items():
            key = int(key)
            for item in items:
                if item.id == key:
                    total += item.price * value
        return total
    
    
    def __len__(self): 
        return len(self.cart)
    
    
    
    def get_items(self):
        item_ids =self.cart.keys()
        items = Item.objects.filter(id__in=item_ids)
        
        return items
    
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    
    def update(self, item, quantity):
        item_id = str(item)
        item_qty = int(quantity)
        
        ourcart= self.cart
        ourcart [item_id] = item_qty
        self.session.modified = True
        
        thing = self.cart
        return thing
    
    def delete(self, item):
        item_id = str(item)
        if item_id in self.cart:
            del self.cart[item_id]
            
        self.session.modified = True
        