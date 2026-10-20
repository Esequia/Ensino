#!/usr/bin/env python3
"""Gera os gráficos da questão 4 da variante A2. Execute: python3 pics/gerar_graficos_A2.py.

Dependência: matplotlib. Os arquivos são salvos junto desta rotina.
As derivadas são tomadas em t > 0: não há impulso na origem.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    plt.rcParams.update({"font.family": "DejaVu Serif", "font.size": 11,
                         "mathtext.fontset": "dejavuserif", "pdf.fonttype": 42,
                         "ps.fonttype": 42})
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 3.1), layout="constrained")
    for ax in axes:
        ax.spines[["top", "right"]].set_visible(False)
        ax.spines["bottom"].set_position("zero")
        ax.spines["left"].set_position("zero")
        ax.set_xlim(-0.35, 9)
        ax.set_xticks([0, 3, 6, 9])
        ax.set_xlabel("$t$", loc="right")
        ax.tick_params(direction="out")

    ax = axes[0]
    ax.plot([0, 3, 6, 9], [0, -3, 0, 0], color="black", lw=1.8)
    ax.set_ylim(-3.6, 0.7)
    ax.set_yticks([-3, -2, -1])
    ax.set_title("$f(t)$")

    ax = axes[1]
    for left, right, height in [(0, 3, -1), (3, 6, 1), (6, 9, 0)]:
        ax.plot([left, right], [height, height], color="black", lw=1.8)
    # Círculos abertos: os valores nos pontos de salto não são especificados.
    ax.plot([0, 3, 3, 6, 6], [-1, -1, 1, 1, 0], "o", color="black",
            markerfacecolor="white", markersize=5, zorder=4)
    ax.set_ylim(-1.65, 1.65)
    ax.set_yticks([-1, 1])
    ax.set_title("$f'(t)$")

    ax = axes[2]
    ax.set_ylim(-1.65, 2.65)
    ax.set_yticks([])
    ax.set_title("$f''(t)$")
    for position, weight in [(3, 2), (6, -1)]:
        ax.annotate("", xy=(position, weight), xytext=(position, 0),
                    arrowprops={"arrowstyle": "-|>", "color": "black",
                                "lw": 1.8, "mutation_scale": 14})
        ax.annotate(f"${weight}$", xy=(position, weight), xytext=(7, 0),
                    textcoords="offset points", va="center")
    ax.text(0.5, 0.02, "Setas: pesos dos impulsos", transform=ax.transAxes,
            ha="center", fontsize=9)
    destination = Path(__file__).resolve().parent
    for extension in ("eps", "pdf"):
        filename = destination / f"questao4_A2_gabarito.{extension}"
        fig.savefig(filename, bbox_inches="tight", metadata={"Creator": "Matplotlib"})
        print(filename)
    plt.close(fig)


if __name__ == "__main__":
    main()

