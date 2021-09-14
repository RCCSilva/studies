(define (p) (p))
(define (test x y)
(if (= x 0) 0 y))

; Normal Order: when an interpreter uses "Normal Order Evaluation" it does not evaluate the operands until it is necessary. Thus, in the case above the "p" would not be evaluated since x is equal to 0 and the progrom should return 0.

; application-order evaluation on the other hand evalutes the operands before passing to next step. Hence "p" is evaluated and it starts an infinite loop.
