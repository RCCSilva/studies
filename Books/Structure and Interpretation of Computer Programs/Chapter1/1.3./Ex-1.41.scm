(define (double proc)
	(lambda (x) (proc (proc x))))

(define (inc x) (+ x 1))

(((double (double double)) inc) 5)

; (double double) ==> (lambda (x) (double (double x))) ==> dd

; (((double dd) inc) 5)

; (double dd) ==> (lambda (x) ((lambda (x) (double (double x))) ((lambda (x) (double (double x))) x))) ==>> dddd

; ((dddd inc) 5)

; ==> ((lambda (x) ((lambda (x) (double (double x))) ((lambda (x) (double (double x))) x))) inc)
; ==> (((lambda (x) (double (double inc))) ((lambda (x) (double (double x))) inc)))
; ==> (((lambda (x) (double (double x))) lambda (x) (inc (inc (inc (inc x))))))
; ==> (((lambda (x) (double (double x))) lambda (x) (inc (inc (inc (inc x))))))
; ==> (lambda (x) (inc (inc (inc (inc (inc (inc (inc (inc (inc (inc (inc (inc (inc (inc (inc (inc x)))))))))))))))))

; In the end  you'll have 16 (2 ^ 4) added to 21. Thus, 21.