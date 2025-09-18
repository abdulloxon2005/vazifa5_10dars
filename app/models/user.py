from sqlalchemy import Integer, String, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


roles_user = Table(
    "roles_user",
    Base.metadata,
    Column("user_id",Integer,ForeignKey("users.id")),
    Column("role_id",Integer,ForeignKey("roles.id"))
)


class Roles:
    pass


class User(Base):
    __tablename__ = "users"

    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    username:Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)

    roles:Mapped[list["Roles"]] = relationship("Role",secondary=roles_user)
class Role(Base):
    __tablename__ = "roles"

    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String)

    users = relationship("User",secondary=roles_user)