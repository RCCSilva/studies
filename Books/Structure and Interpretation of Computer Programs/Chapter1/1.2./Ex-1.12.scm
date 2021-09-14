; Imagine someone asks you what is the 8th number of the pascal triangle. Given that, 
; one way to approach this problem is to extract the row and column position of this number.
; With this information, we are able to use a recursive procedure "iterate-pascal" which builds
; the Pascal tree from bottom to top until it finds the edges of the triangle and sum everything up.

(define (pascal n)
	(iterate-pascal (get-x-position n 1 1) (get-y-position n 1 1)))

; Returns the row position (left to right) of the provided number
(define (get-y-position n sum i)
	(if (<= n sum) i
		(get-y-position n (+ sum (+ i 1)) (+ i 1))))

(define (get-x-position n row-max i)
	(if (> n row-max) (get-x-position n (+ row-max (+ i 1)) (+ i 1))
		(- n (- row-max i))))

(define (iterate-pascal row-position i)
	(if (or (= row-position 1) (= row-position i)) 1
		(+ (iterate-pascal (- row-position 1) (- i 1)) (iterate-pascal row-position (- i 1)))))


; Simplified version. If someone already know the row and column of the number X, we
; don't have to discover this parameters. Thus, we may use directly the recursive process
; and find the edges of the triangle.
(define (pascal x y)
	(if (or (= x 1) (= x y)) 1
		(+ (pascal (- x 1) (- y 1)) (pascal x (- y 1)))))

