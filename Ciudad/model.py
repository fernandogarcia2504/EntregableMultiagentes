import mesa 
import random

class CalleNorte(mesa.Agent):  # noqa
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        super().__init__(unique_id, model)

    def __str__(self):
        return "Calle Norte"

    def step(self):
        pass

class CalleSur(mesa.Agent):  # noqa
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        super().__init__(unique_id, model)

    def posiblesVecinos(self):
        vecindario = self.model.grid.get_neighborhood(self.pos, include_center=False, moore=False)
        vecindario = [(x, y) for x, y in vecindario if
                        0 <= x < self.model.grid.width and 0 <= y < self.model.grid.height]
        vecinos = self.model.grid.get_cell_list_contents(vecindario)
        vecinos_calle = [False, False, False, False]
        for vecino in vecinos:
            x, y = vecino.pos
            if x < 0 or y < 0 or x > 23 or y > 23:
                pass
            else:
                if (vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Oeste" or vecino.__str__() == "Estacionamiento") and self.pos == (x + 1, y):
                    vecinos_calle[0] = True
                if (vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Este" or vecino.__str__() == "Estacionamiento") and self.pos == (x - 1, y):
                    vecinos_calle[1] = True
                if (vecino.__str__() == "Calle Sur" or vecino.__str__() == "Calle Este" or vecino.__str__() == "Calle Oeste" or vecino.__str__() == "Estacionamiento") and self.pos == (x, y + 1):
                    vecinos_calle[2] = True
        return vecinos_calle

    def __str__(self):
        return "Calle Sur"

    def step(self):
        pass

class CalleEste(mesa.Agent):  # noqa
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        super().__init__(unique_id, model)

    def __str__(self):
        return "Calle Este"

    def step(self):
        pass

class CalleOeste(mesa.Agent):  # noqa
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        super().__init__(unique_id, model)

    def __str__(self):
        return "Calle Oeste"

    def step(self):
        pass

class Estacionamiento(mesa.Agent):
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        super().__init__(unique_id, model)

    def __str__(self):
        return "Estacionamiento"

    def step(self):
        pass

class Banqueta(mesa.Agent):
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        super().__init__(unique_id, model)

    def __str__(self):
        return "Banqueta"

    def step(self):
        pass


class Edificio(mesa.Agent):
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        super().__init__(unique_id, model)

    def __str__(self):
        return "Edificio"

    def step(self):
        pass

class Ciudad(mesa.Model):
    def __init__(self,num_agents, width, height):
        super().__init__()
        self.num_agents = num_agents
        self.schedule = mesa.time.RandomActivation(self)
        self.grid = mesa.space.MultiGrid(width=width, height=height, torus=False)

        #Primeros 20 id para estacionamientos.

        banqueta = Banqueta(21,self)
        self.schedule.add(banqueta)

        edificio = Edificio(22, self)
        self.schedule.add(edificio)

#============================Orilla Oeste ========================

        for i in range(31):
            calle_sur = CalleSur(i + 23, self)
            self.schedule.add(calle_sur)
            self.grid.place_agent(calle_sur,(0, i + 1))
               
        for i in range(29):
            calle_sur = CalleSur(i + 54 , self)
            self.schedule.add(calle_sur)
            self.grid.place_agent(calle_sur, (1, i + 2))

#============================Orilla Sur ========================
        for i in range(31):
            calle_este = CalleEste(85 + i, self)
            self.schedule.add(calle_este)
            self.grid.place_agent(calle_este, (i, 0))

        for i in range(29):
            calle_este = CalleEste(116 + i, self)
            self.schedule.add(calle_este)
            self.grid.place_agent(calle_este, (i + 1, 1))

#============================Orilla Este ========================
        for i in range(31):
            calle_norte = CalleNorte(146 + i, self)
            self.schedule.add(calle_norte)
            self.grid.place_agent(calle_norte, (30, i))

        for i in range(29):
            calle_norte = CalleNorte(177 + i, self)
            self.schedule.add(calle_norte)
            self.grid.place_agent(calle_norte, (29, i + 1))

#============================Orilla Norte ========================
        for i in range(30):
            calle_oeste = CalleOeste(206 + i, self)
            self.schedule.add(calle_oeste)
            self.grid.place_agent(calle_oeste, (i + 1, 31))

        for i in range(29):
            calle_oeste = CalleOeste(236 + i, self)
            self.schedule.add(calle_oeste)
            self.grid.place_agent(calle_oeste, (i + 2, 30))

#============================Banquetas ========================
        for i in range(4):
            for j in range(17):
                self.grid.place_agent(banqueta, (j + 2, i + 26))

        for i in range(4):
            for j in range(8):
                self.grid.place_agent(banqueta, (j + 2, i + 20))

        for i in range(4):
            for j in range(8):
                self.grid.place_agent(banqueta, (j + 2, i + 14))

        for i in range(4):
            for j in range(8):
                self.grid.place_agent(banqueta, (j + 2, i + 8))

        for i in range(4):
            for j in range(8):
                self.grid.place_agent(banqueta, (j + 11, i + 8))

        for i in range(4):
            for j in range(8):
                self.grid.place_agent(banqueta, (j + 21, i + 8))

        for i in range(4):
            for j in range(8):
                self.grid.place_agent(banqueta, (j + 2, i + 2))

        for i in range(4):
            for j in range(8):
                self.grid.place_agent(banqueta, (j + 11, i + 2))

        for i in range(4):
            for j in range(8):
                self.grid.place_agent(banqueta, (j + 21, i + 2))

        for i in range(4):
            for j in range(8):
                self.grid.place_agent(banqueta, (j + 21, i + 14))

        #Banqueta sobrepuesta sobre calle norte
        for i in range(4):
            for j in range(10):
                self.grid.place_agent(banqueta, (j + 21, i + 20))

        for i in range(4):
            for j in range(8):
                self.grid.place_agent(banqueta, (j + 21, i + 26))

        for i in range(1):
            for j in range(2):
                self.grid.place_agent(banqueta, (j + 19, i + 29))

        for i in range(10):
            for j in range(8):
                self.grid.place_agent(banqueta, (j + 11, i + 14))


#============================ Edificios ========================

        for i in range(2):
            for j in range(7):
                self.grid.place_agent(edificio, (j + 3, i + 27))

        for i in range(2):
            for j in range(8):
                self.grid.place_agent(edificio, (j + 11, i + 27))

        for i in range(2):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 22, i + 27))

        for i in range(2):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 3, i + 21))

        for i in range(3):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 12, i + 20))

        for i in range(2):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 22, i + 21))

        for i in range(2):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 3, i + 15))

        for i in range(4):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 12, i + 15))

        for i in range(2):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 22, i + 15))

        for i in range(2):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 3, i + 9))

        for i in range(2):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 12, i + 9))

        for i in range(2):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 22, i + 9))

        for i in range(2):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 3, i + 3))

        for i in range(2):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 12, i + 3))

        for i in range(2):
            for j in range(6):
                self.grid.place_agent(edificio, (j + 22, i + 3))

