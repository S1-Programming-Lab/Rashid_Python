class publisher():
    def__init__(self,pname):
        self.pname=pname
        def display(self):
            print("name:"self.pname)
            class book(publisher):
                def__init(self,pname,bname,title):
                    self.pname=pname
                    self.bname=bname
                    self.title=title
                    def display(self):
                        print("name:"self.pname)
                        print("name:"self.bname)
                        print("title:"self.title)
                        class Python(book):
                            def__init__(self,pname,bname,title,page,price):
                                self.pname=pname
                                self.bname=bname
                                self.title=title
                                self.page=page
                                self.price=price
                                def display(self):
                                    print("name:"self.pname)
                                    print("name:"self.bname)
                                    print("title:"self.title)
                                    print("page",self.page)
                                    print("price",self.price)
                                    n=input("enter publisher:"))
                                    b=input("enter author:")
                                    p=int(input("enter pager:"))
                                    pr=int(input("enter price:"))
                                    obj=python(n,b,t,p,pr)
                                    obj.display()
