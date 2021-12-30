# ORM:Object Relational Mapping 对象关系映射
# 即在关系型数据库和对象之间作一个映射，这样，我们在具体操作数据库时，就不需要和SQL语句打交道，直接操作对象就好了
# 通过sqlalchemy模块可以实现

from re import T
from sqlalchemy import Column, create_engine,String,Integer, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class math(Base):
    __tablename__ = 'math'
    id = Column(String(20), primary_key=True)
    name = Column(String(50))
    ms = Column(Integer)
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/score')
DBsession = sessionmaker(bind=engine)
session = DBsession()
danco = math(id='001', name='danco', ms=99)
alex = math(id='002', name='alex', ms=93)
kudo = math(id='003', name='kudo', ms=92)
session.add(danco)
session.add(alex)
session.add(kudo)
session.commit()
session.close()