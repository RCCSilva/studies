(define (f g) (g 2))

; (f f)
; (f 2)
; (2 2)

; The program will invoke a new procedure call `(f 2)` which will try to 
; to (2 2). The latter is not possible and the program will break.