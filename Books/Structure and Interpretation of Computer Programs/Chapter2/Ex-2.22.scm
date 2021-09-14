(define (square-list items)
    (define (iter things answer)
    (if (null? things)
    answer
    (iter (cdr things)
          (cons (square (car things)) answer))))
    (iter items '()))


(square-list '(1 2 3))
(iter '(2 3) '(1 . ()))
(iter '(3) '( 4 . (1 . ())))
(iter '() '(9 . (4 . (1 . ())))
'(9 . (4 . (1 . ())))

; This solution concatenate the values starting from the end of the list (value, null) and brings more and more
; valures to left of the previous result. (value2 . (value1 . (value0 . null))). This creates a new list from end to
; its beginning.

(define (square-list items)
    (define (iter things answer)
    (if (null? things)
    answer
    (iter (cdr things)
          (cons answer (square (car things))))))
    (iter items '()))

(square-list '(1 2 3))
(iter '(2 3) '((). 1))
(iter '(3) '((() . 1) . 4))
(iter '() '(((() . 1) . 4) . 9))

; By interting the `cons` parameters you do not get the desired answer. Instead of creating a list (which needs
; the null value a the end of the last pair). You end up creating a kind of recursive pair structure where
; each pair has for its first value another pair.


(define (square-list items)
    (define (iter things answer)
    (if (null? things)
    (cons (car ())
    (iter (cdr things)
          (cons (square (car things)) (square (car things))))))
    (iter items '()))

(square-list '(1 2 3))
(iter '(2 3) '((). 1))
(iter '(3) '((() . 1) . 4))
(iter '() '(((() . 1) . 4) . 9))