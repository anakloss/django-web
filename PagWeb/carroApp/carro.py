

class Cart:
    def __init__(self, req):
        self.request = req
        self.session = req.session
        carro = self.req.session.get('carro')
        if not carro:
            carro = self.session('carro')
        else:
            self.carro = carro
    
    def saveCart(self):
        self.session['carro'] = self.carro
        self.session.modified = True
    
    def emptyCart(self):
        carro = self.session['carro'] = {}
        self.session.modified = True
    
    def addProduct(self, product):
        if str(product.id) is not self.carro.keys():
            self.carro[product.id] = {
                'product_id': product.id,
                'product_name': product.name,
                'product_price': str(product.price),
                'product_cant': 1,
                'product_img': product.image.url
            }
        else:
            self.carro[product.id].product_cant += 1 
            # for key, value in self.carro.items():
            #     if key == str(product.id):
            #         value['product_cant'] += 1
            #         break
        self.saveCart()
        
    def subProduct(self, product):
        self.carro[product.id].product_cant -= 1 
        if self.carro[product.id].product_cant < 1:
            self.delProduct(product)
        # for key, value in self.carro.items():
        #     if key == str(product.id):
        #         value['product_cant'] -= 1
        #         if value['product_cant'] < 1:
        #             self.delProduct(product)
        #         break        
        self.saveCart()
    
    def delProduct(self, product):
        if str(product.id) in self.carro:
            del self.carro[str(product.id)]
            self.saveCart()
