import flet as ft
import random
import os
def main(page: ft.Page):
    # ================= CONFIGURACIÓN =================
    page.title = "Preguntas para conocer a Nelly Noemi"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#FFFFFF"
    page.padding = 40
    page.scroll = "adaptive"

    preguntas = [
    # ================= NORMALES =================
    "¿Cuál es tu color favorito?",
    "¿Prefieres café o té?",
    "¿Día o noche?",
    "¿Playa o montaña?",
    "¿Película o serie?",
    "¿Qué música escuchas más seguido?",
    "¿Tu comida favorita?",
    "¿Qué te hace reír fácilmente?",
    "¿Prefieres hablar o escuchar?",
    "¿Eres más organizado o espontáneo?",
    "¿Lluvia o sol?",
    "¿Dulce o salado?",
    "¿Libro físico o digital?",
    "¿Salir o quedarte en casa?",
    "¿Amanecer o atardecer?",
    "¿Silencio o música de fondo?",
    "¿Mensajes o llamadas?",
    "¿Improvisar o planear?",
    "¿Cocinar o pedir comida?",
    "¿Ciudad o pueblo?",

    # ================= PROFUNDAS =================
    "¿Qué es lo que más valoras en una persona?",
    "¿Cuál ha sido el momento más difícil de tu vida?",
    "¿Qué te da más miedo perder?",
    "¿Qué te hace sentir en paz?",
    "¿Qué te gustaría sanar de tu pasado?",
    "¿Qué te motiva a seguir adelante?",
    "¿Qué significa para ti la felicidad?",
    "¿Qué te cuesta expresar?",
    "¿Qué te hace sentir amado/a?",
    "¿Qué parte de ti casi nadie conoce?",
    "¿Qué te rompe emocionalmente?",
    "¿Qué te hace sentir incomprendida?",
    "¿Qué herida aún no cierra?",
    "¿Qué te da ansiedad en silencio?",
    "¿Qué te da miedo aceptar de ti?",
    "¿Qué te hace sentir suficiente?",
    "¿Qué te duele recordar?",
    "¿Qué te cuesta soltar?",
    "¿Qué te hace llorar sin avisar?",
    "¿Qué emoción escondes mejor?",

    # ================= VIDA & IDENTIDAD =================
    "¿Cuál es tu mayor sueño por cumplir?",
    "¿Qué te gustaría que recordaran de ti?",
    "¿Qué te enoja con facilidad?",
    "¿Qué haces cuando te sientes sola?",
    "¿Qué cualidad admiras más?",
    "¿Qué te hace sentir orgullosa de ti?",
    "¿Qué cambiarías de tu personalidad?",
    "¿Qué te define más allá de lo que haces?",
    "¿Qué versión tuya te gusta más?",
    "¿Qué versión tuya te da miedo?",
    "¿Qué parte de tu vida estás reconstruyendo?",
    "¿Qué te hizo madurar antes de tiempo?",
    "¿Qué te hace sentir auténtica?",
    "¿Qué parte de ti proteges más?",
    "¿Qué parte de ti te cuesta amar?",
    "¿Qué mentira te dices a veces?",
    "¿Qué te hace sentir real?",
    "¿Qué te hace sentir vacía?",
    "¿Qué te hace sentir completa?",
    "¿Qué no volverías a permitir?",

    # ================= AMOR & VÍNCULOS =================
    "¿Cómo defines el amor verdadero?",
    "¿Qué te hace sentir segura en una relación?",
    "¿Qué te hace alejarte de alguien?",
    "¿Qué necesitas para confiar?",
    "¿Qué te enamora lentamente?",
    "¿Qué te enamora de golpe?",
    "¿Qué te rompe el corazón?",
    "¿Qué te cuesta perdonar?",
    "¿Qué límite nunca cruzarías por amor?",
    "¿Qué te hace quedarte?",
    "¿Qué te hace irte?",
    "¿Qué te duele del amor?",
    "¿Qué te ilusiona del amor?",
    "¿Qué tipo de amor sueñas?",
    "¿Qué tipo de amor temes?",
    "¿Qué aprendiste de tu última relación?",
    "¿Qué te gustaría que entendieran de ti al amar?",
    "¿Qué te hace sentir deseada?",
    "¿Qué te hace sentir invisible?",
    "¿Qué promesa te gustaría que cumplieran contigo?",

    # ================= DARK ROMANCE =================
    "¿Te atraen más las historias que duelen o las que sanan?",
    "¿Crees que el amor debe doler un poco?",
    "¿Te atrae la intensidad o la estabilidad?",
    "¿Qué tipo de persona oscura te atrae?",
    "¿Qué parte oscura de ti escondes?",
    "¿Qué te resulta peligroso pero atractivo?",
    "¿Te enamoras de ideas o de personas?",
    "¿Prefieres un amor tranquilo o uno que consuma?",
    "¿Qué te resulta más seductor: misterio o vulnerabilidad?",
    "¿Qué harías por amor que nadie esperaría?",
    "¿Qué te excita emocionalmente?",
    "¿Qué te hace sentir prohibida?",
    "¿Qué te hace sentir poderosa?",
    "¿Qué te hace sentir frágil?",
    "¿Qué te atrae del caos?",
    "¿Qué te atrae del dolor ajeno?",
    "¿Qué parte de ti ama lo intenso?",
    "¿Qué parte de ti teme perder el control?",
    "¿Qué te hace sentir peligrosa?",
    "¿Qué fantasía emocional no confiesas?",

    # ================= ESCRITURA =================
    "¿Escribes cuando estás triste o cuando estás llena?",
    "¿Qué parte de ti solo existe al escribir?",
    "¿Escribes para sanar o para recordar?",
    "¿Qué palabra te define últimamente?",
    "¿Qué frase te gustaría que alguien te dijera?",
    "¿Qué historia te daría miedo escribir?",
    "¿Qué emoción expresas mejor con palabras?",
    "¿Qué tema siempre vuelve a tus textos?",
    "¿Qué te gustaría escribir y nunca te atreviste?",
    "¿Qué escribirías si nadie te juzgara?",
    "¿Qué escribirías sobre tu corazón?",
    "¿Qué escribirías sobre tu soledad?",
    "¿Qué escribirías sobre tu deseo?",
    "¿Qué escribirías sobre tu miedo?",
    "¿Qué escribirías sobre tu pasado?",
    "¿Qué escribirías sobre tu futuro?",
    "¿Qué parte de tu historia duele más?",
    "¿Qué parte de tu historia amas más?",
    "¿Qué personaje se parece a ti?",
    "¿Qué final mereces?",

    # ================= MÚSICA =================
    "¿Qué canción te representa hoy?",
    "¿Qué canción te rompe el alma?",
    "¿Qué canción te hace sentir libre?",
    "¿Qué canción pondrías en una noche de insomnio?",
    "¿Qué artista te entiende sin conocerte?",
    "¿Qué canción te recuerda a alguien?",
    "¿Qué canción te hace sentir peligrosa?",
    "¿Qué canción te hace sentir viva?",
    "¿Qué canción describe tu forma de amar?",
    "¿Qué canción describe tu tristeza?",
    "¿Qué canción describe tu deseo?",
    "¿Qué canción describe tu silencio?",
    "¿Qué canción escucharías al escribir?",
    "¿Qué canción te acompaña cuando lloras?",
    "¿Qué canción te hace sentir fuerte?",
    "¿Qué canción de Lana Del Rey te define?",
    "¿Qué canción de Arctic Monkeys habla de ti?",
    "¿Qué canción de Foster The People te refleja?",
    "¿Qué letra sientes escrita para ti?",
    "¿Qué canción pondrías para despedirte?",

    # ================= EXISTENCIA =================
    "¿Qué te hace sentir en el camino correcto?",
    "¿Qué te hace dudar de ti?",
    "¿Qué te da esperanza?",
    "¿Qué te hace perder la fe?",
    "¿Qué te sostiene cuando caes?",
    "¿Qué te salva en silencio?",
    "¿Qué te duele aceptar?",
    "¿Qué te da calma?",
    "¿Qué te da miedo enfrentar?",
    "¿Qué te gustaría agradecer hoy?",
    "¿Qué te gustaría dejar ir?",
    "¿Qué te gustaría conservar siempre?",
    "¿Qué te hace sentir viva de verdad?",
    "¿Qué te hace sentir parte de algo más?",
    "¿Qué te gustaría crear en tu vida?",
    "¿Qué te gustaría experimentar antes de envejecer?",
    "¿Qué te gustaría dejar como legado?",
    "¿Qué te gustaría perdonarte?",
    "¿Qué te gustaría que perdonaran de ti?",
    "¿Qué le dirías al universo hoy?"
    ]


    # ================= TEXTO DE PREGUNTA =================
    pregunta_texto = ft.Text(
        "Presiona el botón para comenzar",
        size=26,
        weight=ft.FontWeight.W_600,
        text_align=ft.TextAlign.CENTER,
        color="#000000"
    )

    # ================= FUNCIÓN RANDOM =================
    def nueva_pregunta(e):
        pregunta_texto.value = random.choice(preguntas)
        page.update()

    # ================= INTERFAZ =================
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Icon(ft.Icons.PSYCHOLOGY, size=60, color="#000000"),

                    ft.Text(
                        "Preguntas para conocer a Nelly Noemi (Double N) ",
                        size=34,
                        weight=ft.FontWeight.BOLD,
                        color="#000000",
                        text_align=ft.TextAlign.CENTER
                    ),

                    ft.Divider(height=30, color="#000000"),

                    pregunta_texto,

                    ft.Divider(height=30),

                    ft.ElevatedButton(
                        "Nueva pregunta",
                        icon=ft.Icons.CASINO,
                        on_click=nueva_pregunta,
                        bgcolor="#000000",
                        color="#FFFFFF",
                        height=55,
                        width=260,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=12)
                        )
                    ),

                    ft.Text(
                        "Respira, lee y responde con honestidad",
                        size=14,
                        color="#444444",
                        italic=True,
                        text_align=ft.TextAlign.CENTER
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            ),
            padding=40,
            border_radius=20,
            border=ft.border.all(2, "#000000"),
            bgcolor="#FFFFFF",
            alignment=ft.alignment.center
        )
    )

ft.app(
    target=main,
    view=ft.AppView.WEB_BROWSER,
    port=int(os.environ.get("PORT", 5000)),
    host="0.0.0.0"
)
