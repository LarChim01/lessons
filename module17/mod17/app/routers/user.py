from fastapi import APIRouter, Depends, status, HTTPException
from app.backend.db import get_db
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from slugify import slugify
from app.models import *
from app.models.user import User
from app.models.task import Task
from sqlalchemy import insert, select, update, delete
from app.schemas import CreateUser, UpdateUser

router = APIRouter(prefix="/user", tags=['user'])


@router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()

    return users


@router.get("/{user_id}")
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is not None:
        return user

    raise HTTPException(
        status_code=404,
        detail="User was not found"
    )


@router.post("/create")
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    db.execute(insert(User).values(username=create_user.username,
                                   firstname=create_user.firstname,
                                   lastname=create_user.lastname,
                                   age=create_user.age,
                                   slug=slugify(create_user.username)))

    db.commit()

    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }





@router.put("/update")
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, update_user: UpdateUser):
    user = db.scalar(select(User).where(User.id == user_id))

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no user found'
        )
    db.execute(update(User).where(User.id == user_id).values(username=update_user.username,
                                                             firstname=update_user.firstname,
                                                             lastname=update_user.lastname,
                                                             age=update_user.age,
                                                             slug=slugify(update_user.username)))

@router.delete("/delete")
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no user found'
        )
    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Category delete is successful'
    }
