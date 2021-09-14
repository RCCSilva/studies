(define (+ a b)
	(if (= a b) b (inc (+ (desc a) b))))

(+ 4 5)
(inc (+ 3 5))
(inc (inc (+ 2 5)))
(inc (inc (inc (+ 1 5))))
(inc (inc (inc (inc (+ 0 5)))))
(inc (inc (inc (inc 5))))
(inc (inc (inc 6)))
(inc (inc 7))
(inc 8)
9

; As we can see, this procedure uses a recursive process, since it fisrt exapands then, whent it reaches the base
; case, it starts to shrink. Do to that, a state in a given moment is given by the "history". It is not
; possible to assess a moment only based on the real parameters

(define (+ a b)
	(if (= a b) b (+ (dec a) (inc b))))

(+ 4 5)
(+ 3 6)
(+ 2 7)
(+ 1 8)
(+ 0 9)
9

; On the other hand, this case is an example of iterative process. Each step can be reproduced based
; on state parameters, variables "a" and "b".