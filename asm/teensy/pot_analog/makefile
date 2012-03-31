#--------------------------------------------------------------------
# Makefile: pot_analog.S
# Date:     05/09/2010
#--------------------------------------------------------------------

TARGET  =   pot_analog
FORMAT  =   ihex
MCU     =   at90usb1286

# This line lists the source files for this project
ASRCS   =   $(TARGET).S

# where are the tools we will use
TOOLS   =   C:/WinAVR-20100110/bin
CC      =   $(TOOLS)/avr-gcc.exe
ASM     =   $(TOOLS)/avr-as.exe
LINK    =   $(TOOLS)/avr-ld.exe
SIZE    =   $(TOOLS)/avr-size.exe
OBJCOPY =   $(TOOLS)/avr-objcopy.exe
OBJDUMP =   $(TOOLS)/avr-objdump.exe
NM      =   $(TOOLS)/avr-nm.exe
RM      =   rm -f
LOADER  =	teensy_loader_cli.exe

# DO NOT MODIFY ANYTHING BELOW THIS LINE ----------------------#

# derive the object and listing file names
OBJ     =   $(ASRCS:.S=.o)
LST     =   $(ASRCS:.S=.lst)

# flags for the tools
CFLAGS  =
ASFLAGS =   -Wa,-adhlns=$(<:.S=.lst),-gstabs
LDFLAGS =   -Wl,-Map=$(TARGET).map,--cref
LDFLAGS +=	-nostartfiles

ALL_CFLAGS  = -mmcu=$(MCU) -I. $(CFLAGS)
ALL_AFLAGS  = -mmcu=$(MCU) -I. $(AFLAGS)

# default targets for this project
all:    elf hex lss sym

elf:    $(TARGET).elf
hex:    $(TARGET).hex
eep:    $(TARGET).eep
lss:    $(TARGET).lss
sym:    $(TARGET).sym

%.hex: %.elf
	$(OBJCOPY) -O $(FORMAT) -R .eeprom $< $@

%.eep:  %.elf
	$(OBJCOPY) -j .eeprom --set-section-flags=.eeprom="alloc,load" \
		--change-section-lma .eeprom=0 -O $(FORMAT) $< $@

%sym:   %.elf
	$(NM) -n $< > $@

%.lss:  %.elf
	$(OBJDUMP) -h -S $< > $@

%.elf: $(OBJ)
	$(CC) $(ALL_CFLAGS) $(OBJ) --output $@ $(LDFLAGS)

%.o:    %.S
	$(CC) -c $(ALL_AFLAGS) $< -o $@

clean:
	$(RM) $(TARGET).hex
	$(RM) $(TARGET).elf
	$(RM) $(TARGET).eep
	$(RM) $(TARGET).o
	$(RM) $(TARGET).map
	$(RM) $(TARGET).sym
	$(RM) $(TARGET).lss
	$(RM) $(OBJ)
	$(RM) $(LST)
	
load: $(TARGET).hex
	$(LOADER) -mmcu=$(MCU) -r $(TARGET).hex

size:
	$(SIZE) -A $(TARGET).elf