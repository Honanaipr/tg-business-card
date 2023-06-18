from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import SwitchTo, Row, Start, Group
from aiogram_dialog.widgets.media import StaticMedia, Media

from aiogram.types import ContentType

from business_card.states import MainSG, TranslateSG
from business_card.utils import get_placehold_image_url

main_diolog = Dialog(
    Window(
        StaticMedia(url=Const(get_placehold_image_url(text="Main window")), type=ContentType.PHOTO),
        Row(
            SwitchTo(id="btn_start_services", state=MainSG.services, text=Const("🛠️ Services")),
        ),
        Row(
            SwitchTo(id="btn_help", text=Const("📃❓ Help"), state=MainSG.help),
            SwitchTo(id="btn_settings", text=Const("⚙️ Settings"), state=MainSG.settings),
        ),
        state=MainSG.main
    ),
    Window(
        StaticMedia(url=Const(get_placehold_image_url(text="Services")), type=ContentType.PHOTO),
        Const("Здесь находятся бесплатные сервисы"),
        Group(
            Start(id="btn_translate", text=Const("🌍💬 Transalte"), state=TranslateSG.main),
            Start(id="btn_translate", text=Const("🌍💬 Transalte"), state=TranslateSG.main),
            Start(id="btn_translate", text=Const("🌍💬 Transalte"), state=TranslateSG.main),
            Start(id="btn_translate", text=Const("🌍💬 Transalte"), state=TranslateSG.main),
            width=2
        ),
        SwitchTo(id="btn_main", text=Const("↩️ Main menu"), state=MainSG.main),
        state=MainSG.services
    ),
    Window(
        StaticMedia(url=Const(get_placehold_image_url(text="Help")), type=ContentType.PHOTO),
        Const("Этот бот умеет несколько прикольных вещей.\n /start - перезапустите бота, если у вас возникли трудности."),
        SwitchTo(id="btn_main", text=Const("↩️ Main menu"), state=MainSG.main),
        state=MainSG.help
    ),
    Window(
        StaticMedia(url=Const(get_placehold_image_url(text="Settings window")), type=ContentType.PHOTO),
        Const("Возможно здесь когданибуть будут настройки."),
        SwitchTo(id="btn_main", text=Const("↩️ Main menu"), state=MainSG.main),
        state=MainSG.settings
    )
)
    