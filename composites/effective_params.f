        program effective
         implicit none
         character*256 string
         real*8 E1, E2, E3
         real*8 G12, G23, G13
         real*8 Nu12, Nu13, Nu23
         real*8 a1, a2, a3
         integer layers
         real*8 phi
         real*8 h
         integer file_unit
         file_unit = 8

          read(*,*) string
          write(*,*) "input file: ",string 
          open(unit = file_unit, file = string)
          read(file_unit, *) string
          read(file_unit, *) E1, E2, E3
          read(file_unit, *) string
          read(file_unit, *) G12, G23, G13
          read(file_unit, *) string
          read(file_unit, *) Nu12, Nu13, Nu23
          read(file_unit, *) string
          read(file_unit, *) a1, a2, a3
          read(file_unit, *) string
          read(file_unit, *) phi, layers, h

10        FORMAT(A12,E12.2,A12,E12.2,A12,E12.2) 
20        FORMAT(A12,F12.2,A12,F12.2,A12,F12.2) 
30        FORMAT(A12,F12.2,A12,I12,A12,F12.4) 
          write(*,10) "E1:",E1, "E2:", E2, "E3:", E3 
          write(*,10) "G12:", G12, "G23:", G23, "G13:", G13
          write(*,20) "Nu12:", Nu12, "Nu13:", Nu13, "Nu23:", Nu23
          write(*,10) "a1:", a1,"a2:", a2, "a3:",  a3
          write(*,30) "phi:", phi, "layers:", layers, "thickness:", h
         close(file_unit)
        end program effective
