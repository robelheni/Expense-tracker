#import out databse setup
from database import Base, engine

#Create all tables defined in our models
#Base.metadata → holds all the information about your tables (columns, types, constraints)
#create_all() → creates the actual tables in the database
#tells SQLAlchemy which database to create them in
Base.metadata.create_all(bind=engine)

print("tables created succesfully")