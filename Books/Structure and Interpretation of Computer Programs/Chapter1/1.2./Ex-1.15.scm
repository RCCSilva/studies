(define (cube x) (* x x x))
(define (p x) (- (* 3 x) (* 4 (cube x))))
(define (sine angle)
(if (not (> (abs angle) 0.1))
angle
(p (sine (/ angle 3.0)))))

(sine 12.15)
(p (sine (4.05)))
(p (sine (p (sine 1.35))))
(p (sine (p (sine (p (sine ( 0.45)))))))
(p (sine (p (sine (p (sine (p (sine 0.15))))))))
(p (sine (p (sine (p (sine (p (sine (p (sine 0.05))))))))))

; a) Function p is applied 5 times.

; b) Since we are dividing the results by 3 in each step. The growth order of steps should
; be around log3.