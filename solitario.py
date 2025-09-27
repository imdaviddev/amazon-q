import random

class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor
        self.visible = False
    
    def __str__(self):
        if not self.visible:
            return "[?]"
        palos = {"♠": "♠", "♥": "♥", "♦": "♦", "♣": "♣"}
        valores = {1: "A", 11: "J", 12: "Q", 13: "K"}
        valor_str = valores.get(self.valor, str(self.valor))
        return f"{valor_str}{palos[self.palo]}"
    
    def es_roja(self):
        return self.palo in ["♥", "♦"]

class Solitario:
    def __init__(self):
        self.mazo = self.crear_mazo()
        self.tableau = [[] for _ in range(7)]
        self.fundaciones = [[] for _ in range(4)]
        self.descarte = []
        self.stock = []
        self.repartir_cartas()
    
    def crear_mazo(self):
        palos = ["♠", "♥", "♦", "♣"]
        cartas = []
        for palo in palos:
            for valor in range(1, 14):
                cartas.append(Carta(palo, valor))
        random.shuffle(cartas)
        return cartas
    
    def repartir_cartas(self):
        # Repartir cartas al tableau
        carta_idx = 0
        for col in range(7):
            for fila in range(col + 1):
                carta = self.mazo[carta_idx]
                if fila == col:  # Última carta visible
                    carta.visible = True
                self.tableau[col].append(carta)
                carta_idx += 1
        
        # Resto al stock
        self.stock = self.mazo[carta_idx:]
    
    def mostrar_juego(self):
        print("\n" + "="*60)
        print("SOLITARIO KLONDIKE")
        print("="*60)
        
        # Mostrar stock y descarte
        stock_str = f"[{len(self.stock)}]" if self.stock else "[ ]"
        descarte_str = str(self.descarte[-1]) if self.descarte else "[ ]"
        print(f"Stock: {stock_str}  Descarte: {descarte_str}")
        
        # Mostrar fundaciones
        print("\nFundaciones:")
        for i, fundacion in enumerate(self.fundaciones):
            carta_str = str(fundacion[-1]) if fundacion else "[ ]"
            print(f"F{i+1}: {carta_str}", end="  ")
        print()
        
        # Mostrar tableau
        print("\nTableau:")
        print("  1    2    3    4    5    6    7")
        
        max_cartas = max(len(col) for col in self.tableau) if any(self.tableau) else 0
        for fila in range(max_cartas):
            for col in range(7):
                if fila < len(self.tableau[col]):
                    print(f"{str(self.tableau[col][fila]):4}", end=" ")
                else:
                    print("    ", end=" ")
            print()
    
    def sacar_del_stock(self):
        if self.stock:
            carta = self.stock.pop()
            carta.visible = True
            self.descarte.append(carta)
        elif self.descarte:
            # Reiniciar stock desde descarte
            self.stock = self.descarte[::-1]
            for carta in self.stock:
                carta.visible = False
            self.descarte = []
    
    def puede_mover_a_fundacion(self, carta, fundacion_idx):
        fundacion = self.fundaciones[fundacion_idx]
        if not fundacion:
            return carta.valor == 1  # Solo As puede ir a fundación vacía
        return (carta.palo == fundacion[-1].palo and 
                carta.valor == fundacion[-1].valor + 1)
    
    def puede_mover_a_tableau(self, carta, col_destino):
        if not self.tableau[col_destino]:
            return carta.valor == 13  # Solo Rey puede ir a columna vacía
        
        carta_destino = self.tableau[col_destino][-1]
        return (carta.es_roja() != carta_destino.es_roja() and 
                carta.valor == carta_destino.valor - 1)
    
    def mover_carta(self, origen, destino):
        try:
            if origen.startswith('d'):  # Desde descarte
                if not self.descarte:
                    return False
                carta = self.descarte[-1]
                
                if destino.startswith('f'):  # A fundación
                    fund_idx = int(destino[1]) - 1
                    if self.puede_mover_a_fundacion(carta, fund_idx):
                        self.fundaciones[fund_idx].append(self.descarte.pop())
                        return True
                
                elif destino.startswith('t'):  # A tableau
                    col = int(destino[1]) - 1
                    if self.puede_mover_a_tableau(carta, col):
                        self.tableau[col].append(self.descarte.pop())
                        return True
            
            elif origen.startswith('t'):  # Desde tableau
                col_origen = int(origen[1]) - 1
                if not self.tableau[col_origen]:
                    return False
                
                carta = self.tableau[col_origen][-1]
                
                if destino.startswith('f'):  # A fundación
                    fund_idx = int(destino[1]) - 1
                    if self.puede_mover_a_fundacion(carta, fund_idx):
                        self.fundaciones[fund_idx].append(self.tableau[col_origen].pop())
                        self.revelar_carta_tableau(col_origen)
                        return True
                
                elif destino.startswith('t'):  # A tableau
                    col_destino = int(destino[1]) - 1
                    if col_origen != col_destino and self.puede_mover_a_tableau(carta, col_destino):
                        self.tableau[col_destino].append(self.tableau[col_origen].pop())
                        self.revelar_carta_tableau(col_origen)
                        return True
            
            return False
        except (ValueError, IndexError):
            return False
    
    def revelar_carta_tableau(self, col):
        if self.tableau[col] and not self.tableau[col][-1].visible:
            self.tableau[col][-1].visible = True
    
    def juego_ganado(self):
        return all(len(fundacion) == 13 for fundacion in self.fundaciones)
    
    def jugar(self):
        print("¡Bienvenido al Solitario Klondike!")
        print("\nComandos:")
        print("- 's': Sacar carta del stock")
        print("- 'mover [origen] [destino]': Mover carta")
        print("  Ejemplos: 'mover d f1', 'mover t1 t2', 'mover t3 f4'")
        print("- 'q': Salir")
        
        while True:
            self.mostrar_juego()
            
            if self.juego_ganado():
                print("\n¡FELICIDADES! ¡Has ganado el Solitario!")
                break
            
            comando = input("\nIngresa comando: ").strip().lower()
            
            if comando == 'q':
                break
            elif comando == 's':
                self.sacar_del_stock()
            elif comando.startswith('mover '):
                partes = comando.split()
                if len(partes) == 3:
                    if self.mover_carta(partes[1], partes[2]):
                        print("Movimiento exitoso!")
                    else:
                        print("Movimiento inválido.")
                else:
                    print("Formato: mover [origen] [destino]")
            else:
                print("Comando no reconocido.")

if __name__ == "__main__":
    juego = Solitario()
    juego.jugar()