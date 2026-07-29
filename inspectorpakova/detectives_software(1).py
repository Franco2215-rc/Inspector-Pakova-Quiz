import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# ==========================
# CONFIGURACIÓN
# ==========================

#ANCHO = 1200
#ALTO = 700

NEGRO = "#111111"
NEGRO_CLARO = "#1E1E1E"
AMARILLO = "#FFD600"
BLANCO = "#FFFFFF"
VERDE = "#00C853"
ROJO = "#FF1744"


# ==========================
# CLASE PRINCIPAL
# ==========================

class InspectorPakova:

    def __init__(self, root):

        self.root = root
        self.root.title("Inspector Pakova 🕵️")

        try:
            logo = Image.open("inspectorpakova/assets/logo_pakova.png")
            logo = logo.resize((60, 60))
            self.logo_barra = ImageTk.PhotoImage(logo)
        except Exception as e:
            print("Error cargando logo:", e)
            self.logo_barra = None
        try:
            icono_img = Image.open("inspectorpakova/assets/logo_pakova.png")
            icono_img = icono_img.resize((32, 32))
            self.icono = ImageTk.PhotoImage(icono_img)

            self.root.iconphoto(True, self.icono)

        except Exception as e:
            print("Error cargando icono:", e)

# Pantalla completa
        self.root.attributes("-fullscreen", True)

# Salir con ESC
        self.root.bind(
        "<Escape>",
        lambda e: self.root.attributes("-fullscreen", False)
)
        logo = Image.open("inspectorpakova/assets/logo_pakova.png")
        logo = logo.resize((60, 60))
        self.logo_barra = ImageTk.PhotoImage(logo)
