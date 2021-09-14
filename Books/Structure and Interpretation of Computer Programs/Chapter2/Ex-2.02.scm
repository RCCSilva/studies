(define x-point car)
(define y-point cdr)

(define make-point cons)

(define (make-segment x1 y1 x2 y2)
	(cons (make-point x1 y1) (make-point x2 y2)))

(define start-segment car)

(define end-segment cdr)

(define (average a b)
	(/ (+ a b) 2))

(define (midpoint-range line)
	(let ((mid-x (average (x-point (start-segment line)) (x-point (end-segment line))))
		  (mid-y (average (y-point (start-segment line)) (y-point (end-segment line)))))
	(cons mid-x mid-y)))

(define (print-point point)
	(newline)
	(display "(")
	(display (x-point point))
	(display ",")
	(display (y-point point))
	(display ")"))

; Example

(print-point (midpoint-range (make-segment 1 2 3 4))) ; (2,3)

(print-point (midpoint-range (make-segment -2 -10 0 2))) ; (-1,-4)