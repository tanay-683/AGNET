import reflex as rx


def modern_input_field():
    return rx.vstack(
                rx.text_area(
                placeholder="Type here...",
                rows="5",
                width="45%",
                border_width="none",
                ),
                rx.divider( width="45%",),
                rx.flex(
                    rx.button("upload"),
                    rx.spacer(),
                    rx.button("model"),
                    rx.spacer(),
                    rx.button("send"),
                    width="45%",
                    ),
            justify="center",
            align="center",
            width="100vw",
            height="100vh",
            font_size="1.2rem",
            
        )
    
    







