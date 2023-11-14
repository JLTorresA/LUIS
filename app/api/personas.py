from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models.persona import  Persona
from fastapi import Depends

router = APIRouter()

@router.get("/personas")
async def obtener_personas(db: Session = Depends(get_db)):
    try:
        personas = db.query(Persona).order_by(Persona.dni, Persona.appPaterno).all()
        return personas

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




