import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

NEGRO = "#0B0B0D"
NEGRO_CLARO = "#17171B"
GRIS_PANEL = "#232329"
GRIS_TEXTO = "#B7B7C2"

AMARILLO = "#FFD600"
AMARILLO_HOVER = "#FFE457"
AMARILLO_OSCURO = "#C9A600"

BLANCO = "#F7F7FA"

VERDE = "#00C853"
VERDE_HOVER = "#20E070"
VERDE_OSCURO = "#00963E"

ROJO = "#FF1744"
ROJO_HOVER = "#FF4D6D"
ROJO_OSCURO = "#C4102F"

AZUL = "#4FC3F7"

FUENTE_TITULO = ("Segoe UI", 24, "bold")
FUENTE_SUBTITULO = ("Segoe UI", 14)
FUENTE_CARD = ("Segoe UI", 16, "bold")
FUENTE_MEDIANA = ("Segoe UI", 18, "bold")
FUENTE_GRANDE = ("Segoe UI", 34, "bold")
FUENTE_EMOJI = ("Segoe UI Emoji", 70)


class InspectorPakova:
    def __init__(self, root):
        self.root = root
        self.root.title("Inspector Pakova 🕵️")
        self.root.configure(bg=NEGRO)
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))

        self.ancho = self.root.winfo_screenwidth()
        self.alto = self.root.winfo_screenheight()

        self.logo_barra = self._cargar_imagen(
            "inspectorpakova/assets/logo_pakova.png", (60, 60)
        )
        self.icono = self._cargar_imagen(
            "inspectorpakova/assets/logo_pakova.png", (32, 32)
        )
        if self.icono is not None:
            try:
                self.root.iconphoto(True, self.icono)
            except Exception as e:
                print("Error cargando icono:", e)

        self.logo = self._cargar_imagen(
            "inspectorpakova/assets/logo_pakova.png", (180, 180)
        )

        self.puntos = 0
        self.vidas = 3
        self.prueba_actual = 0
        self.bugs = {}
        self.bugs_encontrados = []

        self.menu_principal()

    # ==========================
    # UTILIDADES
    # ==========================
    def _cargar_imagen(self, ruta, tamaño):
        try:
            img = Image.open(ruta).resize(tamaño)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error cargando imagen {ruta}:", e)
            return None

    def crear_boton(
        self,
        parent,
        texto,
        comando,
        bg=AMARILLO,
        fg=NEGRO,
        hover_bg=AMARILLO_HOVER,
        font_size=16,
        padx=24,
        pady=12,
        width=None,
    ):
        btn = tk.Button(
            parent,
            text=texto,
            command=comando,
            bg=bg,
            fg=fg,
            activebackground=hover_bg,
            activeforeground=fg,
            font=("Segoe UI", font_size, "bold"),
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=padx,
            pady=pady,
            width=width,
        )
        btn.bind("<Enter>", lambda e: btn.config(bg=hover_bg))
        btn.bind("<Leave>", lambda e: btn.config(bg=bg))
        return btn

    def redondeado(self, canvas, x1, y1, x2, y2, radio=18, **kwargs):
        puntos = [
            x1 + radio, y1,
            x2 - radio, y1,
            x2, y1,
            x2, y1 + radio,
            x2, y2 - radio,
            x2, y2,
            x2 - radio, y2,
            x1 + radio, y2,
            x1, y2,
            x1, y2 - radio,
            x1, y1 + radio,
            x1, y1,
        ]
        return canvas.create_polygon(puntos, smooth=True, **kwargs)

    def limpiar(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def dibujar_fondo(self):
        self.canvas.configure(bg=NEGRO_CLARO)
        self.canvas.create_rectangle(0, 0, self.ancho, self.alto, fill=NEGRO_CLARO, outline="")
        self.canvas.create_rectangle(0, 0, self.ancho, 6, fill=AMARILLO, outline="")

    def preparar_mision(self, numero):
        self.canvas.delete("all")
        self.dibujar_fondo()
        self.actualizar_prueba(f"Prueba {numero}/5")
        return self.ancho // 2

    

    # ==========================
    # MENÚ PRINCIPAL
    # ==========================
    def menu_principal(self):
        self.limpiar()
        canvas = tk.Canvas(self.root, width=self.ancho, height=self.alto, bg=NEGRO, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        centro_x = self.ancho // 2

        canvas.create_rectangle(0, 0, self.ancho, 70, fill=AMARILLO, outline="")
        canvas.create_rectangle(0, 70, self.ancho, 74, fill=AMARILLO_OSCURO, outline="")
        canvas.create_text(
            30, 35, text="🕵️ INSPECTOR PAKOVA",
            fill=NEGRO, font=("Segoe UI", 16, "bold"), anchor="w"
        )

        self.redondeado(
            canvas, centro_x - 480, 140, centro_x + 480, 660,
            radio=28, fill=NEGRO_CLARO, outline=GRIS_PANEL, width=2
        )

        if self.logo:
            canvas.create_image(centro_x - 300, 250, image=self.logo)

        canvas.create_text(centro_x + 300, 220, text="🐞", fill=AMARILLO, font=("Segoe UI Emoji", 90))
        canvas.create_text(centro_x + 300, 330, text="⚠️", fill=AMARILLO, font=("Segoe UI Emoji", 70))

        canvas.create_text(centro_x, 380, text="INSPECTOR PAKOVA", fill=AMARILLO, font=FUENTE_GRANDE)
        canvas.create_text(
            centro_x, 440, text="Encuentra bugs antes que los usuarios",
            fill=BLANCO, font=("Segoe UI", 18)
        )
        canvas.create_text(
            centro_x, 470, text="Encuentra errores antes de que lleguen a los usuarios",
            fill=GRIS_TEXTO, font=("Segoe UI", 15)
        )

        self.redondeado(canvas, centro_x - 220, 500, centro_x + 220, 540, radio=20, fill=NEGRO, outline="")
        canvas.create_text(
            centro_x, 520, text="5 Misiones  •  3 Vidas  •  Muchos Bugs",
            fill=AMARILLO, font=("Segoe UI", 14, "bold")
        )

        boton_jugar = self.crear_boton(
            self.root, "🚀 COMENZAR MISIÓN", self.iniciar_juego,
            bg=AMARILLO, fg=NEGRO, hover_bg=AMARILLO_HOVER, font_size=16, width=22
        )
        canvas.create_window(centro_x, 600, window=boton_jugar)

        canvas.create_text(
            centro_x, 635,
            text="Presiona ESC en cualquier momento para salir de pantalla completa",
            fill=GRIS_TEXTO, font=("Segoe UI", 10)
        )

    # ==========================
    # INICIAR JUEGO
    # ==========================
    def iniciar_juego(self):
        self.puntos = 0
        self.vidas = 3
        self.prueba_actual = 0
        self.pantalla_juego()

    # ==========================
    # PANTALLA JUEGO
    # ==========================
    def pantalla_juego(self):

        self.limpiar()

        self.barra = tk.Canvas(
            self.root,
            width=self.ancho,
            height=80,
            bg=AMARILLO,
            highlightthickness=0
        )
        self.barra.pack(fill="x")

        self.barra.create_rectangle(
            0, 78,
            self.ancho, 80,
            fill=AMARILLO_OSCURO,
            outline=""
        )

        if self.logo_barra:
            self.barra.create_image(
                40,
                40,
                image=self.logo_barra
            )

        # ==========================
        # PUNTOS
        # ==========================

        self.redondeado(
            self.barra,
            110, 20,
            250, 60,
            radio=20,
            fill=NEGRO,
            outline=""
        )

        self.txt_puntos = self.barra.create_text(
            180,
            40,
            text=f"⭐ {self.puntos}",
            fill=AMARILLO,
            font=("Segoe UI", 14, "bold")
        )

        # ==========================
        # VIDAS
        # ==========================

        self.redondeado(
            self.barra,
            280, 20,
            460, 60,
            radio=20,
            fill=NEGRO,
            outline=""
        )

        self.txt_vidas = self.barra.create_text(
            370,
            40,
            text="❤️" * self.vidas,
            fill=ROJO,
            font=("Segoe UI", 14, "bold")
        )

        # ==========================
        # PROGRESO
        # ==========================

        self.redondeado(
            self.barra,
            self.ancho - 240, 20,
            self.ancho - 40, 60,
            radio=20,
            fill=NEGRO,
            outline=""
        )

        self.txt_prueba = self.barra.create_text(
            self.ancho - 140,
            40,
            text="Prueba 1/5",
            fill=BLANCO,
            font=("Segoe UI", 14, "bold")
        )

        # ==========================
        # CANVAS PRINCIPAL
        # ==========================

        self.canvas = tk.Canvas(
            self.root,
            bg=NEGRO_CLARO,
            highlightthickness=0
        )
        self.canvas.pack(
            fill="both",
            expand=True
        )

        self.cargar_mision_2()

    def actualizar_puntos(self):
        self.barra.itemconfig(
            self.txt_puntos,
            text=f"⭐ {self.puntos}"
        )

    def actualizar_vidas(self):
        self.barra.itemconfig(
            self.txt_vidas,
            text="❤️" * self.vidas
        )

    def actualizar_prueba(self, texto):
        self.barra.itemconfig(
            self.txt_prueba,
            text=texto
    )
    

    # ==========================
    # MISIÓN 2
    # ==========================
    def cargar_mision_2(self):
        cx = self.preparar_mision(2)

        self.canvas.create_text(cx, 50, text="❓ MISIÓN 2 - ¿BUG O NO BUG?", fill=AMARILLO, font=FUENTE_TITULO)
        self.redondeado(self.canvas, cx - 300, 150, cx + 300, 450, radio=16, fill="white", outline="")
        self.canvas.create_text(cx, 200, text="Sistema Escolar", font=("Segoe UI", 20, "bold"))
        self.canvas.create_text(cx, 280, text="Matemática: 8", font=("Segoe UI", 16))
        self.canvas.create_text(cx, 320, text="Historia: 7", font=("Segoe UI", 16))
        self.canvas.create_text(cx, 380, text="Promedio: 15", fill=ROJO, font=("Segoe UI", 20, "bold"))

        btn_bug = self.crear_boton(
            self.root, "✅ ES UN BUG", self.mision_2_correcta,
            bg=VERDE, fg="white", hover_bg=VERDE_HOVER, font_size=14
        )
        btn_nobug = self.crear_boton(
            self.root, "❌ NO ES BUG", self.mision_2_incorrecta,
            bg=ROJO, fg="white", hover_bg=ROJO_HOVER, font_size=14
        )
        self.canvas.create_window(cx - 180, 520, window=btn_bug)
        self.canvas.create_window(cx + 180, 520, window=btn_nobug)

    def mision_2_correcta(self):
        self.puntos += 50
        self.actualizar_puntos()
        messagebox.showinfo("Correcto", "El promedio 8 y 7 nunca puede dar 15.")
        self.cargar_mision_3()

    def mision_2_incorrecta(self):
        self.vidas -= 1
        self.actualizar_vidas()
        if self.vidas <= 0:
            self.menu_principal()
            return
        messagebox.showwarning("Incorrecto", "Ese promedio es imposible.")

    # ==========================
    # MISIÓN 3
    # ==========================
    def cargar_mision_3(self):
        cx = self.preparar_mision(3)

        self.canvas.create_text(cx, 50, text="🔒 MISIÓN 3 - SEGURIDAD", fill=AMARILLO, font=FUENTE_TITULO)
        self.canvas.create_text(
            cx, 100, text="Haz clic sobre el problema de seguridad",
            fill=GRIS_TEXTO, font=FUENTE_SUBTITULO
        )
        self.redondeado(self.canvas, cx - 350, 150, cx + 350, 550, radio=16, fill="white", outline="")
        self.canvas.create_text(cx, 220, text="Perfil de Usuario", font=("Segoe UI", 22, "bold"))
        self.canvas.create_text(cx, 300, text="Nombre: Franco", font=("Segoe UI", 16))
        self.canvas.create_text(cx, 350, text="Email: franco@email.com", font=("Segoe UI", 16))
        self.canvas.create_text(cx, 420, text="Contraseña: 123456", fill=ROJO, font=("Segoe UI", 18, "bold"))
        self.canvas.bind("<Button-1>", self.click_mision_3)

    def click_mision_3(self, event):
        cx = self.ancho // 2
        if (cx - 150) <= event.x <= (cx + 160) and 390 <= event.y <= 450:
            self.canvas.unbind("<Button-1>")
            self.puntos += 50
            self.actualizar_puntos()
            messagebox.showinfo("Correcto", "Las contraseñas nunca deben mostrarse.")
            self.cargar_mision_4()

    # ==========================
    # MISIÓN 4
    # ==========================
    def cargar_mision_4(self):
        cx = self.preparar_mision(4)

        self.canvas.create_text(cx, 60, text="🖱️ MISIÓN 4 - BOTÓN CORRECTO", fill=AMARILLO, font=FUENTE_TITULO)
        self.canvas.create_text(
            cx, 110, text="Haz clic en el botón que debería funcionar",
            fill=GRIS_TEXTO, font=FUENTE_SUBTITULO
        )
        self.redondeado(self.canvas, cx - 350, 180, cx + 350, 600, radio=16, fill="white", outline="")
        self.canvas.create_text(cx, 240, text="Formulario de Registro", font=("Segoe UI", 20, "bold"))

        self.redondeado(self.canvas, cx - 250, 400, cx - 80, 470, radio=10, fill="#999999", outline="")
        self.canvas.create_text(cx - 165, 435, text="Guardar", fill="white", font=("Segoe UI", 14, "bold"))

        self.redondeado(self.canvas, cx + 80, 400, cx + 250, 470, radio=10, fill=VERDE, outline="")
        self.canvas.create_text(cx + 165, 435, text="Enviar", fill="white", font=("Segoe UI", 14, "bold"))

        self.canvas.bind("<Button-1>", self.click_mision_4)

    def click_mision_4(self, event):
        cx = self.ancho // 2

        if (cx + 80) <= event.x <= (cx + 250) and 400 <= event.y <= 470:
            self.canvas.unbind("<Button-1>")
            self.puntos += 50
            self.actualizar_puntos()
            messagebox.showinfo("Correcto", "El botón Enviar es el que funciona.")
            self.cargar_mision_5()
            return

        if (cx - 250) <= event.x <= (cx - 80) and 400 <= event.y <= 470:
            self.vidas -= 1
            self.actualizar_vidas()
            messagebox.showwarning("Error", "Elegiste un botón defectuoso.")
            if self.vidas <= 0:
                self.menu_principal()

    # ==========================
    # MISIÓN 5
    # ==========================
    def cargar_mision_5(self):
        cx = self.preparar_mision(5)

        self.canvas.create_text(cx, 70, text="🏆 MISIÓN FINAL", fill=AMARILLO, font=("Segoe UI", 28, "bold"))
        self.canvas.create_text(cx, 140, text="¿Qué hace un tester?", fill=BLANCO, font=("Segoe UI", 18))

        self.opcion1 = self.crear_boton(
            self.root, "Rompe programas", self.final_incorrecto,
            bg=NEGRO_CLARO, fg=BLANCO, hover_bg=GRIS_PANEL, font_size=14
        )
        self.opcion2 = self.crear_boton(
            self.root, "Busca errores para mejorar la calidad", self.final_correcto,
            bg=VERDE, fg="white", hover_bg=VERDE_HOVER, font_size=14
        )

        self.canvas.create_window(cx, 280, window=self.opcion1)
        self.canvas.create_window(cx, 380, window=self.opcion2)

    def final_incorrecto(self):
        messagebox.showwarning("Incorrecto", "El tester ayuda a mejorar el software.")

    def final_correcto(self):
        if hasattr(self, "opcion1") and self.opcion1.winfo_exists():
            self.opcion1.destroy()
        if hasattr(self, "opcion2") and self.opcion2.winfo_exists():
            self.opcion2.destroy()

        self.puntos += 100
        self.actualizar_puntos()

        self.canvas.delete("all")
        self.dibujar_fondo()
        self.actualizar_prueba("Completado")

        cx = self.ancho // 2
        self.canvas.create_text(cx, 180, text="🏆 ¡FELICITACIONES!", fill=VERDE, font=FUENTE_GRANDE)
        self.canvas.create_text(cx, 280, text="Has completado Inspector Pakova", fill=BLANCO, font=("Segoe UI", 24))
        self.canvas.create_text(cx, 380, text=f"Puntaje Final: {self.puntos}", fill=AMARILLO, font=("Segoe UI", 30, "bold"))
        self.canvas.create_text(cx, 480, text="🐞 Ahora ya sabes qué hace un tester", fill=GRIS_TEXTO, font=("Segoe UI", 18))

        btn_reiniciar = self.crear_boton(
            self.root, "🔄 Jugar de Nuevo", self.reiniciar_juego,
            bg=AMARILLO, fg=NEGRO, hover_bg=AMARILLO_HOVER, font_size=16
        )
        self.canvas.create_window(cx, 580, window=btn_reiniciar)

    def reiniciar_juego(self):
        self.puntos = 0
        self.vidas = 3
        self.prueba_actual = 0
        self.iniciar_juego()


if __name__ == "__main__":
    root = tk.Tk()
    juego = InspectorPakova(root)
    root.mainloop()

