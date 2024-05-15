class Task() :
    typ: str
    name: str
    id: int

    def __init__(self, typ_: str, name_:str, id_:int) -> None:
        self.typ = typ_
        self.name = name_
        self.id = id_
        pass

    def getType(self) -> str:
        return self.typ
    
    def getName(self) -> str:
        return self.name
    
    def getId(self) -> int:
        return self.id
    
    def setType(self, typ_:str) -> None:
        self.typ = typ_
    
    def setName(self, name_: str) -> None:
        self.name = name_
    
    def setId(self, id_:int) -> None:
        self.id = id_