from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import create_access_token, create_refresh_token, hash_password, verify_password
from app.models.refresh_token import RefreshToken
from app.models.user import User
from app.schemas.user import TokenResponse, UserCreate, UserLogin, UserOut

router = APIRouter()


@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(user_in: UserCreate, db: Session = Depends(get_db)) -> UserOut:
    existing = db.query(User).filter((User.email == user_in.email) | (User.username == user_in.username)).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    user = User(
        username=user_in.username,
        email=str(user_in.email),
        password_hash=hash_password(user_in.password),
        is_active=True,
        created_at=datetime.utcnow(),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/login", response_model=TokenResponse)
def login(user_in: UserLogin, db: Session = Depends(get_db)) -> TokenResponse:
    user = db.query(User).filter(User.email == str(user_in.email)).first()
    if not user or not verify_password(user_in.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(user.id)
    refresh_token = create_refresh_token(user.id)
    refresh_record = RefreshToken(user_id=user.id, token=refresh_token, expires_at=datetime.utcnow(), revoked=0)
    db.add(refresh_record)
    db.commit()
    return TokenResponse(access_token=access_token, refresh_token=refresh_token)


@router.post("/refresh", response_model=TokenResponse)
def refresh_token(token: str, db: Session = Depends(get_db)) -> TokenResponse:
    refresh_record = db.query(RefreshToken).filter(RefreshToken.token == token).first()
    if not refresh_record or refresh_record.revoked:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    access_token = create_access_token(refresh_record.user_id)
    refresh_token_value = create_refresh_token(refresh_record.user_id)
    refresh_record.token = refresh_token_value
    refresh_record.expires_at = datetime.utcnow()
    db.commit()
    return TokenResponse(access_token=access_token, refresh_token=refresh_token_value)
