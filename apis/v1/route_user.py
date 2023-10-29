from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from apis.v1.route_login import get_current_user
from apis.v1.route_login import oauth2_scheme
from db.models.expired_token import ExpiredToken
from db.repository.user import create_new_user
from db.session import get_db
from schemas.user import ShowUser
from schemas.user import UserCreate


router = APIRouter()


@router.post("/register", response_model=ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user


@router.get("/logout")
async def logout(
    token: str = Depends(oauth2_scheme),
    user=Depends(get_current_user),
    db: Session = Depends(get_db),
):
    expired_token = ExpiredToken(access_token=token)
    db.add(expired_token)
    db.commit()
    db.refresh(expired_token)

    return RedirectResponse(url="/")
