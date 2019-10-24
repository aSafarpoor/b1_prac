.include "m1280def.inc"
	LDI R16,HIGH(RAMEND)
	OUT SPH,R16
	LDI R16,LOW(RAMEND)
	OUT SPL,R16

	LDI R16,0xFF
	STS DDRJ,R16
L4: LDI R16,0X80
    LDI R20,0x01



START1:
	STS PORTJ,R16
	CALL DELAY
	LSR R16
	CPI R16,0
	
	BRNE START1

START2:
	STS PORTJ,R20
	CALL DELAY
	LSL R20
	CPI R20,0

	BRNE START2
	RJMP L4




DELAY:
	IN R17,PINC
L1: LDI R18,0xFF
L2: LDI R19,0x10
L3: DEC R19
	BRNE L3
	DEC R10
	BRNE L2
	DEC R17
	BRNE L1
	RET
