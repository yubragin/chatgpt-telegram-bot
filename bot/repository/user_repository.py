from typing import List, Optional

from sqlalchemy.orm import Session

from bot.init_sql import session
from bot.repository.model.user import User


class UserRepository:
    def __init__(self, session_arg: Session):
        self.session = session_arg

    def add_user(self, user_id: int, role) -> User:
        new_user = User(role=role, tg_user_id=user_id)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def get_user(self, user_id) -> Optional[User]:
        return self.session.query(User).filter(User.tg_user_id == user_id).first()

    def get_admins(self) -> List[User]:
        return self.session.query(User).filter(User.role == 'ADMIN').all()

    def list_users(self) -> List[User]:
        return self.session.query(User).all()

    def delete_user(self, user_id) -> bool:
        user = self.get_user(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False

    def update_user_role(self, user_id, new_role) -> Optional[User]:
        user = self.get_user(user_id)
        if user:
            user.role = new_role
            self.session.commit()
            return user
        return None


user_repository = UserRepository(session_arg=session)

