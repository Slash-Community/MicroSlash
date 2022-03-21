from Slash.types_ import *


class Users(Table, metaclass=TableMeta):
    useraname = Column(Text, None)
    password = Column(Hidden, None)

    __table__name__ = "users"
