from typing import Optional

from sqlalchemy.orm import Session

from entities.users import User
from repositories.user import IUserRepository
from repositories.user import UserRepository


class TestUserRepository:
    def test_find_by_id_if_user_is_exists(self, session: Session) -> None:
        # Arrange
        expected: User = User(1, 'Test', 'testmail@test.mail.com')
        session.add(expected)
        session.commit()
        repository: IUserRepository = UserRepository(session)

        # Act
        actual: Optional[User] = repository.find_by_id(1)
        session.commit()

        # Assert
        assert actual.user_id == expected.user_id
        assert actual.username == expected.username
        assert actual.email == expected.email

    def test_find_by_id_if_user_doesnt_exists(self, session: Session) -> None:
        # Arrange
        repository: IUserRepository = UserRepository(session)

        # Act
        actual: Optional[User] = repository.find_by_id(999)
        session.commit()

        # Assert
        assert actual is None

    def test_add_user(self, session: Session) -> None:
        # Arrange
        expected: User = User(15, 'Hello, World!', 'hello@world.ua')
        repository: IUserRepository = UserRepository(session)

        # Act
        repository.add(expected)
        session.commit()

        actual: Optional[User] = session.query(User).get(15)
        session.commit()

        # Assert
        assert actual.user_id == expected.user_id
        assert actual.username == expected.username
        assert actual.email == expected.email

    def test_remove_user(self, session: Session) -> None:
        # Arrange
        user: User = User(9, 'Someone', 'someone@gmail.com')
        session.add(user)
        session.commit()
        repository: IUserRepository = UserRepository(session)

        # Act
        repository.remove(user)
        session.commit()

        actual: Optional[User] = session.query(User).get(9)
        session.commit()

        # Assert
        assert actual is None
