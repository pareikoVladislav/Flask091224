# from typing import Any
#
# from sqlalchemy.exc import IntegrityError, DataError
# from sqlalchemy.orm import Session
#
# from sqlalchemy_lessons import engine
# from sqlalchemy_lessons.db_connector import DBConnector
# from sqlalchemy_lessons.social_blogs_models import Role, User, News, Comment
# from sqlalchemy_lessons.social_blogs_schemas import UserResponseSchema, UserCreateSchema, UserUpdateSchema
#
# from datetime import datetime, timezone
import datetime
import json

from sqlalchemy import or_

# def create_user(session: Session, raw_data: dict[str, Any]) -> UserResponseSchema:
#     try:
#         validated_data = UserCreateSchema.model_validate(raw_data)
#
#         user = User(**validated_data.model_dump())
#
#         session.add(user)
#         session.flush()
#         session.refresh(user)
#         session.commit()
#
#         return UserResponseSchema.model_validate(user)
#     except ValueError as err:
#         raise err
#     except (IntegrityError, DataError) as db_err:
#         session.rollback()
#         raise db_err
#
#
# def get_user_by_id(session: Session, user_id: int) -> UserResponseSchema:
#     user = session.get(User, user_id) # NEW
#     # user = session.query(User).get(user_id) # OLD
#
#     if not user:
#         raise ValueError("User not found")
#
#     return UserResponseSchema.model_validate(user)
#
#
# def update_user(session: Session, user_id: int, raw_data: dict[str, Any]) -> UserResponseSchema:
#     user = session.get(User, user_id) # NEW
#     if not user:
#         raise ValueError("User not found")
#
#     validated_data = UserUpdateSchema.model_validate(raw_data)
#
#     for field, value in validated_data.model_dump(exclude_unset=True).items():
#         setattr(user, field, value)
#
#     session.flush()
#     session.refresh(user)
#     session.commit()
#
#     return UserResponseSchema.model_validate(user)
#
#
# def delete_user(session: Session, user_id: int) -> dict[str, str]:
#     user = session.get(User, user_id) # NEW
#
#     if not user:
#         raise ValueError("User not found")
#
#     session.delete(user)
#     session.commit()
#
#     return {"message": "User was deleted successfully"}


# with DBConnector(engine=engine) as session:
    # try:
    #     updated_user = update_user(
    #         session=session,
    #         user_id=27,
    #         raw_data={
    #             "last_name": "UPDATED LASTNAME",
    #             "rating": 5.8,
    #             "updated_at": datetime.now(tz=timezone.utc)
    #         }
    #     )
    #
    #     print("🟢 User found and updated!")
    #     print(updated_user.model_dump_json(indent=3))
    # except ValueError as err:
    #     print(err)

    # try:
    #     user = get_user_by_id(session=session, user_id=1)
    #
    #     print("🟢 User found!")
    #     print(user.model_dump_json(indent=2))
    # except ValueError as err:
    #     print(err)

    # data = {
    #     "first_name": "Alex",
    #     "last_name": "Grey",
    #     "email": "a.grey@gmail.com",
    #     "password": "MySecurePassword",
    #     "repeat_password": "MySecurePassword",
    #     "phone": "+1 255 777 9999",
    #     "role_id": 3
    # }
    #
    # try:
    #     new_user = create_user(session=session, raw_data=data)
    #
    #     print("🟢 User Created!")
    #     print(new_user.model_dump_json(indent=4))
    # except Exception as err:
    #     print(f"Error: {err}")


from sqlalchemy_lessons import engine
from sqlalchemy_lessons.db_connector import DBConnector
from sqlalchemy_lessons.social_blogs_models import Role, User, News, Comment
from sqlalchemy import desc, or_, and_, not_, func, text
from sqlalchemy.orm import aliased, joinedload, contains_eager

from sqlalchemy_lessons.social_blogs_schemas import UserWithNewsSchema

