# 9-11 Imported Admin
# Note that this below takes everything from the user_admin_module and print in terminal as well.

from user_admin_module import Admin

print("\t9-11 Imported admin\n")
admin_user = Admin("liam", "neesam", 35, "pretoria", "pilot")

admin_user.describe_user()
admin_user.show_privileges()

print("-------------------------------------------")