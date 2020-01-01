from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class User(Base):
    __tablename__='user'
    id = Column(String(20),primary_key=True)
    name = Column(String(20))

engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/py_test')
DBSession=sessionmaker(bind=engine)

def main():
    session=DBSession()
    new_user=User(id='1',name='kiki')
    session.add(new_user)
    session.commit()
    session.close()

    sessionQ=DBSession()
    user=sessionQ.query(User).filter(User.id=='1').one()
    print('type:', type(user))
    print('name:', user.name)
    sessionQ.close()

if __name__ == '__main__':
    main()
