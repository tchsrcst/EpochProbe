import matplotlib.pyplot as plt
from src.core.utils import calculator
from src.core.data import input


def plot_calc(_axs, calc, color):
    _axs[0, 0].plot(calc.x, calc.y[0], color, label=calc.name)
    _axs[0, 1].plot(calc.x, calc.y[1], color, label=calc.name)
    _axs[0, 2].plot(calc.x, calc.y[2], color, label=calc.name)
    _axs[0, 3].plot(calc.x, calc.y[3], color, label=calc.name)
    _axs[1, 0].plot(calc.x, calc.y[4], color, label=calc.name)
    _axs[1, 1].plot(calc.x, calc.y[5], color, label=calc.name)
    _axs[1, 2].plot(calc.x, calc.y[6], color, label=calc.name)
    _axs[1, 3].plot(calc.x, calc.y[7], color, label=calc.name)
    _axs[2, 0].plot(calc.x, calc.y[8], color, label=calc.name)
    _axs[2, 1].plot(calc.x, calc.y[9], color, label=calc.name)
    _axs[2, 2].plot(calc.x, calc.y[10], color, label=calc.name)
    _axs[2, 3].plot(calc.x, calc.y[11], color, label=calc.name)


def main(_skill, _base, _scenario):
    calc1 = calculator.Calculator(_skill, input.InputBase, _scenario)
    calc1.print()
    calc1.compute(True)

    calc2 = calculator.Calculator(_skill, input.InputChanceToIgniteOnHit, _scenario)
    calc2.compute(False)

    calc3 = calculator.Calculator(_skill, input.InputElementalDot, _scenario)
    calc3.compute(False)

    calc4 = calculator.Calculator(_skill, input.InputCastSpeed, _scenario)
    calc4.compute(False)

    calc5 = calculator.Calculator(_skill, input.InputSpellCriticalStrikeChance, _scenario)
    calc5.compute(False)

    calc6 = calculator.Calculator(_skill, input.InputCriticalStrikeMultiplier, _scenario)
    calc6.compute(False)

    figure, axs = plt.subplots(3, 4, figsize=(18, 8))
    figure.tight_layout(pad=5.0)
    figure.suptitle('Damage Calculator - ' + _skill.name, fontsize=10)

    axs[0, 0].set_title('Hits Inflicted')
    axs[0, 0].set_xlabel('Time, sec.')
    axs[0, 0].grid(True)
    axs[0, 1].set_title('Ignites Inflicted')
    axs[0, 1].set_xlabel('Time, sec.')
    axs[0, 1].grid(True)
    axs[0, 2].set_title('Total Hit Damage')
    axs[0, 2].set_xlabel('Time, sec.')
    axs[0, 2].grid(True)
    axs[0, 3].set_title('Total Ignite Damage')
    axs[0, 3].set_xlabel('Time, sec.')
    axs[0, 3].grid(True)

    axs[1, 0].set_title('Total Combined Damage')
    axs[1, 0].set_xlabel('Time, sec.')
    axs[1, 0].grid(True)
    axs[1, 1].set_title('Simplified DPS')
    axs[1, 1].set_xlabel('Time, sec.')
    axs[1, 1].grid(True)
    axs[1, 2].set_title('Simulated Current Ignite Stacks')
    axs[1, 2].set_xlabel('Time, sec.')
    axs[1, 2].grid(True)
    axs[1, 3].set_title('Simulated Crits')
    axs[1, 3].set_xlabel('Time, sec.')
    axs[1, 3].grid(True)

    axs[2, 0].set_title('Simulated Total Hit Damage')
    axs[2, 0].set_xlabel('Time, sec.')
    axs[2, 0].grid(True)
    axs[2, 1].set_title('Simulated Total Ignite Damage')
    axs[2, 1].set_xlabel('Time, sec.')
    axs[2, 1].grid(True)
    axs[2, 2].set_title('Simulated Total Combined Damage')
    axs[2, 2].set_xlabel('Time, sec.')
    axs[2, 2].grid(True)
    axs[2, 3].set_title('Simulated DPS')
    axs[2, 3].set_xlabel('Time, sec.')
    axs[2, 3].grid(True)

    plot_calc(axs, calc1, 'b-')
    plot_calc(axs, calc2, 'r-')
    plot_calc(axs, calc3, 'g-')
    plot_calc(axs, calc4, 'y-')
    plot_calc(axs, calc5, 'c-')
    plot_calc(axs, calc6, 'm-')

    axs[0, 0].legend(loc="upper left", prop={'size': 6})
    axs[0, 1].legend(loc="upper left", prop={'size': 6})
    axs[0, 2].legend(loc="upper left", prop={'size': 6})
    axs[0, 3].legend(loc="upper left", prop={'size': 6})
    axs[1, 0].legend(loc="upper left", prop={'size': 6})
    axs[1, 1].legend(loc="upper left", prop={'size': 6})
    axs[1, 2].legend(loc="upper left", prop={'size': 6})
    axs[1, 3].legend(loc="upper left", prop={'size': 6})
    axs[2, 0].legend(loc="upper left", prop={'size': 6})
    axs[2, 1].legend(loc="upper left", prop={'size': 6})
    axs[2, 2].legend(loc="upper left", prop={'size': 6})

    plt.show()
