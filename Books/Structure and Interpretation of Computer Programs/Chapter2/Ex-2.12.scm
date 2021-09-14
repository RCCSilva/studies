(define (make-interval a b) (cons a b))

(define upper-bound cdr)
(define lower-bound car)
(define (average a b)
    (/ (+ a b) 2))
(define (center interval)
    (average (lower-bound interval) (upper-bound interval)))

(define (make-center-percent center percentage)
    (let ((upper (* center (+ 1 (/ percentage 100))))
          (lower (* center (- 1 (/ percentage 100)))))
    (make-interval lower upper)))

(define (percent interval)
    (- (/ (upper-bound interval) (center interval)) 1))