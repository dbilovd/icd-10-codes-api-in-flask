import factory
from faker import Faker
from app.models import db
from app.models.code import Code

fake = Faker()


class CodeFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Code
        sqlalchemy_session = db.session

    code = factory.Sequence(
        lambda n: fake.bothify(text='?###', letters='ABCD'))
    title = factory.Sequence(lambda n: fake.sentence())
