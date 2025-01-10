# Importamos las cosas que necesitamos para que el juego funcione.
# QApplication:
#
# Función : Es el punto de entrada a cualquier aplicación PyQt5. Sin esta clase, no podríamos crear una aplicación gráfica. Aquí, se utiliza en el bloque if __name__ == "__main__":para crear la aplicación que manejará la ventana del juego.
# Uso en el código : Se usa para iniciar la aplicación gráfica con app = QApplication([]), lo que permite que se inicie la interfaz del juego.
# QWidget:
#
# Función : Es el contenedor base para todos los elementos visuales en PyQt. Básicamente, cualquier ventana o área interactiva en una aplicación PyQt se construye sobre QWidgetsus subclases.
# Uso en el código : Ahorcadohereda de QWidget, lo que significa que Ahorcadoes una ventana o un contenedor de widgets. Esto permite que se construyan los elementos visuales del juego dentro de la ventana de la aplicación.
# QLabel:
#
# Función : Se utiliza para mostrar texto en la interfaz gráfica. Puede ser cualquier texto estático o dinámico.
# Uso en el código : En el juego, se usa para mostrar el progreso del jugador (las letras adivinadas y los guiones bajos) y el número de intentos restantes.
# Ejemplo de uso: self.label_progreso = QLabel(" ".join(self.progreso), self)y self.label_intentos = QLabel(f"Intentos restantes: {self.intentos_restantes}", self).
# QLineEdit:
#
# Función : Permite al usuario ingresar texto (en este caso, una letra) a través de un campo de entrada.
# Uso en el código : Se usa para que el jugador ingrese una letra que cree que forma parte de la palabra secreta. En el código, se define como self.input_letra = QLineEdit(self).
# QPushButton:
#
# Función : Representa un botón en la interfaz. Los botones pueden tener acciones asociadas cuando se hacen clic.
# Uso en el código : Se utiliza para crear el botón "Adivinar", que cuando es presionado, activa el proceso de verificación si la letra ingresada está en la palabra secreta. Esto se conecta con self.boton_verificar.clicked.connect(self.verificar_letra).
# QVBoxLayout:
#
# Función : Es un tipo de diseño que organiza los widgets (componentes de la interfaz gráfica) en una columna vertical.
# Uso en el código : En este caso, se utiliza para organizar los diferentes elementos del juego (las etiquetas con el progreso, los intentos restantes, el campo de texto para ingresar una letra y el botón para adivinar) uno debajo del otro.
# Ejemplo: layout = QVBoxLayout()y luego se añaden los widgets con layout.addWidget(...).
# QMessageBox:
#
# Función : Es un cuadro de diálogo emergente que se utiliza para mostrar mensajes al usuario. Puede ser un mensaje de advertencia, información o error.
# Uso en el código :
# QMessageBox.warning: Se utiliza para anunciar al jugador si no ha ingresado una letra o ha ingresado más de una letra. Ejemplo: QMessageBox.warning(self, "Advertencia", "Por favor, ingresa solo una letra.").
# QMessageBox.information: Muestra un mensaje cuando el jugador adivina la palabra correctamente. Ejemplo: QMessageBox.information(self, "¡Ganaste!", f"¡Adivinaste la palabra: {''.join(self.progreso)}!").
# QMessageBox.critical: Muestra un mensaje cuando el jugador pierde, indicando que se ha quedado sin intentos. Ejemplo: QMessageBox.critical(self, "¡Perdiste!", f"La palabra era: {self.palabra_secreta}").

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import random  # Esta es como una "caja mágica" que nos ayuda a elegir cosas al azar.

# Creamos una lista con palabras que el jugador debe adivinar.
PALABRAS = ["python", "computadora", "programar", "juego", "teclado"]