with DBConnector(engine=engine) as session:
    # users = session.query(User) # SELECT * from users;
    #
    # print("=" * 100)
    # print(users)
    # print("=" * 100)

    # for user in users.all():
    #     print(user.email, user.role_id, user.rating)

    # us = users.first()
    #
    # print(us.email, us.role_id, us.rating)


    # user = session.query(User).filter(User.role_id == 18).one()
    #
    # print(user)

    # user = session.query(User).filter(User.role_id == 1).one_or_none()
    #
    # if not user:
    #     ...
    #
    # print(user)

    # moderator_users = session.query(User).filter_by(role_id=2).all()
    #
    # for user in moderator_users:
    #     print(user.last_name, user.role_id, user.role.name)

    # moderator_users = session.query(User).filter(
    #     User.last_name.like('W%')
    # ).all()
    #
    # for user in moderator_users:
    #     print(user.last_name, user.rating, user.role.name)


    # users = session.query(User).filter(
    #     User.rating.between(5, 8)
    # ).all()
    #
    # for user in users:
    #     print(user.last_name, user.rating, user.role.name)


    # req_names = {'Mcneil', 'Randolph', 'Miller'}
    #
    # users = session.query(User).filter(
    #     User.last_name.in_(req_names)
    # ).all()
    #
    # for user in users:
    #     print(user.last_name, user.rating, user.role.name)

    # users = session.query(
    #     User.role_id,
    #     User.rating,
    #     User.created_at,
    # ).filter(
    #     or_(
    #         (
    #             and_(
    #                 User.role_id == 3,
    #                 User.rating > 6
    #             )
    #         ),
    #         (User.created_at > datetime.datetime.now())
    #     )
    # ).order_by(desc(User.rating), User.created_at).all()
    #
    # for user in users:
    #     print(user.role_id, user.rating, user.created_at)

    # total_rating = session.query(
    #     User.role_id,
    #     func.sum(User.rating)
    # ).group_by(User.role_id).all()
    # print(total_rating)

    # avg_rating = session.query(func.avg(User.rating)).scalar()

    # avg_rating = 50
    # print(f"{avg_rating=}")

    # users = session.query(
    #     User
    # ).filter(User.rating > avg_rating).all()
    #
    # print(users)

    # moderated_news_count = session.query(
    #     func.count(News.id)
    # ).filter(News.moderated == 1).scalar()
    #
    # print(f"{moderated_news_count=}")

    # us: User = aliased(element=User, name='us')
    # us2: User = aliased(element=User, name='us2')

    # users_by_role = session.query(
    #     us.role_id,
    #     func.count(us.id).label("count_of_users")
    # ).group_by(us.role_id).all()

    # users_by_role = session.query(
    #     us.role_id
    # ).filter(us.manager_id == us2.id)

    # for user in users_by_role:
    #     print(user.role_id, user.count_of_users)

    # stmt = text(
    #     """
    #     SELECT * FROM users;
    #     """
    # )
    #
    # session.execute(stmt)

    # authors = session.query(
    #     User.role_id,
    #     User.rating,
    #     func.count(User.id).label("count_of_users")
    # ).group_by(User.role_id).having(User.rating > 5).all()
    #
    #
    # for user in authors:
    #     print(f"{user.role_id=}  {user.rating=}  {user.count_of_users}")


    # users_with_news_more_than_3 = session.query(
    #     News.author_id,
    #     func.count(News.id).label('count_of_news')
    # ).group_by(News.author_id).having(func.count(News.id) > 4).all()
    #
    # for n in users_with_news_more_than_3:
    #     print(f"{n.author_id=}  {n.count_of_news=}")


    # avg_rating_subq = session.query(
    #     func.avg(User.rating).label('avg_rating')
    # ).scalar_subquery()
    #
    # core_query = session.query(
    #     User.email,
    #     User.rating
    # ).filter(User.rating > avg_rating_subq).all()
    #
    # for u in core_query:
    #     print(f"{u.email}     {u.rating}")
    #
    #
    # req_role = session.query(
    #     Role.id
    # ).filter(Role.name == 'moderator').scalar_subquery()
    #
    #
    # only_moderators = session.query(
    #     User.role_id,
    #     User.email
    # ).filter(User.role_id == req_role).all()
    #
    # for u in only_moderators:
    #     print(f"{u.role_id}     {u.email}")


    # join
    # selecinjoin
    # subqueryload
    # joinedload


    # only_moderators = session.query(
    #     User.last_name,
    #     User.rating,
    #     Role.name.label('role_name')
    # ).join(User.role).filter(
    # # ).join(Role, Role.id == User.role_id).filter(
    #     Role.name == 'moderator'
    # ).all()
    #
    # for u in only_moderators:
    #     print(f"{u.last_name}     {u.rating}     {u.role_name}")
    #

    # outerjoin

    # authors_and_news = session.query(
    #     User.email,
    #     User.rating,
    #     Role.name.label('role_name'),
    #     News.title.label('news_title'),
    #     News.moderated.label('news_moderated')
    # ).outerjoin(Role, Role.id == User.role_id).outerjoin(
    #     User.news
    #     # News, News.author_id == User.id
    # ).filter(
    #     Role.name == 'author'
    # )

    # all() - []
    # one() - {} | ERROR
    # one_or_none() - {} | None | ERROR
    # first() - {} | None
    # scalar() - value

    # for u in authors_and_news:
    #     print(f"{u.email}     {u.rating}     {u.role_name}     {u.news_title}     {u.news_moderated}")



    # users_with_news = session.query(User).all()

    users_with_news = session.query(User).options(
        joinedload(User.news)
    ).all()


    res = [
        UserWithNewsSchema.model_validate(user).model_dump(mode='json')
        for user in users_with_news
    ]


    print(json.dumps(res, indent=4))