#===================== Calles interiores =============================
        it = 0
        for i in range(2):
            for j in range(27):
                calle_este = CalleEste(265 + it, self)
                self.schedule.add(calle_este)
                self.grid.place_agent(calle_este, (j + 2, i + 24))
                it += 1

        it = 0
        for i in range(2):
            for j in range(27):
                calle_este = CalleEste(320 + it, self)
                self.schedule.add(calle_este)
                self.grid.place_agent(calle_este, (j + 2, i + 12))
                it += 1

        it = 0
        for i in range(2):
            for j in range(27):
                calle_oeste = CalleOeste(376 + it, self)
                self.schedule.add(calle_oeste)
                self.grid.place_agent(calle_oeste, (j + 2, i + 6))
                it += 1

        it = 0
        for i in range(2):
            for j in range(8):
                calle_oeste = CalleOeste(431 + it, self)
                self.schedule.add(calle_oeste)
                self.grid.place_agent(calle_oeste, (j + 2, i + 18))
                it += 1

        it = 0
        for i in range(22):
            for j in range(1):
                calle_norte = CalleNorte(449 + it, self)
                self.schedule.add(calle_norte)
                self.grid.place_agent(calle_norte, (j + 10, i + 2))
                it += 1


        it = 0
        for i in range(27):
            for j in range(2):
                calle_sur = CalleSur(473 + it, self)
                self.schedule.add(calle_sur)
                self.grid.place_agent(calle_sur, (j + 19, i + 2))
                it += 1


        it = 0
        for i in range(2):
            for j in range(8):
                calle_oeste = CalleOeste(527 + it, self)
                self.schedule.add(calle_oeste)
                self.grid.place_agent(calle_oeste, (j + 21, i + 18))
                it += 1


        


