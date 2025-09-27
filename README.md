# 🃏 Solitario Klondike

El clásico juego de cartas donde debes organizar todas las cartas en las fundaciones.

## 📋 Descripción

El Solitario Klondike es el juego de cartas más popular del mundo. El objetivo es mover todas las 52 cartas a las 4 fundaciones en orden ascendente por palo.

## 🚀 Cómo ejecutar

### Versión Python:
```bash
python solitario.py
```

### Versión Web:
Abre `solitario.html` en tu navegador

## 🎯 Cómo jugar

1. **Objetivo:** Mover todas las cartas a las 4 fundaciones
2. **Fundaciones:** Orden ascendente por palo (A, 2, 3... K)
3. **Tableau:** 7 columnas, mover cartas alternando colores
4. **Stock:** Haz clic para sacar cartas del mazo
5. **Movimientos:** Solo cartas visibles, Rey a columna vacía

## ✨ Características

- 🎴 **Baraja completa** de 52 cartas mezcladas
- 🎯 **Lógica completa** del Klondike tradicional
- 🎨 **Interfaz visual** en la versión web
- 🔄 **Reinicio automático** del stock
- ✅ **Validación** de movimientos legales
- 🏆 **Detección automática** de victoria

## 🎪 Ejemplo de juego

```
SOLITARIO KLONDIKE
Stock: [24]  Descarte: [ ]

Fundaciones:
F1: [ ]  F2: [ ]  F3: [ ]  F4: [ ]

Tableau:
  1    2    3    4    5    6    7
 [?]  [?]  [?]  [?]  [?]  [?]  [?]
      [?]  [?]  [?]  [?]  [?]  [?]
           [?]  [?]  [?]  [?]  [?]

Comandos:
- 's': Sacar carta del stock
- 'mover d f1': Mover del descarte a fundación 1
- 'mover t1 t2': Mover de tableau 1 a tableau 2
```

## 🛠️ Requisitos

- **Python:** 3.6 o superior (versión de consola)
- **Web:** Cualquier navegador moderno
- **Sin dependencias externas**

## 📁 Estructura del proyecto

```
nerdearla/
├── solitario.py     # Solitario en Python
├── solitario.html   # Solitario web
└── README.md        # Este archivo
```

---

¡Disfruta de este clásico atemporal! 🎉