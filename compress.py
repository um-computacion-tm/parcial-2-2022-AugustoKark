class Compress():
    def __init__(self):
        self.dicc = {}
        self.lista=[]
        self.listarep=[]
        self.texto=''
        self.lista2=[]
        self.llaves=[]
        self.valores=[]
       

    def compress(self,text):
        
        separadorespacio=' '
        lista=text.split(separadorespacio)
       
        for i in range(len(lista)):
            if  lista[i] not in self.listarep:
                self.listarep.append(lista[i])
                self.listacontador=int(i)
            else:
                pass

        for j in range(len(self.listarep)):
            self.dicc[self.listarep[j]]=j+1
        
        for i in range(len(lista)):
            self.lista.append(self.dicc[lista[i]])
        return self.lista,self.dicc


                
    
      
    
    def uncompress(self,lista,dicc):

        for pepe in range(len(dicc)):
            self.llaves+=dicc.keys()
      
            self.valores+=list(dicc.values())
        for i in lista:


            self.texto+=(self.llaves[(self.valores.index(i))])
            self.texto+=' '
        self.texto=self.texto[:-1]
        
        
        return self.texto

    
                

        
    





        

        



