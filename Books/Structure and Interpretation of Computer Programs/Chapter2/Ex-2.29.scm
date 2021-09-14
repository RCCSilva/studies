(define (make-mobile left right)
    (list left right))

(define (make-branch length structure)
    (list length structure))

;; a.
(define (left-branch mobile)
    (car mobile))

(define (right-branch mobile)
    (car (cdr mobile)))

(define (branch-length branch)
    (car branch))

(define (branch-structure branch)
    (car (cdr branch)))

;; b.
(define (total-weight mobile)
    (let ((left-structure (branch-structure (left-branch mobile)))
          (right-structure (branch-structure (right-branch mobile))))
         (cond ((and (not (pair? left-structure)) (not (pair? right-structure))) (+ left-structure right-structure))
               ((and (pair? left-structure) (not (pair? right-structure))) (+ (total-weight left-structure) right-structure))
               ((and (not (pair? left-structure)) (pair? right-structure)) (+ left-structure (total-weight right-structure)))
               (else (+ (total-weight left-structure) (total-weight right-structure))))))
;; c.

(define (total-branch-weight branch)
    (let ((structure (branch-structure branch)))
        (if (not (pair? structure))
            structure
            (total-weight structure))))

(define (total-branch-length branch)
    (if (not (pair? branch-structure))
        (branch-length branch)
        (+ (total-branch-length (left-branch (branch-structure mobile))) 
           (total-branch-length (right-branch (branch-structure mobile))))))

(define (torque branch)
    (* (total-branch-weight branch) (total-branch-length branch)))

(define (is-balanced? mobile)
    (= (torque (left-branch mobile)) (torque (right-branch mobile))))

;; d.
(define (make-mobile left right) (cons left right))
(define (make-branch length structure)
    (cons length structure))