# URM
Program to model a URM as given from "CS-275: Automata and Formal Language Theory" module @ Swansea University.

Instructions:
 - Rk := Rk + 1
 - Rk := Rk - 1
 - if Rk = 0 then goto q
 - stop: finished entering instructions (only applies to console)
 
 <h2>Example run for function f(x, y) = 2(2x + y)</h2>
Input file:

```if R0 = 0 then goto 5
R0 := R0 - 1
R1 := R1 + 1
R1 := R1 + 1
if R2 = 0 then goto 0
if R1 = 0 then goto 10
R1 := R1 - 1
R0 := R0 + 1
R0 := R0 + 1
if R2 = 0 then goto 5
```

Input parameters: `4, 5`

Output:
```PC: 0 Registers: [4, 5] Executed: 'if R0 = 0 then goto 5'
PC: 1 Registers: [3, 5] Executed: 'R0 := R0 - 1'
PC: 2 Registers: [3, 6] Executed: 'R1 := R1 + 1'
PC: 3 Registers: [3, 7] Executed: 'R1 := R1 + 1'
PC: 4 Registers: [3, 7] Executed: 'if R2 = 0 then goto 0'
PC: 0 Registers: [3, 7] Executed: 'if R0 = 0 then goto 5'
PC: 1 Registers: [2, 7] Executed: 'R0 := R0 - 1'
PC: 2 Registers: [2, 8] Executed: 'R1 := R1 + 1'
PC: 3 Registers: [2, 9] Executed: 'R1 := R1 + 1'
PC: 4 Registers: [2, 9] Executed: 'if R2 = 0 then goto 0'
PC: 0 Registers: [2, 9] Executed: 'if R0 = 0 then goto 5'
PC: 1 Registers: [1, 9] Executed: 'R0 := R0 - 1'
PC: 2 Registers: [1, 10] Executed: 'R1 := R1 + 1'
PC: 3 Registers: [1, 11] Executed: 'R1 := R1 + 1'
PC: 4 Registers: [1, 11] Executed: 'if R2 = 0 then goto 0'
PC: 0 Registers: [1, 11] Executed: 'if R0 = 0 then goto 5'
PC: 1 Registers: [0, 11] Executed: 'R0 := R0 - 1'
PC: 2 Registers: [0, 12] Executed: 'R1 := R1 + 1'
PC: 3 Registers: [0, 13] Executed: 'R1 := R1 + 1'
PC: 4 Registers: [0, 13] Executed: 'if R2 = 0 then goto 0'
PC: 0 Registers: [0, 13] Executed: 'if R0 = 0 then goto 5'
PC: 5 Registers: [0, 13] Executed: 'if R1 = 0 then goto 10'
PC: 6 Registers: [0, 12] Executed: 'R1 := R1 - 1'
PC: 7 Registers: [1, 12] Executed: 'R0 := R0 + 1'
PC: 8 Registers: [2, 12] Executed: 'R0 := R0 + 1'
PC: 9 Registers: [2, 12] Executed: 'if R2 = 0 then goto 5'
PC: 5 Registers: [2, 12] Executed: 'if R1 = 0 then goto 10'
PC: 6 Registers: [2, 11] Executed: 'R1 := R1 - 1'
PC: 7 Registers: [3, 11] Executed: 'R0 := R0 + 1'
PC: 8 Registers: [4, 11] Executed: 'R0 := R0 + 1'
PC: 9 Registers: [4, 11] Executed: 'if R2 = 0 then goto 5'
PC: 5 Registers: [4, 11] Executed: 'if R1 = 0 then goto 10'
PC: 6 Registers: [4, 10] Executed: 'R1 := R1 - 1'
PC: 7 Registers: [5, 10] Executed: 'R0 := R0 + 1'
PC: 8 Registers: [6, 10] Executed: 'R0 := R0 + 1'
PC: 9 Registers: [6, 10] Executed: 'if R2 = 0 then goto 5'
PC: 5 Registers: [6, 10] Executed: 'if R1 = 0 then goto 10'
PC: 6 Registers: [6, 9] Executed: 'R1 := R1 - 1'
PC: 7 Registers: [7, 9] Executed: 'R0 := R0 + 1'
PC: 8 Registers: [8, 9] Executed: 'R0 := R0 + 1'
PC: 9 Registers: [8, 9] Executed: 'if R2 = 0 then goto 5'
PC: 5 Registers: [8, 9] Executed: 'if R1 = 0 then goto 10'
PC: 6 Registers: [8, 8] Executed: 'R1 := R1 - 1'
PC: 7 Registers: [9, 8] Executed: 'R0 := R0 + 1'
PC: 8 Registers: [10, 8] Executed: 'R0 := R0 + 1'
PC: 9 Registers: [10, 8] Executed: 'if R2 = 0 then goto 5'
PC: 5 Registers: [10, 8] Executed: 'if R1 = 0 then goto 10'
PC: 6 Registers: [10, 7] Executed: 'R1 := R1 - 1'
PC: 7 Registers: [11, 7] Executed: 'R0 := R0 + 1'
PC: 8 Registers: [12, 7] Executed: 'R0 := R0 + 1'
PC: 9 Registers: [12, 7] Executed: 'if R2 = 0 then goto 5'
PC: 5 Registers: [12, 7] Executed: 'if R1 = 0 then goto 10'
PC: 6 Registers: [12, 6] Executed: 'R1 := R1 - 1'
PC: 7 Registers: [13, 6] Executed: 'R0 := R0 + 1'
PC: 8 Registers: [14, 6] Executed: 'R0 := R0 + 1'
PC: 9 Registers: [14, 6] Executed: 'if R2 = 0 then goto 5'
PC: 5 Registers: [14, 6] Executed: 'if R1 = 0 then goto 10'
PC: 6 Registers: [14, 5] Executed: 'R1 := R1 - 1'
PC: 7 Registers: [15, 5] Executed: 'R0 := R0 + 1'
PC: 8 Registers: [16, 5] Executed: 'R0 := R0 + 1'
PC: 9 Registers: [16, 5] Executed: 'if R2 = 0 then goto 5'
PC: 5 Registers: [16, 5] Executed: 'if R1 = 0 then goto 10'
PC: 6 Registers: [16, 4] Executed: 'R1 := R1 - 1'
PC: 7 Registers: [17, 4] Executed: 'R0 := R0 + 1'
PC: 8 Registers: [18, 4] Executed: 'R0 := R0 + 1'
PC: 9 Registers: [18, 4] Executed: 'if R2 = 0 then goto 5'
PC: 5 Registers: [18, 4] Executed: 'if R1 = 0 then goto 10'
PC: 6 Registers: [18, 3] Executed: 'R1 := R1 - 1'
PC: 7 Registers: [19, 3] Executed: 'R0 := R0 + 1'
PC: 8 Registers: [20, 3] Executed: 'R0 := R0 + 1'
PC: 9 Registers: [20, 3] Executed: 'if R2 = 0 then goto 5'
PC: 5 Registers: [20, 3] Executed: 'if R1 = 0 then goto 10'
PC: 6 Registers: [20, 2] Executed: 'R1 := R1 - 1'
PC: 7 Registers: [21, 2] Executed: 'R0 := R0 + 1'
PC: 8 Registers: [22, 2] Executed: 'R0 := R0 + 1'
PC: 9 Registers: [22, 2] Executed: 'if R2 = 0 then goto 5'
PC: 5 Registers: [22, 2] Executed: 'if R1 = 0 then goto 10'
PC: 6 Registers: [22, 1] Executed: 'R1 := R1 - 1'
PC: 7 Registers: [23, 1] Executed: 'R0 := R0 + 1'
PC: 8 Registers: [24, 1] Executed: 'R0 := R0 + 1'
PC: 9 Registers: [24, 1] Executed: 'if R2 = 0 then goto 5'
PC: 5 Registers: [24, 1] Executed: 'if R1 = 0 then goto 10'
PC: 6 Registers: [24] Executed: 'R1 := R1 - 1'
PC: 7 Registers: [25] Executed: 'R0 := R0 + 1'
PC: 8 Registers: [26] Executed: 'R0 := R0 + 1'
PC: 9 Registers: [26] Executed: 'if R2 = 0 then goto 5'
PC: 5 Registers: [26] Executed: 'if R1 = 0 then goto 10'
```
