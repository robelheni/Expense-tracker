from fastapi import FastAPI, Depends

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
#lest's us create models-blueprints for our data
from pydantic import BaseModel 

from sqlalchemy.orm import Session

#impporting our databse setup
from database import SessionLocal, engine, Base, ExpenseDB

#creating an instance of the FastAPI- this is the webb app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

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
    return FileResponse('static/index.html')

#depends - Hey FastAPI, before running this function, please get me a database session using get_db()
@app.post("/expenses")
def add_expense(expense:Expense, db: SessionLocal = Depends(get_db)):
    #creating a row in the database
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

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id:int, db:Session = Depends(get_db)):

    expense = db.query(ExpenseDB).filter(ExpenseDB.id == expense_id).first()

    if not expense:
        return{"error":"Expense not found"}

    db.delete(expense)
    db.commit()

    return{"message": "Expense deleted successfully"}



    #then rrun http://127.0.0.1:8000