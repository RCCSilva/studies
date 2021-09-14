; Math Abstrasction Barrier

(define (square x) (* x x))

(define (sqrt-iter old-guess actual-guess x)
(if (good-enough? old-guess actual-guess)
actual-guess
(sqrt-iter actual-guess (improve actual-guess x) x)))

(define (improve guess x)
(average guess (/ x guess)))

(define (average x y)
(/ (+ x y) 2))

(define (good-enough? old-guess actual-guess)
(< (abs (- actual-guess old-guess)) 0.001))

(define (sqrt x)
(sqrt-iter 0.5 1.0 x))

; Basic Geometric Data Abstraction Barrier

(define make-point cons)

(define (equal-point a b)
    (and (= (car a) (car b)) (= (cdr a) (cdr b))))

(define x-point car)

(define y-point cdr)

(define make-segment cons)

(define start-segment car)

(define end-segment cdr)

(define (point? x)
    (if (pair? x)
        (and (number? (car x)) (number? (cdr x)))
        #f))

(define (segment? x)
    (if (pair? x)
        (and (point? (car x)) (point? (cdr x)))
        #f))

(define (consecutive-segments? a b)
    (or (equal-point (car a) (car b)) (equal-point (car a) (cdr b)) (equal-point (cdr a) (car b)) (equal-point (cdr a) (cdr b))))

(define (length-segment segment)
    (let ((base (abs (- (x-point (start-segment segment)) (x-point (end-segment segment)))))
          (height (abs (- (y-point (start-segment segment)) (y-point (end-segment segment))))))
    (sqrt (+ (square base) (square height)))))

; Rectangle Abstraction Barrier

; 1. Rectangles as a set of points

(define (make-rectangle point1 point2 point3 point4)
    (cons (cons point1 point2) (cons point3 point4)))

; 2. Rectangles as a set of segments

(define (make-rectangle seg1 seg2 seg3 seg4)
    (cons (cons seg1 seg2) (cons seg3 seg4)))

; 3. Regtangle as either a set of points or a set of segments

(define (make-rectangle geom1 geom2 geom3 geom4)
    (cons (cons geom1 geom2) (cons geom3 geom4)))

; Functions that are applyed on rectangles
; Final barrier of abstraction 

; Probably the best approach is to develop procedures that returns two consecutive
; points.

(define (get-consecutive-segments geom)
    ; This function returns a pair of consecutive segments from a rectangle
    ; It is not as elegant as I would like, but for now It works
    ; We're assuming that at leas the geometries (points or segments) used in make-rectangle are consecutive.
    (define (iter-geom next last)
        (if (segment? next)
            (cons next (cdr last))
            (iter-geom (car next) next)))
    (let ((segments (iter-geom (car geom) geom)))
        (if (consecutive-segments? (car segments) (cdr segments))
            segments
            (make-segment (car segments) (cons (car (cdr segments)) (cdr (car segments)))))))

; 
(define (rectangle-area rectangle)
    (let ((segments (get-consecutive-segments rectangle)))
        (let ((base (length-segment (car segments)))
              (height (length-segment (cdr segments))))
        (* base height))))
        

;
(define (rectangle-perimeter rectangle)
    (let ((base (length-segment (rectangle-base rectangle)))
          (height (length-segment (rectangle-height rectangle))))
    (+ (* 2 base) (* 2 height))))

; Examples

(rectangle-area (make-rectangle (make-point 0 0) (make-point 0 2) (make-point 2 2) (make-point 2 0)))

(rectangle-area (make-rectangle 
    (make-segment (make-point 0 0) (make-point 0 2))
    (make-segment (make-point 0 2) (make-point 2 2))
    (make-segment (make-point 2 2) (make-point 2 0))
    (make-segment (make-point 2 0) (make-point 0 0))))