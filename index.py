import numpy as np
from scipy.integrate import quad

class AerodinamicaPrandtl:
    def __init__(self, angulo_ataque_graus, AR, delta, tau, alpha_0_graus):
        self.angulo_ataque = np.radians(angulo_ataque_graus)  # Convertendo para radianos
        self.AR = AR  # Razão de Aspecto
        self.delta = delta  # Fator de arrasto induzido
        self.tau = tau  # Fator de inclinação da curva de sustentação
        self.alpha_0 = np.radians(alpha_0_graus)  # Ângulo de ataque de sustentação zero em radianos

    def inclinacao_sustentacao(self):
        """Calcula a inclinação da curva de sustentação para uma asa finita."""
        a0 = 2 * np.pi  # Assumindo a0 = 2π para teoria do perfil fino
        return a0 / (1 + (a0 / (np.pi * self.AR)) * (1 + self.tau))

    def coeficiente_sustentacao(self, a):
        """Calcula o coeficiente de sustentação para um ângulo de ataque específico."""
        return a * (self.angulo_ataque - self.alpha_0)

    def coeficiente_arrasto_induzido(self, CL):
        """Calcula o coeficiente de arrasto induzido com base no coeficiente de sustentação."""
        # Integrando ao longo da envergadura da asa
        CDi_integrado, _ = quad(lambda y: CL**2 / (np.pi * self.AR * (1 + self.delta)), -self.AR/2, self.AR/2)
        return CDi_integrado / self.AR  # Dividindo pelo span para obter o CDi

    def calcular_resultados(self):
        """Realiza os cálculos e retorna os resultados."""
        a = self.inclinacao_sustentacao()
        CL = self.coeficiente_sustentacao(a)
        CDi = self.coeficiente_arrasto_induzido(CL)
        return CL, CDi

# Exemplo 1 com AR=8, delta=tau=0.055, alpha_0=0 graus, angulo_ataque=5 graus
aero_exemplo1 = AerodinamicaPrandtl(angulo_ataque_graus=5, AR=8, delta=0.055, tau=0.055, alpha_0_graus=0)
CL_exemplo1, CDi_exemplo1 = aero_exemplo1.calcular_resultados()

# Exemplo 2 com AR=10, delta=tau=0.105, alpha_0=-2 graus, angulo_ataque=3.4 graus
aero_exemplo2 = AerodinamicaPrandtl(angulo_ataque_graus=3.4
                                    , AR=10
                                    , delta=0.105
                                    , tau=0.105
                                    , alpha_0_graus=-2)
CL_exemplo2, CDi_exemplo2 = aero_exemplo2.calcular_resultados()


print(CL_exemplo1)
print(CDi_exemplo1)
print(CL_exemplo2)
print(CDi_exemplo2)
