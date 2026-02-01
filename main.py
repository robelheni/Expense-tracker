from fastapi import FastAPI, Depends

#lest's us create models-blueprints for our data
from pydantic import BaseModel 

from sqlalchemy.orm import Session

#impporting our databse setup
from database import SessionLocal, engine, Base, ExpenseDB

#creating an instance of the FastAPI- this is the webb app
app = FastAPI()


#Pydantic model (for API requests/responses)
class Expense(BaseModel):
    description: str
    amount: float

#creates an new database session and lends it to someone and closes it afterwards
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

#depends - Hey FastAPI, before running this function, please get me a database session using get_db()
@app.post("/expenses")
def add_expense(expense:Expense, db: SessionLocal = Depends(get_db)):
    db_expense = ExpenseDB(
        description = expense.description,
        amount = expense.amount
    )

    db.add(db_expense)

    db.commit()

    #this is how it gives the expenses an id
    db.refresh(db_expense)

    return {
    "message": "Expense added successfully",
    "expense": {
        "id": db_expense.id,
        "description": db_expense.description,
        "amount": db_expense.amount
    }
}
    

@app.get("/expenses")
def get_expenses(db: Session = Depends(get_db)):


    expenses = db.query(ExpenseDB).all()
    return{"expenses": expenses}

@app.get("/expenses/total")
def get_total(db: Session = Depends(get_db)):
    expenses = db.query(ExpenseDB).all()
    total=sum(expense.amount for expense in expenses)
    return {"total": total}