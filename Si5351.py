
from Adafruit_I2C import Adafruit_I2C
import smbus
import time

SI5351_REGISTER_0_DEVICE_STATUS                       = 0
SI5351_REGISTER_1_INTERRUPT_STATUS_STICKY             = 1
SI5351_REGISTER_2_INTERRUPT_STATUS_MASK               = 2
SI5351_REGISTER_3_OUTPUT_ENABLE_CONTROL               = 3
SI5351_REGISTER_9_OEB_PIN_ENABLE_CONTROL              = 9
SI5351_REGISTER_15_PLL_INPUT_SOURCE                   = 15
SI5351_REGISTER_16_CLK0_CONTROL                       = 16
SI5351_REGISTER_17_CLK1_CONTROL                       = 17
SI5351_REGISTER_18_CLK2_CONTROL                       = 18
SI5351_REGISTER_19_CLK3_CONTROL                       = 19
SI5351_REGISTER_20_CLK4_CONTROL                       = 20
SI5351_REGISTER_21_CLK5_CONTROL                       = 21
SI5351_REGISTER_22_CLK6_CONTROL                       = 22
SI5351_REGISTER_23_CLK7_CONTROL                       = 23
SI5351_REGISTER_24_CLK3_0_DISABLE_STATE               = 24
SI5351_REGISTER_25_CLK7_4_DISABLE_STATE               = 25
SI5351_REGISTER_42_MULTISYNTH0_PARAMETERS_1           = 42
SI5351_REGISTER_43_MULTISYNTH0_PARAMETERS_2           = 43
SI5351_REGISTER_44_MULTISYNTH0_PARAMETERS_3           = 44
SI5351_REGISTER_45_MULTISYNTH0_PARAMETERS_4           = 45
SI5351_REGISTER_46_MULTISYNTH0_PARAMETERS_5           = 46
SI5351_REGISTER_47_MULTISYNTH0_PARAMETERS_6           = 47
SI5351_REGISTER_48_MULTISYNTH0_PARAMETERS_7           = 48
SI5351_REGISTER_49_MULTISYNTH0_PARAMETERS_8           = 49
SI5351_REGISTER_50_MULTISYNTH1_PARAMETERS_1           = 50
SI5351_REGISTER_51_MULTISYNTH1_PARAMETERS_2           = 51
SI5351_REGISTER_52_MULTISYNTH1_PARAMETERS_3           = 52
SI5351_REGISTER_53_MULTISYNTH1_PARAMETERS_4           = 53
SI5351_REGISTER_54_MULTISYNTH1_PARAMETERS_5           = 54
SI5351_REGISTER_55_MULTISYNTH1_PARAMETERS_6           = 55
SI5351_REGISTER_56_MULTISYNTH1_PARAMETERS_7           = 56
SI5351_REGISTER_57_MULTISYNTH1_PARAMETERS_8           = 57
SI5351_REGISTER_58_MULTISYNTH2_PARAMETERS_1           = 58
SI5351_REGISTER_59_MULTISYNTH2_PARAMETERS_2           = 59
SI5351_REGISTER_60_MULTISYNTH2_PARAMETERS_3           = 60
SI5351_REGISTER_61_MULTISYNTH2_PARAMETERS_4           = 61
SI5351_REGISTER_62_MULTISYNTH2_PARAMETERS_5           = 62
SI5351_REGISTER_63_MULTISYNTH2_PARAMETERS_6           = 63
SI5351_REGISTER_64_MULTISYNTH2_PARAMETERS_7           = 64
SI5351_REGISTER_65_MULTISYNTH2_PARAMETERS_8           = 65
SI5351_REGISTER_66_MULTISYNTH3_PARAMETERS_1           = 66
SI5351_REGISTER_67_MULTISYNTH3_PARAMETERS_2           = 67
SI5351_REGISTER_68_MULTISYNTH3_PARAMETERS_3           = 68
SI5351_REGISTER_69_MULTISYNTH3_PARAMETERS_4           = 69
SI5351_REGISTER_70_MULTISYNTH3_PARAMETERS_5           = 70
SI5351_REGISTER_71_MULTISYNTH3_PARAMETERS_6           = 71
SI5351_REGISTER_72_MULTISYNTH3_PARAMETERS_7           = 72
SI5351_REGISTER_73_MULTISYNTH3_PARAMETERS_8           = 73
SI5351_REGISTER_74_MULTISYNTH4_PARAMETERS_1           = 74
SI5351_REGISTER_75_MULTISYNTH4_PARAMETERS_2           = 75
SI5351_REGISTER_76_MULTISYNTH4_PARAMETERS_3           = 76
SI5351_REGISTER_77_MULTISYNTH4_PARAMETERS_4           = 77
SI5351_REGISTER_78_MULTISYNTH4_PARAMETERS_5           = 78
SI5351_REGISTER_79_MULTISYNTH4_PARAMETERS_6           = 79
SI5351_REGISTER_80_MULTISYNTH4_PARAMETERS_7           = 80
SI5351_REGISTER_81_MULTISYNTH4_PARAMETERS_8           = 81
SI5351_REGISTER_82_MULTISYNTH5_PARAMETERS_1           = 82
SI5351_REGISTER_83_MULTISYNTH5_PARAMETERS_2           = 83
SI5351_REGISTER_84_MULTISYNTH5_PARAMETERS_3           = 84
SI5351_REGISTER_85_MULTISYNTH5_PARAMETERS_4           = 85
SI5351_REGISTER_86_MULTISYNTH5_PARAMETERS_5           = 86
SI5351_REGISTER_87_MULTISYNTH5_PARAMETERS_6           = 87
SI5351_REGISTER_88_MULTISYNTH5_PARAMETERS_7           = 88
SI5351_REGISTER_89_MULTISYNTH5_PARAMETERS_8           = 89
SI5351_REGISTER_90_MULTISYNTH6_PARAMETERS             = 90
SI5351_REGISTER_91_MULTISYNTH7_PARAMETERS             = 91
SI5351_REGISTER_092_CLOCK_6_7_OUTPUT_DIVIDER          = 92
SI5351_REGISTER_165_CLK0_INITIAL_PHASE_OFFSET         = 165
SI5351_REGISTER_166_CLK1_INITIAL_PHASE_OFFSET         = 166
SI5351_REGISTER_167_CLK2_INITIAL_PHASE_OFFSET         = 167
SI5351_REGISTER_168_CLK3_INITIAL_PHASE_OFFSET         = 168
SI5351_REGISTER_169_CLK4_INITIAL_PHASE_OFFSET         = 169
SI5351_REGISTER_170_CLK5_INITIAL_PHASE_OFFSET         = 170
SI5351_REGISTER_177_PLL_RESET                         = 177
SI5351_REGISTER_183_CRYSTAL_INTERNAL_LOAD_CAPACITANCE = 183

