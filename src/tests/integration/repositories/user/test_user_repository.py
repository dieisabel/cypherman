from typing import Optional
from typing import List

from sqlalchemy.orm import Session

from entities.users import User
from repositories.user import IUserRepository
from repositories.user import UserRepository


class TestUserRepository:
    def test_find_user_by_id_if_user_is_exists(self, session: Session) -> None:
        # Arrange
        session.query(User).delete()
        expected: User = User(1, 'Test', 'testmail@test.mail.com')
        session.add(expected)
        session.commit()
        repository: IUserRepository = UserRepository(session)

        # Act
        actual: Optional[User] = repository.find_user_by_id(1)
        session.commit()

        # Assert
        assert actual.user_id == expected.user_id
        assert actual.username == expected.username
        assert actual.email == expected.email

    def test_find_user_by_id_if_user_doesnt_exists(self, session: Session) -> None:
        # Arrange
        session.query(User).delete()
        repository: IUserRepository = UserRepository(session)

        # Act
        actual: Optional[User] = repository.find_user_by_id(999)
        session.commit()

        # Assert
        assert actual is None

    def test_find_all_users_if_there_are_users_in_database(self, session: Session):
        # Arrange
        session.query(User).delete()
        user0: User = User(1, 'Valeriy', 'valerich@ukr.net')
        user1: User = User(2, 'Danila', 'danya_pacan@gmail.com')
        user2: User = User(3, 'Kirill', 'kerchan@protonmail.com')
        session.add_all([user0, user1, user2])
        session.commit()
        repository: IUserRepository = UserRepository(session)

        # Act
        users: List[User] = repository.find_all_users()
        session.commit()

        # Assert
        assert users[0].user_id == user0.user_id
        assert users[0].username == user0.username
        assert users[0].email == user0.email

        assert users[1].user_id == user1.user_id
        assert users[1].username == user1.username
        assert users[1].email == user1.email

        assert users[2].user_id == user2.user_id
        assert users[2].username == user2.username
        assert users[2].email == user2.email

    def test_find_all_users_if_there_are_no_users_in_database(self, session: Session):
        # Arrange
        session.query(User).delete()
        session.commit()
        repository: IUserRepository = UserRepository(session)

        # Act
        actual: List[User] = repository.find_all_users()
        session.commit()

        # Assert
        assert not actual

    def test_add_user(self, session: Session) -> None:
        # Arrange
        session.query(User).delete()
        expected: User = User(1, 'Hello, World!', 'hello@world.ua')
        repository: IUserRepository = UserRepository(session)

        # Act
        repository.add_user(expected)
        session.commit()

        actual: Optional[User] = session.query(User).get(1)
        session.commit()

        # Assert
        assert actual.user_id == expected.user_id
        assert actual.username == expected.username
        assert actual.email == expected.email

    def test_remove_user(self, session: Session) -> None:
        # Arrange
        session.query(User).delete()
        user: User = User(1, 'Valera', 'valera@ukr.net')
        session.add(user)
        session.commit()
        repository: IUserRepository = UserRepository(session)

        # Act
        repository.remove_user(user)
        session.commit()

        actual: Optional[User] = session.query(User).get(1)
        session.commit()

        # Assert
        assert actual is None
