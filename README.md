# ⚡ Calculadora de Consumo de Energia

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

## 📌 Sobre o Projeto

A **Calculadora de Consumo de Energia** é uma aplicação simples desenvolvida em Python para rodar via linha de comando (terminal). O objetivo do programa é ajudar os usuários a estimarem o consumo mensal de energia de diferentes aparelhos eletrodomésticos, além de calcular o custo em Reais ($R\$) associado a esse uso.

---

## ⚙️ Funcionalidades

- **Cálculo de Consumo:** Estimativa mensal do consumo em Quilowatts-hora ($kWh$).
- **Cálculo de Custo:** Estimativa financeira baseada em uma tarifa pré-definida ($R\$ 0,75/kWh$). 
- **Validação de Dados:** Trata erros de digitação caso o usuário insira valores inválidos.
- **Modo Contínuo:** Permite calcular múltiplos aparelhos em sequência sem precisar reiniciar o programa.

---

## 🧮 Fórmula Utilizada

O consumo mensal em kWh é calculado considerando um mês de **30 dias**:

$$\text{Consumo Mensal (kWh)} = \frac{\text{Potência (W)} \times \text{Horas de Uso Diário} \times 30}{1000}$$


---

## 🚀 Como utilizar o programa:

  Digite o nome do eletrodoméstico ou sair para encerrar o programa.
  
  Digite o consumo em Wats (W).
  
  Digite o tempo de consumo (horas).

  Caso queira calcular o uso de outro eletrodoméstico, basta digitar um novo.

