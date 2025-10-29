# 9-12 Multiple Modules
# Imports from the documents e_admin and b_user.

from e_admin import Admin
print("\t----From e_admin----")
from b_user import User
print("-------------------------------------------")
print("\t----From b_user----")

admin_user = Admin("denzil", "de wet", 35, "cape town", "system administrator")

admin_user.describe_user()
admin_user.show_privileges()

print("-------------------------------------------")

admin_user1 = User("jaco", "schalkwyk", 100, "USA", "pilot")

admin_user.describe_user()
admin_user.show_privileges()