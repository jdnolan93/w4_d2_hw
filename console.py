import pdb

from models.staff import Staff

import repositories.staff_repository as staff_repository

staff_repository.delete_all()

staff1 = Staff("Jamie Nolan", "30th March", "lions", 5)
staff_repository.save(staff1)

staff2 = Staff("Namie Jolan", "20th April", "tigers", 1)
staff_repository.save(staff2)

staff = Staff("John", "1st April", "fish", 4)
staff_repository.save(staff)

staff_repository.select_all()

pdb.set_trace()