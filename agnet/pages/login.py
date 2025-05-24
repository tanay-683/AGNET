import reflex as rx

class FormState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


@rx.page()
def login_page() -> rx.Component:
    return rx.flex(
        rx.card(
            rx.vstack(
                rx.center(
                    rx.image(
                        src="/logo.jpg",
                        width="2.5em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Sign in to your account",
                        size="6",
                        as_="h2",
                        text_align="center",
                        width="100%",
                    ),
                    direction="column",
                    spacing="5",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        "Email address",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("user")),
                        placeholder="user@reflex.dev",
                        type="email",
                        size="3",
                        width="100%",
                        color_scheme="iris",
                        required=True,
                        default_value="",
                    ),
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.hstack(
                        rx.text(
                            "Password",
                            size="3",
                            weight="medium",
                        ),
                        rx.link(
                            "Forgot password?",
                            href="#",
                            size="3",
                        ),
                        justify="between",
                        width="100%",
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("lock")),
                        placeholder="Enter your password",
                        type="password",
                        size="3",
                        width="100%",
                        color_scheme="iris",
                        required=True,
                        default_value="",
                    ),
                    spacing="2",
                    width="100%",
                ),
                rx.button(
                    "Sign in",
                    size="3",
                    width="100%",
                    type="submit",
                    color_scheme="iris",
                ),
                rx.center(
                    rx.text("New here?", size="3"),
                    rx.link("Sign up", href="#", size="3"),
                    opacity="0.8",
                    spacing="2",
                    direction="row",
                    width="100%",
                ),
                spacing="6",
                width="100%",
            ),
            max_width="28em",
            size="4",
            width="100%",
            color_scheme="iris",
        ),
        justify="center",
        align="center",
        direction="column",
        width="100vw",
        height="100vh",
    )
