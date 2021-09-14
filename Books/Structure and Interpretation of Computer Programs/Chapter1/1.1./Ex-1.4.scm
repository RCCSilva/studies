(define (a-plus-abs-b a b)
((if (> b 0) + -) a b))

; First, it evaluates if b is greater then 0. If it is, is simply sums a and b. If not, it will subtract a and b.
