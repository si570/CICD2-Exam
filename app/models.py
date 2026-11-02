from sqlalchemy  import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass
class UserDB(Base):
    __tablename__="users"
    id:Mapped[int] = mapped_column(primary_key=True,unique=True, index=True)
    equipment_id:Mapped[int]=mapped_column(Integer, nullable=False)
    borrower_name:Mapped[str]= mapped_column(string(60),nullable=False)
    loan_days:Mapped[int]=mapped_column(Integer(14),nullable=False)
    purpose:Mapped[str]= mapped_column(string(100), unique=True, nullable=False)
    status:Mapped[Integer]=mapped_column(string(7), nullable=False)
    
    


