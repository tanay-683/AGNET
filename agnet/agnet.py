import reflex as rx
from agnet.pages import login
from agnet.pages import home
app = rx.App()
app.add_page(login.login_page, route="/")
# app.add_page(home.sidebar_item, route="/home")
app.add_page(home.home_page, route="/home")

app._compile()