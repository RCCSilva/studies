(define (smallest-divisor n) (find-divisor n 2))

(define (find-divisor n test-divisor)
    (cond ((> (square test-divisor) n) n)
          ((divides? test-divisor n) test-divisor)
          (else (find-divisor n (+ test-divisor 1)))))

(define (divides? a b) (= (remainder b a) 0))

(define (prime? n) (= (smallest-divisor n) n))

(define (accumulate op initial seq)
    (if (null? seq)
        initial
        (op (car seq) (accumulate op initial (cdr seq)))))

(define (enumerate-interval a b)
    (if (> a b)
        '()
        (cons a (enumerate-interval (+ a 1) b))))

(define (flatmap proc seq)
    (accumulate append '() (map proc seq)))

(define (prime-sum? pair)
    (prime? (+ (car pair) (cadr pair))))

(define (make-pair-sum pair)
    (list (car pair) (cadr pair) (+ (car pair) (cadr pair))))

(define (prime-sum-pairs n)
    (map make-pair-sum
        (filter prime-sum? (flatmap
        (lambda (i)
        (map (lambda (j) (list i j))
        (enumerate-interval 1 (- i 1))))
        (enumerate-interval 1 n)))))

(define (remove value seq)
    (filter (lambda (x) (not (= value x))) seq))

(define (permutations s) 
   (if (null? s)  ; empty set?
        (list '()) ; sequence containing empty set
        (flatmap (lambda (x)
                    (map (lambda (p) (cons x p)) (permutations (remove x s)))) s)))


;; Ex

(define (unique-pairs n)
    (flatmap (lambda (x) (map (lambda (b) (list x b)) (enumerate-interval 1 (- x 1)))) (enumerate-interval 1 n)))

(define (prime-sum-pairs n)
    (map make-pair-sum
        (filter prime-sum? (unique-pairs n))))