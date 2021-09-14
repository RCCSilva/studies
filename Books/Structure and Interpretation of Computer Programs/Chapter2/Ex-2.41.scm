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

(define (unique-pairs n)
    (flatmap (lambda (x) (map (lambda (b) (list x b)) (enumerate-interval 1 (- x 1)))) (enumerate-interval 1 n)))

(define (unique-triples n)
	(flatmap (lambda (a) (map (lambda (b) (append (list a) b)) (unique-pairs (- a 1)))) (enumerate-interval 1 n)))