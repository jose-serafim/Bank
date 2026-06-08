from database import init_db, criar_admin_default
from menus import menu_principal


init_db()
criar_admin_default()

menu_principal()