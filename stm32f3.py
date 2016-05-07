#-----------------------------------------------------------------------------
"""

SoC file for stm32f3x devices

"""
#-----------------------------------------------------------------------------

import cortexm

#-----------------------------------------------------------------------------
# SoC Exception Tables
# irq_number : name

# Table 81. STM32F303xB/C/D/E, STM32F358xC and STM32F398xE vector table
soc_vector_table0 = {
}

# Table 82. STM32F303x6/8and STM32F328x8 vector table
soc_vector_table1 = {
  0: 'WWDG',
  1: 'PVD',
  2: 'TAMPER_STAMP',
  3: 'RTC_WKUP',
  4: 'FLASH',
  5: 'RCC',
  6: 'EXTI0',
  7: 'EXTI1',
  8: 'EXTI2_TS',
  9: 'EXTI3',
  10: 'EXTI4',
  11: 'DMA1_Channel1',
  12: 'DMA1_Channel2',
  13: 'DMA1_Channel3',
  14: 'DMA1_Channel4',
  15: 'DMA1_Channel5',
  16: 'DMA1_Channel6',
  17: 'DMA1_Channel7',
  18: 'ADC1_2',
  19: 'CAN_TX',
  20: 'CAN_RX0',
  21: 'CAN_RX1',
  22: 'CAN_SCE',
  23: 'EXTI9_5',
  24: 'TIM1_BRK/TIM15',
  25: 'TIM1_UP/TIM16',
  26: 'TIM1_TRG_COM/TIM17',
  27: 'TIM1_CC',
  28: 'TIM2',
  29: 'TIM3',
  31: 'I2C1_EV',
  32: 'I2C1_ER',
  35: 'SPI1',
  37: 'USART1',
  38: 'USART2',
  39: 'USART3',
  40: 'EXTI15_10',
  41: 'RTC_Alarm',
  54: 'TIM6_DAC1',
  55: 'TIM7_DAC2',
  64: 'COMP2',
  65: 'COMP4_6',
  81: 'FPU',
}

#-----------------------------------------------------------------------------

class soc(object):
  """stm32f3x SoC"""

  def __init__(self, cpu, device):
    self.cpu = cpu
    self.menu = (
      ('exceptions', 'show exception status', self.cmd_exceptions),
    )

    if device == 'STM32F303VCT6':
      self.exceptions = cortexm.build_exceptions(soc_vector_table1)
      self.priority_bits = 4
    else:
      assert False, 'unknown SoC device %s' % device

  def cmd_exceptions(self, ui, args):
    """display the exceptions table"""
    ui.put('%s\n' % cortexm.exceptions_str(self.cpu, self))

#-----------------------------------------------------------------------------