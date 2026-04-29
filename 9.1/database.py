from sqlalchemy.types import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Products(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    count: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(String(200), nullable=False)