# Aquí hacemos una clase, como una receta, que construirá el juego.
class Ahorcado(QWidget):
    def __init__(self):
        # Esta línea es como decirle a la receta que empiece a cocinar.
        super().__init__()

        # Elegimos una palabra al azar de nuestra lista.
        self.palabra_secreta = random.choice(PALABRAS)
        # Aquí ponemos guiones bajos (_) para cada letra de la palabra secreta.
        self.progreso = ["_"] * len(self.palabra_secreta)
        # Este es un número que cuenta cuántos intentos nos quedan.
        self.intentos_restantes = 6

        # Aquí empezamos a construir la ventana del juego.
        self.initUI()

    # Este método crea y organiza las cosas en la ventana (botones, texto, etc.).
    def initUI(self):
        # Ponemos un título en la ventana para saber qué estamos jugando.
        self.setWindowTitle("Juego del Ahorcado")

        # Creamos una etiqueta que muestra cómo vamos en el juego (los guiones bajos y letras adivinadas).
        self.label_progreso = QLabel(" ".join(self.progreso), self)

        # Creamos otra etiqueta que le dice al jugador cuántos intentos le quedan.
        self.label_intentos = QLabel(f"Intentos restantes: {self.intentos_restantes}", self)

        # Este es un cuadro donde el jugador escribe una letra.
        self.input_letra = QLineEdit(self)
        self.input_letra.setPlaceholderText("Ingresa una letra")  # Le decimos qué escribir.

        # Creamos un botón para que el jugador confirme la letra que escribió.
        self.boton_verificar = QPushButton("Adivinar", self)
        self.boton_verificar.clicked.connect(self.verificar_letra)  # Esto dice: "Cuando hagas clic, revisa la letra".

        # Organizamos todo con un diseño vertical (todo se pone uno debajo de otro).
        layout = QVBoxLayout()
        layout.addWidget(self.label_progreso)  # Añadimos el texto de los guiones bajos.
        layout.addWidget(self.label_intentos)  # Añadimos el texto de los intentos.
        layout.addWidget(self.input_letra)  # Añadimos el cuadro de texto.
        layout.addWidget(self.boton_verificar)  # Añadimos el botón.

        # Aplicamos este diseño a la ventana principal.
        self.setLayout(layout)

    # Este método se llama cada vez que el jugador presiona el botón "Adivinar".
    def verificar_letra(self):
        # Aquí leemos la letra que el jugador escribió.
        letra = self.input_letra.text().lower()

        # Si no escribió nada o más de una letra, le mostramos un mensaje de error.
        if len(letra) != 1:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingresa solo una letra.")
            return  # Salimos de esta función y no seguimos.

        # Ahora revisamos si la letra está en la palabra secreta.
        if letra in self.palabra_secreta:
            # Si la letra está, la ponemos en los lugares correctos.
            for i in range(len(self.palabra_secreta)):
                if self.palabra_secreta[i] == letra:
                    self.progreso[i] = letra
        else:
            # Si no está, le quitamos un intento al jugador.
            self.intentos_restantes -= 1

        # Actualizamos el texto en la pantalla para mostrar el progreso y los intentos restantes.
        self.label_progreso.setText(" ".join(self.progreso))
        self.label_intentos.setText(f"Intentos restantes: {self.intentos_restantes}")

        # Limpiamos el cuadro de texto para que el jugador pueda escribir otra letra.
        self.input_letra.clear()

        # Si el jugador adivina toda la palabra, mostramos un mensaje de victoria.
        if "_" not in self.progreso:
            QMessageBox.information(self, "¡Ganaste!", f"¡Adivinaste la palabra: {''.join(self.progreso)}!")
            self.reiniciar_juego()  # Reiniciamos el juego.

        # Si se queda sin intentos, mostramos un mensaje de derrota.
        elif self.intentos_restantes == 0:
            QMessageBox.critical(self, "¡Perdiste!", f"La palabra era: {self.palabra_secreta}")
            self.reiniciar_juego()  # Reiniciamos el juego.

    # Este método reinicia el juego cuando el jugador gana o pierde.
    def reiniciar_juego(self):
        # Elegimos una nueva palabra secreta.
        self.palabra_secreta = random.choice(PALABRAS)
        # Reiniciamos los guiones bajos.
        self.progreso = ["_"] * len(self.palabra_secreta)
        # Volvemos a poner los intentos en 6.
        self.intentos_restantes = 6

        # Actualizamos las etiquetas para empezar de nuevo.
        self.label_progreso.setText(" ".join(self.progreso))
        self.label_intentos.setText(f"Intentos restantes: {self.intentos_restantes}")

# Este es el inicio del programa. Aquí es donde comienza todo.
if __name__ == "__main__":
    # Creamos la aplicación, que es como la caja donde pondremos el juego.
    app = QApplication([])

    # Creamos una ventana del juego usando nuestra receta llamada "Ahorcado".
    ventana = Ahorcado()
    # Mostramos la ventana en la pantalla.
    ventana.show()

    # Este es un bucle que mantiene la ventana abierta y funcionando.
    app.exec_()
