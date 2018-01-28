
(define problem
 (lambda ()
  (total-num-chars 1000)
 )
)

(define total-num-chars
 (lambda (lim)
  (cond
   ((zero? lim) 0)
   (else (+ (num-chars lim)
            (total-num-chars (- lim 1)))
   )
  )
 )
)

(define num-chars
 (lambda (num)
  (cond

   ((= num 1000) 11)

   ((> num 99)
    (cond
     ((zero? (modulo num 100))
      (+ 7 (num-chars (quotient num 100)))
     )
     (else
      (+
       (num-chars (* 100 (quotient num 100)))
       (+
        3  ; and
        (num-chars (remainder num 100))
       )
      )
     )
    )
   )

   ((< num 20)
    (cond
     ((= num 0) 4)
     ((= num 1) 3)
     ((= num 2) 3)
     ((= num 3) 5)
     ((= num 4) 4)
     ((= num 5) 4)
     ((= num 6) 3)
     ((= num 7) 5)
     ((= num 8) 5)
     ((= num 9) 4)
     ((= num 10) 3)
     ((= num 11) 6)
     ((= num 12) 6)
     ((= num 13) 8)
     ((= num 14) 8)
     ((= num 15) 7)
     ((= num 16) 7)
     ((= num 17) 9)
     ((= num 18) 8)
     ((= num 19) 8)
    )
   )

   ((divisible num 10)
    (cond
     ((= (quotient num 10) 2) 6)
     ((= (quotient num 10) 3) 6)
     ((= (quotient num 10) 4) 5)
     ((= (quotient num 10) 5) 5)
     ((= (quotient num 10) 6) 5)
     ((= (quotient num 10) 7) 7)
     ((= (quotient num 10) 8) 6)
     ((= (quotient num 10) 9) 6)
    )
   )

   (else
    (+ (num-chars (* 10 (quotient num 10)))
       (num-chars (remainder num 10)))
   )
  )
 )
)

