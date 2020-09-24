import FISIK as fsk

print(fsk.Cinematics(kind="mas", find="a", w=20, A=0.1, t=0.2))
print(fsk.convert(1000, From="meter", To="kilometer"))
print(fsk.gravity(radius=3389500, Planet="Mars"))
print(fsk.gravity())
print(fsk.Cinematics(kind="MAS", find="x", w=10, A = 0.5, t=0.01, angle0=50, Degree=True, cos=False))
print(fsk.Cinematics(kind="mcu", find="T", w=78))