SI5351_I2C_ADDRESS_DEFAULT = 0x60

SI5351_CRYSTAL_LOAD_6PF  = (1<<6)
SI5351_CRYSTAL_LOAD_8PF  = (2<<6)
SI5351_CRYSTAL_LOAD_10PF = (3<<6)

SI5351_CRYSTAL_FREQ_25MHZ = 25000000
SI5351_CRYSTAL_FREQ_27MHZ = 27000000


class Si5351(object):

    PLL_A = 0
    PLL_B = 1

    R_DIV_1   = 0
    R_DIV_2   = 1
    R_DIV_4   = 2
    R_DIV_8   = 3
    R_DIV_16  = 4
    R_DIV_32  = 5
    R_DIV_64  = 6
    R_DIV_128 = 7


    def __init__(self, address = SI5351_I2C_ADDRESS_DEFAULT, busnum=-1):

        self.crystalFreq     = SI5351_CRYSTAL_FREQ_25MHZ
        self.crystalLoad     = SI5351_CRYSTAL_LOAD_10PF
        self.crystalPPM      = 30
        self.plla_freq       = 0
        self.pllb_freq       = 0

        self.i2c = Adafruit_I2C(address=address, busnum=busnum)
        self.address = address

        # Disable all outputs setting CLKx_DIS high
        self.i2c.write8(SI5351_REGISTER_3_OUTPUT_ENABLE_CONTROL, 0xFF)

        # Power down all output drivers
        self.i2c.write8(SI5351_REGISTER_16_CLK0_CONTROL, 0x80)
        self.i2c.write8(SI5351_REGISTER_17_CLK1_CONTROL, 0x80)
        self.i2c.write8(SI5351_REGISTER_18_CLK2_CONTROL, 0x80)
        self.i2c.write8(SI5351_REGISTER_19_CLK3_CONTROL, 0x80)
        self.i2c.write8(SI5351_REGISTER_20_CLK4_CONTROL, 0x80)
        self.i2c.write8(SI5351_REGISTER_21_CLK5_CONTROL, 0x80)
        self.i2c.write8(SI5351_REGISTER_22_CLK6_CONTROL, 0x80)
        self.i2c.write8(SI5351_REGISTER_23_CLK7_CONTROL, 0x80)

        # Set the load capacitance for the XTAL
        self.i2c.write8(SI5351_REGISTER_183_CRYSTAL_INTERNAL_LOAD_CAPACITANCE, self.crystalLoad)


    def setupPLL(self, pll, mult, num=0, denom=1):

        # @brief  Sets the multiplier for the specified PLL
        # @param  pll   The PLL to configure, which must be one of the following:
        #               - SI5351_PLL_A
        #               - SI5351_PLL_B
        # @param  mult  The PLL integer multiplier (must be between 15 and 90)
        # @param  num   The 20-bit numerator for fractional output (0..1,048,575).
        #               Set this to '0' for integer output.
        # @param  denom The 20-bit denominator for fractional output (1..1,048,575).
        #               Set this to '1' or higher to avoid divider by zero errors.
        # @section PLL Configuration
        #     fVCO is the PLL output, and must be between 600..900MHz, where:
        #     fVCO = fXTAL * (a+(b/c))
        #     fXTAL = the crystal input frequency
        #     a     = an integer between 15 and 90
        #     b     = the fractional numerator (0..1,048,575)
        #     c     = the fractional denominator (1..1,048,575)
        # @note Try to use integers whenever possible to avoid clock jitter
        #     (only use the a part, setting b to '0' and c to '1').
        #     See: http://www.silabs.com/Support%20Documents/TechnicalDocs/AN619.pdf
        #
        # Feedback Multisynth Divider Equation
        # where: a = mult, b = num and c = denom
        # P1[17:0] = 128 * mult + floor(128*(num/denom)) - 512
        # P2[19:0] = 128 * num - denom * floor(128*(num/denom))
        # P3[19:0] = denom

        # Set the main PLL config registers
        P1 = 128 * mult + int(128.0 * num / denom) - 512
        P2 = 128 * num - denom * int(128.0 * num / denom)
        P3 = denom

        # Get the appropriate starting point for the PLL registers
        baseaddr = 26 if pll == self.PLL_A else 34

        # The datasheet is a nightmare of typos and inconsistencies here!
        self.i2c.write8(baseaddr,   (P3 & 0x0000FF00) >> 8)
        self.i2c.write8(baseaddr + 1, (P3 & 0x000000FF))
        self.i2c.write8(baseaddr + 2, (P1 & 0x00030000) >> 16)
        self.i2c.write8(baseaddr + 3, (P1 & 0x0000FF00) >> 8)
        self.i2c.write8(baseaddr + 4, (P1 & 0x000000FF))
        self.i2c.write8(baseaddr + 5, ((P3 & 0x000F0000) >> 12) | ((P2 & 0x000F0000) >> 16) )
        self.i2c.write8(baseaddr + 6, (P2 & 0x0000FF00) >> 8)
        self.i2c.write8(baseaddr + 7, (P2 & 0x000000FF))

        # Reset both PLLs
        self.i2c.write8(SI5351_REGISTER_177_PLL_RESET, (1<<7) | (1<<5))

        # Store the frequency settings for use with the Multisynth helper
        fvco = int(self.crystalFreq * (mult + float(num) / denom))
        if pll == self.PLL_A:
            self.plla_freq = fvco
        else:
            self.pllb_freq = fvco


    def setupRdiv(self, output, div):

        if output == 0: Rreg = SI5351_REGISTER_44_MULTISYNTH0_PARAMETERS_3
        if output == 1: Rreg = SI5351_REGISTER_52_MULTISYNTH1_PARAMETERS_3
        if output == 2: Rreg = SI5351_REGISTER_60_MULTISYNTH2_PARAMETERS_3
        return self.i2c.write8(Rreg, (div & 0x07) << 4)


    def setupMultisynth(self, output, pll, div, num=0, denom=1):

        # @brief  Configures the Multisynth divider, which determines the
        #         output clock frequency based on the specified PLL input.
        # 
        # @param  output    The output channel to use (0..2)
        # @param  pll       The PLL input source to use, which must be one of:
        #                   - SI5351_PLL_A
        #                   - SI5351_PLL_B
        # @param  div       The integer divider for the Multisynth output.
        #                   If pure integer values are used, this value must
        #                   be one of:
        #                   - SI5351_MULTISYNTH_DIV_4
        #                   - SI5351_MULTISYNTH_DIV_6
        #                   - SI5351_MULTISYNTH_DIV_8
        #                   If fractional output is used, this value must be
        #                   between 8 and 900.
        # @param  num       The 20-bit numerator for fractional output
        #                   (0..1,048,575). Set this to '0' for integer output.
        # @param  denom     The 20-bit denominator for fractional output
        #                   (1..1,048,575). Set this to '1' or higher to
        #                   avoid divide by zero errors.
        # 
        # @section Output Clock Configuration
        # 
        # The multisynth dividers are applied to the specified PLL output,
        # and are used to reduce the PLL output to a valid range (500kHz
        # to 160MHz). The relationship can be seen in this formula, where
        # fVCO is the PLL output frequency and MSx is the multisynth
        # divider:
        #     fOUT = fVCO / MSx
        # Valid multisynth dividers are 4, 6, or 8 when using integers,
        # or any fractional values between 8 + 1/1,048,575 and 900 + 0/1
        # The following formula is used for the fractional mode divider:
        #     a + b / c
        # a = The integer value, which must be 4, 6 or 8 in integer mode (MSx_INT=1)
        #     or 8..900 in fractional mode (MSx_INT=0).
        # b = The fractional numerator (0..1,048,575)
        # c = The fractional denominator (1..1,048,575)
        # @note   Try to use integers whenever possible to avoid clock jitter
        # @note   For output frequencies > 150MHz, you must set the divider
        #         to 4 and adjust to PLL to generate the frequency (for example
        #         a PLL of 640 to generate a 160MHz output clock). This is not
        #         yet supported in the driver, which limits frequencies to
        #         500kHz .. 150MHz.
        # @note   For frequencies below 500kHz (down to 8kHz) Rx_DIV must be
        #         used, but this isn't currently implemented in the driver.
        #
        # Output Multisynth Divider Equations
        # where: a = div, b = num and c = denom
        # P1[17:0] = 128 * a + floor(128*(b/c)) - 512
        # P2[19:0] = 128 * b - c * floor(128*(b/c))
        # P3[19:0] = c

        # Set the main PLL config registers
        P1 = 128 * div + int(128.0 * num / denom) - 512
        P2 = 128 * num - denom * int(128.0 * num / denom)
        P3 = denom

        # Get the appropriate starting point for the PLL registers
        if output == 0: baseaddr = SI5351_REGISTER_42_MULTISYNTH0_PARAMETERS_1
        if output == 1: baseaddr = SI5351_REGISTER_50_MULTISYNTH1_PARAMETERS_1
        if output == 2: baseaddr = SI5351_REGISTER_58_MULTISYNTH2_PARAMETERS_1

        # Set the MSx config registers
        self.i2c.write8(baseaddr,   (P3 & 0x0000FF00) >> 8)
        self.i2c.write8(baseaddr + 1, (P3 & 0x000000FF))
        self.i2c.write8(baseaddr + 2, (P1 & 0x00030000) >> 16)	# ToDo: Add DIVBY4 (>150MHz) and R0 support (<500kHz) later
        self.i2c.write8(baseaddr + 3, (P1 & 0x0000FF00) >> 8)
        self.i2c.write8(baseaddr + 4, (P1 & 0x000000FF))
        self.i2c.write8(baseaddr + 5, ((P3 & 0x000F0000) >> 12) | ((P2 & 0x000F0000) >> 16) )
        self.i2c.write8(baseaddr + 6, (P2 & 0x0000FF00) >> 8)
        self.i2c.write8(baseaddr + 7, (P2 & 0x000000FF))

        # Configure the clk control and enable the output
        clkControlReg = 0x0F                              # 8mA drive strength, MS0 as CLK0 source, Clock not inverted, powered up
        if pll == self.PLL_B: clkControlReg |= (1 << 5)   # Uses PLLB 
        if num == 0: clkControlReg |= (1 << 6)            # Integer mode
        if output == 0: self.i2c.write8(SI5351_REGISTER_16_CLK0_CONTROL, clkControlReg)
        if output == 1: self.i2c.write8(SI5351_REGISTER_17_CLK1_CONTROL, clkControlReg)
        if output == 2: self.i2c.write8(SI5351_REGISTER_18_CLK2_CONTROL, clkControlReg)


    def enableOutputs(self, enabled):

        # Enabled desired outputs (see Register 3)
        val = 0x00 if enabled else 0xFF
        self.i2c.write8(SI5351_REGISTER_3_OUTPUT_ENABLE_CONTROL, val)






