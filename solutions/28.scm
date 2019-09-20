
(require xrepl)

(define SIZE 1001)

(define problem
 (lambda ()
  (longest_collatz LIMIT)
 )
)

(define diag_sum
 (lambda (n)
  (cond
    ((eq? 0 (modulo n 2)) 0)
    ((<= 1 n) (max n 0))
    (else (+ (* 4 (
  )
 )
)
