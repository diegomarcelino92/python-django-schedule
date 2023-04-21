from django_seed import Seed

from contacts.models import Category, Contact

seeder = Seed.seeder()

seeder.add_entity(Category, 5)

seeder.add_entity(Contact, 10, {
    'telephone': lambda _: seeder.fake.cellphone()
})

seeder.execute()
