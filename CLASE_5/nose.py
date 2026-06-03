import turtle
import random

# Configuración de pantalla
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Sígueme si puedes 👀")

# Crear la tortuga perseguidora
chaser = turtle.Turtle()
chaser.shape("circle")
chaser.color("cyan")
chaser.penup()
chaser.speed(0)

# Variable para guardar posición del mouse
target_x, target_y = 0, 0

# Función que actualiza la posición del mouse
def move_mouse(x, y):
    global target_x, target_y
    target_x = x
    target_y = y

screen.onscreenclick(move_mouse)

# Efecto de rastro divertido
trail = turtle.Turtle()
trail.hideturtle()
trail.speed(0)
trail.width(2)

colors = ["red", "yellow", "blue", "green", "purple", "orange"]

# Bucle de animación
def animate():
    chaser.setheading(chaser.towards(target_x, target_y))
    chaser.forward(3)

    # Dibujar rastro colorido
    trail.penup()
    trail.goto(chaser.position())
    trail.pendown()
    trail.pencolor(random.choice(colors))
    trail.dot(random.randint(5, 12))

    screen.update()
    screen.ontimer(animate, 20)

# Configuración inicial
screen.tracer(0)
animate()

turtle.done()