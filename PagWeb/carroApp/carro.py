
class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.request.session.get('carro')
        if not carro:
            carro = self.session['carro'] = {}
        self.carro = carro
    
    def saveCart(self):
        self.session['carro'] = self.carro
        self.session.modified = True
    
    def emptyCart(self):
        carro = self.session['carro'] = {}
        self.session.modified = True
    
    def addProduct(self, product):
        prod = str(product.id)
        if self.carro == {} or not prod in self.carro:
            self.carro[product.id] = {
                'product_id': product.id,
                'product_name': product.name,
                'product_price': float(product.price),
                'product_cant': 1,
                'product_img': product.image.url
            }
        else:
            self.carro[prod]['product_cant'] += 1 
            self.carro[prod]['product_price'] += product.price
        self.saveCart()
        
    def subProduct(self, product):
        prod = str(product.id)
        self.carro[prod]['product_cant'] -= 1
        self.carro[prod]['product_price'] -= product.price
        
        if self.carro[prod]['product_cant'] < 1:
            self.delProduct(product)      
        self.saveCart()
    
    def delProduct(self, product):
        if str(product.id) in self.carro:
            del self.carro[str(product.id)]
            self.saveCart()