# Tamaño real de pantalla
        self.ancho = self.root.winfo_screenwidth()
        self.alto = self.root.winfo_screenheight()
        self.root.configure(bg=NEGRO)
        

        self.puntos = 0
        self.vidas = 3
        self.prueba_actual = 0
        
        

        self.cargar_logo()

        self.menu_principal()

    # ==========================
    # CARGAR LOGO
    # ==========================
    def dibujar_fondo(self):

        self.canvas.configure(bg=NEGRO_CLARO)

        self.canvas.create_rectangle(
        0,
        0,
        self.ancho,
        self.alto,
        fill=NEGRO_CLARO,
        outline=""
    )

    def cargar_logo(self):

        self.logo = None

        try:

            logo = Image.open(
                "inspectorpakova/assets/logo_pakova.png"
            )

            logo = logo.resize(
                (180, 180)
            )

            self.logo = ImageTk.PhotoImage(
                logo
            )

        except:
            pass

    # ==========================
    # LIMPIAR
    # ==========================

    def limpiar(self):

        for widget in self.root.winfo_children():
            widget.destroy()

    # ==========================
    # DETECTIVE CANVAS
    # ==========================

    def dibujar_detective(self, canvas, x, y):

        # Sombrero

        canvas.create_rectangle(
            x-45, y-70,
            x+45, y-45,
            fill="#3E2723",
            outline=""
        )

        canvas.create_rectangle(
            x-60, y-50,
            x+60, y-40,
            fill="#3E2723",
            outline=""
        )

        # Cabeza

        canvas.create_oval(
            x-30, y-40,
            x+30, y+20,
            fill="#FFD180",
            outline=""
        )

        # Ojos

        canvas.create_oval(
            x-12, y-10,
            x-4, y-2,
            fill="black"
        )

        canvas.create_oval(
            x+4, y-10,
            x+12, y-2,
            fill="black"
        )

        # Gabardina

        canvas.create_polygon(
            x-50, y+20,
            x+50, y+20,
            x+25, y+110,
            x-25, y+110,
            fill="#795548",
            outline=""
        )

        # Lupa

        canvas.create_oval(
            x+35, y-5,
            x+75, y+35,
            outline="#4FC3F7",
            width=4
        )

        canvas.create_line(
            x+70, y+30,
            x+95, y+55,
            fill="#4FC3F7",
            width=4
        )

    # ==========================
    # MENÚ PRINCIPAL
    # ==========================

    def menu_principal(self):

        self.limpiar()

        canvas = tk.Canvas(
        self.root,
        width=self.ancho,
        height=self.alto,
        bg=NEGRO,
        highlightthickness=0
    )

        canvas.pack(fill="both", expand=True)

        centro_x = self.ancho // 2
        centro_y = self.alto // 2

    # Barra superior
        canvas.create_rectangle(
        0,
        0,
        self.ancho,
        70,
        fill=AMARILLO,
        outline=""
    )

    # Logo
        if self.logo:
            canvas.create_image(
            centro_x - 300,
            250,
            image=self.logo
        )

    # Iconos decorativos
        canvas.create_text(
        centro_x + 300,
        220,
        text="🐞",
        fill=AMARILLO,
        font=("Segoe UI Emoji", 90)
    )

        canvas.create_text(
        centro_x + 300,
        330,
        text="⚠️",
        fill=AMARILLO,
        font=("Segoe UI Emoji", 70)
    )

    # Título
        canvas.create_text(
        centro_x,
        380,
        text="INSPECTOR PAKOVA",
        fill=AMARILLO,
        font=("Segoe UI", 32, "bold")
    )

    # Subtítulos
        canvas.create_text(
        centro_x,
        440,
        text="Encuentra bugs antes que los usuarios",
        fill=BLANCO,
        font=("Segoe UI", 18)
    )

        canvas.create_text(
        centro_x,
        470,
        text="Encuentra errores antes de que lleguen a los usuarios",
        fill=BLANCO,
        font=("Segoe UI", 16)
    )

        canvas.create_text(
        centro_x,
        520,
        text="5 Misiones • 3 Vidas • Muchos Bugs",
        fill=BLANCO,
        font=("Segoe UI", 14)
    )

    # Botón comenzar
        boton_jugar = tk.Button(
        self.root,
        text="🚀 COMENZAR MISIÓN",
        bg=AMARILLO,
        fg="black",
        font=("Segoe UI", 16, "bold"),
        relief="flat",
        width=22,
        command=self.iniciar_juego
    )

        canvas.create_window(
        centro_x,
        600,
        window=boton_jugar
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

        barra = tk.Canvas(
    self.root,
    width=self.ancho,
    height=80,
    bg=AMARILLO,
    highlightthickness=0
)

        barra.pack(fill="x")

# Logo
        
        barra.create_image(
    40,
    40,
    image=self.logo_barra
)

# Puntos
        self.lbl_puntos = tk.Label(
    barra,
    text=f"⭐ {self.puntos}",
    bg=AMARILLO,
    fg="black",
    font=("Segoe UI", 14, "bold")
)

        barra.create_window(
    180,
    40,
    window=self.lbl_puntos
)

        self.lbl_vidas = tk.Label(
        barra,
        text="❤️" * self.vidas,
        bg="black",
        fg="red",
        font=("Segoe UI", 14, "bold")
)

        barra.create_window(
        350,
        60,
        window=self.lbl_vidas
)

        self.lbl_prueba = tk.Label(
        barra,
        text="Prueba 1/5",
        bg="black",
        fg="white",
        font=("Segoe UI", 14, "bold")
)

        barra.create_window(
        self.ancho - 120,
        60,
        window=self.lbl_prueba
)

        barra.create_window(1080, 60, window=self.lbl_prueba)
    
        self.canvas = tk.Canvas(
        self.root,
        bg=NEGRO_CLARO,
        highlightthickness=0
    )

        self.canvas.pack(
        fill="both",
        expand=True
    )
        self.cargar_mision_1()


    # MISIÓN 1
    # ==========================

    def cargar_mision_1(self):
            print("MISION 1 CARGADA")

            self.canvas.delete("all")
            self.dibujar_fondo()

            self.lbl_prueba.config(
            text="Prueba 1/5"
        )

            self.canvas.create_text(
            600,
            40,
            text="🐞 MISIÓN 1 - CAZA DE BUGS",
            fill=AMARILLO,
            font=("Segoe UI", 24, "bold")
        )

            self.canvas.create_text(
            600,
            80,
            text="Encuentra los errores visibles",
            fill=BLANCO,
            font=("Segoe UI", 14)
        )

        # Ventana simulada

            self.canvas.create_rectangle(
            250, 120,
            950, 580,
            fill="white",
            outline=""
        )

        # Barra azul

            self.canvas.create_rectangle(
            250, 120,
            950, 180,
            fill="#2563EB",
            outline=""
        )

            self.canvas.create_text(
            600,
            150,
            text="Sistema de Gestión",
            fill="white",
            font=("Segoe UI", 18, "bold")
        )

        # Tarjeta usuarios

            self.canvas.create_rectangle(
            300, 220,
            520, 340,
            fill="#F5F5F5",
            outline="#CCCCCC"
        )

            self.canvas.create_text(
            410,
            250,
            text="Usuarrio",
            fill="red",
            font=("Segoe UI", 16, "bold")
        )

            self.canvas.create_text(
            410,
            300,
            text="Franco",
            font=("Segoe UI", 14)
        )

        # Tarjeta contraseña

            self.canvas.create_rectangle(
            560, 220,
            900, 340,
            fill="#F5F5F5",
            outline="#CCCCCC"
        )

            self.canvas.create_text(
            730,
            250,
            text="Contraseña",
            font=("Segoe UI", 16)
        )

            self.canvas.create_text(
            730,
            300,
            text="123456",
            fill="red",
            font=("Segoe UI", 18, "bold")
        )

        # Imagen faltante

            self.canvas.create_rectangle(
            300, 390,
            520, 520,
            fill="#FFFFFF",
            outline="red",
            width=3
        )

            self.canvas.create_text(
            410,
            455,
            text="❌ Imagen\nNo Encontrada",
            fill="red",
            font=("Segoe UI", 16, "bold")
        )

        # Botón roto

            self.canvas.create_rectangle(
            650, 420,
            850, 490,
            fill="#999999",
            outline=""
        )

            self.canvas.create_text(
            750,
            455,
            text="Guardar",
            fill="white",
            font=("Segoe UI", 16, "bold")
        )

            self.canvas.create_text(
            750,
            520,
            text="⚠️ No funciona",
            fill="red",
            font=("Segoe UI", 12, "bold")
        )

            self.bugs_encontrados = []

            self.bugs = {

            "ortografia": (
                330, 230,
                490, 270,
                10,
                "Error ortográfico encontrado."
            ),

            "password": (
                650, 270,
                820, 320,
                30,
                "Las contraseñas nunca deben mostrarse."
            ),

            "imagen": (
                300, 390,
                520, 520,
                30,
                "La imagen no cargó correctamente."
            ),

            "boton": (
                650, 420,
                850, 520,
                20,
                "El botón principal está roto."
            )
        }

            self.canvas.bind(
            "<Button-1>",
            self.click_mision_1
        )
    def click_mision_1(self, event):

        encontrado = False

        for bug, datos in self.bugs.items():

            if bug in self.bugs_encontrados:
                continue

            x1, y1, x2, y2, puntos, mensaje = datos

            if x1 <= event.x <= x2 and y1 <= event.y <= y2:

                encontrado = True

                self.bugs_encontrados.append(bug)
                print("Encontrados:", self.bugs_encontrados)
                print("Cantidad:", len(self.bugs_encontrados), "/", len(self.bugs))

                self.puntos += puntos

                self.lbl_puntos.config(
                text=f"⭐ {self.puntos}"
            )

                self.canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    outline=VERDE,
                    width=5
            )

                messagebox.showinfo(
                    "✅ Bug encontrado",
                    f"+{puntos} puntos\n\n{mensaje}"
            )

                break

        if not encontrado:

                self.vidas -= 1
                print("Vidas actuales:", self.vidas)

                self.lbl_vidas.config(
                text="❤️" * self.vidas
        )

        if self.vidas <= 0:

                messagebox.showerror(
                "Fin del Juego",
                "Te quedaste sin vidas."
            )

                self.menu_principal()
                return

        if len(self.bugs_encontrados) == len(self.bugs):

            self.canvas.unbind("<Button-1>")

            messagebox.showinfo(
            "🎉 Misión completada",
            "Encontraste todos los bugs."
        )

            self.prueba_actual = 1
            self.cargar_mision_2()

    def cargar_mision_2(self):

        self.canvas.delete("all")
        self.dibujar_fondo()

        self.lbl_prueba.config(
        text="Prueba 2/5"
    )

        self.canvas.create_text(
        600,
        50,
        text="❓ MISIÓN 2 - ¿BUG O NO BUG?",
        fill=AMARILLO,
        font=("Segoe UI", 24, "bold")
    )

        self.canvas.create_rectangle(
        300, 150,
        900, 450,
        fill="white",
        outline=""
    )

        self.canvas.create_text(
        600,
        200,
        text="Sistema Escolar",
        font=("Segoe UI", 20, "bold")
    )

        self.canvas.create_text(
        600,
        280,
        text="Matemática: 8",
        font=("Segoe UI", 16)
    )

        self.canvas.create_text(
        600,
        320,
        text="Historia: 7",
        font=("Segoe UI", 16)
    )

        self.canvas.create_text(
        600,
        380,
        text="Promedio: 15",
        fill="red",
        font=("Segoe UI", 20, "bold")
    )

        btn_bug = tk.Button(
        self.root,
        text="✅ ES UN BUG",
        bg=VERDE,
        fg="white",
        font=("Segoe UI", 14, "bold"),
        command=self.mision_2_correcta
    )

        btn_nobug = tk.Button(
        self.root,
        text="❌ NO ES BUG",
        bg=ROJO,
        fg="white",
        font=("Segoe UI", 14, "bold"),
        command=self.mision_2_incorrecta
    )

        self.canvas.create_window(
        470,
        550,
        window=btn_bug
    )

        self.canvas.create_window(
        730,
        550,
        window=btn_nobug
    )
    def mision_2_correcta(self):

        self.puntos += 50

        self.lbl_puntos.config(
        text=f"⭐ {self.puntos}"
    )

        messagebox.showinfo(
        "Correcto",
        "El promedio 8 y 7 nunca puede dar 15."
    )

        self.cargar_mision_3()


    def mision_2_incorrecta(self):

        self.vidas -= 1

        self.lbl_vidas.config(
        text="❤️" * self.vidas
    )

        if self.vidas <= 0:

            self.menu_principal()
            return

        messagebox.showwarning(
        "Incorrecto",
        "Ese promedio es imposible."
    )
    


    def mision_2_incorrecta(self):

        self.vidas -= 1

        self.lbl_vidas.config(
        text="❤️" * self.vidas
    )

        if self.vidas <= 0:

            self.menu_principal()
            return

        messagebox.showwarning(
        "Incorrecto",
        "Ese promedio es imposible."
    )
    def cargar_mision_3(self):

            self.canvas.delete("all")
            self.dibujar_fondo()

            self.lbl_prueba.config(
            text="Prueba 3/5"
    )

            self.canvas.create_text(
            600,
            50,
            text="🔒 MISIÓN 3 - SEGURIDAD",
            fill=AMARILLO,
            font=("Segoe UI", 24, "bold")
    )

            self.canvas.create_text(
        600,
        100,
        text="Haz clic sobre el problema de seguridad",
        fill=BLANCO,
        font=("Segoe UI", 14)
    )

            self.canvas.create_rectangle(
        250,
        150,
        950,
        550,
        fill="white"
    )

            self.canvas.create_text(
        600,
        220,
        text="Perfil de Usuario",
        font=("Segoe UI", 22, "bold")
    )

            self.canvas.create_text(
        600,
        300,
        text="Nombre: Franco",
        font=("Segoe UI", 16)
    )

            self.canvas.create_text(
        600,
        350,
        text="Email: franco@email.com",
        font=("Segoe UI", 16)
    )

            self.canvas.create_text(
        600,
        420,
        text="Contraseña: 123456",
        fill="red",
        font=("Segoe UI", 18, "bold")
    )

            self.canvas.bind(
        "<Button-1>",
        self.click_mision_3
    )
        
    def click_mision_3(self, event):

        if 450 <= event.x <= 760 and 390 <= event.y <= 450:

            self.canvas.unbind("<Button-1>")

            self.puntos += 50

            self.lbl_puntos.config(
            text=f"⭐ {self.puntos}"
        )

            messagebox.showinfo(
            "Correcto",
            "Las contraseñas nunca deben mostrarse."
        )
            self.cargar_mision_4()

    def cargar_mision_4(self):

        self.canvas.delete("all")
        self.dibujar_fondo()

        self.lbl_prueba.config(
        text="Prueba 4/5"
    )

        self.canvas.create_text(
        600,
        60,
        text="🖱️ MISIÓN 4 - BOTÓN CORRECTO",
        fill=AMARILLO,
        font=("Segoe UI", 24, "bold")
    )

        self.canvas.create_text(
        600,
        110,
        text="Haz clic en el botón que debería funcionar",
        fill=BLANCO,
        font=("Segoe UI", 14)
    )

        self.canvas.create_rectangle(
        250, 180,
        950, 600,
        fill="white"
    )

        self.canvas.create_text(
        600,
        240,
        text="Formulario de Registro",
        font=("Segoe UI", 20, "bold")
    )

        self.canvas.create_rectangle(
        350, 400,
        520, 470,
        fill="#999999"
    )

        self.canvas.create_text(
        435,
        435,
        text="Guardar",
        fill="white",
        font=("Segoe UI", 14, "bold")
    )

        self.canvas.create_rectangle(
        680, 400,
        850, 470,
        fill=VERDE
    )

        self.canvas.create_text(
        765,
        435,
        text="Enviar",
        fill="white",
        font=("Segoe UI", 14, "bold")
    )

        self.canvas.bind(
        "<Button-1>",
        self.click_mision_4
    )
        

    
    def click_mision_4(self, event):

        # Botón correcto

        if 680 <= event.x <= 850 and 400 <= event.y <= 470:

            self.canvas.unbind("<Button-1>")

            self.puntos += 50

            self.lbl_puntos.config(
            text=f"⭐ {self.puntos}"
        )

            messagebox.showinfo(
            "Correcto",
            "El botón Enviar es el que funciona."
        )

            self.cargar_mision_5()

            return

    # Botón roto

        if 350 <= event.x <= 520 and 400 <= event.y <= 470:

            self.vidas -= 1

            self.lbl_vidas.config(
            text="❤️" * self.vidas
        )

            messagebox.showwarning(
            "Error",
            "Elegiste un botón defectuoso."
        )

            if self.vidas <= 0:
                self.menu_principal()
    def cargar_mision_5(self):

        self.canvas.delete("all")
        self.dibujar_fondo()

        self.lbl_prueba.config(
        text="Prueba 5/5"
    )

        self.canvas.create_text(
        600,
        70,
        text="🏆 MISIÓN FINAL",
        fill=AMARILLO,
        font=("Segoe UI", 28, "bold")
    )

        self.canvas.create_text(
        600,
        140,
        text="¿Qué hace un tester?",
        fill=BLANCO,
        font=("Segoe UI", 18)
    )

        self.opcion1 = tk.Button(
        self.root,
        text="Rompe programas",
        font=("Segoe UI", 14),
        command=self.final_incorrecto
    )

        self.opcion2 = tk.Button(
        self.root,
        text="Busca errores para mejorar la calidad",
        font=("Segoe UI", 14),
        bg=VERDE,
        fg="white",
        command=self.final_correcto
    )

        self.canvas.create_window(
        600,
        280,
        window=self.opcion1
    )

        self.canvas.create_window(
        600,
        380,
        window=self.opcion2
    ) 
    def final_incorrecto(self):

        messagebox.showwarning(
        "Incorrecto",
        "El tester ayuda a mejorar el software."
    )
    def final_correcto(self):

        self.opcion1.destroy()
        self.opcion2.destroy()

        self.puntos += 100

        self.lbl_puntos.config(
        text=f"⭐ {self.puntos}"
    )

        self.canvas.delete("all")
        self.dibujar_fondo()

        self.lbl_prueba.config(
        text="Completado"
    )

        self.canvas.create_text(
        600,
        180,
        text="🏆 ¡FELICITACIONES!",
        fill=VERDE,
        font=("Segoe UI", 34, "bold")
    )

        self.canvas.create_text(
        600,
        280,
        text="Has completado Inspector Pakova",
        fill=BLANCO,
        font=("Segoe UI", 24)
    )

        self.canvas.create_text(
        600,
        380,
        text=f"Puntaje Final: {self.puntos}",
        fill=AMARILLO,
        font=("Segoe UI", 30, "bold")
    )

        self.canvas.create_text(
        600,
        480,
        text="🐞 Ahora ya sabes qué hace un tester",
        fill=BLANCO,
        font=("Segoe UI", 18)
    )
        def reiniciar_juego(self):

            self.btn_reiniciar = tk.Button(
            self.root,
            text="🔄 Jugar de Nuevo",
            font=("Segoe UI", 16, "bold"),
            bg=AMARILLO,
            fg="black",
            command=self.reiniciar_juego
)

        self.canvas.create_window(
    self.ancho // 2,
    self.alto // 2 + 150,
    window=self.btn_reiniciar
)

# ==========================
# EJECUCIÓN
# ==========================

if __name__ == "__main__":

    root = tk.Tk()

    juego = InspectorPakova(root)

    root.mainloop()