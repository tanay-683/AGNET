# Home Page
import reflex as rx
from agnet.components.input_field import modern_input_field
from agnet.components.sidebar import sidebar_item


@rx.page()
def home_page() -> rx.Component:
    return rx.flex(
        sidebar_item(text="Agnet", icon="home", href="/home"),
        rx.vstack(
            modern_input_field(),
            width="100%",
            height="100%",
            justify="center",
            align="center",
        ),
    )