# Только подгрузка связанных объектов (без фильтрации):
#     joinedload(Model.field)
#
# Фильтрация по связанным объектам (с relationship):
#     join(Model.field) или outerjoin(Model.field) + можно также добавить .options(joinedload(...)) для загрузки.
#
# Фильтрация без relationship:
#     join(Model) или outerjoin(Model) с явным условием типа join(Model, Main.id == Model.id).
#
#
# selectinload() и subqueryload() полезны, когда много связанных объектов.





# Если вам вдруг будет нужно самим делать джоин в построении запроса и понадобится, чтобы
# результат амтоматом распознался как вложенный объект - можно использовать так же contains_eager()
# Это ручная подсказка SQLAlchemy, что вы сами сделали JOIN и SQLAlchemy
    # # не нужно делать дополнительный запрос для подгрузки связанных данных.


    from sqlalchemy.orm import contains_eager
    from datetime import datetime
    import json

    users_and_news = (
        session.query(User)
        .join(User.role)
        .join(User.news)
        .filter(Role.name == "author", News.moderated == 1)
        .options(
            # Этим методом вы фактически говорите SQLAlchemy: "используй вот эти данные для поля .related".
            contains_eager(User.news).joinedload(News.comments)
        ).all()
    )

    json_data = [
        {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone": user.phone,
            "role_id": user.role_id,
            "deleted": user.deleted,
            "news": [
                {
                    "id": n.id,
                    "title": n.title,
                    "moderated": n.moderated,
                    "created_at": datetime.strftime(n.created_at, "%Y-%m-%d %H:%M:%S"),
                    "comments": [
                        {
                            "id": c.id,
                            "body": c.body,
                            "deleted": c.deleted,
                            "created_at": datetime.strftime(c.created_at, "%Y-%m-%d %H:%M:%S")
                        }
                        for c in n.comments
                    ]
                }
                for n in user.news
            ],
        }
        for user in users_and_news
    ]

    print(json.dumps(json_data, indent=4))


# 📦 Когда использовать contains_eager
#
#                     Когда	                                                           Почему
# Сам делаешь JOIN и хочешь заполнить relationship	                Иначе поле будет пустым (ORM не знает про join)
# Нужно фильтровать по joined таблице, но сохранить eager	            Только contains_eager позволит связать результат
# Работаешь с aliased() отношениями	                                ORM иначе не поймёт, куда положить результат
#