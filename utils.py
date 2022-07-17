"""
Получаем все записи из таблицы
"""
from config import db


def get_all(model):
    result = []
    for row in model.query.all():
        result.append(row.to_dict())

    return result


"""
Получаем записи по id
"""


def get_by_id(models, pid):
    row = models.query.get(pid)
    if row is None:
        return "data not found"
    return row.to_dict()


# def union_all(model1, model2):
#     data = db.session.query(model1, model2).join(model2).all()
#     result = []
#     for row in data:
#         res = row[0].to_dict()
#         res.update(row[1].to_dict())
#
#         result.append(res)
#
#     return result

"""
Получаем записи по id из связанных таблиц
"""


def union_all_by_id(model1, model2, pid):
    data = db.session.query(model1, model2).join(model2).filter(model1.id == pid).all()[0]

    result = data[0].to_dict()
    result.update(data[1].to_dict())
    return result


"""
Обновляем данные в таблицах
"""


# def update_user(model, user_id, values):
#     data = db.session.query(model).get(user_id)
#     data.id = values.get("id")
#     data.first_name = values.get("first_name")
#     data.last_name = values.get("last_name")
#     data.age = values.get("age")
#     data.email = values.get("email")
#     data.role = values.get("role")
#     data.phone = values.get("phone")
#
#     db.session.commit()


def update_user_uni(model, user_id, values):
    db.session.query(model).filter(model.id == user_id).update(values)
    db.session.commit()


"""
удаляем данные из таблицы
"""


def delete_user_uni(model, user_id):
    try:
        db.session.query(model).filter(model.id == user_id).delete()
        db.session.commit()
    except Exception as e:
        print(e)
